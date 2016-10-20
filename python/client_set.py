
"""
ClientSet is a set of kubernetes clients for each API group/version.

"""

from __future__ import absolute_import

import yaml
import urllib3

def find_object_with_name(o, name):
    for c in o:
        if c['name'] == name:
            return c
    return None


class ClientSet(object):
    """
    ClientSet for kubernetes.

    This class represents a set of clients for kubernetes. Each client is created for an API endpoint (usually
    GroupVersion). The ClientSet can be created using a kubernetes config file (usually located in ~/.kube/config) or
    directly using (host, token) and/or (host, username, password).

    :param config_file: kube config file (refer to TODO for file format). If provided, the rest of parameters will be ignored.
    :param host: The basic path for kubernetes API server.
    :param ssl_ca_cert: customize the certificate file to verify the peer.
    :param token: Authentication token for the API server.
    :param username: authentication username for the API server.
    :param password: authentication password for the API server.
    """
    def __init__(self, config_file=None, host="https://localhost", ssl_ca_cert=None, token="", username="", password=""):
        self.host = host
        self.ssl_ca_cert = ssl_ca_cert
        self.username = username
        self.password = password
        self.token = token
        self._clients = {}
        if config_file:
            f = open(config_file)
            try:
                config = yaml.load(f)
                active_context = find_object_with_name(config['contexts'], config['current-context'])['context']
                user = find_object_with_name(config['users'],active_context['user'])['user']
                cluster = find_object_with_name(config['clusters'],active_context['cluster'])['cluster']
                if 'server' in cluster:
                    self.host = cluster['server']
                if 'username' in user:
                    self.username = user['username']
                if 'password' in user:
                    self.password = user['password']
                if 'token' in user:
                    self.token = user['token']
                #if 'certificate-authority-data' in cluster:
                #    self.ssl_ca_cert = cluster['certificate-authority-data']
            finally:
                f.close()

    def _load_client(self, name):
        if not name in self._clients:
            config = __import__('k8sclient_%s.configuration' % (name))
            api = __import__('k8sclient_%s.apis.default_api' % (name))
            models = __import__('k8sclient_%s.models' % (name))
            config_cls = config.Configuration()
            config_cls.host = self.host
            if self.token:
                config_cls.api_key['authorization'] = "bearer " + self.token
            else:
                config_cls.api_key['authorization'] = urllib3.util.make_headers(
                    basic_auth=self.username + ':' + self.password).get('authorization')
#            config_cls.ssl_ca_cert = self.ssl_ca_cert
            config.verify_ssl = False
            self._clients[name] = {'config': config, 'api': api, models: 'models'}

    def get_client(self, name, api_client=None):
        self._load_client(name)
        return self._clients[name]['api'].DefaultApi(api_client=api_client)

    def get_models(self, name):
        self._load_client(name)
        return self._clients[name]['models']

    def __str__(self):
        return "ClientSet:\n  host=%s\n  username=%s\n  password=%s\n  token=%s\n  ssl_ca_cert=%s\n" % (self.host, self.username, self.password, self.token, self.ssl_ca_cert)
