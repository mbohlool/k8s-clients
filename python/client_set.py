
"""
ClientSet is a set of kubernetes clients for each API group/version.

"""

from __future__ import absolute_import

import yaml

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
    :param token: Authentication token for the API server.
    :param username: authentication username for the API server.
    :param password: authentication password for the API server.
    """
    def __init__(self, config_file=None, host="https://localhost", token="", username="", password=""):
        self.host = host
        self.username = username
        self.password = password
        self.token = token
        self._clients = {}
        if config_file:
            f = open("/Users/mehdy/.kube/config")
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
            finally:
                f.close()

    def _load_client(self, name):
        if not name in self._clients:
            config = __import__('k8sclient_%s.configuration' % (name))
            api = __import__('k8sclient_%s.apis.default_api' % (name))
            models = __import__('k8sclient_%s.models' % (name))
            self._clients[name] = {'config': config, 'api': api, models: 'models'}

    def get_client(self, name):
        self._load_client(name)
        return self._clients[name]['api']

    def get_models(self, name):
        self._load_client(name)
        return self._clients[name]['models']










def get_client(name, config_file):
  try:
      get_client = __import__("client_%s.client" % (name))
  except Exception, e:
      print e
      return None
  return get_client.get_client(config_file)

def Main():
    f = open("/Users/mehdy/.kube/config")
    config = yaml.load(f)
    f.close()
    for k in config:
        print k
    contexts = config['contexts']
    context = find_object_with_name(contexts, config['current-context'])['context']
    print context
    user = find_object_with_name(config['users'],context['user'])['user']
    print user['token']
    cluster = find_object_with_name(config['clusters'],context['cluster'])['cluster']
    print cluster['server']


Main()
