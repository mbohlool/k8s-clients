# k8sclient.V1beta1AuthenticationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authentication_v1beta1_token_review**](V1beta1AuthenticationApi.md#create_authentication_v1beta1_token_review) | **POST** /apis/authentication.k8s.io/v1beta1/tokenreviews | 
[**get_authentication_v1beta1_api_resources**](V1beta1AuthenticationApi.md#get_authentication_v1beta1_api_resources) | **GET** /apis/authentication.k8s.io/v1beta1/ | 


# **create_authentication_v1beta1_token_review**
> V1beta1TokenReview create_authentication_v1beta1_token_review(body, pretty=pretty)



create a TokenReview

### Example 
```python
from __future__ import print_statement
import time
import k8sclient
from k8sclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
k8sclient.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient.V1beta1AuthenticationApi()
body = k8sclient.V1beta1TokenReview() # V1beta1TokenReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_authentication_v1beta1_token_review(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1beta1AuthenticationApi->create_authentication_v1beta1_token_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1TokenReview**](V1beta1TokenReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1TokenReview**](V1beta1TokenReview.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_v1beta1_api_resources**
> UnversionedAPIResourceList get_authentication_v1beta1_api_resources()



get available resources

### Example 
```python
from __future__ import print_statement
import time
import k8sclient
from k8sclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
k8sclient.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient.V1beta1AuthenticationApi()

try: 
    api_response = api_instance.get_authentication_v1beta1_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1beta1AuthenticationApi->get_authentication_v1beta1_api_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnversionedAPIResourceList**](UnversionedAPIResourceList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

