
"""
ClientSet is a set of kubernetes clients for each API group/version.

"""

from __future__ import absolute_import

import yaml
import urllib3
import tempfile
import base64
import ipaddress
import urllib3
import sys
import atexit
import os

import k8sclient.configuration


prev_match_hostname = None


def _to_unicode(obj):
    if isinstance(obj, str) and sys.version_info < (3,):
        obj = unicode(obj, encoding='ascii', errors='strict')
    return obj


def _ip_address(str):
    return ipaddress.ip_address(_to_unicode(str).rstrip())


def _match_hostname(cert, hostname):
    global prev_match_hostname
    if not prev_match_hostname:
        raise TypeError("prev_match_hostname should not be None")
    try:
        # Divergence from upstream: ipaddress can't handle byte str
        host_ip = _ip_address(hostname)
        san = cert.get('subjectAltName', ())
        for key, value in san:
            if key == 'IP Address':
                if host_ip is not None and _ip_address(value) == host_ip:
                    return
    except ValueError:
        pass
    return prev_match_hostname(cert, hostname)


def find_object_with_name(o, name):
    for c in o:
        if c['name'] == name:
            return c
    return None

_tempfiles = []


def _cleanup_tempfiles():
    for f in _tempfiles:
        os.remove(f)


def _create_temp_file_with_content(title, content):
    if len(_tempfiles) == 0:
        atexit.register(_cleanup_tempfiles)
    _, name = tempfile.mkstemp()
    _tempfiles.append(name)
    fd = open(name, 'w')
    try:
        fd.write(base64.decodestring(content))
    finally:
        fd.close()
    return name


def load_config(config_file):
    c = k8sclient.configuration
    f = open(config_file)
    try:
        config = yaml.load(f)
        active_context = find_object_with_name(config['contexts'], config['current-context'])['context']
        user = find_object_with_name(config['users'],active_context['user'])['user']
        cluster = find_object_with_name(config['clusters'],active_context['cluster'])['cluster']
        if 'server' in cluster:
            c.host = cluster['server']
        if 'username' in user and 'password' in user:
            c.api_key['authorization'] = urllib3.util.make_headers(
                basic_auth=user['username'] + ':' + user['password']).get('authorization')
        if 'token' in user:
            c.api_key['authorization'] = "bearer " + user['token']
        if 'certificate-authority-data' in cluster:
            c.ssl_ca_cert = _create_temp_file_with_content("CERTIFICATE REQUEST", cluster['certificate-authority-data'])
        if 'client-certificate-data' in user:
            c.cert_file = _create_temp_file_with_content("CERTIFICATE AUTHORITY", user['client-certificate-data'])
        if 'client-key-data' in user:
            c.key_file = _create_temp_file_with_content("RSA PRIVATE KEY", user['client-key-data'])

        # urllib3 match_hostname does not support IP addresses, adding the support by this hack
        global prev_match_hostname
        if getattr(getattr(urllib3, "connectionpool", None), "match_hostname", None):
            prev_match_hostname=urllib3.connectionpool.match_hostname
            urllib3.connectionpool.match_hostname = _match_hostname
        if getattr(getattr(urllib3, "connection", None), "match_hostname", None):
            prev_match_hostname=urllib3.connection.match_hostname
            urllib3.connection.match_hostname = _match_hostname
    finally:
        f.close()
