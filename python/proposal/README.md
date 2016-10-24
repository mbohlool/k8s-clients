# Kubernetes Python Client

Kubernetes only have one supported client right now (go). The goal of this project is to extend it by developing and supporting a python client. Python has been chosen because of many automation tools use python and also there are community interest in it.

This client is auto-generated from OpenAPI spec. There is a manually written part that takes care of authentication, SSL, and any other shortcoming of generated clients (currently I can name streaming output for watch API calls).

## Example

```python
import client_set
import client.k8sclient_v1

# Configs can be set in Configuration class directly or using helper class config (manually written)
c=config.load_config(config_file=os.environ["HOME"] + '/.kube/config')
v1_client=k8sclient_core_v1.CoreV1Client()
pods=v1_client.list_pod_for_all_namespaces()
```

## Author

mbohlool

