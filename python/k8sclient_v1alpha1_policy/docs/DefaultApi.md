# k8sclient_v1alpha1_policy.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_pod_disruption_budget**](DefaultApi.md#create_namespaced_pod_disruption_budget) | **POST** /apis/policy/v1alpha1/namespaces/{namespace}/poddisruptionbudgets | 
[**delete_namespaced_pod_disruption_budget**](DefaultApi.md#delete_namespaced_pod_disruption_budget) | **DELETE** /apis/policy/v1alpha1/namespaces/{namespace}/poddisruptionbudgets/{name} | 
[**deletecollection_namespaced_pod_disruption_budget**](DefaultApi.md#deletecollection_namespaced_pod_disruption_budget) | **DELETE** /apis/policy/v1alpha1/namespaces/{namespace}/poddisruptionbudgets | 
[**get_api_resources**](DefaultApi.md#get_api_resources) | **GET** /apis/policy/v1alpha1/ | 
[**list_namespaced_pod_disruption_budget**](DefaultApi.md#list_namespaced_pod_disruption_budget) | **GET** /apis/policy/v1alpha1/namespaces/{namespace}/poddisruptionbudgets | 
[**list_pod_disruption_budget_for_all_namespaces**](DefaultApi.md#list_pod_disruption_budget_for_all_namespaces) | **GET** /apis/policy/v1alpha1/poddisruptionbudgets | 
[**patch_namespaced_pod_disruption_budget**](DefaultApi.md#patch_namespaced_pod_disruption_budget) | **PATCH** /apis/policy/v1alpha1/namespaces/{namespace}/poddisruptionbudgets/{name} | 
[**patch_namespaced_pod_disruption_budget_status**](DefaultApi.md#patch_namespaced_pod_disruption_budget_status) | **PATCH** /apis/policy/v1alpha1/namespaces/{namespace}/poddisruptionbudgets/{name}/status | 
[**read_namespaced_pod_disruption_budget**](DefaultApi.md#read_namespaced_pod_disruption_budget) | **GET** /apis/policy/v1alpha1/namespaces/{namespace}/poddisruptionbudgets/{name} | 
[**read_namespaced_pod_disruption_budget_status**](DefaultApi.md#read_namespaced_pod_disruption_budget_status) | **GET** /apis/policy/v1alpha1/namespaces/{namespace}/poddisruptionbudgets/{name}/status | 
[**replace_namespaced_pod_disruption_budget**](DefaultApi.md#replace_namespaced_pod_disruption_budget) | **PUT** /apis/policy/v1alpha1/namespaces/{namespace}/poddisruptionbudgets/{name} | 
[**replace_namespaced_pod_disruption_budget_status**](DefaultApi.md#replace_namespaced_pod_disruption_budget_status) | **PUT** /apis/policy/v1alpha1/namespaces/{namespace}/poddisruptionbudgets/{name}/status | 
[**watch_namespaced_pod_disruption_budget**](DefaultApi.md#watch_namespaced_pod_disruption_budget) | **GET** /apis/policy/v1alpha1/watch/namespaces/{namespace}/poddisruptionbudgets/{name} | 
[**watch_namespaced_pod_disruption_budget_list**](DefaultApi.md#watch_namespaced_pod_disruption_budget_list) | **GET** /apis/policy/v1alpha1/watch/namespaces/{namespace}/poddisruptionbudgets | 
[**watch_pod_disruption_budget_list_for_all_namespaces**](DefaultApi.md#watch_pod_disruption_budget_list_for_all_namespaces) | **GET** /apis/policy/v1alpha1/watch/poddisruptionbudgets | 


# **create_namespaced_pod_disruption_budget**
> V1alpha1PodDisruptionBudget create_namespaced_pod_disruption_budget(namespace, body, pretty=pretty)



create a PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1alpha1_policy.V1alpha1PodDisruptionBudget() # V1alpha1PodDisruptionBudget | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_pod_disruption_budget(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->create_namespaced_pod_disruption_budget: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1alpha1PodDisruptionBudget**](V1alpha1PodDisruptionBudget.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1PodDisruptionBudget**](V1alpha1PodDisruptionBudget.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_pod_disruption_budget**
> UnversionedStatus delete_namespaced_pod_disruption_budget(name, namespace, body, pretty=pretty)



delete a PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1alpha1_policy.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_namespaced_pod_disruption_budget(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->delete_namespaced_pod_disruption_budget: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
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

# **deletecollection_namespaced_pod_disruption_budget**
> UnversionedStatus deletecollection_namespaced_pod_disruption_budget(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.deletecollection_namespaced_pod_disruption_budget(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->deletecollection_namespaced_pod_disruption_budget: %s\n" % e
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
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()

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

# **list_namespaced_pod_disruption_budget**
> V1alpha1PodDisruptionBudgetList list_namespaced_pod_disruption_budget(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_pod_disruption_budget(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_namespaced_pod_disruption_budget: %s\n" % e
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

[**V1alpha1PodDisruptionBudgetList**](V1alpha1PodDisruptionBudgetList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pod_disruption_budget_for_all_namespaces**
> V1alpha1PodDisruptionBudgetList list_pod_disruption_budget_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_pod_disruption_budget_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_pod_disruption_budget_for_all_namespaces: %s\n" % e
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

[**V1alpha1PodDisruptionBudgetList**](V1alpha1PodDisruptionBudgetList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_pod_disruption_budget**
> V1alpha1PodDisruptionBudget patch_namespaced_pod_disruption_budget(name, namespace, body, pretty=pretty)



partially update the specified PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1alpha1_policy.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_pod_disruption_budget(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_pod_disruption_budget: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1PodDisruptionBudget**](V1alpha1PodDisruptionBudget.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_pod_disruption_budget_status**
> V1alpha1PodDisruptionBudget patch_namespaced_pod_disruption_budget_status(name, namespace, body, pretty=pretty)



partially update status of the specified PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1alpha1_policy.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_pod_disruption_budget_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_pod_disruption_budget_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1PodDisruptionBudget**](V1alpha1PodDisruptionBudget.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_pod_disruption_budget**
> V1alpha1PodDisruptionBudget read_namespaced_pod_disruption_budget(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_pod_disruption_budget(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_pod_disruption_budget: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1alpha1PodDisruptionBudget**](V1alpha1PodDisruptionBudget.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_pod_disruption_budget_status**
> V1alpha1PodDisruptionBudget read_namespaced_pod_disruption_budget_status(name, namespace, pretty=pretty)



read status of the specified PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_pod_disruption_budget_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_pod_disruption_budget_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1PodDisruptionBudget**](V1alpha1PodDisruptionBudget.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_pod_disruption_budget**
> V1alpha1PodDisruptionBudget replace_namespaced_pod_disruption_budget(name, namespace, body, pretty=pretty)



replace the specified PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1alpha1_policy.V1alpha1PodDisruptionBudget() # V1alpha1PodDisruptionBudget | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_pod_disruption_budget(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_pod_disruption_budget: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1alpha1PodDisruptionBudget**](V1alpha1PodDisruptionBudget.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1PodDisruptionBudget**](V1alpha1PodDisruptionBudget.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_pod_disruption_budget_status**
> V1alpha1PodDisruptionBudget replace_namespaced_pod_disruption_budget_status(name, namespace, body, pretty=pretty)



replace status of the specified PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1alpha1_policy.V1alpha1PodDisruptionBudget() # V1alpha1PodDisruptionBudget | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_pod_disruption_budget_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_pod_disruption_budget_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1alpha1PodDisruptionBudget**](V1alpha1PodDisruptionBudget.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1PodDisruptionBudget**](V1alpha1PodDisruptionBudget.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_pod_disruption_budget**
> VersionedEvent watch_namespaced_pod_disruption_budget(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
name = 'name_example' # str | name of the PodDisruptionBudget
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_pod_disruption_budget(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_pod_disruption_budget: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodDisruptionBudget | 
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

# **watch_namespaced_pod_disruption_budget_list**
> VersionedEvent watch_namespaced_pod_disruption_budget_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_pod_disruption_budget_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_pod_disruption_budget_list: %s\n" % e
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

# **watch_pod_disruption_budget_list_for_all_namespaces**
> VersionedEvent watch_pod_disruption_budget_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of PodDisruptionBudget

### Example 
```python
import time
import k8sclient_v1alpha1_policy
from k8sclient_v1alpha1_policy.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1alpha1_policy.configuration.username = 'YOUR_USERNAME'
k8sclient_v1alpha1_policy.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1alpha1_policy.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1alpha1_policy.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1alpha1_policy.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_pod_disruption_budget_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_pod_disruption_budget_list_for_all_namespaces: %s\n" % e
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

