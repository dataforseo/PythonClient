# AppDataApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**appDataIdList**](AppDataApi.md#appDataIdList) | **POST**  /v3/app_data/id_list  |
[**appDataErrors**](AppDataApi.md#appDataErrors) | **POST**  /v3/app_data/errors  |
[**googleCategories**](AppDataApi.md#googleCategories) | **GET**  /v3/app_data/google/categories  |
[**appDataGoogleLocations**](AppDataApi.md#appDataGoogleLocations) | **GET**  /v3/app_data/google/locations  |
[**appDataGoogleLocationsCountry**](AppDataApi.md#appDataGoogleLocationsCountry) | **GET**  /v3/app_data/google/locations/{country}  |
[**appDataGoogleLanguages**](AppDataApi.md#appDataGoogleLanguages) | **GET**  /v3/app_data/google/languages  |
[**googleAppSearchesTaskPost**](AppDataApi.md#googleAppSearchesTaskPost) | **POST**  /v3/app_data/google/app_searches/task_post  |
[**googleAppSearchesTasksReady**](AppDataApi.md#googleAppSearchesTasksReady) | **GET**  /v3/app_data/google/app_searches/tasks_ready  |
[**appDataTasksReady**](AppDataApi.md#appDataTasksReady) | **GET**  /v3/app_data/tasks_ready  |
[**googleAppSearchesTaskGetAdvanced**](AppDataApi.md#googleAppSearchesTaskGetAdvanced) | **GET**  /v3/app_data/google/app_searches/task_get/advanced/{id}  |
[**googleAppSearchesTaskGetHtml**](AppDataApi.md#googleAppSearchesTaskGetHtml) | **GET**  /v3/app_data/google/app_searches/task_get/html/{id}  |
[**googleAppListTaskPost**](AppDataApi.md#googleAppListTaskPost) | **POST**  /v3/app_data/google/app_list/task_post  |
[**googleAppListTasksReady**](AppDataApi.md#googleAppListTasksReady) | **GET**  /v3/app_data/google/app_list/tasks_ready  |
[**googleAppListTaskGetAdvanced**](AppDataApi.md#googleAppListTaskGetAdvanced) | **GET**  /v3/app_data/google/app_list/task_get/advanced/{id}  |
[**googleAppListTaskGetHtml**](AppDataApi.md#googleAppListTaskGetHtml) | **GET**  /v3/app_data/google/app_list/task_get/html/{id}  |
[**googleAppInfoTaskPost**](AppDataApi.md#googleAppInfoTaskPost) | **POST**  /v3/app_data/google/app_info/task_post  |
[**googleAppInfoTasksReady**](AppDataApi.md#googleAppInfoTasksReady) | **GET**  /v3/app_data/google/app_info/tasks_ready  |
[**googleAppInfoTaskGetAdvanced**](AppDataApi.md#googleAppInfoTaskGetAdvanced) | **GET**  /v3/app_data/google/app_info/task_get/advanced/{id}  |
[**googleAppInfoTaskGetHtml**](AppDataApi.md#googleAppInfoTaskGetHtml) | **GET**  /v3/app_data/google/app_info/task_get/html/{id}  |
[**googleAppReviewsTaskPost**](AppDataApi.md#googleAppReviewsTaskPost) | **POST**  /v3/app_data/google/app_reviews/task_post  |
[**googleAppReviewsTasksReady**](AppDataApi.md#googleAppReviewsTasksReady) | **GET**  /v3/app_data/google/app_reviews/tasks_ready  |
[**googleAppReviewsTaskGetAdvanced**](AppDataApi.md#googleAppReviewsTaskGetAdvanced) | **GET**  /v3/app_data/google/app_reviews/task_get/advanced/{id}  |
[**googleAppReviewsTaskGetHtml**](AppDataApi.md#googleAppReviewsTaskGetHtml) | **GET**  /v3/app_data/google/app_reviews/task_get/html/{id}  |
[**googleAppListingsCategories**](AppDataApi.md#googleAppListingsCategories) | **GET**  /v3/app_data/google/app_listings/categories  |
[**googleAppListingsSearchLive**](AppDataApi.md#googleAppListingsSearchLive) | **POST**  /v3/app_data/google/app_listings/search/live  |
[**appleCategories**](AppDataApi.md#appleCategories) | **GET**  /v3/app_data/apple/categories  |
[**appDataAppleLocations**](AppDataApi.md#appDataAppleLocations) | **GET**  /v3/app_data/apple/locations  |
[**appDataAppleLanguages**](AppDataApi.md#appDataAppleLanguages) | **GET**  /v3/app_data/apple/languages  |
[**appleAppSearchesTaskPost**](AppDataApi.md#appleAppSearchesTaskPost) | **POST**  /v3/app_data/apple/app_searches/task_post  |
[**appleAppSearchesTasksReady**](AppDataApi.md#appleAppSearchesTasksReady) | **GET**  /v3/app_data/apple/app_searches/tasks_ready  |
[**appleAppSearchesTaskGetAdvanced**](AppDataApi.md#appleAppSearchesTaskGetAdvanced) | **GET**  /v3/app_data/apple/app_searches/task_get/advanced/{id}  |
[**appleAppInfoTaskPost**](AppDataApi.md#appleAppInfoTaskPost) | **POST**  /v3/app_data/apple/app_info/task_post  |
[**appleAppInfoTasksReady**](AppDataApi.md#appleAppInfoTasksReady) | **GET**  /v3/app_data/apple/app_info/tasks_ready  |
[**appleAppInfoTaskGetAdvanced**](AppDataApi.md#appleAppInfoTaskGetAdvanced) | **GET**  /v3/app_data/apple/app_info/task_get/advanced/{id}  |
[**appleAppListTaskPost**](AppDataApi.md#appleAppListTaskPost) | **POST**  /v3/app_data/apple/app_list/task_post  |
[**appleAppListTasksReady**](AppDataApi.md#appleAppListTasksReady) | **GET**  /v3/app_data/apple/app_list/tasks_ready  |
[**appleAppListTaskGetAdvanced**](AppDataApi.md#appleAppListTaskGetAdvanced) | **GET**  /v3/app_data/apple/app_list/task_get/advanced/{id}  |
[**appleAppReviewsTaskPost**](AppDataApi.md#appleAppReviewsTaskPost) | **POST**  /v3/app_data/apple/app_reviews/task_post  |
[**appleAppReviewsTasksReady**](AppDataApi.md#appleAppReviewsTasksReady) | **GET**  /v3/app_data/apple/app_reviews/tasks_ready  |
[**appleAppReviewsTaskGetAdvanced**](AppDataApi.md#appleAppReviewsTaskGetAdvanced) | **GET**  /v3/app_data/apple/app_reviews/task_get/advanced/{id}  |
[**appleAppListingsCategories**](AppDataApi.md#appleAppListingsCategories) | **GET**  /v3/app_data/apple/app_listings/categories  |
[**appleAppListingsSearchLive**](AppDataApi.md#appleAppListingsSearchLive) | **POST**  /v3/app_data/apple/app_listings/search/live  |

<a id="appDataIdList"></a>
# **appDataIdList**
> AppDataIdListResponseInfo appDataIdList()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_id_list_request_info import List[Optional[AppDataIdListRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.app_data_id_list([AppDataIdListRequestInfo(
                datetime_from="2025-08-22 08:11:16 +00:00",
                datetime_to="2025-10-22 08:11:16 +00:00",
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
    | **** | [**List&lt;List[Optional[AppDataIdListRequestInfo]]&gt;**](List[Optional[AppDataIdListRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataIdListResponseInfo**](AppDataIdListResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appDataErrors"></a>
# **appDataErrors**
> AppDataErrorsResponseInfo appDataErrors()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_errors_request_info import List[Optional[AppDataErrorsRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.app_data_errors([AppDataErrorsRequestInfo(
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
    | **** | [**List&lt;List[Optional[AppDataErrorsRequestInfo]]&gt;**](List[Optional[AppDataErrorsRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataErrorsResponseInfo**](AppDataErrorsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleCategories"></a>
# **googleCategories**
> AppDataGoogleCategoriesResponseInfo googleCategories()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.google_categories()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleCategoriesResponseInfo**](AppDataGoogleCategoriesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appDataGoogleLocations"></a>
# **appDataGoogleLocations**
> AppDataGoogleLocationsResponseInfo appDataGoogleLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.app_data_google_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleLocationsResponseInfo**](AppDataGoogleLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appDataGoogleLocationsCountry"></a>
# **appDataGoogleLocationsCountry**
> AppDataGoogleLocationsCountryResponseInfo appDataGoogleLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        country = "us"
        response = app_data_api.app_data_google_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleLocationsCountryResponseInfo**](AppDataGoogleLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appDataGoogleLanguages"></a>
# **appDataGoogleLanguages**
> AppDataGoogleLanguagesResponseInfo appDataGoogleLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.app_data_google_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleLanguagesResponseInfo**](AppDataGoogleLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppSearchesTaskPost"></a>
# **googleAppSearchesTaskPost**
> AppDataGoogleAppSearchesTaskPostResponseInfo googleAppSearchesTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_google_app_searches_task_post_request_info import List[Optional[AppDataGoogleAppSearchesTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.google_app_searches_task_post([AppDataGoogleAppSearchesTaskPostRequestInfo(
                keyword="vpn",
                location_code=2840,
                language_code="en",
                depth=30,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AppDataGoogleAppSearchesTaskPostRequestInfo]]&gt;**](List[Optional[AppDataGoogleAppSearchesTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataGoogleAppSearchesTaskPostResponseInfo**](AppDataGoogleAppSearchesTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppSearchesTasksReady"></a>
# **googleAppSearchesTasksReady**
> AppDataGoogleAppSearchesTasksReadyResponseInfo googleAppSearchesTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.google_app_searches_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppSearchesTasksReadyResponseInfo**](AppDataGoogleAppSearchesTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appDataTasksReady"></a>
# **appDataTasksReady**
> AppDataTasksReadyResponseInfo appDataTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.app_data_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataTasksReadyResponseInfo**](AppDataTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppSearchesTaskGetAdvanced"></a>
# **googleAppSearchesTaskGetAdvanced**
> AppDataGoogleAppSearchesTaskGetAdvancedResponseInfo googleAppSearchesTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.google_app_searches_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppSearchesTaskGetAdvancedResponseInfo**](AppDataGoogleAppSearchesTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppSearchesTaskGetHtml"></a>
# **googleAppSearchesTaskGetHtml**
> AppDataGoogleAppSearchesTaskGetHtmlResponseInfo googleAppSearchesTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.google_app_searches_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppSearchesTaskGetHtmlResponseInfo**](AppDataGoogleAppSearchesTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppListTaskPost"></a>
# **googleAppListTaskPost**
> AppDataGoogleAppListTaskPostResponseInfo googleAppListTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_google_app_list_task_post_request_info import List[Optional[AppDataGoogleAppListTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.google_app_list_task_post([AppDataGoogleAppListTaskPostRequestInfo(
                app_collection="topselling_free",
                location_code=2840,
                language_code="en",
                depth=100,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AppDataGoogleAppListTaskPostRequestInfo]]&gt;**](List[Optional[AppDataGoogleAppListTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataGoogleAppListTaskPostResponseInfo**](AppDataGoogleAppListTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppListTasksReady"></a>
# **googleAppListTasksReady**
> AppDataGoogleAppListTasksReadyResponseInfo googleAppListTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.google_app_list_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppListTasksReadyResponseInfo**](AppDataGoogleAppListTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppListTaskGetAdvanced"></a>
# **googleAppListTaskGetAdvanced**
> AppDataGoogleAppListTaskGetAdvancedResponseInfo googleAppListTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.google_app_list_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppListTaskGetAdvancedResponseInfo**](AppDataGoogleAppListTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppListTaskGetHtml"></a>
# **googleAppListTaskGetHtml**
> AppDataGoogleAppListTaskGetHtmlResponseInfo googleAppListTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.google_app_list_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppListTaskGetHtmlResponseInfo**](AppDataGoogleAppListTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppInfoTaskPost"></a>
# **googleAppInfoTaskPost**
> AppDataGoogleAppInfoTaskPostResponseInfo googleAppInfoTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_google_app_info_task_post_request_info import List[Optional[AppDataGoogleAppInfoTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.google_app_info_task_post([AppDataGoogleAppInfoTaskPostRequestInfo(
                app_id="org.telegram.messenger",
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
    | **** | [**List&lt;List[Optional[AppDataGoogleAppInfoTaskPostRequestInfo]]&gt;**](List[Optional[AppDataGoogleAppInfoTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataGoogleAppInfoTaskPostResponseInfo**](AppDataGoogleAppInfoTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppInfoTasksReady"></a>
# **googleAppInfoTasksReady**
> AppDataGoogleAppInfoTasksReadyResponseInfo googleAppInfoTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.google_app_info_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppInfoTasksReadyResponseInfo**](AppDataGoogleAppInfoTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppInfoTaskGetAdvanced"></a>
# **googleAppInfoTaskGetAdvanced**
> AppDataGoogleAppInfoTaskGetAdvancedResponseInfo googleAppInfoTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.google_app_info_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppInfoTaskGetAdvancedResponseInfo**](AppDataGoogleAppInfoTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppInfoTaskGetHtml"></a>
# **googleAppInfoTaskGetHtml**
> AppDataGoogleAppInfoTaskGetHtmlResponseInfo googleAppInfoTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.google_app_info_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppInfoTaskGetHtmlResponseInfo**](AppDataGoogleAppInfoTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppReviewsTaskPost"></a>
# **googleAppReviewsTaskPost**
> AppDataGoogleAppReviewsTaskPostResponseInfo googleAppReviewsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_google_app_reviews_task_post_request_info import List[Optional[AppDataGoogleAppReviewsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.google_app_reviews_task_post([AppDataGoogleAppReviewsTaskPostRequestInfo(
                app_id="org.telegram.messenger",
                location_code=2840,
                language_code="en",
                depth=150,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AppDataGoogleAppReviewsTaskPostRequestInfo]]&gt;**](List[Optional[AppDataGoogleAppReviewsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataGoogleAppReviewsTaskPostResponseInfo**](AppDataGoogleAppReviewsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppReviewsTasksReady"></a>
# **googleAppReviewsTasksReady**
> AppDataGoogleAppReviewsTasksReadyResponseInfo googleAppReviewsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.google_app_reviews_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppReviewsTasksReadyResponseInfo**](AppDataGoogleAppReviewsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppReviewsTaskGetAdvanced"></a>
# **googleAppReviewsTaskGetAdvanced**
> AppDataGoogleAppReviewsTaskGetAdvancedResponseInfo googleAppReviewsTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.google_app_reviews_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppReviewsTaskGetAdvancedResponseInfo**](AppDataGoogleAppReviewsTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppReviewsTaskGetHtml"></a>
# **googleAppReviewsTaskGetHtml**
> AppDataGoogleAppReviewsTaskGetHtmlResponseInfo googleAppReviewsTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.google_app_reviews_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppReviewsTaskGetHtmlResponseInfo**](AppDataGoogleAppReviewsTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppListingsCategories"></a>
# **googleAppListingsCategories**
> AppDataGoogleAppListingsCategoriesResponseInfo googleAppListingsCategories()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.google_app_listings_categories()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataGoogleAppListingsCategoriesResponseInfo**](AppDataGoogleAppListingsCategoriesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppListingsSearchLive"></a>
# **googleAppListingsSearchLive**
> AppDataGoogleAppListingsSearchLiveResponseInfo googleAppListingsSearchLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_google_app_listings_search_live_request_info import List[Optional[AppDataGoogleAppListingsSearchLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.google_app_listings_search_live([AppDataGoogleAppListingsSearchLiveRequestInfo(
                categories=[
                    "Tools",
                    ],
                description="vpn",
                title="vpn",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AppDataGoogleAppListingsSearchLiveRequestInfo]]&gt;**](List[Optional[AppDataGoogleAppListingsSearchLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataGoogleAppListingsSearchLiveResponseInfo**](AppDataGoogleAppListingsSearchLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleCategories"></a>
# **appleCategories**
> AppDataAppleCategoriesResponseInfo appleCategories()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.apple_categories()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleCategoriesResponseInfo**](AppDataAppleCategoriesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appDataAppleLocations"></a>
# **appDataAppleLocations**
> AppDataAppleLocationsResponseInfo appDataAppleLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.app_data_apple_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleLocationsResponseInfo**](AppDataAppleLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appDataAppleLanguages"></a>
# **appDataAppleLanguages**
> AppDataAppleLanguagesResponseInfo appDataAppleLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.app_data_apple_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleLanguagesResponseInfo**](AppDataAppleLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppSearchesTaskPost"></a>
# **appleAppSearchesTaskPost**
> AppDataAppleAppSearchesTaskPostResponseInfo appleAppSearchesTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_apple_app_searches_task_post_request_info import List[Optional[AppDataAppleAppSearchesTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.apple_app_searches_task_post([AppDataAppleAppSearchesTaskPostRequestInfo(
                keyword="vpn",
                location_code=2840,
                language_code="en",
                depth=200,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AppDataAppleAppSearchesTaskPostRequestInfo]]&gt;**](List[Optional[AppDataAppleAppSearchesTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataAppleAppSearchesTaskPostResponseInfo**](AppDataAppleAppSearchesTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppSearchesTasksReady"></a>
# **appleAppSearchesTasksReady**
> AppDataAppleAppSearchesTasksReadyResponseInfo appleAppSearchesTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.apple_app_searches_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleAppSearchesTasksReadyResponseInfo**](AppDataAppleAppSearchesTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppSearchesTaskGetAdvanced"></a>
# **appleAppSearchesTaskGetAdvanced**
> AppDataAppleAppSearchesTaskGetAdvancedResponseInfo appleAppSearchesTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.apple_app_searches_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleAppSearchesTaskGetAdvancedResponseInfo**](AppDataAppleAppSearchesTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppInfoTaskPost"></a>
# **appleAppInfoTaskPost**
> AppDataAppleAppInfoTaskPostResponseInfo appleAppInfoTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_apple_app_info_task_post_request_info import List[Optional[AppDataAppleAppInfoTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.apple_app_info_task_post([AppDataAppleAppInfoTaskPostRequestInfo(
                app_id="835599320",
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
    | **** | [**List&lt;List[Optional[AppDataAppleAppInfoTaskPostRequestInfo]]&gt;**](List[Optional[AppDataAppleAppInfoTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataAppleAppInfoTaskPostResponseInfo**](AppDataAppleAppInfoTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppInfoTasksReady"></a>
# **appleAppInfoTasksReady**
> AppDataAppleAppInfoTasksReadyResponseInfo appleAppInfoTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.apple_app_info_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleAppInfoTasksReadyResponseInfo**](AppDataAppleAppInfoTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppInfoTaskGetAdvanced"></a>
# **appleAppInfoTaskGetAdvanced**
> AppDataAppleAppInfoTaskGetAdvancedResponseInfo appleAppInfoTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.apple_app_info_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleAppInfoTaskGetAdvancedResponseInfo**](AppDataAppleAppInfoTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppListTaskPost"></a>
# **appleAppListTaskPost**
> AppDataAppleAppListTaskPostResponseInfo appleAppListTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_apple_app_list_task_post_request_info import List[Optional[AppDataAppleAppListTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.apple_app_list_task_post([AppDataAppleAppListTaskPostRequestInfo(
                app_collection="top_free_ios",
                location_code=2840,
                language_code="en",
                depth=200,
                app_category="games",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AppDataAppleAppListTaskPostRequestInfo]]&gt;**](List[Optional[AppDataAppleAppListTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataAppleAppListTaskPostResponseInfo**](AppDataAppleAppListTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppListTasksReady"></a>
# **appleAppListTasksReady**
> AppDataAppleAppListTasksReadyResponseInfo appleAppListTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.apple_app_list_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleAppListTasksReadyResponseInfo**](AppDataAppleAppListTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppListTaskGetAdvanced"></a>
# **appleAppListTaskGetAdvanced**
> AppDataAppleAppListTaskGetAdvancedResponseInfo appleAppListTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.apple_app_list_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleAppListTaskGetAdvancedResponseInfo**](AppDataAppleAppListTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppReviewsTaskPost"></a>
# **appleAppReviewsTaskPost**
> AppDataAppleAppReviewsTaskPostResponseInfo appleAppReviewsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_apple_app_reviews_task_post_request_info import List[Optional[AppDataAppleAppReviewsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.apple_app_reviews_task_post([AppDataAppleAppReviewsTaskPostRequestInfo(
                app_id="835599320",
                location_code=2840,
                language_code="en",
                depth=200,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AppDataAppleAppReviewsTaskPostRequestInfo]]&gt;**](List[Optional[AppDataAppleAppReviewsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataAppleAppReviewsTaskPostResponseInfo**](AppDataAppleAppReviewsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppReviewsTasksReady"></a>
# **appleAppReviewsTasksReady**
> AppDataAppleAppReviewsTasksReadyResponseInfo appleAppReviewsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.apple_app_reviews_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleAppReviewsTasksReadyResponseInfo**](AppDataAppleAppReviewsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppReviewsTaskGetAdvanced"></a>
# **appleAppReviewsTaskGetAdvanced**
> AppDataAppleAppReviewsTaskGetAdvancedResponseInfo appleAppReviewsTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = app_data_api.apple_app_reviews_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleAppReviewsTaskGetAdvancedResponseInfo**](AppDataAppleAppReviewsTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppListingsCategories"></a>
# **appleAppListingsCategories**
> AppDataAppleAppListingsCategoriesResponseInfo appleAppListingsCategories()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.apple_app_listings_categories()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AppDataAppleAppListingsCategoriesResponseInfo**](AppDataAppleAppListingsCategoriesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppListingsSearchLive"></a>
# **appleAppListingsSearchLive**
> AppDataAppleAppListingsSearchLiveResponseInfo appleAppListingsSearchLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_app_data_apple_app_listings_search_live_request_info import List[Optional[AppDataAppleAppListingsSearchLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        app_data_api = AppDataApi(api_client)

        response = app_data_api.apple_app_listings_search_live([AppDataAppleAppListingsSearchLiveRequestInfo(
                categories=[
                    "Tools",
                    ],
                description="vpn",
                title="vpn",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AppDataAppleAppListingsSearchLiveRequestInfo]]&gt;**](List[Optional[AppDataAppleAppListingsSearchLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AppDataAppleAppListingsSearchLiveResponseInfo**](AppDataAppleAppListingsSearchLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |