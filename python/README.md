# Kubernetes Python Client

Kubernetes python client for talking to kubernetes cluster.

This client is auto-generated from OpenAPI specs for each APi server's end-point (Group/Versions). There is a manually written client-set wrapper that take care of authentication and returning the right client.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

you can install directly from Github (future github repo)

```sh
pip install git+https://github.com/kubernetes/client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/kubernetes/client-python.git`)

Then import the package:
```python
import client_set
```

### Setuptools (TODO)

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import client_set
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import client_set
c=client_set.ClientSet(config_file=os.environ["HOME"] + '/.kube/config')
v1=c.get_client('v1')
pods=v1.list_pod_for_all_namespaces()
```

## Documentation for API Endpoints (TODO: Update)

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_api_group**](docs/DefaultApi.md#get_api_group) | **GET** /apis/extensions/ | 


## Documentation For Models (TODO: Update)

 - [UnversionedAPIGroup](docs/UnversionedAPIGroup.md)
 - [UnversionedGroupVersionForDiscovery](docs/UnversionedGroupVersionForDiscovery.md)
 - [UnversionedServerAddressByClientCIDR](docs/UnversionedServerAddressByClientCIDR.md)


## Documentation For Authorization


## BearerToken

- **Type**: API key
- **API key parameter name**: authorization
- **Location**: HTTP header


## Author



