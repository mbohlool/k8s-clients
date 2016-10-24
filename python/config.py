
"""
ClientSet is a set of kubernetes clients for each API group/version.

"""

from __future__ import absolute_import

import yaml
import urllib3
import tempfile
import base64

import k8sclient.configuration


def find_object_with_name(o, name):
    for c in o:
        if c['name'] == name:
            return c
    return None

_tempfiles = []

def _create_temp_file_with_content(title, content):
    _, name = tempfile.mkstemp()
    fd = open(name, 'w')
    try:
        fd.write(base64.decodestring(content))
    finally:
        fd.close()
    print name
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
    finally:
        f.close()
