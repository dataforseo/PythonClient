# KeywordsDataApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**keywordsDataIdList**](KeywordsDataApi.md#keywordsDataIdList) | **POST**  /v3/keywords_data/id_list  |
[**keywordsDataErrors**](KeywordsDataApi.md#keywordsDataErrors) | **POST**  /v3/keywords_data/errors  |
[**googleAdsStatus**](KeywordsDataApi.md#googleAdsStatus) | **GET**  /v3/keywords_data/google_ads/status  |
[**keywordsDataGoogleAdsLocations**](KeywordsDataApi.md#keywordsDataGoogleAdsLocations) | **GET**  /v3/keywords_data/google_ads/locations  |
[**keywordsDataGoogleAdsLocationsCountry**](KeywordsDataApi.md#keywordsDataGoogleAdsLocationsCountry) | **GET**  /v3/keywords_data/google_ads/locations/{country}  |
[**keywordsDataGoogleAdsLanguages**](KeywordsDataApi.md#keywordsDataGoogleAdsLanguages) | **GET**  /v3/keywords_data/google_ads/languages  |
[**googleAdsSearchVolumeTaskPost**](KeywordsDataApi.md#googleAdsSearchVolumeTaskPost) | **POST**  /v3/keywords_data/google_ads/search_volume/task_post  |
[**googleAdsSearchVolumeTasksReady**](KeywordsDataApi.md#googleAdsSearchVolumeTasksReady) | **GET**  /v3/keywords_data/google_ads/search_volume/tasks_ready  |
[**googleAdsSearchVolumeTaskGet**](KeywordsDataApi.md#googleAdsSearchVolumeTaskGet) | **GET**  /v3/keywords_data/google_ads/search_volume/task_get/{id}  |
[**googleAdsSearchVolumeLive**](KeywordsDataApi.md#googleAdsSearchVolumeLive) | **POST**  /v3/keywords_data/google_ads/search_volume/live  |
[**googleAdsKeywordsForSiteTaskPost**](KeywordsDataApi.md#googleAdsKeywordsForSiteTaskPost) | **POST**  /v3/keywords_data/google_ads/keywords_for_site/task_post  |
[**googleAdsKeywordsForSiteTasksReady**](KeywordsDataApi.md#googleAdsKeywordsForSiteTasksReady) | **GET**  /v3/keywords_data/google_ads/keywords_for_site/tasks_ready  |
[**googleAdsKeywordsForSiteTaskGet**](KeywordsDataApi.md#googleAdsKeywordsForSiteTaskGet) | **GET**  /v3/keywords_data/google_ads/keywords_for_site/task_get/{id}  |
[**googleAdsKeywordsForSiteLive**](KeywordsDataApi.md#googleAdsKeywordsForSiteLive) | **POST**  /v3/keywords_data/google_ads/keywords_for_site/live  |
[**googleAdsKeywordsForKeywordsTaskPost**](KeywordsDataApi.md#googleAdsKeywordsForKeywordsTaskPost) | **POST**  /v3/keywords_data/google_ads/keywords_for_keywords/task_post  |
[**googleAdsKeywordsForKeywordsTasksReady**](KeywordsDataApi.md#googleAdsKeywordsForKeywordsTasksReady) | **GET**  /v3/keywords_data/google_ads/keywords_for_keywords/tasks_ready  |
[**googleAdsKeywordsForKeywordsTaskGet**](KeywordsDataApi.md#googleAdsKeywordsForKeywordsTaskGet) | **GET**  /v3/keywords_data/google_ads/keywords_for_keywords/task_get/{id}  |
[**googleAdsKeywordsForKeywordsLive**](KeywordsDataApi.md#googleAdsKeywordsForKeywordsLive) | **POST**  /v3/keywords_data/google_ads/keywords_for_keywords/live  |
[**googleAdsAdTrafficByKeywordsTaskPost**](KeywordsDataApi.md#googleAdsAdTrafficByKeywordsTaskPost) | **POST**  /v3/keywords_data/google_ads/ad_traffic_by_keywords/task_post  |
[**googleAdsAdTrafficByKeywordsTasksReady**](KeywordsDataApi.md#googleAdsAdTrafficByKeywordsTasksReady) | **GET**  /v3/keywords_data/google_ads/ad_traffic_by_keywords/tasks_ready  |
[**googleAdsAdTrafficByKeywordsTaskGet**](KeywordsDataApi.md#googleAdsAdTrafficByKeywordsTaskGet) | **GET**  /v3/keywords_data/google_ads/ad_traffic_by_keywords/task_get/{id}  |
[**googleAdsAdTrafficByKeywordsLive**](KeywordsDataApi.md#googleAdsAdTrafficByKeywordsLive) | **POST**  /v3/keywords_data/google_ads/ad_traffic_by_keywords/live  |
[**keywordsDataGoogleTrendsLocations**](KeywordsDataApi.md#keywordsDataGoogleTrendsLocations) | **GET**  /v3/keywords_data/google_trends/locations  |
[**keywordsDataGoogleTrendsLocationsCountry**](KeywordsDataApi.md#keywordsDataGoogleTrendsLocationsCountry) | **GET**  /v3/keywords_data/google_trends/locations/{country}  |
[**keywordsDataGoogleTrendsLanguages**](KeywordsDataApi.md#keywordsDataGoogleTrendsLanguages) | **GET**  /v3/keywords_data/google_trends/languages  |
[**googleTrendsCategories**](KeywordsDataApi.md#googleTrendsCategories) | **GET**  /v3/keywords_data/google_trends/categories  |
[**googleTrendsExploreTaskPost**](KeywordsDataApi.md#googleTrendsExploreTaskPost) | **POST**  /v3/keywords_data/google_trends/explore/task_post  |
[**googleTrendsExploreTasksReady**](KeywordsDataApi.md#googleTrendsExploreTasksReady) | **GET**  /v3/keywords_data/google_trends/explore/tasks_ready  |
[**googleTrendsExploreTaskGet**](KeywordsDataApi.md#googleTrendsExploreTaskGet) | **GET**  /v3/keywords_data/google_trends/explore/task_get/{id}  |
[**googleTrendsExploreLive**](KeywordsDataApi.md#googleTrendsExploreLive) | **POST**  /v3/keywords_data/google_trends/explore/live  |
[**keywordsDataDataforseoTrendsLocations**](KeywordsDataApi.md#keywordsDataDataforseoTrendsLocations) | **GET**  /v3/keywords_data/dataforseo_trends/locations  |
[**keywordsDataDataforseoTrendsLocationsCountry**](KeywordsDataApi.md#keywordsDataDataforseoTrendsLocationsCountry) | **GET**  /v3/keywords_data/dataforseo_trends/locations/{country}  |
[**dataforseoTrendsExploreLive**](KeywordsDataApi.md#dataforseoTrendsExploreLive) | **POST**  /v3/keywords_data/dataforseo_trends/explore/live  |
[**dataforseoTrendsSubregionInterestsLive**](KeywordsDataApi.md#dataforseoTrendsSubregionInterestsLive) | **POST**  /v3/keywords_data/dataforseo_trends/subregion_interests/live  |
[**dataforseoTrendsDemographyLive**](KeywordsDataApi.md#dataforseoTrendsDemographyLive) | **POST**  /v3/keywords_data/dataforseo_trends/demography/live  |
[**dataforseoTrendsMergedDataLive**](KeywordsDataApi.md#dataforseoTrendsMergedDataLive) | **POST**  /v3/keywords_data/dataforseo_trends/merged_data/live  |
[**keywordsDataBingLocations**](KeywordsDataApi.md#keywordsDataBingLocations) | **GET**  /v3/keywords_data/bing/locations  |
[**keywordsDataBingLanguages**](KeywordsDataApi.md#keywordsDataBingLanguages) | **GET**  /v3/keywords_data/bing/languages  |
[**bingSearchVolumeTaskPost**](KeywordsDataApi.md#bingSearchVolumeTaskPost) | **POST**  /v3/keywords_data/bing/search_volume/task_post  |
[**bingSearchVolumeTasksReady**](KeywordsDataApi.md#bingSearchVolumeTasksReady) | **GET**  /v3/keywords_data/bing/search_volume/tasks_ready  |
[**bingSearchVolumeTaskGet**](KeywordsDataApi.md#bingSearchVolumeTaskGet) | **GET**  /v3/keywords_data/bing/search_volume/task_get/{id}  |
[**bingSearchVolumeLive**](KeywordsDataApi.md#bingSearchVolumeLive) | **POST**  /v3/keywords_data/bing/search_volume/live  |
[**bingAudienceEstimationJobFunctions**](KeywordsDataApi.md#bingAudienceEstimationJobFunctions) | **GET**  /v3/keywords_data/bing/audience_estimation/job_functions  |
[**bingAudienceEstimationIndustries**](KeywordsDataApi.md#bingAudienceEstimationIndustries) | **GET**  /v3/keywords_data/bing/audience_estimation/industries  |
[**bingAudienceEstimationTaskPost**](KeywordsDataApi.md#bingAudienceEstimationTaskPost) | **POST**  /v3/keywords_data/bing/audience_estimation/task_post  |
[**bingAudienceEstimationTasksReady**](KeywordsDataApi.md#bingAudienceEstimationTasksReady) | **GET**  /v3/keywords_data/bing/audience_estimation/tasks_ready  |
[**bingAudienceEstimationTaskGet**](KeywordsDataApi.md#bingAudienceEstimationTaskGet) | **GET**  /v3/keywords_data/bing/audience_estimation/task_get/{id}  |
[**bingAudienceEstimationLive**](KeywordsDataApi.md#bingAudienceEstimationLive) | **POST**  /v3/keywords_data/bing/audience_estimation/live  |
[**bingKeywordsForSiteTaskPost**](KeywordsDataApi.md#bingKeywordsForSiteTaskPost) | **POST**  /v3/keywords_data/bing/keywords_for_site/task_post  |
[**bingKeywordsForSiteTasksReady**](KeywordsDataApi.md#bingKeywordsForSiteTasksReady) | **GET**  /v3/keywords_data/bing/keywords_for_site/tasks_ready  |
[**bingKeywordsForSiteTaskGet**](KeywordsDataApi.md#bingKeywordsForSiteTaskGet) | **GET**  /v3/keywords_data/bing/keywords_for_site/task_get/{id}  |
[**bingKeywordsForSiteLive**](KeywordsDataApi.md#bingKeywordsForSiteLive) | **POST**  /v3/keywords_data/bing/keywords_for_site/live  |
[**bingKeywordsForKeywordsTaskPost**](KeywordsDataApi.md#bingKeywordsForKeywordsTaskPost) | **POST**  /v3/keywords_data/bing/keywords_for_keywords/task_post  |
[**bingKeywordsForKeywordsTasksReady**](KeywordsDataApi.md#bingKeywordsForKeywordsTasksReady) | **GET**  /v3/keywords_data/bing/keywords_for_keywords/tasks_ready  |
[**bingKeywordsForKeywordsTaskGet**](KeywordsDataApi.md#bingKeywordsForKeywordsTaskGet) | **GET**  /v3/keywords_data/bing/keywords_for_keywords/task_get/{id}  |
[**bingKeywordsForKeywordsLive**](KeywordsDataApi.md#bingKeywordsForKeywordsLive) | **POST**  /v3/keywords_data/bing/keywords_for_keywords/live  |
[**keywordsDataBingKeywordPerformanceLocationsAndLanguages**](KeywordsDataApi.md#keywordsDataBingKeywordPerformanceLocationsAndLanguages) | **GET**  /v3/keywords_data/bing/keyword_performance/locations_and_languages  |
[**bingKeywordPerformanceTaskPost**](KeywordsDataApi.md#bingKeywordPerformanceTaskPost) | **POST**  /v3/keywords_data/bing/keyword_performance/task_post  |
[**bingKeywordPerformanceTasksReady**](KeywordsDataApi.md#bingKeywordPerformanceTasksReady) | **GET**  /v3/keywords_data/bing/keyword_performance/tasks_ready  |
[**bingKeywordPerformanceTaskGet**](KeywordsDataApi.md#bingKeywordPerformanceTaskGet) | **GET**  /v3/keywords_data/bing/keyword_performance/task_get/{id}  |
[**bingKeywordPerformanceLive**](KeywordsDataApi.md#bingKeywordPerformanceLive) | **POST**  /v3/keywords_data/bing/keyword_performance/live  |
[**keywordsDataBingSearchVolumeHistoryLocationsAndLanguages**](KeywordsDataApi.md#keywordsDataBingSearchVolumeHistoryLocationsAndLanguages) | **GET**  /v3/keywords_data/bing/search_volume_history/locations_and_languages  |
[**bingSearchVolumeHistoryTaskPost**](KeywordsDataApi.md#bingSearchVolumeHistoryTaskPost) | **POST**  /v3/keywords_data/bing/search_volume_history/task_post  |
[**bingSearchVolumeHistoryTasksReady**](KeywordsDataApi.md#bingSearchVolumeHistoryTasksReady) | **GET**  /v3/keywords_data/bing/search_volume_history/tasks_ready  |
[**bingSearchVolumeHistoryTaskGet**](KeywordsDataApi.md#bingSearchVolumeHistoryTaskGet) | **GET**  /v3/keywords_data/bing/search_volume_history/task_get/{id}  |
[**bingSearchVolumeHistoryLive**](KeywordsDataApi.md#bingSearchVolumeHistoryLive) | **POST**  /v3/keywords_data/bing/search_volume_history/live  |
[**keywordsDataClickstreamDataLocationsAndLanguages**](KeywordsDataApi.md#keywordsDataClickstreamDataLocationsAndLanguages) | **GET**  /v3/keywords_data/clickstream_data/locations_and_languages  |
[**clickstreamDataDataforseoSearchVolumeLive**](KeywordsDataApi.md#clickstreamDataDataforseoSearchVolumeLive) | **POST**  /v3/keywords_data/clickstream_data/dataforseo_search_volume/live  |
[**clickstreamDataGlobalSearchVolumeLive**](KeywordsDataApi.md#clickstreamDataGlobalSearchVolumeLive) | **POST**  /v3/keywords_data/clickstream_data/global_search_volume/live  |
[**clickstreamDataBulkSearchVolumeLive**](KeywordsDataApi.md#clickstreamDataBulkSearchVolumeLive) | **POST**  /v3/keywords_data/clickstream_data/bulk_search_volume/live  |

<a id="keywordsDataIdList"></a>
# **keywordsDataIdList**
> KeywordsDataIdListResponseInfo keywordsDataIdList()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_id_list_request_info import List[Optional[KeywordsDataIdListRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_id_list([KeywordsDataIdListRequestInfo(
                datetime_from="2025-04-17 06:08:20 +00:00",
                datetime_to="2025-06-17 06:08:20 +00:00",
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
    | **** | [**List&lt;List[Optional[KeywordsDataIdListRequestInfo]]&gt;**](List[Optional[KeywordsDataIdListRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataIdListResponseInfo**](KeywordsDataIdListResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataErrors"></a>
# **keywordsDataErrors**
> KeywordsDataErrorsResponseInfo keywordsDataErrors()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_errors_request_info import List[Optional[KeywordsDataErrorsRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_errors([KeywordsDataErrorsRequestInfo(
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
    | **** | [**List&lt;List[Optional[KeywordsDataErrorsRequestInfo]]&gt;**](List[Optional[KeywordsDataErrorsRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataErrorsResponseInfo**](KeywordsDataErrorsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsStatus"></a>
# **googleAdsStatus**
> KeywordsDataGoogleAdsStatusResponseInfo googleAdsStatus()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_status()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsStatusResponseInfo**](KeywordsDataGoogleAdsStatusResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataGoogleAdsLocations"></a>
# **keywordsDataGoogleAdsLocations**
> KeywordsDataGoogleAdsLocationsResponseInfo keywordsDataGoogleAdsLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_google_ads_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsLocationsResponseInfo**](KeywordsDataGoogleAdsLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataGoogleAdsLocationsCountry"></a>
# **keywordsDataGoogleAdsLocationsCountry**
> KeywordsDataGoogleAdsLocationsCountryResponseInfo keywordsDataGoogleAdsLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        country = "us"
        response = keywords_data_api.keywords_data_google_ads_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsLocationsCountryResponseInfo**](KeywordsDataGoogleAdsLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataGoogleAdsLanguages"></a>
# **keywordsDataGoogleAdsLanguages**
> KeywordsDataGoogleAdsLanguagesResponseInfo keywordsDataGoogleAdsLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_google_ads_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsLanguagesResponseInfo**](KeywordsDataGoogleAdsLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsSearchVolumeTaskPost"></a>
# **googleAdsSearchVolumeTaskPost**
> KeywordsDataGoogleAdsSearchVolumeTaskPostResponseInfo googleAdsSearchVolumeTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_google_ads_search_volume_task_post_request_info import List[Optional[KeywordsDataGoogleAdsSearchVolumeTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_search_volume_task_post([KeywordsDataGoogleAdsSearchVolumeTaskPostRequestInfo(
                keywords=[
                        "buy laptop",
                        "cheap laptops for sale",
                        "purchase laptop",
                    ],
                location_name="United States",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataGoogleAdsSearchVolumeTaskPostRequestInfo]]&gt;**](List[Optional[KeywordsDataGoogleAdsSearchVolumeTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataGoogleAdsSearchVolumeTaskPostResponseInfo**](KeywordsDataGoogleAdsSearchVolumeTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsSearchVolumeTasksReady"></a>
# **googleAdsSearchVolumeTasksReady**
> KeywordsDataGoogleAdsSearchVolumeTasksReadyResponseInfo googleAdsSearchVolumeTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_search_volume_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsSearchVolumeTasksReadyResponseInfo**](KeywordsDataGoogleAdsSearchVolumeTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsSearchVolumeTaskGet"></a>
# **googleAdsSearchVolumeTaskGet**
> KeywordsDataGoogleAdsSearchVolumeTaskGetResponseInfo googleAdsSearchVolumeTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = keywords_data_api.google_ads_search_volume_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsSearchVolumeTaskGetResponseInfo**](KeywordsDataGoogleAdsSearchVolumeTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsSearchVolumeLive"></a>
# **googleAdsSearchVolumeLive**
> KeywordsDataGoogleAdsSearchVolumeLiveResponseInfo googleAdsSearchVolumeLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_google_ads_search_volume_live_request_info import List[Optional[KeywordsDataGoogleAdsSearchVolumeLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_search_volume_live([KeywordsDataGoogleAdsSearchVolumeLiveRequestInfo(
                keywords=[
                        "buy laptop",
                        "cheap laptops for sale",
                        "purchase laptop",
                    ],
                location_code=2840,
                search_partners=True,
                date_from="2025-04-17",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataGoogleAdsSearchVolumeLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataGoogleAdsSearchVolumeLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataGoogleAdsSearchVolumeLiveResponseInfo**](KeywordsDataGoogleAdsSearchVolumeLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsKeywordsForSiteTaskPost"></a>
# **googleAdsKeywordsForSiteTaskPost**
> KeywordsDataGoogleAdsKeywordsForSiteTaskPostResponseInfo googleAdsKeywordsForSiteTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_google_ads_keywords_for_site_task_post_request_info import List[Optional[KeywordsDataGoogleAdsKeywordsForSiteTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_keywords_for_site_task_post([KeywordsDataGoogleAdsKeywordsForSiteTaskPostRequestInfo(
                target="dataforseo.com",
                location_code=2840,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataGoogleAdsKeywordsForSiteTaskPostRequestInfo]]&gt;**](List[Optional[KeywordsDataGoogleAdsKeywordsForSiteTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataGoogleAdsKeywordsForSiteTaskPostResponseInfo**](KeywordsDataGoogleAdsKeywordsForSiteTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsKeywordsForSiteTasksReady"></a>
# **googleAdsKeywordsForSiteTasksReady**
> KeywordsDataGoogleAdsKeywordsForSiteTasksReadyResponseInfo googleAdsKeywordsForSiteTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_keywords_for_site_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsKeywordsForSiteTasksReadyResponseInfo**](KeywordsDataGoogleAdsKeywordsForSiteTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsKeywordsForSiteTaskGet"></a>
# **googleAdsKeywordsForSiteTaskGet**
> KeywordsDataGoogleAdsKeywordsForSiteTaskGetResponseInfo googleAdsKeywordsForSiteTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = keywords_data_api.google_ads_keywords_for_site_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsKeywordsForSiteTaskGetResponseInfo**](KeywordsDataGoogleAdsKeywordsForSiteTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsKeywordsForSiteLive"></a>
# **googleAdsKeywordsForSiteLive**
> KeywordsDataGoogleAdsKeywordsForSiteLiveResponseInfo googleAdsKeywordsForSiteLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_google_ads_keywords_for_site_live_request_info import List[Optional[KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_keywords_for_site_live([KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo(
                target="dataforseo.com",
                location_code=2840,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataGoogleAdsKeywordsForSiteLiveResponseInfo**](KeywordsDataGoogleAdsKeywordsForSiteLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsKeywordsForKeywordsTaskPost"></a>
# **googleAdsKeywordsForKeywordsTaskPost**
> KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostResponseInfo googleAdsKeywordsForKeywordsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_google_ads_keywords_for_keywords_task_post_request_info import List[Optional[KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_keywords_for_keywords_task_post([KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostRequestInfo(
                keywords=[
                        "phone",
                        "cellphone",
                    ],
                location_code=2840,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostRequestInfo]]&gt;**](List[Optional[KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostResponseInfo**](KeywordsDataGoogleAdsKeywordsForKeywordsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsKeywordsForKeywordsTasksReady"></a>
# **googleAdsKeywordsForKeywordsTasksReady**
> KeywordsDataGoogleAdsKeywordsForKeywordsTasksReadyResponseInfo googleAdsKeywordsForKeywordsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_keywords_for_keywords_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsKeywordsForKeywordsTasksReadyResponseInfo**](KeywordsDataGoogleAdsKeywordsForKeywordsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsKeywordsForKeywordsTaskGet"></a>
# **googleAdsKeywordsForKeywordsTaskGet**
> KeywordsDataGoogleAdsKeywordsForKeywordsTaskGetResponseInfo googleAdsKeywordsForKeywordsTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = keywords_data_api.google_ads_keywords_for_keywords_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsKeywordsForKeywordsTaskGetResponseInfo**](KeywordsDataGoogleAdsKeywordsForKeywordsTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsKeywordsForKeywordsLive"></a>
# **googleAdsKeywordsForKeywordsLive**
> KeywordsDataGoogleAdsKeywordsForKeywordsLiveResponseInfo googleAdsKeywordsForKeywordsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_google_ads_keywords_for_keywords_live_request_info import List[Optional[KeywordsDataGoogleAdsKeywordsForKeywordsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_keywords_for_keywords_live([KeywordsDataGoogleAdsKeywordsForKeywordsLiveRequestInfo(
                keywords=[
                        "phone",
                        "cellphone",
                    ],
                location_code=2840,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataGoogleAdsKeywordsForKeywordsLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataGoogleAdsKeywordsForKeywordsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataGoogleAdsKeywordsForKeywordsLiveResponseInfo**](KeywordsDataGoogleAdsKeywordsForKeywordsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsAdTrafficByKeywordsTaskPost"></a>
# **googleAdsAdTrafficByKeywordsTaskPost**
> KeywordsDataGoogleAdsAdTrafficByKeywordsTaskPostResponseInfo googleAdsAdTrafficByKeywordsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_google_ads_ad_traffic_by_keywords_task_post_request_info import List[Optional[KeywordsDataGoogleAdsAdTrafficByKeywordsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_ad_traffic_by_keywords_task_post([KeywordsDataGoogleAdsAdTrafficByKeywordsTaskPostRequestInfo(
                keywords=[
                        "seo marketing",
                    ],
                bid=999,
                match="exact",
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
    | **** | [**List&lt;List[Optional[KeywordsDataGoogleAdsAdTrafficByKeywordsTaskPostRequestInfo]]&gt;**](List[Optional[KeywordsDataGoogleAdsAdTrafficByKeywordsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataGoogleAdsAdTrafficByKeywordsTaskPostResponseInfo**](KeywordsDataGoogleAdsAdTrafficByKeywordsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsAdTrafficByKeywordsTasksReady"></a>
# **googleAdsAdTrafficByKeywordsTasksReady**
> KeywordsDataGoogleAdsAdTrafficByKeywordsTasksReadyResponseInfo googleAdsAdTrafficByKeywordsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_ad_traffic_by_keywords_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsAdTrafficByKeywordsTasksReadyResponseInfo**](KeywordsDataGoogleAdsAdTrafficByKeywordsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsAdTrafficByKeywordsTaskGet"></a>
# **googleAdsAdTrafficByKeywordsTaskGet**
> KeywordsDataGoogleAdsAdTrafficByKeywordsTaskGetResponseInfo googleAdsAdTrafficByKeywordsTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = keywords_data_api.google_ads_ad_traffic_by_keywords_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleAdsAdTrafficByKeywordsTaskGetResponseInfo**](KeywordsDataGoogleAdsAdTrafficByKeywordsTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAdsAdTrafficByKeywordsLive"></a>
# **googleAdsAdTrafficByKeywordsLive**
> KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResponseInfo googleAdsAdTrafficByKeywordsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_google_ads_ad_traffic_by_keywords_live_request_info import List[Optional[KeywordsDataGoogleAdsAdTrafficByKeywordsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_ads_ad_traffic_by_keywords_live([KeywordsDataGoogleAdsAdTrafficByKeywordsLiveRequestInfo(
                keywords=[
                        "seo marketing",
                    ],
                bid=999,
                match="exact",
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
    | **** | [**List&lt;List[Optional[KeywordsDataGoogleAdsAdTrafficByKeywordsLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataGoogleAdsAdTrafficByKeywordsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResponseInfo**](KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataGoogleTrendsLocations"></a>
# **keywordsDataGoogleTrendsLocations**
> KeywordsDataGoogleTrendsLocationsResponseInfo keywordsDataGoogleTrendsLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_google_trends_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleTrendsLocationsResponseInfo**](KeywordsDataGoogleTrendsLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataGoogleTrendsLocationsCountry"></a>
# **keywordsDataGoogleTrendsLocationsCountry**
> KeywordsDataGoogleTrendsLocationsCountryResponseInfo keywordsDataGoogleTrendsLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        country = "us"
        response = keywords_data_api.keywords_data_google_trends_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleTrendsLocationsCountryResponseInfo**](KeywordsDataGoogleTrendsLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataGoogleTrendsLanguages"></a>
# **keywordsDataGoogleTrendsLanguages**
> KeywordsDataGoogleTrendsLanguagesResponseInfo keywordsDataGoogleTrendsLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_google_trends_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleTrendsLanguagesResponseInfo**](KeywordsDataGoogleTrendsLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleTrendsCategories"></a>
# **googleTrendsCategories**
> KeywordsDataGoogleTrendsCategoriesResponseInfo googleTrendsCategories()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_trends_categories()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleTrendsCategoriesResponseInfo**](KeywordsDataGoogleTrendsCategoriesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleTrendsExploreTaskPost"></a>
# **googleTrendsExploreTaskPost**
> KeywordsDataGoogleTrendsExploreTaskPostResponseInfo googleTrendsExploreTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_google_trends_explore_task_post_request_info import List[Optional[KeywordsDataGoogleTrendsExploreTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_trends_explore_task_post([KeywordsDataGoogleTrendsExploreTaskPostRequestInfo(
                keywords=[
                        "seo api",
                        "rank api",
                    ],
                type="youtube",
                category_code=3,
                date_from="2025-04-17",
                date_to="2025-06-17",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataGoogleTrendsExploreTaskPostRequestInfo]]&gt;**](List[Optional[KeywordsDataGoogleTrendsExploreTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataGoogleTrendsExploreTaskPostResponseInfo**](KeywordsDataGoogleTrendsExploreTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleTrendsExploreTasksReady"></a>
# **googleTrendsExploreTasksReady**
> KeywordsDataGoogleTrendsExploreTasksReadyResponseInfo googleTrendsExploreTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_trends_explore_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleTrendsExploreTasksReadyResponseInfo**](KeywordsDataGoogleTrendsExploreTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleTrendsExploreTaskGet"></a>
# **googleTrendsExploreTaskGet**
> KeywordsDataGoogleTrendsExploreTaskGetResponseInfo googleTrendsExploreTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = keywords_data_api.google_trends_explore_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataGoogleTrendsExploreTaskGetResponseInfo**](KeywordsDataGoogleTrendsExploreTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleTrendsExploreLive"></a>
# **googleTrendsExploreLive**
> KeywordsDataGoogleTrendsExploreLiveResponseInfo googleTrendsExploreLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_google_trends_explore_live_request_info import List[Optional[KeywordsDataGoogleTrendsExploreLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.google_trends_explore_live([KeywordsDataGoogleTrendsExploreLiveRequestInfo(
                keywords=[
                        "rugby",
                        "cricket",
                    ],
                location_name="United States",
                type="youtube",
                category_code=3,
                date_from="2025-04-17",
                date_to="2025-06-17",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataGoogleTrendsExploreLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataGoogleTrendsExploreLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataGoogleTrendsExploreLiveResponseInfo**](KeywordsDataGoogleTrendsExploreLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataDataforseoTrendsLocations"></a>
# **keywordsDataDataforseoTrendsLocations**
> KeywordsDataDataforseoTrendsLocationsResponseInfo keywordsDataDataforseoTrendsLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_dataforseo_trends_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataDataforseoTrendsLocationsResponseInfo**](KeywordsDataDataforseoTrendsLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataDataforseoTrendsLocationsCountry"></a>
# **keywordsDataDataforseoTrendsLocationsCountry**
> KeywordsDataDataforseoTrendsLocationsCountryResponseInfo keywordsDataDataforseoTrendsLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        country = "us"
        response = keywords_data_api.keywords_data_dataforseo_trends_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataDataforseoTrendsLocationsCountryResponseInfo**](KeywordsDataDataforseoTrendsLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="dataforseoTrendsExploreLive"></a>
# **dataforseoTrendsExploreLive**
> KeywordsDataDataforseoTrendsExploreLiveResponseInfo dataforseoTrendsExploreLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_dataforseo_trends_explore_live_request_info import List[Optional[KeywordsDataDataforseoTrendsExploreLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.dataforseo_trends_explore_live([KeywordsDataDataforseoTrendsExploreLiveRequestInfo(
                keywords=[
                        "iphone 14",
                        "samsung s23",
                    ],
                location_code=2840,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataDataforseoTrendsExploreLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataDataforseoTrendsExploreLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataDataforseoTrendsExploreLiveResponseInfo**](KeywordsDataDataforseoTrendsExploreLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="dataforseoTrendsSubregionInterestsLive"></a>
# **dataforseoTrendsSubregionInterestsLive**
> KeywordsDataDataforseoTrendsSubregionInterestsLiveResponseInfo dataforseoTrendsSubregionInterestsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_dataforseo_trends_subregion_interests_live_request_info import List[Optional[KeywordsDataDataforseoTrendsSubregionInterestsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.dataforseo_trends_subregion_interests_live([KeywordsDataDataforseoTrendsSubregionInterestsLiveRequestInfo(
                keywords=[
                        "rugby",
                        "cricket",
                    ],
                location_name="United States",
                type="web",
                date_from="2025-04-17",
                date_to="2025-06-17",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataDataforseoTrendsSubregionInterestsLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataDataforseoTrendsSubregionInterestsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataDataforseoTrendsSubregionInterestsLiveResponseInfo**](KeywordsDataDataforseoTrendsSubregionInterestsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="dataforseoTrendsDemographyLive"></a>
# **dataforseoTrendsDemographyLive**
> KeywordsDataDataforseoTrendsDemographyLiveResponseInfo dataforseoTrendsDemographyLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_dataforseo_trends_demography_live_request_info import List[Optional[KeywordsDataDataforseoTrendsDemographyLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.dataforseo_trends_demography_live([KeywordsDataDataforseoTrendsDemographyLiveRequestInfo(
                keywords=[
                        "rugby",
                        "cricket",
                    ],
                location_name="United States",
                type="web",
                date_from="2025-04-17",
                date_to="2025-06-17",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataDataforseoTrendsDemographyLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataDataforseoTrendsDemographyLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataDataforseoTrendsDemographyLiveResponseInfo**](KeywordsDataDataforseoTrendsDemographyLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="dataforseoTrendsMergedDataLive"></a>
# **dataforseoTrendsMergedDataLive**
> KeywordsDataDataforseoTrendsMergedDataLiveResponseInfo dataforseoTrendsMergedDataLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_dataforseo_trends_merged_data_live_request_info import List[Optional[KeywordsDataDataforseoTrendsMergedDataLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.dataforseo_trends_merged_data_live([KeywordsDataDataforseoTrendsMergedDataLiveRequestInfo(
                keywords=[
                        "rugby",
                        "cricket",
                    ],
                location_name="United States",
                type="web",
                date_from="2025-04-17",
                date_to="2025-06-17",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataDataforseoTrendsMergedDataLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataDataforseoTrendsMergedDataLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataDataforseoTrendsMergedDataLiveResponseInfo**](KeywordsDataDataforseoTrendsMergedDataLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataBingLocations"></a>
# **keywordsDataBingLocations**
> KeywordsDataBingLocationsResponseInfo keywordsDataBingLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_bing_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingLocationsResponseInfo**](KeywordsDataBingLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataBingLanguages"></a>
# **keywordsDataBingLanguages**
> KeywordsDataBingLanguagesResponseInfo keywordsDataBingLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_bing_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingLanguagesResponseInfo**](KeywordsDataBingLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingSearchVolumeTaskPost"></a>
# **bingSearchVolumeTaskPost**
> KeywordsDataBingSearchVolumeTaskPostResponseInfo bingSearchVolumeTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_search_volume_task_post_request_info import List[Optional[KeywordsDataBingSearchVolumeTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_search_volume_task_post([KeywordsDataBingSearchVolumeTaskPostRequestInfo(
                keywords=[
                        "average page rpm adsense",
                        "adsense blank ads how long",
                        "leads and prospects",
                    ],
                location_name="United States",
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataBingSearchVolumeTaskPostRequestInfo]]&gt;**](List[Optional[KeywordsDataBingSearchVolumeTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingSearchVolumeTaskPostResponseInfo**](KeywordsDataBingSearchVolumeTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingSearchVolumeTasksReady"></a>
# **bingSearchVolumeTasksReady**
> KeywordsDataBingSearchVolumeTasksReadyResponseInfo bingSearchVolumeTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_search_volume_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingSearchVolumeTasksReadyResponseInfo**](KeywordsDataBingSearchVolumeTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingSearchVolumeTaskGet"></a>
# **bingSearchVolumeTaskGet**
> KeywordsDataBingSearchVolumeTaskGetResponseInfo bingSearchVolumeTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = keywords_data_api.bing_search_volume_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingSearchVolumeTaskGetResponseInfo**](KeywordsDataBingSearchVolumeTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingSearchVolumeLive"></a>
# **bingSearchVolumeLive**
> KeywordsDataBingSearchVolumeLiveResponseInfo bingSearchVolumeLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_search_volume_live_request_info import List[Optional[KeywordsDataBingSearchVolumeLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_search_volume_live([KeywordsDataBingSearchVolumeLiveRequestInfo(
                keywords=[
                        "tom and jerry",
                        "silicon valley",
                        "spider man",
                    ],
                location_name="United States",
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataBingSearchVolumeLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataBingSearchVolumeLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingSearchVolumeLiveResponseInfo**](KeywordsDataBingSearchVolumeLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingAudienceEstimationJobFunctions"></a>
# **bingAudienceEstimationJobFunctions**
> KeywordsDataBingAudienceEstimationJobFunctionsResponseInfo bingAudienceEstimationJobFunctions()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_audience_estimation_job_functions()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingAudienceEstimationJobFunctionsResponseInfo**](KeywordsDataBingAudienceEstimationJobFunctionsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingAudienceEstimationIndustries"></a>
# **bingAudienceEstimationIndustries**
> KeywordsDataBingAudienceEstimationIndustriesResponseInfo bingAudienceEstimationIndustries()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_audience_estimation_industries()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingAudienceEstimationIndustriesResponseInfo**](KeywordsDataBingAudienceEstimationIndustriesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingAudienceEstimationTaskPost"></a>
# **bingAudienceEstimationTaskPost**
> KeywordsDataBingAudienceEstimationTaskPostResponseInfo bingAudienceEstimationTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_audience_estimation_task_post_request_info import List[Optional[KeywordsDataBingAudienceEstimationTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_audience_estimation_task_post([KeywordsDataBingAudienceEstimationTaskPostRequestInfo(
                location_coordinate="29.6821525,-82.4098881,100",
                age=[
                        "twenty_five_to_thirty_four",
                        "eighteen_to_twenty_four",
                        "unknown",
                    ],
                bid=1,
                daily_budget=24,
                gender=[
                        "male",
                    ],
                industry=[
                        "806303407",
                        "806301758",
                    ],
                job_function=[
                        "806298607",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataBingAudienceEstimationTaskPostRequestInfo]]&gt;**](List[Optional[KeywordsDataBingAudienceEstimationTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingAudienceEstimationTaskPostResponseInfo**](KeywordsDataBingAudienceEstimationTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingAudienceEstimationTasksReady"></a>
# **bingAudienceEstimationTasksReady**
> KeywordsDataBingAudienceEstimationTasksReadyResponseInfo bingAudienceEstimationTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_audience_estimation_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingAudienceEstimationTasksReadyResponseInfo**](KeywordsDataBingAudienceEstimationTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingAudienceEstimationTaskGet"></a>
# **bingAudienceEstimationTaskGet**
> KeywordsDataBingAudienceEstimationTaskGetResponseInfo bingAudienceEstimationTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = keywords_data_api.bing_audience_estimation_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingAudienceEstimationTaskGetResponseInfo**](KeywordsDataBingAudienceEstimationTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingAudienceEstimationLive"></a>
# **bingAudienceEstimationLive**
> KeywordsDataBingAudienceEstimationLiveResponseInfo bingAudienceEstimationLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_audience_estimation_live_request_info import List[Optional[KeywordsDataBingAudienceEstimationLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_audience_estimation_live([KeywordsDataBingAudienceEstimationLiveRequestInfo(
                location_coordinate="29.6821525,-82.4098881,100",
                age=[
                        "twenty_five_to_thirty_four",
                        "eighteen_to_twenty_four",
                        "unknown",
                    ],
                bid=1,
                daily_budget=24,
                gender=[
                        "male",
                    ],
                industry=[
                        "806303407",
                        "806301758",
                    ],
                job_function=[
                        "806298607",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataBingAudienceEstimationLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataBingAudienceEstimationLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingAudienceEstimationLiveResponseInfo**](KeywordsDataBingAudienceEstimationLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordsForSiteTaskPost"></a>
# **bingKeywordsForSiteTaskPost**
> KeywordsDataBingKeywordsForSiteTaskPostResponseInfo bingKeywordsForSiteTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_keywords_for_site_task_post_request_info import List[Optional[KeywordsDataBingKeywordsForSiteTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_keywords_for_site_task_post([KeywordsDataBingKeywordsForSiteTaskPostRequestInfo(
                target="dataforseo.com",
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
    | **** | [**List&lt;List[Optional[KeywordsDataBingKeywordsForSiteTaskPostRequestInfo]]&gt;**](List[Optional[KeywordsDataBingKeywordsForSiteTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingKeywordsForSiteTaskPostResponseInfo**](KeywordsDataBingKeywordsForSiteTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordsForSiteTasksReady"></a>
# **bingKeywordsForSiteTasksReady**
> KeywordsDataBingKeywordsForSiteTasksReadyResponseInfo bingKeywordsForSiteTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_keywords_for_site_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingKeywordsForSiteTasksReadyResponseInfo**](KeywordsDataBingKeywordsForSiteTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordsForSiteTaskGet"></a>
# **bingKeywordsForSiteTaskGet**
> KeywordsDataBingKeywordsForSiteTaskGetResponseInfo bingKeywordsForSiteTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = keywords_data_api.bing_keywords_for_site_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingKeywordsForSiteTaskGetResponseInfo**](KeywordsDataBingKeywordsForSiteTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordsForSiteLive"></a>
# **bingKeywordsForSiteLive**
> KeywordsDataBingKeywordsForSiteLiveResponseInfo bingKeywordsForSiteLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_keywords_for_site_live_request_info import List[Optional[KeywordsDataBingKeywordsForSiteLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_keywords_for_site_live([KeywordsDataBingKeywordsForSiteLiveRequestInfo(
                target="dataforseo.com",
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
    | **** | [**List&lt;List[Optional[KeywordsDataBingKeywordsForSiteLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataBingKeywordsForSiteLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingKeywordsForSiteLiveResponseInfo**](KeywordsDataBingKeywordsForSiteLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordsForKeywordsTaskPost"></a>
# **bingKeywordsForKeywordsTaskPost**
> KeywordsDataBingKeywordsForKeywordsTaskPostResponseInfo bingKeywordsForKeywordsTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_keywords_for_keywords_task_post_request_info import List[Optional[KeywordsDataBingKeywordsForKeywordsTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_keywords_for_keywords_task_post([KeywordsDataBingKeywordsForKeywordsTaskPostRequestInfo(
                keywords=[
                        "average page rpm adsense",
                        "adsense blank ads how long",
                        "leads and prospects",
                    ],
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
    | **** | [**List&lt;List[Optional[KeywordsDataBingKeywordsForKeywordsTaskPostRequestInfo]]&gt;**](List[Optional[KeywordsDataBingKeywordsForKeywordsTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingKeywordsForKeywordsTaskPostResponseInfo**](KeywordsDataBingKeywordsForKeywordsTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordsForKeywordsTasksReady"></a>
# **bingKeywordsForKeywordsTasksReady**
> KeywordsDataBingKeywordsForKeywordsTasksReadyResponseInfo bingKeywordsForKeywordsTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_keywords_for_keywords_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingKeywordsForKeywordsTasksReadyResponseInfo**](KeywordsDataBingKeywordsForKeywordsTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordsForKeywordsTaskGet"></a>
# **bingKeywordsForKeywordsTaskGet**
> KeywordsDataBingKeywordsForKeywordsTaskGetResponseInfo bingKeywordsForKeywordsTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = keywords_data_api.bing_keywords_for_keywords_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingKeywordsForKeywordsTaskGetResponseInfo**](KeywordsDataBingKeywordsForKeywordsTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordsForKeywordsLive"></a>
# **bingKeywordsForKeywordsLive**
> KeywordsDataBingKeywordsForKeywordsLiveResponseInfo bingKeywordsForKeywordsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_keywords_for_keywords_live_request_info import List[Optional[KeywordsDataBingKeywordsForKeywordsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_keywords_for_keywords_live([KeywordsDataBingKeywordsForKeywordsLiveRequestInfo(
                keywords=[
                        "average page rpm adsense",
                        "adsense blank ads how long",
                        "leads and prospects",
                    ],
                location_name="United States",
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataBingKeywordsForKeywordsLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataBingKeywordsForKeywordsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingKeywordsForKeywordsLiveResponseInfo**](KeywordsDataBingKeywordsForKeywordsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataBingKeywordPerformanceLocationsAndLanguages"></a>
# **keywordsDataBingKeywordPerformanceLocationsAndLanguages**
> KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResponseInfo keywordsDataBingKeywordPerformanceLocationsAndLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_bing_keyword_performance_locations_and_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResponseInfo**](KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordPerformanceTaskPost"></a>
# **bingKeywordPerformanceTaskPost**
> KeywordsDataBingKeywordPerformanceTaskPostResponseInfo bingKeywordPerformanceTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_keyword_performance_task_post_request_info import List[Optional[KeywordsDataBingKeywordPerformanceTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_keyword_performance_task_post([KeywordsDataBingKeywordPerformanceTaskPostRequestInfo(
                keywords=[
                        "dataforseo",
                        "seo",
                        "ranking",
                    ],
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
    | **** | [**List&lt;List[Optional[KeywordsDataBingKeywordPerformanceTaskPostRequestInfo]]&gt;**](List[Optional[KeywordsDataBingKeywordPerformanceTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingKeywordPerformanceTaskPostResponseInfo**](KeywordsDataBingKeywordPerformanceTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordPerformanceTasksReady"></a>
# **bingKeywordPerformanceTasksReady**
> KeywordsDataBingKeywordPerformanceTasksReadyResponseInfo bingKeywordPerformanceTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_keyword_performance_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingKeywordPerformanceTasksReadyResponseInfo**](KeywordsDataBingKeywordPerformanceTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordPerformanceTaskGet"></a>
# **bingKeywordPerformanceTaskGet**
> KeywordsDataBingKeywordPerformanceTaskGetResponseInfo bingKeywordPerformanceTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = keywords_data_api.bing_keyword_performance_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingKeywordPerformanceTaskGetResponseInfo**](KeywordsDataBingKeywordPerformanceTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingKeywordPerformanceLive"></a>
# **bingKeywordPerformanceLive**
> KeywordsDataBingKeywordPerformanceLiveResponseInfo bingKeywordPerformanceLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_keyword_performance_live_request_info import List[Optional[KeywordsDataBingKeywordPerformanceLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_keyword_performance_live([KeywordsDataBingKeywordPerformanceLiveRequestInfo(
                keywords=[
                        "dataforseo",
                        "seo",
                        "ranking",
                    ],
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
    | **** | [**List&lt;List[Optional[KeywordsDataBingKeywordPerformanceLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataBingKeywordPerformanceLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingKeywordPerformanceLiveResponseInfo**](KeywordsDataBingKeywordPerformanceLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataBingSearchVolumeHistoryLocationsAndLanguages"></a>
# **keywordsDataBingSearchVolumeHistoryLocationsAndLanguages**
> KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResponseInfo keywordsDataBingSearchVolumeHistoryLocationsAndLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_bing_search_volume_history_locations_and_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResponseInfo**](KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingSearchVolumeHistoryTaskPost"></a>
# **bingSearchVolumeHistoryTaskPost**
> KeywordsDataBingSearchVolumeHistoryTaskPostResponseInfo bingSearchVolumeHistoryTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_search_volume_history_task_post_request_info import List[Optional[KeywordsDataBingSearchVolumeHistoryTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_search_volume_history_task_post([KeywordsDataBingSearchVolumeHistoryTaskPostRequestInfo(
                keywords=[
                        "10 minute timer",
                    ],
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
    | **** | [**List&lt;List[Optional[KeywordsDataBingSearchVolumeHistoryTaskPostRequestInfo]]&gt;**](List[Optional[KeywordsDataBingSearchVolumeHistoryTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingSearchVolumeHistoryTaskPostResponseInfo**](KeywordsDataBingSearchVolumeHistoryTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingSearchVolumeHistoryTasksReady"></a>
# **bingSearchVolumeHistoryTasksReady**
> KeywordsDataBingSearchVolumeHistoryTasksReadyResponseInfo bingSearchVolumeHistoryTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_search_volume_history_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingSearchVolumeHistoryTasksReadyResponseInfo**](KeywordsDataBingSearchVolumeHistoryTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingSearchVolumeHistoryTaskGet"></a>
# **bingSearchVolumeHistoryTaskGet**
> KeywordsDataBingSearchVolumeHistoryTaskGetResponseInfo bingSearchVolumeHistoryTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = keywords_data_api.bing_search_volume_history_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataBingSearchVolumeHistoryTaskGetResponseInfo**](KeywordsDataBingSearchVolumeHistoryTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingSearchVolumeHistoryLive"></a>
# **bingSearchVolumeHistoryLive**
> KeywordsDataBingSearchVolumeHistoryLiveResponseInfo bingSearchVolumeHistoryLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_bing_search_volume_history_live_request_info import List[Optional[KeywordsDataBingSearchVolumeHistoryLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.bing_search_volume_history_live([KeywordsDataBingSearchVolumeHistoryLiveRequestInfo(
                keywords=[
                        "10 minute timer",
                    ],
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
    | **** | [**List&lt;List[Optional[KeywordsDataBingSearchVolumeHistoryLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataBingSearchVolumeHistoryLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataBingSearchVolumeHistoryLiveResponseInfo**](KeywordsDataBingSearchVolumeHistoryLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="keywordsDataClickstreamDataLocationsAndLanguages"></a>
# **keywordsDataClickstreamDataLocationsAndLanguages**
> KeywordsDataClickstreamDataLocationsAndLanguagesResponseInfo keywordsDataClickstreamDataLocationsAndLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.keywords_data_clickstream_data_locations_and_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**KeywordsDataClickstreamDataLocationsAndLanguagesResponseInfo**](KeywordsDataClickstreamDataLocationsAndLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="clickstreamDataDataforseoSearchVolumeLive"></a>
# **clickstreamDataDataforseoSearchVolumeLive**
> KeywordsDataClickstreamDataDataforseoSearchVolumeLiveResponseInfo clickstreamDataDataforseoSearchVolumeLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_clickstream_data_dataforseo_search_volume_live_request_info import List[Optional[KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.clickstream_data_dataforseo_search_volume_live([KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo(
                keywords=[
                        "you tube",
                        "youtube",
                        "youtub",
                    ],
                location_code=2840,
                language_code="en",
                tag="test-tag",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataClickstreamDataDataforseoSearchVolumeLiveResponseInfo**](KeywordsDataClickstreamDataDataforseoSearchVolumeLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="clickstreamDataGlobalSearchVolumeLive"></a>
# **clickstreamDataGlobalSearchVolumeLive**
> KeywordsDataClickstreamDataGlobalSearchVolumeLiveResponseInfo clickstreamDataGlobalSearchVolumeLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_clickstream_data_global_search_volume_live_request_info import List[Optional[KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.clickstream_data_global_search_volume_live([KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo(
                keywords=[
                        "you tube",
                        "youtube",
                        "youtub",
                    ],
                tag="test-tag",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataClickstreamDataGlobalSearchVolumeLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataClickstreamDataGlobalSearchVolumeLiveResponseInfo**](KeywordsDataClickstreamDataGlobalSearchVolumeLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="clickstreamDataBulkSearchVolumeLive"></a>
# **clickstreamDataBulkSearchVolumeLive**
> KeywordsDataClickstreamDataBulkSearchVolumeLiveResponseInfo clickstreamDataBulkSearchVolumeLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_keywords_data_clickstream_data_bulk_search_volume_live_request_info import List[Optional[KeywordsDataClickstreamDataBulkSearchVolumeLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        keywords_data_api = KeywordsDataApi(api_client)

        response = keywords_data_api.clickstream_data_bulk_search_volume_live([KeywordsDataClickstreamDataBulkSearchVolumeLiveRequestInfo(
                keywords=[
                        "you tube",
                        "youtube",
                        "youtub",
                    ],
                location_code=2840,
                tag="test-tag",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[KeywordsDataClickstreamDataBulkSearchVolumeLiveRequestInfo]]&gt;**](List[Optional[KeywordsDataClickstreamDataBulkSearchVolumeLiveRequestInfo]].md)|  | [optional] |



### Return type

[**KeywordsDataClickstreamDataBulkSearchVolumeLiveResponseInfo**](KeywordsDataClickstreamDataBulkSearchVolumeLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |