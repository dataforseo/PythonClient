# AppendixApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**userData**](AppendixApi.md#userData) | **GET**  /v3/appendix/user_data  |
[**appendixErrors**](AppendixApi.md#appendixErrors) | **GET**  /v3/appendix/errors  |
[**webhookResend**](AppendixApi.md#webhookResend) | **POST**  /v3/appendix/webhook_resend  |
[**appendixStatus**](AppendixApi.md#appendixStatus) | **GET**  /v3/appendix/status  |

<a id="userData"></a>
# **userData**
> AppendixUserDataResponseInfo userData()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.appendix_api import AppendixApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        appendix_api = AppendixApi(api_client)

        response = appendix_api.user_data()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppendixUserDataResponseInfo**](AppendixUserDataResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appendixErrors"></a>
# **appendixErrors**
> AppendixErrorsResponseInfo appendixErrors()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.appendix_api import AppendixApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        appendix_api = AppendixApi(api_client)

        response = appendix_api.appendix_errors()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppendixErrorsResponseInfo**](AppendixErrorsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="webhookResend"></a>
# **webhookResend**
> AppendixWebhookResendResponseInfo webhookResend()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.appendix_api import AppendixApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_appendix_webhook_resend_request_info import List[Optional[AppendixWebhookResendRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        appendix_api = AppendixApi(api_client)

        response = appendix_api.webhook_resend([AppendixWebhookResendRequestInfo(
                id="00000000-0000-0000-0000-000000000000",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AppendixWebhookResendRequestInfo]]&gt;**](List[Optional[AppendixWebhookResendRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="appendixStatus"></a>
# **appendixStatus**
> AppendixStatusResponseInfo appendixStatus()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.appendix_api import AppendixApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        appendix_api = AppendixApi(api_client)

        response = appendix_api.appendix_status()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppendixStatusResponseInfo**](AppendixStatusResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |