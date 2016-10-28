from __future__ import absolute_import

from util import load_config
import k8sclient
import k8sclient.apis.v1_core_api
import os

# Configs can be set in Configuration class directly or using helper class
# config class (that is added after code generation)
load_config(os.environ["HOME"] + '/.kube/config')

v1=k8sclient.CoreV1Api()
print "Listing pods with their IPs:"
ret = v1.list_core_v1_pod_for_all_namespaces(watch=False)
for i in ret.items:
  print "%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name)
