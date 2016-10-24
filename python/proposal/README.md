# Kubernetes Python Client

Kubernetes only have one supported client right now (go). The goal of this project is to extend it by developing and supporting a python client. Python has been chosen because of many automation tools use python and also there are community interest in it.

This client is auto-generated from OpenAPI spec. There is a manually written part that takes care of authentication, SSL, and any other shortcoming of generated clients (currently I can name streaming output for watch API calls).

## Example

```python
from __future__ import absolute_import

import config
import k8sclient.apis.v1_core_api
import os

# Configs can be set in Configuration class directly or using helper class config (manually written)
config.load_config(os.environ["HOME"] + '/.kube/config')

v1=k8sclient.apis.v1_core_api.V1CoreApi()
print v1.list_core_v1_pod_for_all_namespaces(watch=False)
```

## Timeline

- 1.5 Release: Generate the client, load config from file with SSL support
- Q4 2016:     List missing/useful missing funtionalities
- 1.6 Release: Support stream responses for watch API calls

## Author

mbohlool

