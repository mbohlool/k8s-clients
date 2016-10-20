# k8sclient_apis.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_versions**](DefaultApi.md#get_api_versions) | **GET** /apis/ | 


# **get_api_versions**
> UnversionedAPIGroupList get_api_versions()



get available API versions

### Example 
```python
import time
import k8sclient_apis
from k8sclient_apis.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_apis.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_apis.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_apis.configuration.username = 'YOUR_USERNAME'
k8sclient_apis.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_apis.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_apis.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_apis.DefaultApi()

try: 
    api_response = api_instance.get_api_versions()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_api_versions: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnversionedAPIGroupList**](UnversionedAPIGroupList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

