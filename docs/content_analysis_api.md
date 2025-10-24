# ContentAnalysisApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**contentAnalysisIdList**](ContentAnalysisApi.md#contentAnalysisIdList) | **POST**  /v3/content_analysis/id_list  |
[**contentAnalysisAvailableFilters**](ContentAnalysisApi.md#contentAnalysisAvailableFilters) | **GET**  /v3/content_analysis/available_filters  |
[**contentAnalysisLocations**](ContentAnalysisApi.md#contentAnalysisLocations) | **GET**  /v3/content_analysis/locations  |
[**contentAnalysisLanguages**](ContentAnalysisApi.md#contentAnalysisLanguages) | **GET**  /v3/content_analysis/languages  |
[**contentAnalysisCategories**](ContentAnalysisApi.md#contentAnalysisCategories) | **GET**  /v3/content_analysis/categories  |
[**searchLive**](ContentAnalysisApi.md#searchLive) | **POST**  /v3/content_analysis/search/live  |
[**contentAnalysisSummaryLive**](ContentAnalysisApi.md#contentAnalysisSummaryLive) | **POST**  /v3/content_analysis/summary/live  |
[**sentimentAnalysisLive**](ContentAnalysisApi.md#sentimentAnalysisLive) | **POST**  /v3/content_analysis/sentiment_analysis/live  |
[**ratingDistributionLive**](ContentAnalysisApi.md#ratingDistributionLive) | **POST**  /v3/content_analysis/rating_distribution/live  |
[**phraseTrendsLive**](ContentAnalysisApi.md#phraseTrendsLive) | **POST**  /v3/content_analysis/phrase_trends/live  |
[**categoryTrendsLive**](ContentAnalysisApi.md#categoryTrendsLive) | **POST**  /v3/content_analysis/category_trends/live  |

<a id="contentAnalysisIdList"></a>
# **contentAnalysisIdList**
> ContentAnalysisIdListResponseInfo contentAnalysisIdList()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_analysis_id_list_request_info import List[Optional[ContentAnalysisIdListRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_analysis_api = ContentAnalysisApi(api_client)

        response = content_analysis_api.content_analysis_id_list([ContentAnalysisIdListRequestInfo(
                datetime_from="2025-07-24 12:05:26 +00:00",
                datetime_to="2025-09-24 12:05:26 +00:00",
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
    | **** | [**List&lt;List[Optional[ContentAnalysisIdListRequestInfo]]&gt;**](List[Optional[ContentAnalysisIdListRequestInfo]].md)|  | [optional] |



### Return type

[**ContentAnalysisIdListResponseInfo**](ContentAnalysisIdListResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="contentAnalysisAvailableFilters"></a>
# **contentAnalysisAvailableFilters**
> ContentAnalysisAvailableFiltersResponseInfo contentAnalysisAvailableFilters()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_analysis_api = ContentAnalysisApi(api_client)

        response = content_analysis_api.content_analysis_available_filters()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**ContentAnalysisAvailableFiltersResponseInfo**](ContentAnalysisAvailableFiltersResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="contentAnalysisLocations"></a>
# **contentAnalysisLocations**
> ContentAnalysisLocationsResponseInfo contentAnalysisLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_analysis_api = ContentAnalysisApi(api_client)

        response = content_analysis_api.content_analysis_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**ContentAnalysisLocationsResponseInfo**](ContentAnalysisLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="contentAnalysisLanguages"></a>
# **contentAnalysisLanguages**
> ContentAnalysisLanguagesResponseInfo contentAnalysisLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_analysis_api = ContentAnalysisApi(api_client)

        response = content_analysis_api.content_analysis_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**ContentAnalysisLanguagesResponseInfo**](ContentAnalysisLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="contentAnalysisCategories"></a>
# **contentAnalysisCategories**
> ContentAnalysisCategoriesResponseInfo contentAnalysisCategories()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_analysis_api = ContentAnalysisApi(api_client)

        response = content_analysis_api.content_analysis_categories()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**ContentAnalysisCategoriesResponseInfo**](ContentAnalysisCategoriesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="searchLive"></a>
# **searchLive**
> ContentAnalysisSearchLiveResponseInfo searchLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_analysis_search_live_request_info import List[Optional[ContentAnalysisSearchLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_analysis_api = ContentAnalysisApi(api_client)

        response = content_analysis_api.search_live([ContentAnalysisSearchLiveRequestInfo(
                keyword="logitech",
                keyword_fields={
                    },
                page_type=[
                    "ecommerce",
                    "news",
                    "blogs",
                    "message-boards",
                    "organization",
                    ],
                search_mode="as_is",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentAnalysisSearchLiveRequestInfo]]&gt;**](List[Optional[ContentAnalysisSearchLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentAnalysisSearchLiveResponseInfo**](ContentAnalysisSearchLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="contentAnalysisSummaryLive"></a>
# **contentAnalysisSummaryLive**
> ContentAnalysisSummaryLiveResponseInfo contentAnalysisSummaryLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_analysis_summary_live_request_info import List[Optional[ContentAnalysisSummaryLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_analysis_api = ContentAnalysisApi(api_client)

        response = content_analysis_api.content_analysis_summary_live([ContentAnalysisSummaryLiveRequestInfo(
                keyword="logitech",
                page_type=[
                    "ecommerce",
                    "news",
                    "blogs",
                    "message-boards",
                    "organization",
                    ],
                internal_list_limit=8,
                positive_connotation_threshold=0.5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentAnalysisSummaryLiveRequestInfo]]&gt;**](List[Optional[ContentAnalysisSummaryLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentAnalysisSummaryLiveResponseInfo**](ContentAnalysisSummaryLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="sentimentAnalysisLive"></a>
# **sentimentAnalysisLive**
> ContentAnalysisSentimentAnalysisLiveResponseInfo sentimentAnalysisLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_analysis_sentiment_analysis_live_request_info import List[Optional[ContentAnalysisSentimentAnalysisLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_analysis_api = ContentAnalysisApi(api_client)

        response = content_analysis_api.sentiment_analysis_live([ContentAnalysisSentimentAnalysisLiveRequestInfo(
                keyword="logitech",
                internal_list_limit=1,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentAnalysisSentimentAnalysisLiveRequestInfo]]&gt;**](List[Optional[ContentAnalysisSentimentAnalysisLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentAnalysisSentimentAnalysisLiveResponseInfo**](ContentAnalysisSentimentAnalysisLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="ratingDistributionLive"></a>
# **ratingDistributionLive**
> ContentAnalysisRatingDistributionLiveResponseInfo ratingDistributionLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_analysis_rating_distribution_live_request_info import List[Optional[ContentAnalysisRatingDistributionLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_analysis_api = ContentAnalysisApi(api_client)

        response = content_analysis_api.rating_distribution_live([ContentAnalysisRatingDistributionLiveRequestInfo(
                keyword="logitech",
                internal_list_limit=10,
                search_mode="as_is",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentAnalysisRatingDistributionLiveRequestInfo]]&gt;**](List[Optional[ContentAnalysisRatingDistributionLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentAnalysisRatingDistributionLiveResponseInfo**](ContentAnalysisRatingDistributionLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="phraseTrendsLive"></a>
# **phraseTrendsLive**
> ContentAnalysisPhraseTrendsLiveResponseInfo phraseTrendsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_analysis_phrase_trends_live_request_info import List[Optional[ContentAnalysisPhraseTrendsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_analysis_api = ContentAnalysisApi(api_client)

        response = content_analysis_api.phrase_trends_live([ContentAnalysisPhraseTrendsLiveRequestInfo(
                keyword="logitech",
                search_mode="as_is",
                date_from="2025-07-24",
                date_group="month",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentAnalysisPhraseTrendsLiveRequestInfo]]&gt;**](List[Optional[ContentAnalysisPhraseTrendsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentAnalysisPhraseTrendsLiveResponseInfo**](ContentAnalysisPhraseTrendsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="categoryTrendsLive"></a>
# **categoryTrendsLive**
> ContentAnalysisCategoryTrendsLiveResponseInfo categoryTrendsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_content_analysis_category_trends_live_request_info import List[Optional[ContentAnalysisCategoryTrendsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        content_analysis_api = ContentAnalysisApi(api_client)

        response = content_analysis_api.category_trends_live([ContentAnalysisCategoryTrendsLiveRequestInfo(
                category_code="10994",
                search_mode="as_is",
                date_from="2025-07-24",
                date_group="month",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[ContentAnalysisCategoryTrendsLiveRequestInfo]]&gt;**](List[Optional[ContentAnalysisCategoryTrendsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**ContentAnalysisCategoryTrendsLiveResponseInfo**](ContentAnalysisCategoryTrendsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |