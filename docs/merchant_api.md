# MerchantApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**merchantIdList**](MerchantApi.md#merchantIdList) | **POST**  /v3/merchant/id_list  |
[**merchantErrors**](MerchantApi.md#merchantErrors) | **POST**  /v3/merchant/errors  |
[**merchantGoogleLanguages**](MerchantApi.md#merchantGoogleLanguages) | **GET**  /v3/merchant/google/languages  |
[**merchantGoogleLocations**](MerchantApi.md#merchantGoogleLocations) | **GET**  /v3/merchant/google/locations  |
[**merchantGoogleLocationsCountry**](MerchantApi.md#merchantGoogleLocationsCountry) | **GET**  /v3/merchant/google/locations/{country}  |
[**googleProductsTaskPost**](MerchantApi.md#googleProductsTaskPost) | **POST**  /v3/merchant/google/products/task_post  |
[**googleProductsTasksReady**](MerchantApi.md#googleProductsTasksReady) | **GET**  /v3/merchant/google/products/tasks_ready  |
[**merchantTasksReady**](MerchantApi.md#merchantTasksReady) | **GET**  /v3/merchant/tasks_ready  |
[**googleProductsTaskGetAdvanced**](MerchantApi.md#googleProductsTaskGetAdvanced) | **GET**  /v3/merchant/google/products/task_get/advanced/{id}  |
[**googleProductsTaskGetHtml**](MerchantApi.md#googleProductsTaskGetHtml) | **GET**  /v3/merchant/google/products/task_get/html/{id}  |
[**googleSellersTaskPost**](MerchantApi.md#googleSellersTaskPost) | **POST**  /v3/merchant/google/sellers/task_post  |
[**googleSellersTasksReady**](MerchantApi.md#googleSellersTasksReady) | **GET**  /v3/merchant/google/sellers/tasks_ready  |
[**googleSellersTaskGetAdvanced**](MerchantApi.md#googleSellersTaskGetAdvanced) | **GET**  /v3/merchant/google/sellers/task_get/advanced/{id}  |
[**googleProductInfoTaskPost**](MerchantApi.md#googleProductInfoTaskPost) | **POST**  /v3/merchant/google/product_info/task_post  |
[**googleProductInfoTasksReady**](MerchantApi.md#googleProductInfoTasksReady) | **GET**  /v3/merchant/google/product_info/tasks_ready  |
[**googleProductInfoTaskGetAdvanced**](MerchantApi.md#googleProductInfoTaskGetAdvanced) | **GET**  /v3/merchant/google/product_info/task_get/advanced/{id}  |
[**googleSellersAdUrl**](MerchantApi.md#googleSellersAdUrl) | **GET**  /v3/merchant/google/sellers/ad_url/{shop_ad_aclk}  |
[**merchantAmazonLocations**](MerchantApi.md#merchantAmazonLocations) | **GET**  /v3/merchant/amazon/locations  |
[**merchantAmazonLocationsCountry**](MerchantApi.md#merchantAmazonLocationsCountry) | **GET**  /v3/merchant/amazon/locations/{country}  |
[**merchantAmazonLanguages**](MerchantApi.md#merchantAmazonLanguages) | **GET**  /v3/merchant/amazon/languages  |
[**amazonProductsTaskPost**](MerchantApi.md#amazonProductsTaskPost) | **POST**  /v3/merchant/amazon/products/task_post  |
[**amazonProductsTasksReady**](MerchantApi.md#amazonProductsTasksReady) | **GET**  /v3/merchant/amazon/products/tasks_ready  |
[**amazonProductsTaskGetAdvanced**](MerchantApi.md#amazonProductsTaskGetAdvanced) | **GET**  /v3/merchant/amazon/products/task_get/advanced/{id}  |
[**amazonProductsTaskGetHtml**](MerchantApi.md#amazonProductsTaskGetHtml) | **GET**  /v3/merchant/amazon/products/task_get/html/{id}  |
[**amazonAsinTaskPost**](MerchantApi.md#amazonAsinTaskPost) | **POST**  /v3/merchant/amazon/asin/task_post  |
[**amazonAsinTasksReady**](MerchantApi.md#amazonAsinTasksReady) | **GET**  /v3/merchant/amazon/asin/tasks_ready  |
[**amazonAsinTaskGetAdvanced**](MerchantApi.md#amazonAsinTaskGetAdvanced) | **GET**  /v3/merchant/amazon/asin/task_get/advanced/{id}  |
[**amazonAsinTaskGetHtml**](MerchantApi.md#amazonAsinTaskGetHtml) | **GET**  /v3/merchant/amazon/asin/task_get/html/{id}  |
[**amazonSellersTaskPost**](MerchantApi.md#amazonSellersTaskPost) | **POST**  /v3/merchant/amazon/sellers/task_post  |
[**amazonSellersTasksReady**](MerchantApi.md#amazonSellersTasksReady) | **GET**  /v3/merchant/amazon/sellers/tasks_ready  |
[**amazonSellersTaskGetAdvanced**](MerchantApi.md#amazonSellersTaskGetAdvanced) | **GET**  /v3/merchant/amazon/sellers/task_get/advanced/{id}  |
[**amazonSellersTaskGetHtml**](MerchantApi.md#amazonSellersTaskGetHtml) | **GET**  /v3/merchant/amazon/sellers/task_get/html/{id}  |
[**amazonReviewsTaskPost**](MerchantApi.md#amazonReviewsTaskPost) | **POST**  /v3/merchant/amazon/reviews/task_post  |
[**amazonReviewsTasksReady**](MerchantApi.md#amazonReviewsTasksReady) | **GET**  /v3/merchant/amazon/reviews/tasks_ready  |
[**amazonReviewsTaskGetAdvanced**](MerchantApi.md#amazonReviewsTaskGetAdvanced) | **GET**  /v3/merchant/amazon/reviews/task_get/advanced/{id}  |
[**amazonReviewsTaskGetHtml**](MerchantApi.md#amazonReviewsTaskGetHtml) | **GET**  /v3/merchant/amazon/reviews/task_get/html/{id}  |

<a id="merchantIdList"></a>
# **merchantIdList**
> MerchantIdListResponseInfo merchantIdList()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_merchant_id_list_request_info import List[Optional[MerchantIdListRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.merchant_id_list([MerchantIdListRequestInfo(
                datetime_from="2025-08-10 11:04:49 +00:00",
                datetime_to="2025-10-10 11:04:49 +00:00",
                limit=100,
                offset=0,
                sort="desc",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[MerchantIdListRequestInfo]]&gt;**](List[Optional[MerchantIdListRequestInfo]].md)|  | [optional] |



### Return type

[**MerchantIdListResponseInfo**](MerchantIdListResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="merchantErrors"></a>
# **merchantErrors**
> MerchantErrorsResponseInfo merchantErrors()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_merchant_errors_request_info import List[Optional[MerchantErrorsRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.merchant_errors([MerchantErrorsRequestInfo(
                limit=10,
                offset=0,
                filtered_function="pingback_url",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[MerchantErrorsRequestInfo]]&gt;**](List[Optional[MerchantErrorsRequestInfo]].md)|  | [optional] |



### Return type

[**MerchantErrorsResponseInfo**](MerchantErrorsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="merchantGoogleLanguages"></a>
# **merchantGoogleLanguages**
> MerchantGoogleLanguagesResponseInfo merchantGoogleLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.merchant_google_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantGoogleLanguagesResponseInfo**](MerchantGoogleLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="merchantGoogleLocations"></a>
# **merchantGoogleLocations**
> MerchantGoogleLocationsResponseInfo merchantGoogleLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.merchant_google_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantGoogleLocationsResponseInfo**](MerchantGoogleLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="merchantGoogleLocationsCountry"></a>
# **merchantGoogleLocationsCountry**
> MerchantGoogleLocationsCountryResponseInfo merchantGoogleLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        country = "us"
        response = merchant_api.merchant_google_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantGoogleLocationsCountryResponseInfo**](MerchantGoogleLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleProductsTaskPost"></a>
# **googleProductsTaskPost**
> MerchantGoogleProductsTaskPostResponseInfo googleProductsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_merchant_google_products_task_post_request_info import List[Optional[MerchantGoogleProductsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.google_products_task_post([MerchantGoogleProductsTaskPostRequestInfo(
                keyword="iphone",
                location_code=2840,
                language_code="en",
                price_min=5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[MerchantGoogleProductsTaskPostRequestInfo]]&gt;**](List[Optional[MerchantGoogleProductsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**MerchantGoogleProductsTaskPostResponseInfo**](MerchantGoogleProductsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleProductsTasksReady"></a>
# **googleProductsTasksReady**
> MerchantGoogleProductsTasksReadyResponseInfo googleProductsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.google_products_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantGoogleProductsTasksReadyResponseInfo**](MerchantGoogleProductsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="merchantTasksReady"></a>
# **merchantTasksReady**
> MerchantTasksReadyResponseInfo merchantTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.merchant_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantTasksReadyResponseInfo**](MerchantTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleProductsTaskGetAdvanced"></a>
# **googleProductsTaskGetAdvanced**
> MerchantGoogleProductsTaskGetAdvancedResponseInfo googleProductsTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.google_products_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantGoogleProductsTaskGetAdvancedResponseInfo**](MerchantGoogleProductsTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleProductsTaskGetHtml"></a>
# **googleProductsTaskGetHtml**
> MerchantGoogleProductsTaskGetHtmlResponseInfo googleProductsTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.google_products_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantGoogleProductsTaskGetHtmlResponseInfo**](MerchantGoogleProductsTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleSellersTaskPost"></a>
# **googleSellersTaskPost**
> MerchantGoogleSellersTaskPostResponseInfo googleSellersTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_merchant_google_sellers_task_post_request_info import List[Optional[MerchantGoogleSellersTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.google_sellers_task_post([MerchantGoogleSellersTaskPostRequestInfo(
                product_id="1113158713975221117",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[MerchantGoogleSellersTaskPostRequestInfo]]&gt;**](List[Optional[MerchantGoogleSellersTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**MerchantGoogleSellersTaskPostResponseInfo**](MerchantGoogleSellersTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleSellersTasksReady"></a>
# **googleSellersTasksReady**
> MerchantGoogleSellersTasksReadyResponseInfo googleSellersTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.google_sellers_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantGoogleSellersTasksReadyResponseInfo**](MerchantGoogleSellersTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleSellersTaskGetAdvanced"></a>
# **googleSellersTaskGetAdvanced**
> MerchantGoogleSellersTaskGetAdvancedResponseInfo googleSellersTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.google_sellers_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantGoogleSellersTaskGetAdvancedResponseInfo**](MerchantGoogleSellersTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleProductInfoTaskPost"></a>
# **googleProductInfoTaskPost**
> MerchantGoogleProductInfoTaskPostResponseInfo googleProductInfoTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_merchant_google_product_info_task_post_request_info import List[Optional[MerchantGoogleProductInfoTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.google_product_info_task_post([MerchantGoogleProductInfoTaskPostRequestInfo(
                product_id="1113158713975221117",
                location_code=2840,
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[MerchantGoogleProductInfoTaskPostRequestInfo]]&gt;**](List[Optional[MerchantGoogleProductInfoTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**MerchantGoogleProductInfoTaskPostResponseInfo**](MerchantGoogleProductInfoTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleProductInfoTasksReady"></a>
# **googleProductInfoTasksReady**
> MerchantGoogleProductInfoTasksReadyResponseInfo googleProductInfoTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.google_product_info_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantGoogleProductInfoTasksReadyResponseInfo**](MerchantGoogleProductInfoTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleProductInfoTaskGetAdvanced"></a>
# **googleProductInfoTaskGetAdvanced**
> MerchantGoogleProductInfoTaskGetAdvancedResponseInfo googleProductInfoTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.google_product_info_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantGoogleProductInfoTaskGetAdvancedResponseInfo**](MerchantGoogleProductInfoTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleSellersAdUrl"></a>
# **googleSellersAdUrl**
> MerchantGoogleSellersAdUrlResponseInfo googleSellersAdUrl()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        shop_ad_aclk = "DChcSEwiSl5TKpbPoAhVFmdUKHfa_B_wYABADGgJ3cw&sig"
        response = merchant_api.google_sellers_ad_url(shop_ad_aclk)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantGoogleSellersAdUrlResponseInfo**](MerchantGoogleSellersAdUrlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="merchantAmazonLocations"></a>
# **merchantAmazonLocations**
> MerchantAmazonLocationsResponseInfo merchantAmazonLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.merchant_amazon_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonLocationsResponseInfo**](MerchantAmazonLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="merchantAmazonLocationsCountry"></a>
# **merchantAmazonLocationsCountry**
> MerchantAmazonLocationsCountryResponseInfo merchantAmazonLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        country = "us"
        response = merchant_api.merchant_amazon_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonLocationsCountryResponseInfo**](MerchantAmazonLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="merchantAmazonLanguages"></a>
# **merchantAmazonLanguages**
> MerchantAmazonLanguagesResponseInfo merchantAmazonLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.merchant_amazon_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonLanguagesResponseInfo**](MerchantAmazonLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonProductsTaskPost"></a>
# **amazonProductsTaskPost**
> MerchantAmazonProductsTaskPostResponseInfo amazonProductsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_merchant_amazon_products_task_post_request_info import List[Optional[MerchantAmazonProductsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.amazon_products_task_post([MerchantAmazonProductsTaskPostRequestInfo(
                keyword="shoes",
                location_code=2840,
                language_code="en_US",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[MerchantAmazonProductsTaskPostRequestInfo]]&gt;**](List[Optional[MerchantAmazonProductsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**MerchantAmazonProductsTaskPostResponseInfo**](MerchantAmazonProductsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonProductsTasksReady"></a>
# **amazonProductsTasksReady**
> MerchantAmazonProductsTasksReadyResponseInfo amazonProductsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.amazon_products_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonProductsTasksReadyResponseInfo**](MerchantAmazonProductsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonProductsTaskGetAdvanced"></a>
# **amazonProductsTaskGetAdvanced**
> MerchantAmazonProductsTaskGetAdvancedResponseInfo amazonProductsTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.amazon_products_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonProductsTaskGetAdvancedResponseInfo**](MerchantAmazonProductsTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonProductsTaskGetHtml"></a>
# **amazonProductsTaskGetHtml**
> MerchantAmazonProductsTaskGetHtmlResponseInfo amazonProductsTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.amazon_products_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonProductsTaskGetHtmlResponseInfo**](MerchantAmazonProductsTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonAsinTaskPost"></a>
# **amazonAsinTaskPost**
> MerchantAmazonAsinTaskPostResponseInfo amazonAsinTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_merchant_amazon_asin_task_post_request_info import List[Optional[MerchantAmazonAsinTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.amazon_asin_task_post([MerchantAmazonAsinTaskPostRequestInfo(
                asin="B0756FCPPN",
                location_code=2840,
                language_code="en_US",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[MerchantAmazonAsinTaskPostRequestInfo]]&gt;**](List[Optional[MerchantAmazonAsinTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**MerchantAmazonAsinTaskPostResponseInfo**](MerchantAmazonAsinTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonAsinTasksReady"></a>
# **amazonAsinTasksReady**
> MerchantAmazonAsinTasksReadyResponseInfo amazonAsinTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.amazon_asin_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonAsinTasksReadyResponseInfo**](MerchantAmazonAsinTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonAsinTaskGetAdvanced"></a>
# **amazonAsinTaskGetAdvanced**
> MerchantAmazonAsinTaskGetAdvancedResponseInfo amazonAsinTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.amazon_asin_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonAsinTaskGetAdvancedResponseInfo**](MerchantAmazonAsinTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonAsinTaskGetHtml"></a>
# **amazonAsinTaskGetHtml**
> MerchantAmazonAsinTaskGetHtmlResponseInfo amazonAsinTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.amazon_asin_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonAsinTaskGetHtmlResponseInfo**](MerchantAmazonAsinTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonSellersTaskPost"></a>
# **amazonSellersTaskPost**
> MerchantAmazonSellersTaskPostResponseInfo amazonSellersTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_merchant_amazon_sellers_task_post_request_info import List[Optional[MerchantAmazonSellersTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.amazon_sellers_task_post([MerchantAmazonSellersTaskPostRequestInfo(
                asin="B085RFFC9Q",
                location_code=2840,
                language_code="en_US",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[MerchantAmazonSellersTaskPostRequestInfo]]&gt;**](List[Optional[MerchantAmazonSellersTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**MerchantAmazonSellersTaskPostResponseInfo**](MerchantAmazonSellersTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonSellersTasksReady"></a>
# **amazonSellersTasksReady**
> MerchantAmazonSellersTasksReadyResponseInfo amazonSellersTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.amazon_sellers_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonSellersTasksReadyResponseInfo**](MerchantAmazonSellersTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonSellersTaskGetAdvanced"></a>
# **amazonSellersTaskGetAdvanced**
> MerchantAmazonSellersTaskGetAdvancedResponseInfo amazonSellersTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.amazon_sellers_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonSellersTaskGetAdvancedResponseInfo**](MerchantAmazonSellersTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonSellersTaskGetHtml"></a>
# **amazonSellersTaskGetHtml**
> MerchantAmazonSellersTaskGetHtmlResponseInfo amazonSellersTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.amazon_sellers_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonSellersTaskGetHtmlResponseInfo**](MerchantAmazonSellersTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonReviewsTaskPost"></a>
# **amazonReviewsTaskPost**
> MerchantAmazonReviewsTaskPostResponseInfo amazonReviewsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_merchant_amazon_reviews_task_post_request_info import List[Optional[MerchantAmazonReviewsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.amazon_reviews_task_post([MerchantAmazonReviewsTaskPostRequestInfo(
                asin="B0773ZY26F",
                location_code=2840,
                language_code="en_US",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[MerchantAmazonReviewsTaskPostRequestInfo]]&gt;**](List[Optional[MerchantAmazonReviewsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**MerchantAmazonReviewsTaskPostResponseInfo**](MerchantAmazonReviewsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonReviewsTasksReady"></a>
# **amazonReviewsTasksReady**
> MerchantAmazonReviewsTasksReadyResponseInfo amazonReviewsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        response = merchant_api.amazon_reviews_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonReviewsTasksReadyResponseInfo**](MerchantAmazonReviewsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonReviewsTaskGetAdvanced"></a>
# **amazonReviewsTaskGetAdvanced**
> MerchantAmazonReviewsTaskGetAdvancedResponseInfo amazonReviewsTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.amazon_reviews_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonReviewsTaskGetAdvancedResponseInfo**](MerchantAmazonReviewsTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonReviewsTaskGetHtml"></a>
# **amazonReviewsTaskGetHtml**
> MerchantAmazonReviewsTaskGetHtmlResponseInfo amazonReviewsTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        merchant_api = MerchantApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = merchant_api.amazon_reviews_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**MerchantAmazonReviewsTaskGetHtmlResponseInfo**](MerchantAmazonReviewsTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |