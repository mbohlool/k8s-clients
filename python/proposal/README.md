# Kubernetes Python Client

Kubernetes only have one supported client right now (go). The goal of this project is to extend it by developing and supporting a python client. Python has been chosen because of many automation tools use python and also there are community interest in it.

Requirements:
- Auto-generated to keep in sync with API changes
- Using standard generation tools that can be applied to other languages
- Easy ways to configure clients (e.g. read kube config file)
- Support Secure connections
- Support streaming responses (optional for the first version of client)

## Example

```python
from __future__ import absolute_import

import config
import k8sclient.apis.v1_core_api
import os

# Configs can be set in Configuration class directly or using helper class
# config class (that is added after code generation)
config.load_config(os.environ["HOME"] + '/.kube/config')

v1=k8sclient.apis.v1_core_api.V1CoreApi()
print "Listing pods with their IPs:"
ret = v1.list_core_v1_pod_for_all_namespaces(watch=False)
for i in ret.items:
  print "%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name)
```

## Timeline

- 1.5 Release: Generate the client, load config from file with SSL support
- Q4 2016:     List missing/useful missing funtionalities
- 1.6 Release: Support stream responses for watch API calls

## Author

mbohlool

