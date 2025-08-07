# DataforseoLabsApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**dataforseoLabsIdList**](DataforseoLabsApi.md#dataforseoLabsIdList) | **POST**  /v3/dataforseo_labs/id_list  |
[**dataforseoLabsStatus**](DataforseoLabsApi.md#dataforseoLabsStatus) | **GET**  /v3/dataforseo_labs/status  |
[**dataforseoLabsErrors**](DataforseoLabsApi.md#dataforseoLabsErrors) | **POST**  /v3/dataforseo_labs/errors  |
[**availableFilters**](DataforseoLabsApi.md#availableFilters) | **GET**  /v3/dataforseo_labs/available_filters  |
[**dataforseoLabsLocationsAndLanguages**](DataforseoLabsApi.md#dataforseoLabsLocationsAndLanguages) | **GET**  /v3/dataforseo_labs/locations_and_languages  |
[**categories**](DataforseoLabsApi.md#categories) | **GET**  /v3/dataforseo_labs/categories  |
[**googleAvailableHistory**](DataforseoLabsApi.md#googleAvailableHistory) | **GET**  /v3/dataforseo_labs/google/available_history  |
[**googleKeywordsForSiteLive**](DataforseoLabsApi.md#googleKeywordsForSiteLive) | **POST**  /v3/dataforseo_labs/google/keywords_for_site/live  |
[**googleRelatedKeywordsLive**](DataforseoLabsApi.md#googleRelatedKeywordsLive) | **POST**  /v3/dataforseo_labs/google/related_keywords/live  |
[**googleKeywordSuggestionsLive**](DataforseoLabsApi.md#googleKeywordSuggestionsLive) | **POST**  /v3/dataforseo_labs/google/keyword_suggestions/live  |
[**googleKeywordIdeasLive**](DataforseoLabsApi.md#googleKeywordIdeasLive) | **POST**  /v3/dataforseo_labs/google/keyword_ideas/live  |
[**googleBulkKeywordDifficultyLive**](DataforseoLabsApi.md#googleBulkKeywordDifficultyLive) | **POST**  /v3/dataforseo_labs/google/bulk_keyword_difficulty/live  |
[**googleSearchIntentLive**](DataforseoLabsApi.md#googleSearchIntentLive) | **POST**  /v3/dataforseo_labs/google/search_intent/live  |
[**dataforseoLabsGoogleCategoriesForKeywordsLanguages**](DataforseoLabsApi.md#dataforseoLabsGoogleCategoriesForKeywordsLanguages) | **GET**  /v3/dataforseo_labs/google/categories_for_keywords/languages  |
[**googleCategoriesForDomainLive**](DataforseoLabsApi.md#googleCategoriesForDomainLive) | **POST**  /v3/dataforseo_labs/google/categories_for_domain/live  |
[**googleCategoriesForKeywordsLive**](DataforseoLabsApi.md#googleCategoriesForKeywordsLive) | **POST**  /v3/dataforseo_labs/google/categories_for_keywords/live  |
[**googleKeywordsForCategoriesLive**](DataforseoLabsApi.md#googleKeywordsForCategoriesLive) | **POST**  /v3/dataforseo_labs/google/keywords_for_categories/live  |
[**googleDomainMetricsByCategoriesLive**](DataforseoLabsApi.md#googleDomainMetricsByCategoriesLive) | **POST**  /v3/dataforseo_labs/google/domain_metrics_by_categories/live  |
[**googleTopSearchesLive**](DataforseoLabsApi.md#googleTopSearchesLive) | **POST**  /v3/dataforseo_labs/google/top_searches/live  |
[**googleDomainWhoisOverviewLive**](DataforseoLabsApi.md#googleDomainWhoisOverviewLive) | **POST**  /v3/dataforseo_labs/google/domain_whois_overview/live  |
[**googleRankedKeywordsLive**](DataforseoLabsApi.md#googleRankedKeywordsLive) | **POST**  /v3/dataforseo_labs/google/ranked_keywords/live  |
[**googleSerpCompetitorsLive**](DataforseoLabsApi.md#googleSerpCompetitorsLive) | **POST**  /v3/dataforseo_labs/google/serp_competitors/live  |
[**googleCompetitorsDomainLive**](DataforseoLabsApi.md#googleCompetitorsDomainLive) | **POST**  /v3/dataforseo_labs/google/competitors_domain/live  |
[**googleDomainIntersectionLive**](DataforseoLabsApi.md#googleDomainIntersectionLive) | **POST**  /v3/dataforseo_labs/google/domain_intersection/live  |
[**googleSubdomainsLive**](DataforseoLabsApi.md#googleSubdomainsLive) | **POST**  /v3/dataforseo_labs/google/subdomains/live  |
[**googleRelevantPagesLive**](DataforseoLabsApi.md#googleRelevantPagesLive) | **POST**  /v3/dataforseo_labs/google/relevant_pages/live  |
[**googleDomainRankOverviewLive**](DataforseoLabsApi.md#googleDomainRankOverviewLive) | **POST**  /v3/dataforseo_labs/google/domain_rank_overview/live  |
[**googleHistoricalSerpsLive**](DataforseoLabsApi.md#googleHistoricalSerpsLive) | **POST**  /v3/dataforseo_labs/google/historical_serps/live  |
[**googleHistoricalRankOverviewLive**](DataforseoLabsApi.md#googleHistoricalRankOverviewLive) | **POST**  /v3/dataforseo_labs/google/historical_rank_overview/live  |
[**googlePageIntersectionLive**](DataforseoLabsApi.md#googlePageIntersectionLive) | **POST**  /v3/dataforseo_labs/google/page_intersection/live  |
[**googleBulkTrafficEstimationLive**](DataforseoLabsApi.md#googleBulkTrafficEstimationLive) | **POST**  /v3/dataforseo_labs/google/bulk_traffic_estimation/live  |
[**googleHistoricalBulkTrafficEstimationLive**](DataforseoLabsApi.md#googleHistoricalBulkTrafficEstimationLive) | **POST**  /v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live  |
[**googleHistoricalKeywordDataLive**](DataforseoLabsApi.md#googleHistoricalKeywordDataLive) | **POST**  /v3/dataforseo_labs/google/historical_keyword_data/live  |
[**googleKeywordOverviewLive**](DataforseoLabsApi.md#googleKeywordOverviewLive) | **POST**  /v3/dataforseo_labs/google/keyword_overview/live  |
[**amazonBulkSearchVolumeLive**](DataforseoLabsApi.md#amazonBulkSearchVolumeLive) | **POST**  /v3/dataforseo_labs/amazon/bulk_search_volume/live  |
[**amazonRelatedKeywordsLive**](DataforseoLabsApi.md#amazonRelatedKeywordsLive) | **POST**  /v3/dataforseo_labs/amazon/related_keywords/live  |
[**amazonRankedKeywordsLive**](DataforseoLabsApi.md#amazonRankedKeywordsLive) | **POST**  /v3/dataforseo_labs/amazon/ranked_keywords/live  |
[**amazonProductRankOverviewLive**](DataforseoLabsApi.md#amazonProductRankOverviewLive) | **POST**  /v3/dataforseo_labs/amazon/product_rank_overview/live  |
[**amazonProductCompetitorsLive**](DataforseoLabsApi.md#amazonProductCompetitorsLive) | **POST**  /v3/dataforseo_labs/amazon/product_competitors/live  |
[**amazonProductKeywordIntersectionsLive**](DataforseoLabsApi.md#amazonProductKeywordIntersectionsLive) | **POST**  /v3/dataforseo_labs/amazon/product_keyword_intersections/live  |
[**bingBulkKeywordDifficultyLive**](DataforseoLabsApi.md#bingBulkKeywordDifficultyLive) | **POST**  /v3/dataforseo_labs/bing/bulk_keyword_difficulty/live  |
[**bingBulkTrafficEstimationLive**](DataforseoLabsApi.md#bingBulkTrafficEstimationLive) | **POST**  /v3/dataforseo_labs/bing/bulk_traffic_estimation/live  |
[**bingCompetitorsDomainLive**](DataforseoLabsApi.md#bingCompetitorsDomainLive) | **POST**  /v3/dataforseo_labs/bing/competitors_domain/live  |
[**bingDomainIntersectionLive**](DataforseoLabsApi.md#bingDomainIntersectionLive) | **POST**  /v3/dataforseo_labs/bing/domain_intersection/live  |
[**bingDomainRankOverviewLive**](DataforseoLabsApi.md#bingDomainRankOverviewLive) | **POST**  /v3/dataforseo_labs/bing/domain_rank_overview/live  |
[**bingPageIntersectionLive**](DataforseoLabsApi.md#bingPageIntersectionLive) | **POST**  /v3/dataforseo_labs/bing/page_intersection/live  |
[**bingRankedKeywordsLive**](DataforseoLabsApi.md#bingRankedKeywordsLive) | **POST**  /v3/dataforseo_labs/bing/ranked_keywords/live  |
[**bingRelatedKeywordsLive**](DataforseoLabsApi.md#bingRelatedKeywordsLive) | **POST**  /v3/dataforseo_labs/bing/related_keywords/live  |
[**bingRelevantPagesLive**](DataforseoLabsApi.md#bingRelevantPagesLive) | **POST**  /v3/dataforseo_labs/bing/relevant_pages/live  |
[**bingSerpCompetitorsLive**](DataforseoLabsApi.md#bingSerpCompetitorsLive) | **POST**  /v3/dataforseo_labs/bing/serp_competitors/live  |
[**bingSubdomainsLive**](DataforseoLabsApi.md#bingSubdomainsLive) | **POST**  /v3/dataforseo_labs/bing/subdomains/live  |
[**googleBulkAppMetricsLive**](DataforseoLabsApi.md#googleBulkAppMetricsLive) | **POST**  /v3/dataforseo_labs/google/bulk_app_metrics/live  |
[**googleKeywordsForAppLive**](DataforseoLabsApi.md#googleKeywordsForAppLive) | **POST**  /v3/dataforseo_labs/google/keywords_for_app/live  |
[**googleAppCompetitorsLive**](DataforseoLabsApi.md#googleAppCompetitorsLive) | **POST**  /v3/dataforseo_labs/google/app_competitors/live  |
[**googleAppIntersectionLive**](DataforseoLabsApi.md#googleAppIntersectionLive) | **POST**  /v3/dataforseo_labs/google/app_intersection/live  |
[**appleBulkAppMetricsLive**](DataforseoLabsApi.md#appleBulkAppMetricsLive) | **POST**  /v3/dataforseo_labs/apple/bulk_app_metrics/live  |
[**appleKeywordsForAppLive**](DataforseoLabsApi.md#appleKeywordsForAppLive) | **POST**  /v3/dataforseo_labs/apple/keywords_for_app/live  |
[**appleAppCompetitorsLive**](DataforseoLabsApi.md#appleAppCompetitorsLive) | **POST**  /v3/dataforseo_labs/apple/app_competitors/live  |
[**appleAppIntersectionLive**](DataforseoLabsApi.md#appleAppIntersectionLive) | **POST**  /v3/dataforseo_labs/apple/app_intersection/live  |

<a id="dataforseoLabsIdList"></a>
# **dataforseoLabsIdList**
> DataforseoLabsIdListResponseInfo dataforseoLabsIdList()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_id_list_request_info import List[Optional[DataforseoLabsIdListRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.dataforseo_labs_id_list([DataforseoLabsIdListRequestInfo(
                datetime_from="2025-05-06 08:28:57 +00:00",
                datetime_to="2025-07-06 08:28:57 +00:00",
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
    | **** | [**List&lt;List[Optional[DataforseoLabsIdListRequestInfo]]&gt;**](List[Optional[DataforseoLabsIdListRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsIdListResponseInfo**](DataforseoLabsIdListResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="dataforseoLabsStatus"></a>
# **dataforseoLabsStatus**
> DataforseoLabsStatusResponseInfo dataforseoLabsStatus()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.dataforseo_labs_status()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**DataforseoLabsStatusResponseInfo**](DataforseoLabsStatusResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="dataforseoLabsErrors"></a>
# **dataforseoLabsErrors**
> DataforseoLabsErrorsResponseInfo dataforseoLabsErrors()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_errors_request_info import List[Optional[DataforseoLabsErrorsRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.dataforseo_labs_errors([DataforseoLabsErrorsRequestInfo(
                limit=10,
                offset=0,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsErrorsRequestInfo]]&gt;**](List[Optional[DataforseoLabsErrorsRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsErrorsResponseInfo**](DataforseoLabsErrorsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="availableFilters"></a>
# **availableFilters**
> DataforseoLabsAvailableFiltersResponseInfo availableFilters()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.available_filters()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**DataforseoLabsAvailableFiltersResponseInfo**](DataforseoLabsAvailableFiltersResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="dataforseoLabsLocationsAndLanguages"></a>
# **dataforseoLabsLocationsAndLanguages**
> DataforseoLabsLocationsAndLanguagesResponseInfo dataforseoLabsLocationsAndLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.dataforseo_labs_locations_and_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**DataforseoLabsLocationsAndLanguagesResponseInfo**](DataforseoLabsLocationsAndLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="categories"></a>
# **categories**
> DataforseoLabsCategoriesResponseInfo categories()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.categories()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**DataforseoLabsCategoriesResponseInfo**](DataforseoLabsCategoriesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAvailableHistory"></a>
# **googleAvailableHistory**
> DataforseoLabsGoogleAvailableHistoryResponseInfo googleAvailableHistory()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_available_history()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**DataforseoLabsGoogleAvailableHistoryResponseInfo**](DataforseoLabsGoogleAvailableHistoryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleKeywordsForSiteLive"></a>
# **googleKeywordsForSiteLive**
> DataforseoLabsGoogleKeywordsForSiteLiveResponseInfo googleKeywordsForSiteLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_keywords_for_site_live_request_info import List[Optional[DataforseoLabsGoogleKeywordsForSiteLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_keywords_for_site_live([DataforseoLabsGoogleKeywordsForSiteLiveRequestInfo(
                target="apple.com",
                location_code=2840,
                language_code="en",
                include_serp_info=True,
                include_subdomains=True,
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleKeywordsForSiteLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleKeywordsForSiteLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleKeywordsForSiteLiveResponseInfo**](DataforseoLabsGoogleKeywordsForSiteLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleRelatedKeywordsLive"></a>
# **googleRelatedKeywordsLive**
> DataforseoLabsGoogleRelatedKeywordsLiveResponseInfo googleRelatedKeywordsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_related_keywords_live_request_info import List[Optional[DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_related_keywords_live([DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo(
                keyword="phone",
                location_code=2840,
                language_name="English",
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleRelatedKeywordsLiveResponseInfo**](DataforseoLabsGoogleRelatedKeywordsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleKeywordSuggestionsLive"></a>
# **googleKeywordSuggestionsLive**
> DataforseoLabsGoogleKeywordSuggestionsLiveResponseInfo googleKeywordSuggestionsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_keyword_suggestions_live_request_info import List[Optional[DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_keyword_suggestions_live([DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo(
                keyword="phone",
                location_code=2840,
                language_code="en",
                include_seed_keyword=True,
                include_serp_info=True,
                limit=1,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleKeywordSuggestionsLiveResponseInfo**](DataforseoLabsGoogleKeywordSuggestionsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleKeywordIdeasLive"></a>
# **googleKeywordIdeasLive**
> DataforseoLabsGoogleKeywordIdeasLiveResponseInfo googleKeywordIdeasLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_keyword_ideas_live_request_info import List[Optional[DataforseoLabsGoogleKeywordIdeasLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_keyword_ideas_live([DataforseoLabsGoogleKeywordIdeasLiveRequestInfo(
                keywords=[
                    "phone",
                    "watch",
                    ],
                location_code=2840,
                language_code="en",
                include_serp_info=True,
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleKeywordIdeasLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleKeywordIdeasLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleKeywordIdeasLiveResponseInfo**](DataforseoLabsGoogleKeywordIdeasLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleBulkKeywordDifficultyLive"></a>
# **googleBulkKeywordDifficultyLive**
> DataforseoLabsGoogleBulkKeywordDifficultyLiveResponseInfo googleBulkKeywordDifficultyLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_bulk_keyword_difficulty_live_request_info import List[Optional[DataforseoLabsGoogleBulkKeywordDifficultyLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_bulk_keyword_difficulty_live([DataforseoLabsGoogleBulkKeywordDifficultyLiveRequestInfo(
                keywords=[
                    "dentist new york",
                    "pizza brooklyn",
                    "car dealer los angeles",
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
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleBulkKeywordDifficultyLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleBulkKeywordDifficultyLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleBulkKeywordDifficultyLiveResponseInfo**](DataforseoLabsGoogleBulkKeywordDifficultyLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleSearchIntentLive"></a>
# **googleSearchIntentLive**
> DataforseoLabsGoogleSearchIntentLiveResponseInfo googleSearchIntentLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_search_intent_live_request_info import List[Optional[DataforseoLabsGoogleSearchIntentLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_search_intent_live([DataforseoLabsGoogleSearchIntentLiveRequestInfo(
                keywords=[
                    "login page",
                    "audi a7",
                    "elon musk",
                    "milk store new york",
                    ],
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleSearchIntentLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleSearchIntentLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleSearchIntentLiveResponseInfo**](DataforseoLabsGoogleSearchIntentLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="dataforseoLabsGoogleCategoriesForKeywordsLanguages"></a>
# **dataforseoLabsGoogleCategoriesForKeywordsLanguages**
> DataforseoLabsGoogleCategoriesForKeywordsLanguagesResponseInfo dataforseoLabsGoogleCategoriesForKeywordsLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.dataforseo_labs_google_categories_for_keywords_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**DataforseoLabsGoogleCategoriesForKeywordsLanguagesResponseInfo**](DataforseoLabsGoogleCategoriesForKeywordsLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleCategoriesForDomainLive"></a>
# **googleCategoriesForDomainLive**
> DataforseoLabsGoogleCategoriesForDomainLiveResponseInfo googleCategoriesForDomainLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_categories_for_domain_live_request_info import List[Optional[DataforseoLabsGoogleCategoriesForDomainLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_categories_for_domain_live([DataforseoLabsGoogleCategoriesForDomainLiveRequestInfo(
                target="dataforseo.com",
                location_name="United States",
                language_code="en",
                item_types=[
                    "paid",
                    "organic",
                    "featured_snippet",
                    "local_pack",
                    ],
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleCategoriesForDomainLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleCategoriesForDomainLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleCategoriesForDomainLiveResponseInfo**](DataforseoLabsGoogleCategoriesForDomainLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleCategoriesForKeywordsLive"></a>
# **googleCategoriesForKeywordsLive**
> DataforseoLabsGoogleCategoriesForKeywordsLiveResponseInfo googleCategoriesForKeywordsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_categories_for_keywords_live_request_info import List[Optional[DataforseoLabsGoogleCategoriesForKeywordsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_categories_for_keywords_live([DataforseoLabsGoogleCategoriesForKeywordsLiveRequestInfo(
                keywords=[
                    "dentist new york",
                    "pizza brooklyn",
                    "car dealer los angeles",
                    ],
                language_code="en",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleCategoriesForKeywordsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleCategoriesForKeywordsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleCategoriesForKeywordsLiveResponseInfo**](DataforseoLabsGoogleCategoriesForKeywordsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleKeywordsForCategoriesLive"></a>
# **googleKeywordsForCategoriesLive**
> DataforseoLabsGoogleKeywordsForCategoriesLiveResponseInfo googleKeywordsForCategoriesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_keywords_for_categories_live_request_info import List[Optional[DataforseoLabsGoogleKeywordsForCategoriesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_keywords_for_categories_live([DataforseoLabsGoogleKeywordsForCategoriesLiveRequestInfo(
                category_codes=[
                    "12191",
                    "12193",
                    ],
                location_code=2840,
                language_name="English",
                include_serp_info=True,
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleKeywordsForCategoriesLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleKeywordsForCategoriesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleKeywordsForCategoriesLiveResponseInfo**](DataforseoLabsGoogleKeywordsForCategoriesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDomainMetricsByCategoriesLive"></a>
# **googleDomainMetricsByCategoriesLive**
> DataforseoLabsGoogleDomainMetricsByCategoriesLiveResponseInfo googleDomainMetricsByCategoriesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_domain_metrics_by_categories_live_request_info import List[Optional[DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_domain_metrics_by_categories_live([DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo(
                category_codes=[
                    "13418",
                    "11494",
                    ],
                first_date="2025-05-06",
                second_date="2025-07-06",
                location_code=2840,
                language_code="en",
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleDomainMetricsByCategoriesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleDomainMetricsByCategoriesLiveResponseInfo**](DataforseoLabsGoogleDomainMetricsByCategoriesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleTopSearchesLive"></a>
# **googleTopSearchesLive**
> DataforseoLabsGoogleTopSearchesLiveResponseInfo googleTopSearchesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_top_searches_live_request_info import List[Optional[DataforseoLabsGoogleTopSearchesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_top_searches_live([DataforseoLabsGoogleTopSearchesLiveRequestInfo(
                location_code=2840,
                language_name="English",
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleTopSearchesLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleTopSearchesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleTopSearchesLiveResponseInfo**](DataforseoLabsGoogleTopSearchesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDomainWhoisOverviewLive"></a>
# **googleDomainWhoisOverviewLive**
> DataforseoLabsGoogleDomainWhoisOverviewLiveResponseInfo googleDomainWhoisOverviewLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_domain_whois_overview_live_request_info import List[Optional[DataforseoLabsGoogleDomainWhoisOverviewLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_domain_whois_overview_live([DataforseoLabsGoogleDomainWhoisOverviewLiveRequestInfo(
                limit=2,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleDomainWhoisOverviewLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleDomainWhoisOverviewLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleDomainWhoisOverviewLiveResponseInfo**](DataforseoLabsGoogleDomainWhoisOverviewLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleRankedKeywordsLive"></a>
# **googleRankedKeywordsLive**
> DataforseoLabsGoogleRankedKeywordsLiveResponseInfo googleRankedKeywordsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_ranked_keywords_live_request_info import List[Optional[DataforseoLabsGoogleRankedKeywordsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_ranked_keywords_live([DataforseoLabsGoogleRankedKeywordsLiveRequestInfo(
                target="dataforseo.com",
                location_name="United States",
                language_name="English",
                limit=3,
                load_rank_absolute=True,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleRankedKeywordsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleRankedKeywordsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleRankedKeywordsLiveResponseInfo**](DataforseoLabsGoogleRankedKeywordsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleSerpCompetitorsLive"></a>
# **googleSerpCompetitorsLive**
> DataforseoLabsGoogleSerpCompetitorsLiveResponseInfo googleSerpCompetitorsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_serp_competitors_live_request_info import List[Optional[DataforseoLabsGoogleSerpCompetitorsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_serp_competitors_live([DataforseoLabsGoogleSerpCompetitorsLiveRequestInfo(
                keywords=[
                    "phone",
                    ],
                location_code=2840,
                language_name="English",
                item_types=[
                    "organic",
                    ],
                limit=5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleSerpCompetitorsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleSerpCompetitorsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleSerpCompetitorsLiveResponseInfo**](DataforseoLabsGoogleSerpCompetitorsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleCompetitorsDomainLive"></a>
# **googleCompetitorsDomainLive**
> DataforseoLabsGoogleCompetitorsDomainLiveResponseInfo googleCompetitorsDomainLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_competitors_domain_live_request_info import List[Optional[DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_competitors_domain_live([DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo(
                target="newmouth.com",
                location_code=2840,
                language_name="English",
                limit=3,
                intersecting_domains=[
                    "dentaly.org",
                    "health.com",
                    "trysnow.com",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleCompetitorsDomainLiveResponseInfo**](DataforseoLabsGoogleCompetitorsDomainLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDomainIntersectionLive"></a>
# **googleDomainIntersectionLive**
> DataforseoLabsGoogleDomainIntersectionLiveResponseInfo googleDomainIntersectionLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_domain_intersection_live_request_info import List[Optional[DataforseoLabsGoogleDomainIntersectionLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_domain_intersection_live([DataforseoLabsGoogleDomainIntersectionLiveRequestInfo(
                target_1="mom.com",
                target_2="quora.com",
                location_code=2840,
                language_code="en",
                include_serp_info=True,
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleDomainIntersectionLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleDomainIntersectionLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleDomainIntersectionLiveResponseInfo**](DataforseoLabsGoogleDomainIntersectionLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleSubdomainsLive"></a>
# **googleSubdomainsLive**
> DataforseoLabsGoogleSubdomainsLiveResponseInfo googleSubdomainsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_subdomains_live_request_info import List[Optional[DataforseoLabsGoogleSubdomainsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_subdomains_live([DataforseoLabsGoogleSubdomainsLiveRequestInfo(
                target="dataforseo.com",
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleSubdomainsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleSubdomainsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleSubdomainsLiveResponseInfo**](DataforseoLabsGoogleSubdomainsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleRelevantPagesLive"></a>
# **googleRelevantPagesLive**
> DataforseoLabsGoogleRelevantPagesLiveResponseInfo googleRelevantPagesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_relevant_pages_live_request_info import List[Optional[DataforseoLabsGoogleRelevantPagesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_relevant_pages_live([DataforseoLabsGoogleRelevantPagesLiveRequestInfo(
                target="amazon.com",
                location_code=2840,
                language_name="English",
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleRelevantPagesLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleRelevantPagesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleRelevantPagesLiveResponseInfo**](DataforseoLabsGoogleRelevantPagesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleDomainRankOverviewLive"></a>
# **googleDomainRankOverviewLive**
> DataforseoLabsGoogleDomainRankOverviewLiveResponseInfo googleDomainRankOverviewLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_domain_rank_overview_live_request_info import List[Optional[DataforseoLabsGoogleDomainRankOverviewLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_domain_rank_overview_live([DataforseoLabsGoogleDomainRankOverviewLiveRequestInfo(
                target="dataforseo.com",
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleDomainRankOverviewLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleDomainRankOverviewLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleDomainRankOverviewLiveResponseInfo**](DataforseoLabsGoogleDomainRankOverviewLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHistoricalSerpsLive"></a>
# **googleHistoricalSerpsLive**
> DataforseoLabsGoogleHistoricalSerpsLiveResponseInfo googleHistoricalSerpsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_historical_serps_live_request_info import List[Optional[DataforseoLabsGoogleHistoricalSerpsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_historical_serps_live([DataforseoLabsGoogleHistoricalSerpsLiveRequestInfo(
                keyword="albert einstein",
                date_from="2025-05-06",
                date_to="2025-07-06",
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
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleHistoricalSerpsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleHistoricalSerpsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleHistoricalSerpsLiveResponseInfo**](DataforseoLabsGoogleHistoricalSerpsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHistoricalRankOverviewLive"></a>
# **googleHistoricalRankOverviewLive**
> DataforseoLabsGoogleHistoricalRankOverviewLiveResponseInfo googleHistoricalRankOverviewLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_historical_rank_overview_live_request_info import List[Optional[DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_historical_rank_overview_live([DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo(
                target="dataforseo.com",
                location_code=2840,
                language_code="en",
                date_from="2025-05-06",
                date_to="2025-07-06",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleHistoricalRankOverviewLiveResponseInfo**](DataforseoLabsGoogleHistoricalRankOverviewLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googlePageIntersectionLive"></a>
# **googlePageIntersectionLive**
> DataforseoLabsGooglePageIntersectionLiveResponseInfo googlePageIntersectionLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_page_intersection_live_request_info import List[Optional[DataforseoLabsGooglePageIntersectionLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_page_intersection_live([DataforseoLabsGooglePageIntersectionLiveRequestInfo(
                pages={
                    },
                location_code=2840,
                language_name="English",
                limit=3,
                include_serp_info=True,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGooglePageIntersectionLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGooglePageIntersectionLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGooglePageIntersectionLiveResponseInfo**](DataforseoLabsGooglePageIntersectionLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleBulkTrafficEstimationLive"></a>
# **googleBulkTrafficEstimationLive**
> DataforseoLabsGoogleBulkTrafficEstimationLiveResponseInfo googleBulkTrafficEstimationLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_bulk_traffic_estimation_live_request_info import List[Optional[DataforseoLabsGoogleBulkTrafficEstimationLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_bulk_traffic_estimation_live([DataforseoLabsGoogleBulkTrafficEstimationLiveRequestInfo(
                targets=[
                    "dataforseo.com",
                    "cnn.com",
                    "forbes.com",
                    ],
                location_code=2840,
                language_code="en",
                item_types=[
                    "organic",
                    "paid",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleBulkTrafficEstimationLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleBulkTrafficEstimationLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleBulkTrafficEstimationLiveResponseInfo**](DataforseoLabsGoogleBulkTrafficEstimationLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHistoricalBulkTrafficEstimationLive"></a>
# **googleHistoricalBulkTrafficEstimationLive**
> DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveResponseInfo googleHistoricalBulkTrafficEstimationLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_historical_bulk_traffic_estimation_live_request_info import List[Optional[DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_historical_bulk_traffic_estimation_live([DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo(
                targets=[
                    "dataforseo.com",
                    "cnn.com",
                    "forbes.com",
                    ],
                location_code=2840,
                language_code="en",
                date_from="2025-05-06",
                date_to="2025-07-06",
                item_types=[
                    "organic",
                    "paid",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveResponseInfo**](DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleHistoricalKeywordDataLive"></a>
# **googleHistoricalKeywordDataLive**
> DataforseoLabsGoogleHistoricalKeywordDataLiveResponseInfo googleHistoricalKeywordDataLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_historical_keyword_data_live_request_info import List[Optional[DataforseoLabsGoogleHistoricalKeywordDataLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_historical_keyword_data_live([DataforseoLabsGoogleHistoricalKeywordDataLiveRequestInfo(
                keywords=[
                    "iphone",
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
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleHistoricalKeywordDataLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleHistoricalKeywordDataLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleHistoricalKeywordDataLiveResponseInfo**](DataforseoLabsGoogleHistoricalKeywordDataLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleKeywordOverviewLive"></a>
# **googleKeywordOverviewLive**
> DataforseoLabsGoogleKeywordOverviewLiveResponseInfo googleKeywordOverviewLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_keyword_overview_live_request_info import List[Optional[DataforseoLabsGoogleKeywordOverviewLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_keyword_overview_live([DataforseoLabsGoogleKeywordOverviewLiveRequestInfo(
                keywords=[
                    "iphone",
                    ],
                location_code=2840,
                language_code="en",
                include_serp_info=True,
                include_clickstream_data=True,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleKeywordOverviewLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleKeywordOverviewLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleKeywordOverviewLiveResponseInfo**](DataforseoLabsGoogleKeywordOverviewLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonBulkSearchVolumeLive"></a>
# **amazonBulkSearchVolumeLive**
> DataforseoLabsAmazonBulkSearchVolumeLiveResponseInfo amazonBulkSearchVolumeLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_amazon_bulk_search_volume_live_request_info import List[Optional[DataforseoLabsAmazonBulkSearchVolumeLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.amazon_bulk_search_volume_live([DataforseoLabsAmazonBulkSearchVolumeLiveRequestInfo(
                keywords=[
                    "buy laptop",
                    "cheap laptops for sale",
                    "purchase laptop",
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
    | **** | [**List&lt;List[Optional[DataforseoLabsAmazonBulkSearchVolumeLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsAmazonBulkSearchVolumeLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsAmazonBulkSearchVolumeLiveResponseInfo**](DataforseoLabsAmazonBulkSearchVolumeLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonRelatedKeywordsLive"></a>
# **amazonRelatedKeywordsLive**
> DataforseoLabsAmazonRelatedKeywordsLiveResponseInfo amazonRelatedKeywordsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_amazon_related_keywords_live_request_info import List[Optional[DataforseoLabsAmazonRelatedKeywordsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.amazon_related_keywords_live([DataforseoLabsAmazonRelatedKeywordsLiveRequestInfo(
                keyword="computer mouse",
                location_code=2840,
                language_name="English",
                include_seed_keyword=True,
                limit=5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsAmazonRelatedKeywordsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsAmazonRelatedKeywordsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsAmazonRelatedKeywordsLiveResponseInfo**](DataforseoLabsAmazonRelatedKeywordsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonRankedKeywordsLive"></a>
# **amazonRankedKeywordsLive**
> DataforseoLabsAmazonRankedKeywordsLiveResponseInfo amazonRankedKeywordsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_amazon_ranked_keywords_live_request_info import List[Optional[DataforseoLabsAmazonRankedKeywordsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.amazon_ranked_keywords_live([DataforseoLabsAmazonRankedKeywordsLiveRequestInfo(
                asin="B00R92CL5E",
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
    | **** | [**List&lt;List[Optional[DataforseoLabsAmazonRankedKeywordsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsAmazonRankedKeywordsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsAmazonRankedKeywordsLiveResponseInfo**](DataforseoLabsAmazonRankedKeywordsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonProductRankOverviewLive"></a>
# **amazonProductRankOverviewLive**
> DataforseoLabsAmazonProductRankOverviewLiveResponseInfo amazonProductRankOverviewLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_amazon_product_rank_overview_live_request_info import List[Optional[DataforseoLabsAmazonProductRankOverviewLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.amazon_product_rank_overview_live([DataforseoLabsAmazonProductRankOverviewLiveRequestInfo(
                asins=[
                    "B001TJ3HUG",
                    "B01LW2SL7R",
                    ],
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsAmazonProductRankOverviewLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsAmazonProductRankOverviewLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsAmazonProductRankOverviewLiveResponseInfo**](DataforseoLabsAmazonProductRankOverviewLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonProductCompetitorsLive"></a>
# **amazonProductCompetitorsLive**
> DataforseoLabsAmazonProductCompetitorsLiveResponseInfo amazonProductCompetitorsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_amazon_product_competitors_live_request_info import List[Optional[DataforseoLabsAmazonProductCompetitorsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.amazon_product_competitors_live([DataforseoLabsAmazonProductCompetitorsLiveRequestInfo(
                asin="019005476X",
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
    | **** | [**List&lt;List[Optional[DataforseoLabsAmazonProductCompetitorsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsAmazonProductCompetitorsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsAmazonProductCompetitorsLiveResponseInfo**](DataforseoLabsAmazonProductCompetitorsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="amazonProductKeywordIntersectionsLive"></a>
# **amazonProductKeywordIntersectionsLive**
> DataforseoLabsAmazonProductKeywordIntersectionsLiveResponseInfo amazonProductKeywordIntersectionsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_amazon_product_keyword_intersections_live_request_info import List[Optional[DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.amazon_product_keyword_intersections_live([DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo(
                asins={
                    },
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsAmazonProductKeywordIntersectionsLiveResponseInfo**](DataforseoLabsAmazonProductKeywordIntersectionsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingBulkKeywordDifficultyLive"></a>
# **bingBulkKeywordDifficultyLive**
> DataforseoLabsBingBulkKeywordDifficultyLiveResponseInfo bingBulkKeywordDifficultyLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_bing_bulk_keyword_difficulty_live_request_info import List[Optional[DataforseoLabsBingBulkKeywordDifficultyLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.bing_bulk_keyword_difficulty_live([DataforseoLabsBingBulkKeywordDifficultyLiveRequestInfo(
                keywords=[
                    "dentist new york",
                    "pizza brooklyn",
                    "car dealer los angeles",
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
    | **** | [**List&lt;List[Optional[DataforseoLabsBingBulkKeywordDifficultyLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsBingBulkKeywordDifficultyLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsBingBulkKeywordDifficultyLiveResponseInfo**](DataforseoLabsBingBulkKeywordDifficultyLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingBulkTrafficEstimationLive"></a>
# **bingBulkTrafficEstimationLive**
> DataforseoLabsBingBulkTrafficEstimationLiveResponseInfo bingBulkTrafficEstimationLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_bing_bulk_traffic_estimation_live_request_info import List[Optional[DataforseoLabsBingBulkTrafficEstimationLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.bing_bulk_traffic_estimation_live([DataforseoLabsBingBulkTrafficEstimationLiveRequestInfo(
                targets=[
                    "dataforseo.com",
                    "cnn.com",
                    "forbes.com",
                    ],
                location_code=2840,
                language_code="en",
                item_types=[
                    "organic",
                    "paid",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsBingBulkTrafficEstimationLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsBingBulkTrafficEstimationLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsBingBulkTrafficEstimationLiveResponseInfo**](DataforseoLabsBingBulkTrafficEstimationLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingCompetitorsDomainLive"></a>
# **bingCompetitorsDomainLive**
> DataforseoLabsBingCompetitorsDomainLiveResponseInfo bingCompetitorsDomainLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_bing_competitors_domain_live_request_info import List[Optional[DataforseoLabsBingCompetitorsDomainLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.bing_competitors_domain_live([DataforseoLabsBingCompetitorsDomainLiveRequestInfo(
                target="newmouth.com",
                location_code=2840,
                language_name="English",
                limit=3,
                intersecting_domains=[
                    "dentaly.org",
                    "health.com",
                    "trysnow.com",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsBingCompetitorsDomainLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsBingCompetitorsDomainLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsBingCompetitorsDomainLiveResponseInfo**](DataforseoLabsBingCompetitorsDomainLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingDomainIntersectionLive"></a>
# **bingDomainIntersectionLive**
> DataforseoLabsBingDomainIntersectionLiveResponseInfo bingDomainIntersectionLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_bing_domain_intersection_live_request_info import List[Optional[DataforseoLabsBingDomainIntersectionLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.bing_domain_intersection_live([DataforseoLabsBingDomainIntersectionLiveRequestInfo(
                target_1="mom.me",
                target_2="quora.com",
                location_code=2840,
                language_code="en",
                limit=5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsBingDomainIntersectionLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsBingDomainIntersectionLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsBingDomainIntersectionLiveResponseInfo**](DataforseoLabsBingDomainIntersectionLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingDomainRankOverviewLive"></a>
# **bingDomainRankOverviewLive**
> DataforseoLabsBingDomainRankOverviewLiveResponseInfo bingDomainRankOverviewLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_bing_domain_rank_overview_live_request_info import List[Optional[DataforseoLabsBingDomainRankOverviewLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.bing_domain_rank_overview_live([DataforseoLabsBingDomainRankOverviewLiveRequestInfo(
                target="dataforseo.com",
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsBingDomainRankOverviewLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsBingDomainRankOverviewLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsBingDomainRankOverviewLiveResponseInfo**](DataforseoLabsBingDomainRankOverviewLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingPageIntersectionLive"></a>
# **bingPageIntersectionLive**
> DataforseoLabsBingPageIntersectionLiveResponseInfo bingPageIntersectionLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_bing_page_intersection_live_request_info import List[Optional[DataforseoLabsBingPageIntersectionLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.bing_page_intersection_live([DataforseoLabsBingPageIntersectionLiveRequestInfo(
                pages={
                    },
                location_code=2840,
                language_name="English",
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsBingPageIntersectionLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsBingPageIntersectionLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsBingPageIntersectionLiveResponseInfo**](DataforseoLabsBingPageIntersectionLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingRankedKeywordsLive"></a>
# **bingRankedKeywordsLive**
> DataforseoLabsBingRankedKeywordsLiveResponseInfo bingRankedKeywordsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_bing_ranked_keywords_live_request_info import List[Optional[DataforseoLabsBingRankedKeywordsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.bing_ranked_keywords_live([DataforseoLabsBingRankedKeywordsLiveRequestInfo(
                target="dataforseo.com",
                location_name="United States",
                language_name="English",
                limit=3,
                load_rank_absolute=True,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsBingRankedKeywordsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsBingRankedKeywordsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsBingRankedKeywordsLiveResponseInfo**](DataforseoLabsBingRankedKeywordsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingRelatedKeywordsLive"></a>
# **bingRelatedKeywordsLive**
> DataforseoLabsBingRelatedKeywordsLiveResponseInfo bingRelatedKeywordsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_bing_related_keywords_live_request_info import List[Optional[DataforseoLabsBingRelatedKeywordsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.bing_related_keywords_live([DataforseoLabsBingRelatedKeywordsLiveRequestInfo(
                keyword="phone",
                location_code=2840,
                language_name="English",
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsBingRelatedKeywordsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsBingRelatedKeywordsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsBingRelatedKeywordsLiveResponseInfo**](DataforseoLabsBingRelatedKeywordsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingRelevantPagesLive"></a>
# **bingRelevantPagesLive**
> DataforseoLabsBingRelevantPagesLiveResponseInfo bingRelevantPagesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_bing_relevant_pages_live_request_info import List[Optional[DataforseoLabsBingRelevantPagesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.bing_relevant_pages_live([DataforseoLabsBingRelevantPagesLiveRequestInfo(
                target="dataforseo.com",
                location_code=2840,
                language_name="English",
                limit=5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsBingRelevantPagesLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsBingRelevantPagesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsBingRelevantPagesLiveResponseInfo**](DataforseoLabsBingRelevantPagesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingSerpCompetitorsLive"></a>
# **bingSerpCompetitorsLive**
> DataforseoLabsBingSerpCompetitorsLiveResponseInfo bingSerpCompetitorsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_bing_serp_competitors_live_request_info import List[Optional[DataforseoLabsBingSerpCompetitorsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.bing_serp_competitors_live([DataforseoLabsBingSerpCompetitorsLiveRequestInfo(
                keywords=[
                    "phone",
                    ],
                location_code=2840,
                language_name="English",
                item_types=[
                    "organic",
                    ],
                limit=5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsBingSerpCompetitorsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsBingSerpCompetitorsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsBingSerpCompetitorsLiveResponseInfo**](DataforseoLabsBingSerpCompetitorsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="bingSubdomainsLive"></a>
# **bingSubdomainsLive**
> DataforseoLabsBingSubdomainsLiveResponseInfo bingSubdomainsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_bing_subdomains_live_request_info import List[Optional[DataforseoLabsBingSubdomainsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.bing_subdomains_live([DataforseoLabsBingSubdomainsLiveRequestInfo(
                target="dataforseo.com",
                location_code=2840,
                language_name="English",
                limit=5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsBingSubdomainsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsBingSubdomainsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsBingSubdomainsLiveResponseInfo**](DataforseoLabsBingSubdomainsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleBulkAppMetricsLive"></a>
# **googleBulkAppMetricsLive**
> DataforseoLabsGoogleBulkAppMetricsLiveResponseInfo googleBulkAppMetricsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_bulk_app_metrics_live_request_info import List[Optional[DataforseoLabsGoogleBulkAppMetricsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_bulk_app_metrics_live([DataforseoLabsGoogleBulkAppMetricsLiveRequestInfo(
                app_ids=[
                    "org.telegram.messenger",
                    "com.zhiliaoapp.musically",
                    ],
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleBulkAppMetricsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleBulkAppMetricsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleBulkAppMetricsLiveResponseInfo**](DataforseoLabsGoogleBulkAppMetricsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleKeywordsForAppLive"></a>
# **googleKeywordsForAppLive**
> DataforseoLabsGoogleKeywordsForAppLiveResponseInfo googleKeywordsForAppLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_keywords_for_app_live_request_info import List[Optional[DataforseoLabsGoogleKeywordsForAppLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_keywords_for_app_live([DataforseoLabsGoogleKeywordsForAppLiveRequestInfo(
                app_id="org.telegram.messenger",
                location_code=2840,
                language_name="English",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleKeywordsForAppLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleKeywordsForAppLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleKeywordsForAppLiveResponseInfo**](DataforseoLabsGoogleKeywordsForAppLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppCompetitorsLive"></a>
# **googleAppCompetitorsLive**
> DataforseoLabsGoogleAppCompetitorsLiveResponseInfo googleAppCompetitorsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_app_competitors_live_request_info import List[Optional[DataforseoLabsGoogleAppCompetitorsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_app_competitors_live([DataforseoLabsGoogleAppCompetitorsLiveRequestInfo(
                app_id="org.telegram.messenger",
                location_code=2840,
                language_name="English",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleAppCompetitorsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleAppCompetitorsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleAppCompetitorsLiveResponseInfo**](DataforseoLabsGoogleAppCompetitorsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="googleAppIntersectionLive"></a>
# **googleAppIntersectionLive**
> DataforseoLabsGoogleAppIntersectionLiveResponseInfo googleAppIntersectionLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_google_app_intersection_live_request_info import List[Optional[DataforseoLabsGoogleAppIntersectionLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.google_app_intersection_live([DataforseoLabsGoogleAppIntersectionLiveRequestInfo(
                app_ids={
                    },
                location_code=2840,
                language_name="English",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsGoogleAppIntersectionLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsGoogleAppIntersectionLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsGoogleAppIntersectionLiveResponseInfo**](DataforseoLabsGoogleAppIntersectionLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleBulkAppMetricsLive"></a>
# **appleBulkAppMetricsLive**
> DataforseoLabsAppleBulkAppMetricsLiveResponseInfo appleBulkAppMetricsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_apple_bulk_app_metrics_live_request_info import List[Optional[DataforseoLabsAppleBulkAppMetricsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.apple_bulk_app_metrics_live([DataforseoLabsAppleBulkAppMetricsLiveRequestInfo(
                app_ids=[
                    "686449807",
                    "382617920",
                    ],
                location_code=2840,
                language_name="English",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsAppleBulkAppMetricsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsAppleBulkAppMetricsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsAppleBulkAppMetricsLiveResponseInfo**](DataforseoLabsAppleBulkAppMetricsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleKeywordsForAppLive"></a>
# **appleKeywordsForAppLive**
> DataforseoLabsAppleKeywordsForAppLiveResponseInfo appleKeywordsForAppLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_apple_keywords_for_app_live_request_info import List[Optional[DataforseoLabsAppleKeywordsForAppLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.apple_keywords_for_app_live([DataforseoLabsAppleKeywordsForAppLiveRequestInfo(
                app_id="686449807",
                location_code=2840,
                language_name="English",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsAppleKeywordsForAppLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsAppleKeywordsForAppLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsAppleKeywordsForAppLiveResponseInfo**](DataforseoLabsAppleKeywordsForAppLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppCompetitorsLive"></a>
# **appleAppCompetitorsLive**
> DataforseoLabsAppleAppCompetitorsLiveResponseInfo appleAppCompetitorsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_apple_app_competitors_live_request_info import List[Optional[DataforseoLabsAppleAppCompetitorsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.apple_app_competitors_live([DataforseoLabsAppleAppCompetitorsLiveRequestInfo(
                app_id="686449807",
                location_code=2840,
                language_name="English",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsAppleAppCompetitorsLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsAppleAppCompetitorsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsAppleAppCompetitorsLiveResponseInfo**](DataforseoLabsAppleAppCompetitorsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="appleAppIntersectionLive"></a>
# **appleAppIntersectionLive**
> DataforseoLabsAppleAppIntersectionLiveResponseInfo appleAppIntersectionLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_dataforseo_labs_apple_app_intersection_live_request_info import List[Optional[DataforseoLabsAppleAppIntersectionLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        dataforseo_labs_api = DataforseoLabsApi(api_client)

        response = dataforseo_labs_api.apple_app_intersection_live([DataforseoLabsAppleAppIntersectionLiveRequestInfo(
                app_ids={
                    },
                location_code=2840,
                language_name="English",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[DataforseoLabsAppleAppIntersectionLiveRequestInfo]]&gt;**](List[Optional[DataforseoLabsAppleAppIntersectionLiveRequestInfo]].md)|  | [optional] |



### Return type

[**DataforseoLabsAppleAppIntersectionLiveResponseInfo**](DataforseoLabsAppleAppIntersectionLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |