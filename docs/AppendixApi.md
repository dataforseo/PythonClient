# dataforseo_client.AppendixApi

All URIs are relative to *https://api.dataforseo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appendix_errors**](AppendixApi.md#appendix_errors) | **GET** /v3/appendix/errors | 
[**appendix_status**](AppendixApi.md#appendix_status) | **GET** /v3/appendix/status | 
[**user_data**](AppendixApi.md#user_data) | **GET** /v3/appendix/user_data | 
[**webhook_resend**](AppendixApi.md#webhook_resend) | **POST** /v3/appendix/webhook_resend | 


# **appendix_errors**
> AppendixErrorsResponseInfo appendix_errors()



This endpoint returns a list of possible DataForSEO API errors and general status codes. Below you will find a list of HTTP response codes and internal messages. We recommend storing the data connected to error codes in your application log and designing a necessary system for handling related exceptional or error conditions. for more info please visit 'https://docs.dataforseo.com/v3/appendix/errors/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.appendix_errors_response_info import AppendixErrorsResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.AppendixApi(api_client)

    try:
        api_response = api_instance.appendix_errors()
        print("The response of AppendixApi->appendix_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppendixApi->appendix_errors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppendixErrorsResponseInfo**](AppendixErrorsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **appendix_status**
> AppendixStatusResponseInfo appendix_status()



By calling this API you will receive detailed information about the current status of all our APIs and endpoints. You will also get a full issue description if a problem occurs. for more info please visit 'https://docs.dataforseo.com/v3/appendix/status/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.appendix_status_response_info import AppendixStatusResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.AppendixApi(api_client)

    try:
        api_response = api_instance.appendix_status()
        print("The response of AppendixApi->appendix_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppendixApi->appendix_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppendixStatusResponseInfo**](AppendixStatusResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_data**
> AppendixUserDataResponseInfo user_data()



You will receive detailed information about your API usage, prices, spending and other account details by calling this API. for more info please visit 'https://docs.dataforseo.com/v3/appendix/user_data/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.appendix_user_data_response_info import AppendixUserDataResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.AppendixApi(api_client)

    try:
        api_response = api_instance.user_data()
        print("The response of AppendixApi->user_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppendixApi->user_data: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AppendixUserDataResponseInfo**](AppendixUserDataResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_resend**
> AppendixWebhookResendResponseInfo webhook_resend(appendix_webhook_resend_request_info=appendix_webhook_resend_request_info)



Using this endpoint you can resend webhooks (pingbacks and postbacks) for up to 100 specified tasks. Note: Your account will not be double-charged for resending a webhook. for more info please visit 'https://docs.dataforseo.com/v3/appendix/webhook_resend/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.appendix_webhook_resend_request_info import AppendixWebhookResendRequestInfo
from dataforseo_client.models.appendix_webhook_resend_response_info import AppendixWebhookResendResponseInfo
from dataforseo_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dataforseo.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dataforseo_client.Configuration(
    host = "https://api.dataforseo.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dataforseo_client.AppendixApi(api_client)
    appendix_webhook_resend_request_info = [dataforseo_client.AppendixWebhookResendRequestInfo()] # List[AppendixWebhookResendRequestInfo] |  (optional)

    try:
        api_response = api_instance.webhook_resend(appendix_webhook_resend_request_info=appendix_webhook_resend_request_info)
        print("The response of AppendixApi->webhook_resend:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppendixApi->webhook_resend: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appendix_webhook_resend_request_info** | [**List[AppendixWebhookResendRequestInfo]**](AppendixWebhookResendRequestInfo.md)|  | [optional] 

### Return type

[**AppendixWebhookResendResponseInfo**](AppendixWebhookResendResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

