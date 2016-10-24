from __future__ import absolute_import

import config
import k8sclient.apis.v1_core_api
import os

config.load_config(os.environ["HOME"] + '/.kube/config')
v1=k8sclient.apis.v1_core_api.V1CoreApi()
print v1.list_core_v1_pod_for_all_namespaces(watch=False)
