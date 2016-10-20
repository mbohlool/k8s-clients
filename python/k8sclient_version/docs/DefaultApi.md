# k8sclient_version.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_code_version**](DefaultApi.md#get_code_version) | **GET** /version/ | 


# **get_code_version**
> VersionInfo get_code_version()



get the code version

### Example 
```python
import time
import k8sclient_version
from k8sclient_version.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_version.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_version.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_version.configuration.username = 'YOUR_USERNAME'
k8sclient_version.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_version.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_version.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_version.DefaultApi()

try: 
    api_response = api_instance.get_code_version()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_code_version: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

