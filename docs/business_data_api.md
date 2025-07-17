# BusinessDataApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**businessDataIdList**](BusinessDataApi.md#businessDataIdList) | **POST**  /v3/business_data/id_list  |
[**businessDataErrors**](BusinessDataApi.md#businessDataErrors) | **POST**  /v3/business_data/errors  |
[**businessDataBusinessListingsLocations**](BusinessDataApi.md#businessDataBusinessListingsLocations) | **GET**  /v3/business_data/business_listings/locations  |
[**businessListingsCategories**](BusinessDataApi.md#businessListingsCategories) | **GET**  /v3/business_data/business_listings/categories  |
[**businessListingsAvailableFilters**](BusinessDataApi.md#businessListingsAvailableFilters) | **GET**  /v3/business_data/business_listings/available_filters  |
[**businessListingsSearchLive**](BusinessDataApi.md#businessListingsSearchLive) | **POST**  /v3/business_data/business_listings/search/live  |
[**businessListingsCategoriesAggregationLive**](BusinessDataApi.md#businessListingsCategoriesAggregationLive) | **POST**  /v3/business_data/business_listings/categories_aggregation/live  |
[**businessDataGoogleLocations**](BusinessDataApi.md#businessDataGoogleLocations) | **GET**  /v3/business_data/google/locations  |
[**businessDataGoogleLocationsCountry**](BusinessDataApi.md#businessDataGoogleLocationsCountry) | **GET**  /v3/business_data/google/locations/{country}  |
[**businessDataGoogleLanguages**](BusinessDataApi.md#businessDataGoogleLanguages) | **GET**  /v3/business_data/google/languages  |
[**googleMyBusinessInfoTaskPost**](BusinessDataApi.md#googleMyBusinessInfoTaskPost) | **POST**  /v3/business_data/google/my_business_info/task_post  |
[**googleMyBusinessInfoTasksReady**](BusinessDataApi.md#googleMyBusinessInfoTasksReady) | **GET**  /v3/business_data/google/my_business_info/tasks_ready  |
[**businessDataTasksReady**](BusinessDataApi.md#businessDataTasksReady) | **GET**  /v3/business_data/tasks_ready  |
[**googleMyBusinessInfoTaskGet**](BusinessDataApi.md#googleMyBusinessInfoTaskGet) | **GET**  /v3/business_data/google/my_business_info/task_get/{id}  |
[**googleMyBusinessInfoLive**](BusinessDataApi.md#googleMyBusinessInfoLive) | **POST**  /v3/business_data/google/my_business_info/live  |
[**googleMyBusinessUpdatesTaskPost**](BusinessDataApi.md#googleMyBusinessUpdatesTaskPost) | **POST**  /v3/business_data/google/my_business_updates/task_post  |
[**googleMyBusinessUpdatesTasksReady**](BusinessDataApi.md#googleMyBusinessUpdatesTasksReady) | **GET**  /v3/business_data/google/my_business_updates/tasks_ready  |
[**googleMyBusinessUpdatesTaskGet**](BusinessDataApi.md#googleMyBusinessUpdatesTaskGet) | **GET**  /v3/business_data/google/my_business_updates/task_get/{id}  |
[**googleHotelSearchesTaskPost**](BusinessDataApi.md#googleHotelSearchesTaskPost) | **POST**  /v3/business_data/google/hotel_searches/task_post  |
[**googleHotelSearchesTasksReady**](BusinessDataApi.md#googleHotelSearchesTasksReady) | **GET**  /v3/business_data/google/hotel_searches/tasks_ready  |
[**googleHotelSearchesTaskGet**](BusinessDataApi.md#googleHotelSearchesTaskGet) | **GET**  /v3/business_data/google/hotel_searches/task_get/{id}  |
[**googleHotelSearchesLive**](BusinessDataApi.md#googleHotelSearchesLive) | **POST**  /v3/business_data/google/hotel_searches/live  |
[**googleHotelInfoTaskPost**](BusinessDataApi.md#googleHotelInfoTaskPost) | **POST**  /v3/business_data/google/hotel_info/task_post  |
[**googleHotelInfoTasksReady**](BusinessDataApi.md#googleHotelInfoTasksReady) | **GET**  /v3/business_data/google/hotel_info/tasks_ready  |
[**googleHotelInfoTaskGetAdvanced**](BusinessDataApi.md#googleHotelInfoTaskGetAdvanced) | **GET**  /v3/business_data/google/hotel_info/task_get/advanced/{id}  |
[**googleHotelInfoTaskGetHtml**](BusinessDataApi.md#googleHotelInfoTaskGetHtml) | **GET**  /v3/business_data/google/hotel_info/task_get/html/{id}  |
[**googleHotelInfoLiveAdvanced**](BusinessDataApi.md#googleHotelInfoLiveAdvanced) | **POST**  /v3/business_data/google/hotel_info/live/advanced  |
[**googleHotelInfoLiveHtml**](BusinessDataApi.md#googleHotelInfoLiveHtml) | **POST**  /v3/business_data/google/hotel_info/live/html  |
[**googleReviewsTaskPost**](BusinessDataApi.md#googleReviewsTaskPost) | **POST**  /v3/business_data/google/reviews/task_post  |
[**googleReviewsTasksReady**](BusinessDataApi.md#googleReviewsTasksReady) | **GET**  /v3/business_data/google/reviews/tasks_ready  |
[**googleReviewsTaskGet**](BusinessDataApi.md#googleReviewsTaskGet) | **GET**  /v3/business_data/google/reviews/task_get/{id}  |
[**googleExtendedReviewsTaskPost**](BusinessDataApi.md#googleExtendedReviewsTaskPost) | **POST**  /v3/business_data/google/extended_reviews/task_post  |
[**googleExtendedReviewsTasksReady**](BusinessDataApi.md#googleExtendedReviewsTasksReady) | **GET**  /v3/business_data/google/extended_reviews/tasks_ready  |
[**googleExtendedReviewsTaskGet**](BusinessDataApi.md#googleExtendedReviewsTaskGet) | **GET**  /v3/business_data/google/extended_reviews/task_get/{id}  |
[**googleQuestionsAndAnswersTaskPost**](BusinessDataApi.md#googleQuestionsAndAnswersTaskPost) | **POST**  /v3/business_data/google/questions_and_answers/task_post  |
[**googleQuestionsAndAnswersTasksReady**](BusinessDataApi.md#googleQuestionsAndAnswersTasksReady) | **GET**  /v3/business_data/google/questions_and_answers/tasks_ready  |
[**googleQuestionsAndAnswersTaskGet**](BusinessDataApi.md#googleQuestionsAndAnswersTaskGet) | **GET**  /v3/business_data/google/questions_and_answers/task_get/{id}  |
[**googleQuestionsAndAnswersLive**](BusinessDataApi.md#googleQuestionsAndAnswersLive) | **POST**  /v3/business_data/google/questions_and_answers/live  |
[**trustpilotSearchTaskPost**](BusinessDataApi.md#trustpilotSearchTaskPost) | **POST**  /v3/business_data/trustpilot/search/task_post  |
[**trustpilotSearchTasksReady**](BusinessDataApi.md#trustpilotSearchTasksReady) | **GET**  /v3/business_data/trustpilot/search/tasks_ready  |
[**trustpilotSearchTaskGet**](BusinessDataApi.md#trustpilotSearchTaskGet) | **GET**  /v3/business_data/trustpilot/search/task_get/{id}  |
[**trustpilotReviewsTaskPost**](BusinessDataApi.md#trustpilotReviewsTaskPost) | **POST**  /v3/business_data/trustpilot/reviews/task_post  |
[**trustpilotReviewsTasksReady**](BusinessDataApi.md#trustpilotReviewsTasksReady) | **GET**  /v3/business_data/trustpilot/reviews/tasks_ready  |
[**trustpilotReviewsTaskGet**](BusinessDataApi.md#trustpilotReviewsTaskGet) | **GET**  /v3/business_data/trustpilot/reviews/task_get/{id}  |
[**businessDataTripadvisorLocations**](BusinessDataApi.md#businessDataTripadvisorLocations) | **GET**  /v3/business_data/tripadvisor/locations  |
[**businessDataTripadvisorLocationsCountry**](BusinessDataApi.md#businessDataTripadvisorLocationsCountry) | **GET**  /v3/business_data/tripadvisor/locations/{country}  |
[**businessDataTripadvisorLanguages**](BusinessDataApi.md#businessDataTripadvisorLanguages) | **GET**  /v3/business_data/tripadvisor/languages  |
[**tripadvisorSearchTaskPost**](BusinessDataApi.md#tripadvisorSearchTaskPost) | **POST**  /v3/business_data/tripadvisor/search/task_post  |
[**tripadvisorSearchTasksReady**](BusinessDataApi.md#tripadvisorSearchTasksReady) | **GET**  /v3/business_data/tripadvisor/search/tasks_ready  |
[**tripadvisorSearchTaskGet**](BusinessDataApi.md#tripadvisorSearchTaskGet) | **GET**  /v3/business_data/tripadvisor/search/task_get/{id}  |
[**tripadvisorReviewsTaskPost**](BusinessDataApi.md#tripadvisorReviewsTaskPost) | **POST**  /v3/business_data/tripadvisor/reviews/task_post  |
[**tripadvisorReviewsTasksReady**](BusinessDataApi.md#tripadvisorReviewsTasksReady) | **GET**  /v3/business_data/tripadvisor/reviews/tasks_ready  |
[**tripadvisorReviewsTaskGet**](BusinessDataApi.md#tripadvisorReviewsTaskGet) | **GET**  /v3/business_data/tripadvisor/reviews/task_get/{id}  |
[**socialMediaPinterestLive**](BusinessDataApi.md#socialMediaPinterestLive) | **POST**  /v3/business_data/social_media/pinterest/live  |
[**socialMediaFacebookLive**](BusinessDataApi.md#socialMediaFacebookLive) | **POST**  /v3/business_data/social_media/facebook/live  |
[**socialMediaRedditLive**](BusinessDataApi.md#socialMediaRedditLive) | **POST**  /v3/business_data/social_media/reddit/live  |

<a id="businessDataIdList"></a>
# **businessDataIdList**
> BusinessDataIdListResponseInfo businessDataIdList()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_id_list_request_info import List[Optional[BusinessDataIdListRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_data_id_list([BusinessDataIdListRequestInfo(
                datetime_from="2025-04-17 06:10:40 +00:00",
                datetime_to="2025-06-17 06:10:40 +00:00",
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
    | **** | [**List&lt;List[Optional[BusinessDataIdListRequestInfo]]&gt;**](List[Optional[BusinessDataIdListRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataIdListResponseInfo**](BusinessDataIdListResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessDataErrors"></a>
# **businessDataErrors**
> BusinessDataErrorsResponseInfo businessDataErrors()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_errors_request_info import List[Optional[BusinessDataErrorsRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_data_errors([BusinessDataErrorsRequestInfo(
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
    | **** | [**List&lt;List[Optional[BusinessDataErrorsRequestInfo]]&gt;**](List[Optional[BusinessDataErrorsRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataErrorsResponseInfo**](BusinessDataErrorsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessDataBusinessListingsLocations"></a>
# **businessDataBusinessListingsLocations**
> BusinessDataBusinessListingsLocationsResponseInfo businessDataBusinessListingsLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_data_business_listings_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataBusinessListingsLocationsResponseInfo**](BusinessDataBusinessListingsLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessListingsCategories"></a>
# **businessListingsCategories**
> BusinessDataBusinessListingsCategoriesResponseInfo businessListingsCategories()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_listings_categories()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataBusinessListingsCategoriesResponseInfo**](BusinessDataBusinessListingsCategoriesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessListingsAvailableFilters"></a>
# **businessListingsAvailableFilters**
> BusinessDataBusinessListingsAvailableFiltersResponseInfo businessListingsAvailableFilters()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_listings_available_filters()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataBusinessListingsAvailableFiltersResponseInfo**](BusinessDataBusinessListingsAvailableFiltersResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessListingsSearchLive"></a>
# **businessListingsSearchLive**
> BusinessDataBusinessListingsSearchLiveResponseInfo businessListingsSearchLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_business_listings_search_live_request_info import List[Optional[BusinessDataBusinessListingsSearchLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_listings_search_live([BusinessDataBusinessListingsSearchLiveRequestInfo(
                categories=[
                        "pizza_restaurant",
                    ],
                description="pizza",
                title="pizza",
                is_claimed=True,
                location_coordinate="53.476225,-2.243572,10",
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataBusinessListingsSearchLiveRequestInfo]]&gt;**](List[Optional[BusinessDataBusinessListingsSearchLiveRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataBusinessListingsSearchLiveResponseInfo**](BusinessDataBusinessListingsSearchLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessListingsCategoriesAggregationLive"></a>
# **businessListingsCategoriesAggregationLive**
> BusinessDataBusinessListingsCategoriesAggregationLiveResponseInfo businessListingsCategoriesAggregationLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_business_listings_categories_aggregation_live_request_info import List[Optional[BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_listings_categories_aggregation_live([BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo(
                categories=[
                        "pizza_restaurant",
                    ],
                description="pizza",
                title="pizza",
                is_claimed=True,
                location_coordinate="53.476225,-2.243572,10",
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo]]&gt;**](List[Optional[BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataBusinessListingsCategoriesAggregationLiveResponseInfo**](BusinessDataBusinessListingsCategoriesAggregationLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessDataGoogleLocations"></a>
# **businessDataGoogleLocations**
> BusinessDataGoogleLocationsResponseInfo businessDataGoogleLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_data_google_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleLocationsResponseInfo**](BusinessDataGoogleLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessDataGoogleLocationsCountry"></a>
# **businessDataGoogleLocationsCountry**
> BusinessDataGoogleLocationsCountryResponseInfo businessDataGoogleLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        country = "us"
        response = business_data_api.business_data_google_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleLocationsCountryResponseInfo**](BusinessDataGoogleLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessDataGoogleLanguages"></a>
# **businessDataGoogleLanguages**
> BusinessDataGoogleLanguagesResponseInfo businessDataGoogleLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_data_google_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleLanguagesResponseInfo**](BusinessDataGoogleLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMyBusinessInfoTaskPost"></a>
# **googleMyBusinessInfoTaskPost**
> BusinessDataGoogleMyBusinessInfoTaskPostResponseInfo googleMyBusinessInfoTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_my_business_info_task_post_request_info import List[Optional[BusinessDataGoogleMyBusinessInfoTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_my_business_info_task_post([BusinessDataGoogleMyBusinessInfoTaskPostRequestInfo(
                keyword="RustyBrick, Inc.",
                location_name="New York,New York,United States",
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleMyBusinessInfoTaskPostRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleMyBusinessInfoTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleMyBusinessInfoTaskPostResponseInfo**](BusinessDataGoogleMyBusinessInfoTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMyBusinessInfoTasksReady"></a>
# **googleMyBusinessInfoTasksReady**
> BusinessDataGoogleMyBusinessInfoTasksReadyResponseInfo googleMyBusinessInfoTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_my_business_info_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleMyBusinessInfoTasksReadyResponseInfo**](BusinessDataGoogleMyBusinessInfoTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessDataTasksReady"></a>
# **businessDataTasksReady**
> BusinessDataTasksReadyResponseInfo businessDataTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_data_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTasksReadyResponseInfo**](BusinessDataTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMyBusinessInfoTaskGet"></a>
# **googleMyBusinessInfoTaskGet**
> BusinessDataGoogleMyBusinessInfoTaskGetResponseInfo googleMyBusinessInfoTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.google_my_business_info_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleMyBusinessInfoTaskGetResponseInfo**](BusinessDataGoogleMyBusinessInfoTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMyBusinessInfoLive"></a>
# **googleMyBusinessInfoLive**
> BusinessDataGoogleMyBusinessInfoLiveResponseInfo googleMyBusinessInfoLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_my_business_info_live_request_info import List[Optional[BusinessDataGoogleMyBusinessInfoLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_my_business_info_live([BusinessDataGoogleMyBusinessInfoLiveRequestInfo(
                keyword="RustyBrick, Inc.",
                location_name="New York,New York,United States",
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleMyBusinessInfoLiveRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleMyBusinessInfoLiveRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleMyBusinessInfoLiveResponseInfo**](BusinessDataGoogleMyBusinessInfoLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMyBusinessUpdatesTaskPost"></a>
# **googleMyBusinessUpdatesTaskPost**
> BusinessDataGoogleMyBusinessUpdatesTaskPostResponseInfo googleMyBusinessUpdatesTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_my_business_updates_task_post_request_info import List[Optional[BusinessDataGoogleMyBusinessUpdatesTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_my_business_updates_task_post([BusinessDataGoogleMyBusinessUpdatesTaskPostRequestInfo(
                keyword="RustyBrick, Inc.",
                location_name="New York,New York,United States",
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleMyBusinessUpdatesTaskPostRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleMyBusinessUpdatesTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleMyBusinessUpdatesTaskPostResponseInfo**](BusinessDataGoogleMyBusinessUpdatesTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMyBusinessUpdatesTasksReady"></a>
# **googleMyBusinessUpdatesTasksReady**
> BusinessDataGoogleMyBusinessUpdatesTasksReadyResponseInfo googleMyBusinessUpdatesTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_my_business_updates_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleMyBusinessUpdatesTasksReadyResponseInfo**](BusinessDataGoogleMyBusinessUpdatesTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleMyBusinessUpdatesTaskGet"></a>
# **googleMyBusinessUpdatesTaskGet**
> BusinessDataGoogleMyBusinessUpdatesTaskGetResponseInfo googleMyBusinessUpdatesTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.google_my_business_updates_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleMyBusinessUpdatesTaskGetResponseInfo**](BusinessDataGoogleMyBusinessUpdatesTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHotelSearchesTaskPost"></a>
# **googleHotelSearchesTaskPost**
> BusinessDataGoogleHotelSearchesTaskPostResponseInfo googleHotelSearchesTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_hotel_searches_task_post_request_info import List[Optional[BusinessDataGoogleHotelSearchesTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_hotel_searches_task_post([BusinessDataGoogleHotelSearchesTaskPostRequestInfo(
                keyword="cheap hotel",
                priority=2,
                location_name="New York,New York,United States",
                language_code="en",
                check_in="2023-06-01",
                check_out="2023-06-30",
                currency="USD",
                adults=2,
                children=[
                        "14",
                    ],
                sort_by="highest_rating",
                tag="example",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleHotelSearchesTaskPostRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleHotelSearchesTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleHotelSearchesTaskPostResponseInfo**](BusinessDataGoogleHotelSearchesTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHotelSearchesTasksReady"></a>
# **googleHotelSearchesTasksReady**
> BusinessDataGoogleHotelSearchesTasksReadyResponseInfo googleHotelSearchesTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_hotel_searches_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleHotelSearchesTasksReadyResponseInfo**](BusinessDataGoogleHotelSearchesTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHotelSearchesTaskGet"></a>
# **googleHotelSearchesTaskGet**
> BusinessDataGoogleHotelSearchesTaskGetResponseInfo googleHotelSearchesTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.google_hotel_searches_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleHotelSearchesTaskGetResponseInfo**](BusinessDataGoogleHotelSearchesTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHotelSearchesLive"></a>
# **googleHotelSearchesLive**
> BusinessDataGoogleHotelSearchesLiveResponseInfo googleHotelSearchesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_hotel_searches_live_request_info import List[Optional[BusinessDataGoogleHotelSearchesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_hotel_searches_live([BusinessDataGoogleHotelSearchesLiveRequestInfo(
                keyword="cheap hotel",
                location_name="New York,New York,United States",
                language_code="en",
                check_in="2023-06-01",
                check_out="2023-06-30",
                currency="USD",
                adults=2,
                children=[
                        "14",
                    ],
                sort_by="highest_rating",
                tag="example",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleHotelSearchesLiveRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleHotelSearchesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleHotelSearchesLiveResponseInfo**](BusinessDataGoogleHotelSearchesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHotelInfoTaskPost"></a>
# **googleHotelInfoTaskPost**
> BusinessDataGoogleHotelInfoTaskPostResponseInfo googleHotelInfoTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_hotel_info_task_post_request_info import List[Optional[BusinessDataGoogleHotelInfoTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_hotel_info_task_post([BusinessDataGoogleHotelInfoTaskPostRequestInfo(
                hotel_identifier="ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE",
                location_name="New York,New York,United States",
                language_code="en",
                tag="some_string_123",
                postback_url="https://your-server.com/postbackscript.php",
                postback_data="advanced",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleHotelInfoTaskPostRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleHotelInfoTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleHotelInfoTaskPostResponseInfo**](BusinessDataGoogleHotelInfoTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHotelInfoTasksReady"></a>
# **googleHotelInfoTasksReady**
> BusinessDataGoogleHotelInfoTasksReadyResponseInfo googleHotelInfoTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_hotel_info_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleHotelInfoTasksReadyResponseInfo**](BusinessDataGoogleHotelInfoTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHotelInfoTaskGetAdvanced"></a>
# **googleHotelInfoTaskGetAdvanced**
> BusinessDataGoogleHotelInfoTaskGetAdvancedResponseInfo googleHotelInfoTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.google_hotel_info_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleHotelInfoTaskGetAdvancedResponseInfo**](BusinessDataGoogleHotelInfoTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHotelInfoTaskGetHtml"></a>
# **googleHotelInfoTaskGetHtml**
> BusinessDataGoogleHotelInfoTaskGetHtmlResponseInfo googleHotelInfoTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.google_hotel_info_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleHotelInfoTaskGetHtmlResponseInfo**](BusinessDataGoogleHotelInfoTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHotelInfoLiveAdvanced"></a>
# **googleHotelInfoLiveAdvanced**
> BusinessDataGoogleHotelInfoLiveAdvancedResponseInfo googleHotelInfoLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_hotel_info_live_advanced_request_info import List[Optional[BusinessDataGoogleHotelInfoLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_hotel_info_live_advanced([BusinessDataGoogleHotelInfoLiveAdvancedRequestInfo(
                hotel_identifier="CgoI-KWyzenM_MV3EAE",
                location_name="New York,New York,United States",
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleHotelInfoLiveAdvancedRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleHotelInfoLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleHotelInfoLiveAdvancedResponseInfo**](BusinessDataGoogleHotelInfoLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHotelInfoLiveHtml"></a>
# **googleHotelInfoLiveHtml**
> BusinessDataGoogleHotelInfoLiveHtmlResponseInfo googleHotelInfoLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_hotel_info_live_html_request_info import List[Optional[BusinessDataGoogleHotelInfoLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_hotel_info_live_html([BusinessDataGoogleHotelInfoLiveHtmlRequestInfo(
                hotel_identifier="ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE",
                location_name="New York,New York,United States",
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleHotelInfoLiveHtmlRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleHotelInfoLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleHotelInfoLiveHtmlResponseInfo**](BusinessDataGoogleHotelInfoLiveHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleReviewsTaskPost"></a>
# **googleReviewsTaskPost**
> BusinessDataGoogleReviewsTaskPostResponseInfo googleReviewsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_reviews_task_post_request_info import List[Optional[BusinessDataGoogleReviewsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_reviews_task_post([BusinessDataGoogleReviewsTaskPostRequestInfo(
                keyword="hedonism wines",
                location_name="London,England,United Kingdom",
                language_name="English",
                depth=50,
                sort_by="highest_rating",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleReviewsTaskPostRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleReviewsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleReviewsTaskPostResponseInfo**](BusinessDataGoogleReviewsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleReviewsTasksReady"></a>
# **googleReviewsTasksReady**
> BusinessDataGoogleReviewsTasksReadyResponseInfo googleReviewsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_reviews_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleReviewsTasksReadyResponseInfo**](BusinessDataGoogleReviewsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleReviewsTaskGet"></a>
# **googleReviewsTaskGet**
> BusinessDataGoogleReviewsTaskGetResponseInfo googleReviewsTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.google_reviews_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleReviewsTaskGetResponseInfo**](BusinessDataGoogleReviewsTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleExtendedReviewsTaskPost"></a>
# **googleExtendedReviewsTaskPost**
> BusinessDataGoogleExtendedReviewsTaskPostResponseInfo googleExtendedReviewsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_extended_reviews_task_post_request_info import List[Optional[BusinessDataGoogleExtendedReviewsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_extended_reviews_task_post([BusinessDataGoogleExtendedReviewsTaskPostRequestInfo(
                cid="17626775537598922320",
                location_name="London,England,United Kingdom",
                language_name="english",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleExtendedReviewsTaskPostRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleExtendedReviewsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleExtendedReviewsTaskPostResponseInfo**](BusinessDataGoogleExtendedReviewsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleExtendedReviewsTasksReady"></a>
# **googleExtendedReviewsTasksReady**
> BusinessDataGoogleExtendedReviewsTasksReadyResponseInfo googleExtendedReviewsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_extended_reviews_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleExtendedReviewsTasksReadyResponseInfo**](BusinessDataGoogleExtendedReviewsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleExtendedReviewsTaskGet"></a>
# **googleExtendedReviewsTaskGet**
> BusinessDataGoogleExtendedReviewsTaskGetResponseInfo googleExtendedReviewsTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.google_extended_reviews_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleExtendedReviewsTaskGetResponseInfo**](BusinessDataGoogleExtendedReviewsTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleQuestionsAndAnswersTaskPost"></a>
# **googleQuestionsAndAnswersTaskPost**
> BusinessDataGoogleQuestionsAndAnswersTaskPostResponseInfo googleQuestionsAndAnswersTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_questions_and_answers_task_post_request_info import List[Optional[BusinessDataGoogleQuestionsAndAnswersTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_questions_and_answers_task_post([BusinessDataGoogleQuestionsAndAnswersTaskPostRequestInfo(
                keyword="The Last Bookstore",
                location_name="Los Angeles,California,United States",
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleQuestionsAndAnswersTaskPostRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleQuestionsAndAnswersTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleQuestionsAndAnswersTaskPostResponseInfo**](BusinessDataGoogleQuestionsAndAnswersTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleQuestionsAndAnswersTasksReady"></a>
# **googleQuestionsAndAnswersTasksReady**
> BusinessDataGoogleQuestionsAndAnswersTasksReadyResponseInfo googleQuestionsAndAnswersTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_questions_and_answers_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleQuestionsAndAnswersTasksReadyResponseInfo**](BusinessDataGoogleQuestionsAndAnswersTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleQuestionsAndAnswersTaskGet"></a>
# **googleQuestionsAndAnswersTaskGet**
> BusinessDataGoogleQuestionsAndAnswersTaskGetResponseInfo googleQuestionsAndAnswersTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.google_questions_and_answers_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataGoogleQuestionsAndAnswersTaskGetResponseInfo**](BusinessDataGoogleQuestionsAndAnswersTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleQuestionsAndAnswersLive"></a>
# **googleQuestionsAndAnswersLive**
> BusinessDataGoogleQuestionsAndAnswersLiveResponseInfo googleQuestionsAndAnswersLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_google_questions_and_answers_live_request_info import List[Optional[BusinessDataGoogleQuestionsAndAnswersLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.google_questions_and_answers_live([BusinessDataGoogleQuestionsAndAnswersLiveRequestInfo(
                keyword="The Last Bookstore",
                location_name="Los Angeles,California,United States",
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataGoogleQuestionsAndAnswersLiveRequestInfo]]&gt;**](List[Optional[BusinessDataGoogleQuestionsAndAnswersLiveRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataGoogleQuestionsAndAnswersLiveResponseInfo**](BusinessDataGoogleQuestionsAndAnswersLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="trustpilotSearchTaskPost"></a>
# **trustpilotSearchTaskPost**
> BusinessDataTrustpilotSearchTaskPostResponseInfo trustpilotSearchTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_trustpilot_search_task_post_request_info import List[Optional[BusinessDataTrustpilotSearchTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.trustpilot_search_task_post([BusinessDataTrustpilotSearchTaskPostRequestInfo(
                keyword="pizza restaurant",
                depth=20,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataTrustpilotSearchTaskPostRequestInfo]]&gt;**](List[Optional[BusinessDataTrustpilotSearchTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataTrustpilotSearchTaskPostResponseInfo**](BusinessDataTrustpilotSearchTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="trustpilotSearchTasksReady"></a>
# **trustpilotSearchTasksReady**
> BusinessDataTrustpilotSearchTasksReadyResponseInfo trustpilotSearchTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.trustpilot_search_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTrustpilotSearchTasksReadyResponseInfo**](BusinessDataTrustpilotSearchTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="trustpilotSearchTaskGet"></a>
# **trustpilotSearchTaskGet**
> BusinessDataTrustpilotSearchTaskGetResponseInfo trustpilotSearchTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.trustpilot_search_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTrustpilotSearchTaskGetResponseInfo**](BusinessDataTrustpilotSearchTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="trustpilotReviewsTaskPost"></a>
# **trustpilotReviewsTaskPost**
> BusinessDataTrustpilotReviewsTaskPostResponseInfo trustpilotReviewsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_trustpilot_reviews_task_post_request_info import List[Optional[BusinessDataTrustpilotReviewsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.trustpilot_reviews_task_post([BusinessDataTrustpilotReviewsTaskPostRequestInfo(
                domain="www.thepearlsource.com",
                depth=40,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataTrustpilotReviewsTaskPostRequestInfo]]&gt;**](List[Optional[BusinessDataTrustpilotReviewsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataTrustpilotReviewsTaskPostResponseInfo**](BusinessDataTrustpilotReviewsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="trustpilotReviewsTasksReady"></a>
# **trustpilotReviewsTasksReady**
> BusinessDataTrustpilotReviewsTasksReadyResponseInfo trustpilotReviewsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.trustpilot_reviews_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTrustpilotReviewsTasksReadyResponseInfo**](BusinessDataTrustpilotReviewsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="trustpilotReviewsTaskGet"></a>
# **trustpilotReviewsTaskGet**
> BusinessDataTrustpilotReviewsTaskGetResponseInfo trustpilotReviewsTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.trustpilot_reviews_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTrustpilotReviewsTaskGetResponseInfo**](BusinessDataTrustpilotReviewsTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessDataTripadvisorLocations"></a>
# **businessDataTripadvisorLocations**
> BusinessDataTripadvisorLocationsResponseInfo businessDataTripadvisorLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_data_tripadvisor_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTripadvisorLocationsResponseInfo**](BusinessDataTripadvisorLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessDataTripadvisorLocationsCountry"></a>
# **businessDataTripadvisorLocationsCountry**
> BusinessDataTripadvisorLocationsCountryResponseInfo businessDataTripadvisorLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        country = "us"
        response = business_data_api.business_data_tripadvisor_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTripadvisorLocationsCountryResponseInfo**](BusinessDataTripadvisorLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="businessDataTripadvisorLanguages"></a>
# **businessDataTripadvisorLanguages**
> BusinessDataTripadvisorLanguagesResponseInfo businessDataTripadvisorLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.business_data_tripadvisor_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTripadvisorLanguagesResponseInfo**](BusinessDataTripadvisorLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="tripadvisorSearchTaskPost"></a>
# **tripadvisorSearchTaskPost**
> BusinessDataTripadvisorSearchTaskPostResponseInfo tripadvisorSearchTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_tripadvisor_search_task_post_request_info import List[Optional[BusinessDataTripadvisorSearchTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.tripadvisor_search_task_post([BusinessDataTripadvisorSearchTaskPostRequestInfo(
                keyword="pizza",
                location_code=1003854,
                depth=30,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataTripadvisorSearchTaskPostRequestInfo]]&gt;**](List[Optional[BusinessDataTripadvisorSearchTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataTripadvisorSearchTaskPostResponseInfo**](BusinessDataTripadvisorSearchTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="tripadvisorSearchTasksReady"></a>
# **tripadvisorSearchTasksReady**
> BusinessDataTripadvisorSearchTasksReadyResponseInfo tripadvisorSearchTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.tripadvisor_search_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTripadvisorSearchTasksReadyResponseInfo**](BusinessDataTripadvisorSearchTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="tripadvisorSearchTaskGet"></a>
# **tripadvisorSearchTaskGet**
> BusinessDataTripadvisorSearchTaskGetResponseInfo tripadvisorSearchTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.tripadvisor_search_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTripadvisorSearchTaskGetResponseInfo**](BusinessDataTripadvisorSearchTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="tripadvisorReviewsTaskPost"></a>
# **tripadvisorReviewsTaskPost**
> BusinessDataTripadvisorReviewsTaskPostResponseInfo tripadvisorReviewsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_tripadvisor_reviews_task_post_request_info import List[Optional[BusinessDataTripadvisorReviewsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.tripadvisor_reviews_task_post([BusinessDataTripadvisorReviewsTaskPostRequestInfo(
                url_path="Hotel_Review-g60763-d23462501-Reviews-Margaritaville_Times_Square-New_York_City_New_York.html",
                location_code=1003854,
                tag="some_string_123",
                pingback_url="https://your-server.com/pingback.php?id=$id&tag=$tag",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataTripadvisorReviewsTaskPostRequestInfo]]&gt;**](List[Optional[BusinessDataTripadvisorReviewsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataTripadvisorReviewsTaskPostResponseInfo**](BusinessDataTripadvisorReviewsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="tripadvisorReviewsTasksReady"></a>
# **tripadvisorReviewsTasksReady**
> BusinessDataTripadvisorReviewsTasksReadyResponseInfo tripadvisorReviewsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.tripadvisor_reviews_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTripadvisorReviewsTasksReadyResponseInfo**](BusinessDataTripadvisorReviewsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="tripadvisorReviewsTaskGet"></a>
# **tripadvisorReviewsTaskGet**
> BusinessDataTripadvisorReviewsTaskGetResponseInfo tripadvisorReviewsTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = business_data_api.tripadvisor_reviews_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BusinessDataTripadvisorReviewsTaskGetResponseInfo**](BusinessDataTripadvisorReviewsTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="socialMediaPinterestLive"></a>
# **socialMediaPinterestLive**
> BusinessDataSocialMediaPinterestLiveResponseInfo socialMediaPinterestLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_social_media_pinterest_live_request_info import List[Optional[BusinessDataSocialMediaPinterestLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.social_media_pinterest_live([BusinessDataSocialMediaPinterestLiveRequestInfo(
                targets=[
                        "https://www.simplyrecipes.com/recipes/grilled_salmon_with_cucumber_mango_salsa/",
                        "https://tasty.co/recipe/classic-lasagna",
                        "https://www.allrecipes.com/recipe/255263/sicilian-roasted-chicken/",
                    ],
                tag="some_string_123",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataSocialMediaPinterestLiveRequestInfo]]&gt;**](List[Optional[BusinessDataSocialMediaPinterestLiveRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataSocialMediaPinterestLiveResponseInfo**](BusinessDataSocialMediaPinterestLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="socialMediaFacebookLive"></a>
# **socialMediaFacebookLive**
> BusinessDataSocialMediaFacebookLiveResponseInfo socialMediaFacebookLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_social_media_facebook_live_request_info import List[Optional[BusinessDataSocialMediaFacebookLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.social_media_facebook_live([BusinessDataSocialMediaFacebookLiveRequestInfo(
                targets=[
                        "https://prnt.sc/",
                        "https://developers.facebook.com/docs/plugins/like-button/",
                        "https://www.shbarcelona.com/blog/en/salsa-dance-clubs-in-barcelona/",
                    ],
                tag="some_string_123",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataSocialMediaFacebookLiveRequestInfo]]&gt;**](List[Optional[BusinessDataSocialMediaFacebookLiveRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataSocialMediaFacebookLiveResponseInfo**](BusinessDataSocialMediaFacebookLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="socialMediaRedditLive"></a>
# **socialMediaRedditLive**
> BusinessDataSocialMediaRedditLiveResponseInfo socialMediaRedditLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_business_data_social_media_reddit_live_request_info import List[Optional[BusinessDataSocialMediaRedditLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        business_data_api = BusinessDataApi(api_client)

        response = business_data_api.social_media_reddit_live([BusinessDataSocialMediaRedditLiveRequestInfo(
                targets=[
                        "https://vk.com/",
                        "https://ahrefs.com/",
                        "https://google.com/",
                        "https://twitter.com/",
                        "https://reddit.com/",
                        "https://facebook.com/",
                    ],
                tag="some_string_123",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BusinessDataSocialMediaRedditLiveRequestInfo]]&gt;**](List[Optional[BusinessDataSocialMediaRedditLiveRequestInfo]].md)|  | [optional] |



### Return type

[**BusinessDataSocialMediaRedditLiveResponseInfo**](BusinessDataSocialMediaRedditLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |