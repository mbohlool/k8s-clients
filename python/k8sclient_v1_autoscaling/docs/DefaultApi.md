# k8sclient_v1_autoscaling.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#create_namespaced_horizontal_pod_autoscaler) | **POST** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers | 
[**delete_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#delete_namespaced_horizontal_pod_autoscaler) | **DELETE** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name} | 
[**deletecollection_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#deletecollection_namespaced_horizontal_pod_autoscaler) | **DELETE** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers | 
[**get_api_resources**](DefaultApi.md#get_api_resources) | **GET** /apis/autoscaling/v1/ | 
[**list_horizontal_pod_autoscaler_for_all_namespaces**](DefaultApi.md#list_horizontal_pod_autoscaler_for_all_namespaces) | **GET** /apis/autoscaling/v1/horizontalpodautoscalers | 
[**list_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#list_namespaced_horizontal_pod_autoscaler) | **GET** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers | 
[**patch_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#patch_namespaced_horizontal_pod_autoscaler) | **PATCH** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name} | 
[**patch_namespaced_horizontal_pod_autoscaler_status**](DefaultApi.md#patch_namespaced_horizontal_pod_autoscaler_status) | **PATCH** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status | 
[**read_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#read_namespaced_horizontal_pod_autoscaler) | **GET** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name} | 
[**read_namespaced_horizontal_pod_autoscaler_status**](DefaultApi.md#read_namespaced_horizontal_pod_autoscaler_status) | **GET** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status | 
[**replace_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#replace_namespaced_horizontal_pod_autoscaler) | **PUT** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name} | 
[**replace_namespaced_horizontal_pod_autoscaler_status**](DefaultApi.md#replace_namespaced_horizontal_pod_autoscaler_status) | **PUT** /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status | 
[**watch_horizontal_pod_autoscaler_list_for_all_namespaces**](DefaultApi.md#watch_horizontal_pod_autoscaler_list_for_all_namespaces) | **GET** /apis/autoscaling/v1/watch/horizontalpodautoscalers | 
[**watch_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#watch_namespaced_horizontal_pod_autoscaler) | **GET** /apis/autoscaling/v1/watch/namespaces/{namespace}/horizontalpodautoscalers/{name} | 
[**watch_namespaced_horizontal_pod_autoscaler_list**](DefaultApi.md#watch_namespaced_horizontal_pod_autoscaler_list) | **GET** /apis/autoscaling/v1/watch/namespaces/{namespace}/horizontalpodautoscalers | 


# **create_namespaced_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscaler create_namespaced_horizontal_pod_autoscaler(namespace, body, pretty=pretty)



create a HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1_autoscaling.V1HorizontalPodAutoscaler() # V1HorizontalPodAutoscaler | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_horizontal_pod_autoscaler(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->create_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_horizontal_pod_autoscaler**
> UnversionedStatus delete_namespaced_horizontal_pod_autoscaler(name, namespace, body, pretty=pretty)



delete a HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1_autoscaling.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_namespaced_horizontal_pod_autoscaler(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->delete_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletecollection_namespaced_horizontal_pod_autoscaler**
> UnversionedStatus deletecollection_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.deletecollection_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->deletecollection_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources**
> UnversionedAPIResourceList get_api_resources()



get available resources

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()

try: 
    api_response = api_instance.get_api_resources()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->get_api_resources: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnversionedAPIResourceList**](UnversionedAPIResourceList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_horizontal_pod_autoscaler_for_all_namespaces**
> V1HorizontalPodAutoscalerList list_horizontal_pod_autoscaler_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_horizontal_pod_autoscaler_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_horizontal_pod_autoscaler_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1HorizontalPodAutoscalerList**](V1HorizontalPodAutoscalerList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscalerList list_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1HorizontalPodAutoscalerList**](V1HorizontalPodAutoscalerList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscaler patch_namespaced_horizontal_pod_autoscaler(name, namespace, body, pretty=pretty)



partially update the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1_autoscaling.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_horizontal_pod_autoscaler(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_horizontal_pod_autoscaler_status**
> V1HorizontalPodAutoscaler patch_namespaced_horizontal_pod_autoscaler_status(name, namespace, body, pretty=pretty)



partially update status of the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1_autoscaling.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_horizontal_pod_autoscaler_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_horizontal_pod_autoscaler_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscaler read_namespaced_horizontal_pod_autoscaler(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_horizontal_pod_autoscaler(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_horizontal_pod_autoscaler_status**
> V1HorizontalPodAutoscaler read_namespaced_horizontal_pod_autoscaler_status(name, namespace, pretty=pretty)



read status of the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_horizontal_pod_autoscaler_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_horizontal_pod_autoscaler_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_horizontal_pod_autoscaler**
> V1HorizontalPodAutoscaler replace_namespaced_horizontal_pod_autoscaler(name, namespace, body, pretty=pretty)



replace the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1_autoscaling.V1HorizontalPodAutoscaler() # V1HorizontalPodAutoscaler | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_horizontal_pod_autoscaler(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_horizontal_pod_autoscaler_status**
> V1HorizontalPodAutoscaler replace_namespaced_horizontal_pod_autoscaler_status(name, namespace, body, pretty=pretty)



replace status of the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1_autoscaling.V1HorizontalPodAutoscaler() # V1HorizontalPodAutoscaler | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_horizontal_pod_autoscaler_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_horizontal_pod_autoscaler_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HorizontalPodAutoscaler**](V1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_horizontal_pod_autoscaler_list_for_all_namespaces**
> VersionedEvent watch_horizontal_pod_autoscaler_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_horizontal_pod_autoscaler_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_horizontal_pod_autoscaler_list_for_all_namespaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/json;stream=watch, application/vnd.kubernetes.protobuf, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_horizontal_pod_autoscaler**
> VersionedEvent watch_namespaced_horizontal_pod_autoscaler(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_horizontal_pod_autoscaler(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_horizontal_pod_autoscaler: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HorizontalPodAutoscaler | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/json;stream=watch, application/vnd.kubernetes.protobuf, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_horizontal_pod_autoscaler_list**
> VersionedEvent watch_namespaced_horizontal_pod_autoscaler_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1_autoscaling
from k8sclient_v1_autoscaling.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1_autoscaling.configuration.username = 'YOUR_USERNAME'
k8sclient_v1_autoscaling.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1_autoscaling.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1_autoscaling.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1_autoscaling.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_horizontal_pod_autoscaler_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_horizontal_pod_autoscaler_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/json;stream=watch, application/vnd.kubernetes.protobuf, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

