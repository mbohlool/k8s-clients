
"""
ClientSet is a set of kubernetes clients for each API group/version.

"""

from __future__ import absolute_import

import yaml
import urllib3

import k8sclient.configuration


def find_object_with_name(o, name):
    for c in o:
        if c['name'] == name:
            return c
    return None


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
        c.verify_ssl = False
    finally:
        f.close()
