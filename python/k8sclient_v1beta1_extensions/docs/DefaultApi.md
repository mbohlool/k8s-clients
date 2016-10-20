# k8sclient_v1beta1_extensions.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_daemon_set**](DefaultApi.md#create_namespaced_daemon_set) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets | 
[**create_namespaced_deployment**](DefaultApi.md#create_namespaced_deployment) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/deployments | 
[**create_namespaced_deployment_rollback_rollback**](DefaultApi.md#create_namespaced_deployment_rollback_rollback) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/rollback | 
[**create_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#create_namespaced_horizontal_pod_autoscaler) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers | 
[**create_namespaced_ingress**](DefaultApi.md#create_namespaced_ingress) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses | 
[**create_namespaced_job**](DefaultApi.md#create_namespaced_job) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/jobs | 
[**create_namespaced_network_policy**](DefaultApi.md#create_namespaced_network_policy) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies | 
[**create_namespaced_replica_set**](DefaultApi.md#create_namespaced_replica_set) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets | 
[**create_third_party_resource**](DefaultApi.md#create_third_party_resource) | **POST** /apis/extensions/v1beta1/thirdpartyresources | 
[**delete_namespaced_daemon_set**](DefaultApi.md#delete_namespaced_daemon_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | 
[**delete_namespaced_deployment**](DefaultApi.md#delete_namespaced_deployment) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | 
[**delete_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#delete_namespaced_horizontal_pod_autoscaler) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name} | 
[**delete_namespaced_ingress**](DefaultApi.md#delete_namespaced_ingress) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | 
[**delete_namespaced_job**](DefaultApi.md#delete_namespaced_job) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name} | 
[**delete_namespaced_network_policy**](DefaultApi.md#delete_namespaced_network_policy) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | 
[**delete_namespaced_replica_set**](DefaultApi.md#delete_namespaced_replica_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | 
[**delete_third_party_resource**](DefaultApi.md#delete_third_party_resource) | **DELETE** /apis/extensions/v1beta1/thirdpartyresources/{name} | 
[**deletecollection_namespaced_daemon_set**](DefaultApi.md#deletecollection_namespaced_daemon_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets | 
[**deletecollection_namespaced_deployment**](DefaultApi.md#deletecollection_namespaced_deployment) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/deployments | 
[**deletecollection_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#deletecollection_namespaced_horizontal_pod_autoscaler) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers | 
[**deletecollection_namespaced_ingress**](DefaultApi.md#deletecollection_namespaced_ingress) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses | 
[**deletecollection_namespaced_job**](DefaultApi.md#deletecollection_namespaced_job) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/jobs | 
[**deletecollection_namespaced_network_policy**](DefaultApi.md#deletecollection_namespaced_network_policy) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies | 
[**deletecollection_namespaced_replica_set**](DefaultApi.md#deletecollection_namespaced_replica_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets | 
[**deletecollection_third_party_resource**](DefaultApi.md#deletecollection_third_party_resource) | **DELETE** /apis/extensions/v1beta1/thirdpartyresources | 
[**get_api_resources**](DefaultApi.md#get_api_resources) | **GET** /apis/extensions/v1beta1/ | 
[**list_daemon_set_for_all_namespaces**](DefaultApi.md#list_daemon_set_for_all_namespaces) | **GET** /apis/extensions/v1beta1/daemonsets | 
[**list_deployment_for_all_namespaces**](DefaultApi.md#list_deployment_for_all_namespaces) | **GET** /apis/extensions/v1beta1/deployments | 
[**list_horizontal_pod_autoscaler_for_all_namespaces**](DefaultApi.md#list_horizontal_pod_autoscaler_for_all_namespaces) | **GET** /apis/extensions/v1beta1/horizontalpodautoscalers | 
[**list_ingress_for_all_namespaces**](DefaultApi.md#list_ingress_for_all_namespaces) | **GET** /apis/extensions/v1beta1/ingresses | 
[**list_job_for_all_namespaces**](DefaultApi.md#list_job_for_all_namespaces) | **GET** /apis/extensions/v1beta1/jobs | 
[**list_namespaced_daemon_set**](DefaultApi.md#list_namespaced_daemon_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets | 
[**list_namespaced_deployment**](DefaultApi.md#list_namespaced_deployment) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments | 
[**list_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#list_namespaced_horizontal_pod_autoscaler) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers | 
[**list_namespaced_ingress**](DefaultApi.md#list_namespaced_ingress) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses | 
[**list_namespaced_job**](DefaultApi.md#list_namespaced_job) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/jobs | 
[**list_namespaced_network_policy**](DefaultApi.md#list_namespaced_network_policy) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies | 
[**list_namespaced_replica_set**](DefaultApi.md#list_namespaced_replica_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets | 
[**list_network_policy_for_all_namespaces**](DefaultApi.md#list_network_policy_for_all_namespaces) | **GET** /apis/extensions/v1beta1/networkpolicies | 
[**list_replica_set_for_all_namespaces**](DefaultApi.md#list_replica_set_for_all_namespaces) | **GET** /apis/extensions/v1beta1/replicasets | 
[**list_third_party_resource**](DefaultApi.md#list_third_party_resource) | **GET** /apis/extensions/v1beta1/thirdpartyresources | 
[**patch_namespaced_daemon_set**](DefaultApi.md#patch_namespaced_daemon_set) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | 
[**patch_namespaced_daemon_set_status**](DefaultApi.md#patch_namespaced_daemon_set_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name}/status | 
[**patch_namespaced_deployment**](DefaultApi.md#patch_namespaced_deployment) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | 
[**patch_namespaced_deployment_status**](DefaultApi.md#patch_namespaced_deployment_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/status | 
[**patch_namespaced_deployments_scale**](DefaultApi.md#patch_namespaced_deployments_scale) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/scale | 
[**patch_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#patch_namespaced_horizontal_pod_autoscaler) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name} | 
[**patch_namespaced_horizontal_pod_autoscaler_status**](DefaultApi.md#patch_namespaced_horizontal_pod_autoscaler_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status | 
[**patch_namespaced_ingress**](DefaultApi.md#patch_namespaced_ingress) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | 
[**patch_namespaced_ingress_status**](DefaultApi.md#patch_namespaced_ingress_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name}/status | 
[**patch_namespaced_job**](DefaultApi.md#patch_namespaced_job) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name} | 
[**patch_namespaced_job_status**](DefaultApi.md#patch_namespaced_job_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name}/status | 
[**patch_namespaced_network_policy**](DefaultApi.md#patch_namespaced_network_policy) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | 
[**patch_namespaced_replica_set**](DefaultApi.md#patch_namespaced_replica_set) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | 
[**patch_namespaced_replica_set_status**](DefaultApi.md#patch_namespaced_replica_set_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/status | 
[**patch_namespaced_replicasets_scale**](DefaultApi.md#patch_namespaced_replicasets_scale) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/scale | 
[**patch_namespaced_replicationcontrollers_scale**](DefaultApi.md#patch_namespaced_replicationcontrollers_scale) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicationcontrollers/{name}/scale | 
[**patch_third_party_resource**](DefaultApi.md#patch_third_party_resource) | **PATCH** /apis/extensions/v1beta1/thirdpartyresources/{name} | 
[**read_namespaced_daemon_set**](DefaultApi.md#read_namespaced_daemon_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | 
[**read_namespaced_daemon_set_status**](DefaultApi.md#read_namespaced_daemon_set_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name}/status | 
[**read_namespaced_deployment**](DefaultApi.md#read_namespaced_deployment) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | 
[**read_namespaced_deployment_status**](DefaultApi.md#read_namespaced_deployment_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/status | 
[**read_namespaced_deployments_scale**](DefaultApi.md#read_namespaced_deployments_scale) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/scale | 
[**read_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#read_namespaced_horizontal_pod_autoscaler) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name} | 
[**read_namespaced_horizontal_pod_autoscaler_status**](DefaultApi.md#read_namespaced_horizontal_pod_autoscaler_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status | 
[**read_namespaced_ingress**](DefaultApi.md#read_namespaced_ingress) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | 
[**read_namespaced_ingress_status**](DefaultApi.md#read_namespaced_ingress_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name}/status | 
[**read_namespaced_job**](DefaultApi.md#read_namespaced_job) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name} | 
[**read_namespaced_job_status**](DefaultApi.md#read_namespaced_job_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name}/status | 
[**read_namespaced_network_policy**](DefaultApi.md#read_namespaced_network_policy) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | 
[**read_namespaced_replica_set**](DefaultApi.md#read_namespaced_replica_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | 
[**read_namespaced_replica_set_status**](DefaultApi.md#read_namespaced_replica_set_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/status | 
[**read_namespaced_replicasets_scale**](DefaultApi.md#read_namespaced_replicasets_scale) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/scale | 
[**read_namespaced_replicationcontrollers_scale**](DefaultApi.md#read_namespaced_replicationcontrollers_scale) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicationcontrollers/{name}/scale | 
[**read_third_party_resource**](DefaultApi.md#read_third_party_resource) | **GET** /apis/extensions/v1beta1/thirdpartyresources/{name} | 
[**replace_namespaced_daemon_set**](DefaultApi.md#replace_namespaced_daemon_set) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | 
[**replace_namespaced_daemon_set_status**](DefaultApi.md#replace_namespaced_daemon_set_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name}/status | 
[**replace_namespaced_deployment**](DefaultApi.md#replace_namespaced_deployment) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | 
[**replace_namespaced_deployment_status**](DefaultApi.md#replace_namespaced_deployment_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/status | 
[**replace_namespaced_deployments_scale**](DefaultApi.md#replace_namespaced_deployments_scale) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/scale | 
[**replace_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#replace_namespaced_horizontal_pod_autoscaler) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name} | 
[**replace_namespaced_horizontal_pod_autoscaler_status**](DefaultApi.md#replace_namespaced_horizontal_pod_autoscaler_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status | 
[**replace_namespaced_ingress**](DefaultApi.md#replace_namespaced_ingress) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | 
[**replace_namespaced_ingress_status**](DefaultApi.md#replace_namespaced_ingress_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name}/status | 
[**replace_namespaced_job**](DefaultApi.md#replace_namespaced_job) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name} | 
[**replace_namespaced_job_status**](DefaultApi.md#replace_namespaced_job_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/jobs/{name}/status | 
[**replace_namespaced_network_policy**](DefaultApi.md#replace_namespaced_network_policy) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | 
[**replace_namespaced_replica_set**](DefaultApi.md#replace_namespaced_replica_set) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | 
[**replace_namespaced_replica_set_status**](DefaultApi.md#replace_namespaced_replica_set_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/status | 
[**replace_namespaced_replicasets_scale**](DefaultApi.md#replace_namespaced_replicasets_scale) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/scale | 
[**replace_namespaced_replicationcontrollers_scale**](DefaultApi.md#replace_namespaced_replicationcontrollers_scale) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicationcontrollers/{name}/scale | 
[**replace_third_party_resource**](DefaultApi.md#replace_third_party_resource) | **PUT** /apis/extensions/v1beta1/thirdpartyresources/{name} | 
[**watch_daemon_set_list_for_all_namespaces**](DefaultApi.md#watch_daemon_set_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/daemonsets | 
[**watch_deployment_list_for_all_namespaces**](DefaultApi.md#watch_deployment_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/deployments | 
[**watch_horizontal_pod_autoscaler_list_for_all_namespaces**](DefaultApi.md#watch_horizontal_pod_autoscaler_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/horizontalpodautoscalers | 
[**watch_ingress_list_for_all_namespaces**](DefaultApi.md#watch_ingress_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/ingresses | 
[**watch_job_list_for_all_namespaces**](DefaultApi.md#watch_job_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/jobs | 
[**watch_namespaced_daemon_set**](DefaultApi.md#watch_namespaced_daemon_set) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/daemonsets/{name} | 
[**watch_namespaced_daemon_set_list**](DefaultApi.md#watch_namespaced_daemon_set_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/daemonsets | 
[**watch_namespaced_deployment**](DefaultApi.md#watch_namespaced_deployment) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/deployments/{name} | 
[**watch_namespaced_deployment_list**](DefaultApi.md#watch_namespaced_deployment_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/deployments | 
[**watch_namespaced_horizontal_pod_autoscaler**](DefaultApi.md#watch_namespaced_horizontal_pod_autoscaler) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/horizontalpodautoscalers/{name} | 
[**watch_namespaced_horizontal_pod_autoscaler_list**](DefaultApi.md#watch_namespaced_horizontal_pod_autoscaler_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/horizontalpodautoscalers | 
[**watch_namespaced_ingress**](DefaultApi.md#watch_namespaced_ingress) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/ingresses/{name} | 
[**watch_namespaced_ingress_list**](DefaultApi.md#watch_namespaced_ingress_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/ingresses | 
[**watch_namespaced_job**](DefaultApi.md#watch_namespaced_job) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/jobs/{name} | 
[**watch_namespaced_job_list**](DefaultApi.md#watch_namespaced_job_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/jobs | 
[**watch_namespaced_network_policy**](DefaultApi.md#watch_namespaced_network_policy) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/networkpolicies/{name} | 
[**watch_namespaced_network_policy_list**](DefaultApi.md#watch_namespaced_network_policy_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/networkpolicies | 
[**watch_namespaced_replica_set**](DefaultApi.md#watch_namespaced_replica_set) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/replicasets/{name} | 
[**watch_namespaced_replica_set_list**](DefaultApi.md#watch_namespaced_replica_set_list) | **GET** /apis/extensions/v1beta1/watch/namespaces/{namespace}/replicasets | 
[**watch_network_policy_list_for_all_namespaces**](DefaultApi.md#watch_network_policy_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/networkpolicies | 
[**watch_replica_set_list_for_all_namespaces**](DefaultApi.md#watch_replica_set_list_for_all_namespaces) | **GET** /apis/extensions/v1beta1/watch/replicasets | 
[**watch_third_party_resource**](DefaultApi.md#watch_third_party_resource) | **GET** /apis/extensions/v1beta1/watch/thirdpartyresources/{name} | 
[**watch_third_party_resource_list**](DefaultApi.md#watch_third_party_resource_list) | **GET** /apis/extensions/v1beta1/watch/thirdpartyresources | 


# **create_namespaced_daemon_set**
> V1beta1DaemonSet create_namespaced_daemon_set(namespace, body, pretty=pretty)



create a DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1DaemonSet() # V1beta1DaemonSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_daemon_set(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->create_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1DaemonSet**](V1beta1DaemonSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_deployment**
> V1beta1Deployment create_namespaced_deployment(namespace, body, pretty=pretty)



create a Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Deployment() # V1beta1Deployment | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_deployment(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->create_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Deployment**](V1beta1Deployment.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_deployment_rollback_rollback**
> V1beta1DeploymentRollback create_namespaced_deployment_rollback_rollback(body, name, namespace, pretty=pretty)



create rollback of a DeploymentRollback

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
body = k8sclient_v1beta1_extensions.V1beta1DeploymentRollback() # V1beta1DeploymentRollback | 
name = 'name_example' # str | name of the DeploymentRollback
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_deployment_rollback_rollback(body, name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->create_namespaced_deployment_rollback_rollback: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1DeploymentRollback**](V1beta1DeploymentRollback.md)|  | 
 **name** | **str**| name of the DeploymentRollback | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DeploymentRollback**](V1beta1DeploymentRollback.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_horizontal_pod_autoscaler**
> V1beta1HorizontalPodAutoscaler create_namespaced_horizontal_pod_autoscaler(namespace, body, pretty=pretty)



create a HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1HorizontalPodAutoscaler() # V1beta1HorizontalPodAutoscaler | 
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
 **body** | [**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_ingress**
> V1beta1Ingress create_namespaced_ingress(namespace, body, pretty=pretty)



create a Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Ingress() # V1beta1Ingress | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_ingress(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->create_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Ingress**](V1beta1Ingress.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_job**
> V1beta1Job create_namespaced_job(namespace, body, pretty=pretty)



create a Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Job() # V1beta1Job | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_job(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->create_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Job**](V1beta1Job.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_network_policy**
> V1beta1NetworkPolicy create_namespaced_network_policy(namespace, body, pretty=pretty)



create a NetworkPolicy

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1NetworkPolicy() # V1beta1NetworkPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_network_policy(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->create_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_replica_set**
> V1beta1ReplicaSet create_namespaced_replica_set(namespace, body, pretty=pretty)



create a ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1ReplicaSet() # V1beta1ReplicaSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_replica_set(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->create_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_third_party_resource**
> V1beta1ThirdPartyResource create_third_party_resource(body, pretty=pretty)



create a ThirdPartyResource

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
body = k8sclient_v1beta1_extensions.V1beta1ThirdPartyResource() # V1beta1ThirdPartyResource | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_third_party_resource(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->create_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_daemon_set**
> UnversionedStatus delete_namespaced_daemon_set(name, namespace, body, pretty=pretty)



delete a DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_namespaced_daemon_set(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->delete_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
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

# **delete_namespaced_deployment**
> UnversionedStatus delete_namespaced_deployment(name, namespace, body, pretty=pretty)



delete a Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_namespaced_deployment(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->delete_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
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

# **delete_namespaced_horizontal_pod_autoscaler**
> UnversionedStatus delete_namespaced_horizontal_pod_autoscaler(name, namespace, body, pretty=pretty)



delete a HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1DeleteOptions() # V1DeleteOptions | 
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

# **delete_namespaced_ingress**
> UnversionedStatus delete_namespaced_ingress(name, namespace, body, pretty=pretty)



delete a Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_namespaced_ingress(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->delete_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
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

# **delete_namespaced_job**
> UnversionedStatus delete_namespaced_job(name, namespace, body, pretty=pretty)



delete a Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_namespaced_job(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->delete_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
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

# **delete_namespaced_network_policy**
> UnversionedStatus delete_namespaced_network_policy(name, namespace, body, pretty=pretty)



delete a NetworkPolicy

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the NetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_namespaced_network_policy(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->delete_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetworkPolicy | 
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

# **delete_namespaced_replica_set**
> UnversionedStatus delete_namespaced_replica_set(name, namespace, body, pretty=pretty)



delete a ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_namespaced_replica_set(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->delete_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
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

# **delete_third_party_resource**
> UnversionedStatus delete_third_party_resource(name, body, pretty=pretty)



delete a ThirdPartyResource

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ThirdPartyResource
body = k8sclient_v1beta1_extensions.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_third_party_resource(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->delete_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ThirdPartyResource | 
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

# **deletecollection_namespaced_daemon_set**
> UnversionedStatus deletecollection_namespaced_daemon_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.deletecollection_namespaced_daemon_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->deletecollection_namespaced_daemon_set: %s\n" % e
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

# **deletecollection_namespaced_deployment**
> UnversionedStatus deletecollection_namespaced_deployment(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.deletecollection_namespaced_deployment(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->deletecollection_namespaced_deployment: %s\n" % e
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

# **deletecollection_namespaced_horizontal_pod_autoscaler**
> UnversionedStatus deletecollection_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
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

# **deletecollection_namespaced_ingress**
> UnversionedStatus deletecollection_namespaced_ingress(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.deletecollection_namespaced_ingress(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->deletecollection_namespaced_ingress: %s\n" % e
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

# **deletecollection_namespaced_job**
> UnversionedStatus deletecollection_namespaced_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.deletecollection_namespaced_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->deletecollection_namespaced_job: %s\n" % e
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

# **deletecollection_namespaced_network_policy**
> UnversionedStatus deletecollection_namespaced_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of NetworkPolicy

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.deletecollection_namespaced_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->deletecollection_namespaced_network_policy: %s\n" % e
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

# **deletecollection_namespaced_replica_set**
> UnversionedStatus deletecollection_namespaced_replica_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.deletecollection_namespaced_replica_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->deletecollection_namespaced_replica_set: %s\n" % e
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

# **deletecollection_third_party_resource**
> UnversionedStatus deletecollection_third_party_resource(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of ThirdPartyResource

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.deletecollection_third_party_resource(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->deletecollection_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()

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

# **list_daemon_set_for_all_namespaces**
> V1beta1DaemonSetList list_daemon_set_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_daemon_set_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_daemon_set_for_all_namespaces: %s\n" % e
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

[**V1beta1DaemonSetList**](V1beta1DaemonSetList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployment_for_all_namespaces**
> V1beta1DeploymentList list_deployment_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_deployment_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_deployment_for_all_namespaces: %s\n" % e
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

[**V1beta1DeploymentList**](V1beta1DeploymentList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_horizontal_pod_autoscaler_for_all_namespaces**
> V1beta1HorizontalPodAutoscalerList list_horizontal_pod_autoscaler_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
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

[**V1beta1HorizontalPodAutoscalerList**](V1beta1HorizontalPodAutoscalerList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ingress_for_all_namespaces**
> V1beta1IngressList list_ingress_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_ingress_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_ingress_for_all_namespaces: %s\n" % e
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

[**V1beta1IngressList**](V1beta1IngressList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_job_for_all_namespaces**
> V1beta1JobList list_job_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_job_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_job_for_all_namespaces: %s\n" % e
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

[**V1beta1JobList**](V1beta1JobList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_daemon_set**
> V1beta1DaemonSetList list_namespaced_daemon_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_daemon_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_namespaced_daemon_set: %s\n" % e
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

[**V1beta1DaemonSetList**](V1beta1DaemonSetList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_deployment**
> V1beta1DeploymentList list_namespaced_deployment(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_deployment(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_namespaced_deployment: %s\n" % e
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

[**V1beta1DeploymentList**](V1beta1DeploymentList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_horizontal_pod_autoscaler**
> V1beta1HorizontalPodAutoscalerList list_namespaced_horizontal_pod_autoscaler(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
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

[**V1beta1HorizontalPodAutoscalerList**](V1beta1HorizontalPodAutoscalerList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_ingress**
> V1beta1IngressList list_namespaced_ingress(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_ingress(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_namespaced_ingress: %s\n" % e
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

[**V1beta1IngressList**](V1beta1IngressList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_job**
> V1beta1JobList list_namespaced_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_namespaced_job: %s\n" % e
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

[**V1beta1JobList**](V1beta1JobList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_network_policy**
> V1beta1NetworkPolicyList list_namespaced_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind NetworkPolicy

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_namespaced_network_policy: %s\n" % e
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

[**V1beta1NetworkPolicyList**](V1beta1NetworkPolicyList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_replica_set**
> V1beta1ReplicaSetList list_namespaced_replica_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_replica_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_namespaced_replica_set: %s\n" % e
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

[**V1beta1ReplicaSetList**](V1beta1ReplicaSetList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_policy_for_all_namespaces**
> V1beta1NetworkPolicyList list_network_policy_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind NetworkPolicy

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_network_policy_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_network_policy_for_all_namespaces: %s\n" % e
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

[**V1beta1NetworkPolicyList**](V1beta1NetworkPolicyList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replica_set_for_all_namespaces**
> V1beta1ReplicaSetList list_replica_set_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_replica_set_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_replica_set_for_all_namespaces: %s\n" % e
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

[**V1beta1ReplicaSetList**](V1beta1ReplicaSetList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_third_party_resource**
> V1beta1ThirdPartyResourceList list_third_party_resource(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ThirdPartyResource

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_third_party_resource(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->list_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1beta1ThirdPartyResourceList**](V1beta1ThirdPartyResourceList.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_daemon_set**
> V1beta1DaemonSet patch_namespaced_daemon_set(name, namespace, body, pretty=pretty)



partially update the specified DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_daemon_set(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_daemon_set_status**
> V1beta1DaemonSet patch_namespaced_daemon_set_status(name, namespace, body, pretty=pretty)



partially update status of the specified DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_daemon_set_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_daemon_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_deployment**
> V1beta1Deployment patch_namespaced_deployment(name, namespace, body, pretty=pretty)



partially update the specified Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_deployment(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_deployment_status**
> V1beta1Deployment patch_namespaced_deployment_status(name, namespace, body, pretty=pretty)



partially update status of the specified Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_deployment_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_deployment_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_deployments_scale**
> V1beta1Scale patch_namespaced_deployments_scale(name, namespace, body, pretty=pretty)



partially update scale of the specified Scale

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_deployments_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_deployments_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_horizontal_pod_autoscaler**
> V1beta1HorizontalPodAutoscaler patch_namespaced_horizontal_pod_autoscaler(name, namespace, body, pretty=pretty)



partially update the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
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

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_horizontal_pod_autoscaler_status**
> V1beta1HorizontalPodAutoscaler patch_namespaced_horizontal_pod_autoscaler_status(name, namespace, body, pretty=pretty)



partially update status of the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
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

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_ingress**
> V1beta1Ingress patch_namespaced_ingress(name, namespace, body, pretty=pretty)



partially update the specified Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_ingress(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_ingress_status**
> V1beta1Ingress patch_namespaced_ingress_status(name, namespace, body, pretty=pretty)



partially update status of the specified Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_ingress_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_ingress_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_job**
> V1beta1Job patch_namespaced_job(name, namespace, body, pretty=pretty)



partially update the specified Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_job(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_job_status**
> V1beta1Job patch_namespaced_job_status(name, namespace, body, pretty=pretty)



partially update status of the specified Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_job_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_job_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_network_policy**
> V1beta1NetworkPolicy patch_namespaced_network_policy(name, namespace, body, pretty=pretty)



partially update the specified NetworkPolicy

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the NetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_network_policy(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetworkPolicy | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_replica_set**
> V1beta1ReplicaSet patch_namespaced_replica_set(name, namespace, body, pretty=pretty)



partially update the specified ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_replica_set(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_replica_set_status**
> V1beta1ReplicaSet patch_namespaced_replica_set_status(name, namespace, body, pretty=pretty)



partially update status of the specified ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_replica_set_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_replica_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_replicasets_scale**
> V1beta1Scale patch_namespaced_replicasets_scale(name, namespace, body, pretty=pretty)



partially update scale of the specified Scale

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_replicasets_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_replicasets_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_replicationcontrollers_scale**
> V1beta1Scale patch_namespaced_replicationcontrollers_scale(name, namespace, body, pretty=pretty)



partially update scale of the specified Scale

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_replicationcontrollers_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_namespaced_replicationcontrollers_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_third_party_resource**
> V1beta1ThirdPartyResource patch_third_party_resource(name, body, pretty=pretty)



partially update the specified ThirdPartyResource

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ThirdPartyResource
body = k8sclient_v1beta1_extensions.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_third_party_resource(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->patch_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ThirdPartyResource | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_daemon_set**
> V1beta1DaemonSet read_namespaced_daemon_set(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_daemon_set(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_daemon_set_status**
> V1beta1DaemonSet read_namespaced_daemon_set_status(name, namespace, pretty=pretty)



read status of the specified DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_daemon_set_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_daemon_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_deployment**
> V1beta1Deployment read_namespaced_deployment(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_deployment(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_deployment_status**
> V1beta1Deployment read_namespaced_deployment_status(name, namespace, pretty=pretty)



read status of the specified Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_deployment_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_deployment_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_deployments_scale**
> V1beta1Scale read_namespaced_deployments_scale(name, namespace, pretty=pretty)



read scale of the specified Scale

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_deployments_scale(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_deployments_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_horizontal_pod_autoscaler**
> V1beta1HorizontalPodAutoscaler read_namespaced_horizontal_pod_autoscaler(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
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

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_horizontal_pod_autoscaler_status**
> V1beta1HorizontalPodAutoscaler read_namespaced_horizontal_pod_autoscaler_status(name, namespace, pretty=pretty)



read status of the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
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

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_ingress**
> V1beta1Ingress read_namespaced_ingress(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_ingress(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_ingress_status**
> V1beta1Ingress read_namespaced_ingress_status(name, namespace, pretty=pretty)



read status of the specified Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_ingress_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_ingress_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_job**
> V1beta1Job read_namespaced_job(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_job(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_job_status**
> V1beta1Job read_namespaced_job_status(name, namespace, pretty=pretty)



read status of the specified Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_job_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_job_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_network_policy**
> V1beta1NetworkPolicy read_namespaced_network_policy(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified NetworkPolicy

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the NetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_network_policy(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetworkPolicy | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_replica_set**
> V1beta1ReplicaSet read_namespaced_replica_set(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_replica_set(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_replica_set_status**
> V1beta1ReplicaSet read_namespaced_replica_set_status(name, namespace, pretty=pretty)



read status of the specified ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_replica_set_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_replica_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_replicasets_scale**
> V1beta1Scale read_namespaced_replicasets_scale(name, namespace, pretty=pretty)



read scale of the specified Scale

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_replicasets_scale(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_replicasets_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_replicationcontrollers_scale**
> V1beta1Scale read_namespaced_replicationcontrollers_scale(name, namespace, pretty=pretty)



read scale of the specified Scale

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_replicationcontrollers_scale(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_namespaced_replicationcontrollers_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_third_party_resource**
> V1beta1ThirdPartyResource read_third_party_resource(name, pretty=pretty, exact=exact, export=export)



read the specified ThirdPartyResource

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ThirdPartyResource
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_third_party_resource(name, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->read_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ThirdPartyResource | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_daemon_set**
> V1beta1DaemonSet replace_namespaced_daemon_set(name, namespace, body, pretty=pretty)



replace the specified DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1DaemonSet() # V1beta1DaemonSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_daemon_set(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1DaemonSet**](V1beta1DaemonSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_daemon_set_status**
> V1beta1DaemonSet replace_namespaced_daemon_set_status(name, namespace, body, pretty=pretty)



replace status of the specified DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1DaemonSet() # V1beta1DaemonSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_daemon_set_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_daemon_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1DaemonSet**](V1beta1DaemonSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_deployment**
> V1beta1Deployment replace_namespaced_deployment(name, namespace, body, pretty=pretty)



replace the specified Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Deployment() # V1beta1Deployment | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_deployment(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Deployment**](V1beta1Deployment.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_deployment_status**
> V1beta1Deployment replace_namespaced_deployment_status(name, namespace, body, pretty=pretty)



replace status of the specified Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Deployment() # V1beta1Deployment | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_deployment_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_deployment_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Deployment**](V1beta1Deployment.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Deployment**](V1beta1Deployment.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_deployments_scale**
> V1beta1Scale replace_namespaced_deployments_scale(name, namespace, body, pretty=pretty)



replace scale of the specified Scale

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Scale() # V1beta1Scale | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_deployments_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_deployments_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Scale**](V1beta1Scale.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_horizontal_pod_autoscaler**
> V1beta1HorizontalPodAutoscaler replace_namespaced_horizontal_pod_autoscaler(name, namespace, body, pretty=pretty)



replace the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1HorizontalPodAutoscaler() # V1beta1HorizontalPodAutoscaler | 
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
 **body** | [**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_horizontal_pod_autoscaler_status**
> V1beta1HorizontalPodAutoscaler replace_namespaced_horizontal_pod_autoscaler_status(name, namespace, body, pretty=pretty)



replace status of the specified HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the HorizontalPodAutoscaler
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1HorizontalPodAutoscaler() # V1beta1HorizontalPodAutoscaler | 
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
 **body** | [**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1HorizontalPodAutoscaler**](V1beta1HorizontalPodAutoscaler.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_ingress**
> V1beta1Ingress replace_namespaced_ingress(name, namespace, body, pretty=pretty)



replace the specified Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Ingress() # V1beta1Ingress | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_ingress(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Ingress**](V1beta1Ingress.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_ingress_status**
> V1beta1Ingress replace_namespaced_ingress_status(name, namespace, body, pretty=pretty)



replace status of the specified Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Ingress() # V1beta1Ingress | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_ingress_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_ingress_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Ingress**](V1beta1Ingress.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_job**
> V1beta1Job replace_namespaced_job(name, namespace, body, pretty=pretty)



replace the specified Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Job() # V1beta1Job | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_job(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Job**](V1beta1Job.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_job_status**
> V1beta1Job replace_namespaced_job_status(name, namespace, body, pretty=pretty)



replace status of the specified Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Job() # V1beta1Job | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_job_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_job_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Job**](V1beta1Job.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Job**](V1beta1Job.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_network_policy**
> V1beta1NetworkPolicy replace_namespaced_network_policy(name, namespace, body, pretty=pretty)



replace the specified NetworkPolicy

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the NetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1NetworkPolicy() # V1beta1NetworkPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_network_policy(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetworkPolicy | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replica_set**
> V1beta1ReplicaSet replace_namespaced_replica_set(name, namespace, body, pretty=pretty)



replace the specified ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1ReplicaSet() # V1beta1ReplicaSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_replica_set(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replica_set_status**
> V1beta1ReplicaSet replace_namespaced_replica_set_status(name, namespace, body, pretty=pretty)



replace status of the specified ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1ReplicaSet() # V1beta1ReplicaSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_replica_set_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_replica_set_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replicasets_scale**
> V1beta1Scale replace_namespaced_replicasets_scale(name, namespace, body, pretty=pretty)



replace scale of the specified Scale

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Scale() # V1beta1Scale | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_replicasets_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_replicasets_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Scale**](V1beta1Scale.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replicationcontrollers_scale**
> V1beta1Scale replace_namespaced_replicationcontrollers_scale(name, namespace, body, pretty=pretty)



replace scale of the specified Scale

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient_v1beta1_extensions.V1beta1Scale() # V1beta1Scale | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_replicationcontrollers_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_namespaced_replicationcontrollers_scale: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Scale**](V1beta1Scale.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_third_party_resource**
> V1beta1ThirdPartyResource replace_third_party_resource(name, body, pretty=pretty)



replace the specified ThirdPartyResource

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ThirdPartyResource
body = k8sclient_v1beta1_extensions.V1beta1ThirdPartyResource() # V1beta1ThirdPartyResource | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_third_party_resource(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->replace_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ThirdPartyResource | 
 **body** | [**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

[TokenBearer](../README.md#TokenBearer), [HTTPBasic](../README.md#HTTPBasic), [LoopbackTokenBearer](../README.md#LoopbackTokenBearer)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_daemon_set_list_for_all_namespaces**
> VersionedEvent watch_daemon_set_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_daemon_set_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_daemon_set_list_for_all_namespaces: %s\n" % e
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

# **watch_deployment_list_for_all_namespaces**
> VersionedEvent watch_deployment_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_deployment_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_deployment_list_for_all_namespaces: %s\n" % e
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

# **watch_horizontal_pod_autoscaler_list_for_all_namespaces**
> VersionedEvent watch_horizontal_pod_autoscaler_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
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

# **watch_ingress_list_for_all_namespaces**
> VersionedEvent watch_ingress_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_ingress_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_ingress_list_for_all_namespaces: %s\n" % e
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

# **watch_job_list_for_all_namespaces**
> VersionedEvent watch_job_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_job_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_job_list_for_all_namespaces: %s\n" % e
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

# **watch_namespaced_daemon_set**
> VersionedEvent watch_namespaced_daemon_set(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_daemon_set(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_daemon_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
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

# **watch_namespaced_daemon_set_list**
> VersionedEvent watch_namespaced_daemon_set_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of DaemonSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_daemon_set_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_daemon_set_list: %s\n" % e
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

# **watch_namespaced_deployment**
> VersionedEvent watch_namespaced_deployment(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_deployment(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_deployment: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
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

# **watch_namespaced_deployment_list**
> VersionedEvent watch_namespaced_deployment_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of Deployment

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_deployment_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_deployment_list: %s\n" % e
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

# **watch_namespaced_horizontal_pod_autoscaler**
> VersionedEvent watch_namespaced_horizontal_pod_autoscaler(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind HorizontalPodAutoscaler

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
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
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
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

# **watch_namespaced_ingress**
> VersionedEvent watch_namespaced_ingress(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_ingress(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_ingress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
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

# **watch_namespaced_ingress_list**
> VersionedEvent watch_namespaced_ingress_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of Ingress

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_ingress_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_ingress_list: %s\n" % e
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

# **watch_namespaced_job**
> VersionedEvent watch_namespaced_job(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_job(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
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

# **watch_namespaced_job_list**
> VersionedEvent watch_namespaced_job_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of Job

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_job_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_job_list: %s\n" % e
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

# **watch_namespaced_network_policy**
> VersionedEvent watch_namespaced_network_policy(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind NetworkPolicy

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the NetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_network_policy(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_network_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetworkPolicy | 
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

# **watch_namespaced_network_policy_list**
> VersionedEvent watch_namespaced_network_policy_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of NetworkPolicy

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_network_policy_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_network_policy_list: %s\n" % e
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

# **watch_namespaced_replica_set**
> VersionedEvent watch_namespaced_replica_set(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_replica_set(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_replica_set: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
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

# **watch_namespaced_replica_set_list**
> VersionedEvent watch_namespaced_replica_set_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_replica_set_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_namespaced_replica_set_list: %s\n" % e
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

# **watch_network_policy_list_for_all_namespaces**
> VersionedEvent watch_network_policy_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of NetworkPolicy

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_network_policy_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_network_policy_list_for_all_namespaces: %s\n" % e
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

# **watch_replica_set_list_for_all_namespaces**
> VersionedEvent watch_replica_set_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of ReplicaSet

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_replica_set_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_replica_set_list_for_all_namespaces: %s\n" % e
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

# **watch_third_party_resource**
> VersionedEvent watch_third_party_resource(name, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind ThirdPartyResource

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
name = 'name_example' # str | name of the ThirdPartyResource
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_third_party_resource(name, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_third_party_resource: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ThirdPartyResource | 
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

# **watch_third_party_resource_list**
> VersionedEvent watch_third_party_resource_list(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of ThirdPartyResource

### Example 
```python
import time
import k8sclient_v1beta1_extensions
from k8sclient_v1beta1_extensions.rest import ApiException
from pprint import pprint

# Configure API key authorization: TokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'
# Configure HTTP basic authorization: HTTPBasic
k8sclient_v1beta1_extensions.configuration.username = 'YOUR_USERNAME'
k8sclient_v1beta1_extensions.configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: LoopbackTokenBearer
k8sclient_v1beta1_extensions.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient_v1beta1_extensions.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient_v1beta1_extensions.DefaultApi()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_third_party_resource_list(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DefaultApi->watch_third_party_resource_list: %s\n" % e
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

