# k8sclient_logs.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_file_handler**](DefaultApi.md#log_file_handler) | **GET** /logs/{logpath} | 
[**log_file_list_handler**](DefaultApi.md#log_file_list_handler) | **GET** /logs/ | 


# **log_file_handler**
> log_file_handler(logpath)



### Example 
```python
import time
import k8sclient_logs
from k8sclient_logs.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
k8sclient_logs.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_logs.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_logs.DefaultApi()
logpath = 'logpath_example' # str | path to the log

try: 
    api_instance.log_file_handler(logpath)
except ApiException as e:
    print "Exception when calling DefaultApi->log_file_handler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logpath** | **str**| path to the log | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_file_list_handler**
> log_file_list_handler()



### Example 
```python
import time
import k8sclient_logs
from k8sclient_logs.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
k8sclient_logs.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_logs.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_logs.DefaultApi()

try: 
    api_instance.log_file_list_handler()
except ApiException as e:
    print "Exception when calling DefaultApi->log_file_list_handler: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

