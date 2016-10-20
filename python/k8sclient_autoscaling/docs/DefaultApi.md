# k8sclient_autoscaling.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_group**](DefaultApi.md#get_api_group) | **GET** /apis/autoscaling/ | 


# **get_api_group**
> UnversionedAPIGroup get_api_group()



get information of a group

### Example 
```python
import time
import k8sclient_autoscaling
from k8sclient_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_autoscaling.DefaultApi()

try: 
    api_response = api_instance.get_api_group()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_api_group: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnversionedAPIGroup**](UnversionedAPIGroup.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

