[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# dataforseo_client.ContentAnalysisApi

All URIs are relative to *https://api.dataforseo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**category_trends_live**](ContentAnalysisApi.md#category_trends_live) | **POST** /v3/content_analysis/category_trends/live |
[**content_analysis_available_filters**](ContentAnalysisApi.md#content_analysis_available_filters) | **GET** /v3/content_analysis/available_filters |
[**content_analysis_categories**](ContentAnalysisApi.md#content_analysis_categories) | **GET** /v3/content_analysis/categories |
[**content_analysis_id_list**](ContentAnalysisApi.md#content_analysis_id_list) | **POST** /v3/content_analysis/id_list |
[**content_analysis_languages**](ContentAnalysisApi.md#content_analysis_languages) | **GET** /v3/content_analysis/languages |
[**content_analysis_locations**](ContentAnalysisApi.md#content_analysis_locations) | **GET** /v3/content_analysis/locations |
[**content_analysis_summary_live**](ContentAnalysisApi.md#content_analysis_summary_live) | **POST** /v3/content_analysis/summary/live |
[**phrase_trends_live**](ContentAnalysisApi.md#phrase_trends_live) | **POST** /v3/content_analysis/phrase_trends/live |
[**rating_distribution_live**](ContentAnalysisApi.md#rating_distribution_live) | **POST** /v3/content_analysis/rating_distribution/live |
[**search_live**](ContentAnalysisApi.md#search_live) | **POST** /v3/content_analysis/search/live |
[**sentiment_analysis_live**](ContentAnalysisApi.md#sentiment_analysis_live) | **POST** /v3/content_analysis/sentiment_analysis/live |

# **category_trends_live**

> ContentAnalysisCategoryTrendsLiveResponseInfo category_trends_live(content_analysis_category_trends_live_request_info=content_analysis_category_trends_live_request_info)

‌ This endpoint will provide you with data on all citations in the target category for the indicated date range. for more info please visit 'https://docs.dataforseo.com/v3/content_analysis/category_trends/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_analysis_category_trends_live_request_info import ContentAnalysisCategoryTrendsLiveRequestInfo
from dataforseo_client.models.content_analysis_category_trends_live_response_info import ContentAnalysisCategoryTrendsLiveResponseInfo
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
    api_instance = dataforseo_client.ContentAnalysisApi(api_client)
    content_analysis_category_trends_live_request_info = [dataforseo_client.ContentAnalysisCategoryTrendsLiveRequestInfo()] # List[ContentAnalysisCategoryTrendsLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.category_trends_live(content_analysis_category_trends_live_request_info=content_analysis_category_trends_live_request_info)
        print("The response of ContentAnalysisApi->category_trends_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentAnalysisApi->category_trends_live: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**content_analysis_category_trends_live_request_info** | [**List[ContentAnalysisCategoryTrendsLiveRequestInfo]**](ContentAnalysisCategoryTrendsLiveRequestInfo.md)|  | [optional]

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
**200** | Successful operation |  -  |

   

# **content_analysis_available_filters**

> ContentAnalysisAvailableFiltersResponseInfo content_analysis_available_filters()

‌‌ Here you will find all the necessary information about filters that can be used with Content Analysis API endpoints. for more info please visit 'https://docs.dataforseo.com/v3/content_analysis/filters/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_analysis_available_filters_response_info import ContentAnalysisAvailableFiltersResponseInfo
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
    api_instance = dataforseo_client.ContentAnalysisApi(api_client)

    try:
        api_response = api_instance.content_analysis_available_filters()
        print("The response of ContentAnalysisApi->content_analysis_available_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentAnalysisApi->content_analysis_available_filters: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ContentAnalysisAvailableFiltersResponseInfo**](ContentAnalysisAvailableFiltersResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

   

# **content_analysis_categories**

> ContentAnalysisCategoriesResponseInfo content_analysis_categories()

We use Google product and service categories. This endpoint will provide you with the full list of available categories. You can also download the CSV file by this link. for more info please visit 'https://docs.dataforseo.com/v3/content_analysis/categories/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_analysis_categories_response_info import ContentAnalysisCategoriesResponseInfo
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
    api_instance = dataforseo_client.ContentAnalysisApi(api_client)

    try:
        api_response = api_instance.content_analysis_categories()
        print("The response of ContentAnalysisApi->content_analysis_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentAnalysisApi->content_analysis_categories: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ContentAnalysisCategoriesResponseInfo**](ContentAnalysisCategoriesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

   

# **content_analysis_id_list**

> ContentAnalysisIdListResponseInfo content_analysis_id_list(content_analysis_id_list_request_info=content_analysis_id_list_request_info)

This endpoint is designed to provide you with the list of IDs and metadata of the completed Content Analysis tasks during the specified period. You will get all task IDs that were made including successful, uncompleted, and tasks that responded as errors. for more info please visit 'https://docs.dataforseo.com/v3/content_analysis/id_list/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_analysis_id_list_request_info import ContentAnalysisIdListRequestInfo
from dataforseo_client.models.content_analysis_id_list_response_info import ContentAnalysisIdListResponseInfo
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
    api_instance = dataforseo_client.ContentAnalysisApi(api_client)
    content_analysis_id_list_request_info = [dataforseo_client.ContentAnalysisIdListRequestInfo()] # List[ContentAnalysisIdListRequestInfo] |  (optional)

    try:
        api_response = api_instance.content_analysis_id_list(content_analysis_id_list_request_info=content_analysis_id_list_request_info)
        print("The response of ContentAnalysisApi->content_analysis_id_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentAnalysisApi->content_analysis_id_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**content_analysis_id_list_request_info** | [**List[ContentAnalysisIdListRequestInfo]**](ContentAnalysisIdListRequestInfo.md)|  | [optional]

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
**200** | Successful operation |  -  |

   

# **content_analysis_languages**

> ContentAnalysisLanguagesResponseInfo content_analysis_languages()

You will receive the list of languages by calling this API.   As a response of the API server, you will receive JSON-encoded data containing a tasks array with the information specific to the set tasks. for more info please visit 'https://docs.dataforseo.com/v3/content_analysis/languages/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_analysis_languages_response_info import ContentAnalysisLanguagesResponseInfo
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
    api_instance = dataforseo_client.ContentAnalysisApi(api_client)

    try:
        api_response = api_instance.content_analysis_languages()
        print("The response of ContentAnalysisApi->content_analysis_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentAnalysisApi->content_analysis_languages: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ContentAnalysisLanguagesResponseInfo**](ContentAnalysisLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

   

# **content_analysis_locations**

> ContentAnalysisLocationsResponseInfo content_analysis_locations()

You will receive the list of locations by this API call. for more info please visit 'https://docs.dataforseo.com/v3/content_analysis/locations/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_analysis_locations_response_info import ContentAnalysisLocationsResponseInfo
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
    api_instance = dataforseo_client.ContentAnalysisApi(api_client)

    try:
        api_response = api_instance.content_analysis_locations()
        print("The response of ContentAnalysisApi->content_analysis_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentAnalysisApi->content_analysis_locations: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ContentAnalysisLocationsResponseInfo**](ContentAnalysisLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |

   

# **content_analysis_summary_live**

> ContentAnalysisSummaryLiveResponseInfo content_analysis_summary_live(content_analysis_summary_live_request_info=content_analysis_summary_live_request_info)

‌ This endpoint will provide you with an overview of citation data available for the target keyword. for more info please visit 'https://docs.dataforseo.com/v3/content_analysis/summary/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_analysis_summary_live_request_info import ContentAnalysisSummaryLiveRequestInfo
from dataforseo_client.models.content_analysis_summary_live_response_info import ContentAnalysisSummaryLiveResponseInfo
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
    api_instance = dataforseo_client.ContentAnalysisApi(api_client)
    content_analysis_summary_live_request_info = [dataforseo_client.ContentAnalysisSummaryLiveRequestInfo()] # List[ContentAnalysisSummaryLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.content_analysis_summary_live(content_analysis_summary_live_request_info=content_analysis_summary_live_request_info)
        print("The response of ContentAnalysisApi->content_analysis_summary_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentAnalysisApi->content_analysis_summary_live: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**content_analysis_summary_live_request_info** | [**List[ContentAnalysisSummaryLiveRequestInfo]**](ContentAnalysisSummaryLiveRequestInfo.md)|  | [optional]

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
**200** | Successful operation |  -  |

   

# **phrase_trends_live**

> ContentAnalysisPhraseTrendsLiveResponseInfo phrase_trends_live(content_analysis_phrase_trends_live_request_info=content_analysis_phrase_trends_live_request_info)

‌ This endpoint will provide you with data on all citations of the target keyword for the indicated date range. for more info please visit 'https://docs.dataforseo.com/v3/content_analysis/phrase_trends/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_analysis_phrase_trends_live_request_info import ContentAnalysisPhraseTrendsLiveRequestInfo
from dataforseo_client.models.content_analysis_phrase_trends_live_response_info import ContentAnalysisPhraseTrendsLiveResponseInfo
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
    api_instance = dataforseo_client.ContentAnalysisApi(api_client)
    content_analysis_phrase_trends_live_request_info = [dataforseo_client.ContentAnalysisPhraseTrendsLiveRequestInfo()] # List[ContentAnalysisPhraseTrendsLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.phrase_trends_live(content_analysis_phrase_trends_live_request_info=content_analysis_phrase_trends_live_request_info)
        print("The response of ContentAnalysisApi->phrase_trends_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentAnalysisApi->phrase_trends_live: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**content_analysis_phrase_trends_live_request_info** | [**List[ContentAnalysisPhraseTrendsLiveRequestInfo]**](ContentAnalysisPhraseTrendsLiveRequestInfo.md)|  | [optional]

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
**200** | Successful operation |  -  |

   

# **rating_distribution_live**

> ContentAnalysisRatingDistributionLiveResponseInfo rating_distribution_live(content_analysis_rating_distribution_live_request_info=content_analysis_rating_distribution_live_request_info)

‌ This endpoint will provide you with rating distribution data for the keyword and other parameters specified in the request. for more info please visit 'https://docs.dataforseo.com/v3/content_analysis/rating_distribution/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_analysis_rating_distribution_live_request_info import ContentAnalysisRatingDistributionLiveRequestInfo
from dataforseo_client.models.content_analysis_rating_distribution_live_response_info import ContentAnalysisRatingDistributionLiveResponseInfo
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
    api_instance = dataforseo_client.ContentAnalysisApi(api_client)
    content_analysis_rating_distribution_live_request_info = [dataforseo_client.ContentAnalysisRatingDistributionLiveRequestInfo()] # List[ContentAnalysisRatingDistributionLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.rating_distribution_live(content_analysis_rating_distribution_live_request_info=content_analysis_rating_distribution_live_request_info)
        print("The response of ContentAnalysisApi->rating_distribution_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentAnalysisApi->rating_distribution_live: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**content_analysis_rating_distribution_live_request_info** | [**List[ContentAnalysisRatingDistributionLiveRequestInfo]**](ContentAnalysisRatingDistributionLiveRequestInfo.md)|  | [optional]

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
**200** | Successful operation |  -  |

   

# **search_live**

> ContentAnalysisSearchLiveResponseInfo search_live(content_analysis_search_live_request_info=content_analysis_search_live_request_info)

‌ This endpoint will provide you with detailed citation data available for the target keyword. for more info please visit 'https://docs.dataforseo.com/v3/content_analysis/search/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_analysis_search_live_request_info import ContentAnalysisSearchLiveRequestInfo
from dataforseo_client.models.content_analysis_search_live_response_info import ContentAnalysisSearchLiveResponseInfo
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
    api_instance = dataforseo_client.ContentAnalysisApi(api_client)
    content_analysis_search_live_request_info = [dataforseo_client.ContentAnalysisSearchLiveRequestInfo()] # List[ContentAnalysisSearchLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.search_live(content_analysis_search_live_request_info=content_analysis_search_live_request_info)
        print("The response of ContentAnalysisApi->search_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentAnalysisApi->search_live: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**content_analysis_search_live_request_info** | [**List[ContentAnalysisSearchLiveRequestInfo]**](ContentAnalysisSearchLiveRequestInfo.md)|  | [optional]

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
**200** | Successful operation |  -  |

   

# **sentiment_analysis_live**

> ContentAnalysisSentimentAnalysisLiveResponseInfo sentiment_analysis_live(content_analysis_sentiment_analysis_live_request_info=content_analysis_sentiment_analysis_live_request_info)

‌ This endpoint will provide you with sentiment analysis data for the citations available for the target keyword. for more info please visit 'https://docs.dataforseo.com/v3/content_analysis/sentiment_analysis/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.content_analysis_sentiment_analysis_live_request_info import ContentAnalysisSentimentAnalysisLiveRequestInfo
from dataforseo_client.models.content_analysis_sentiment_analysis_live_response_info import ContentAnalysisSentimentAnalysisLiveResponseInfo
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
    api_instance = dataforseo_client.ContentAnalysisApi(api_client)
    content_analysis_sentiment_analysis_live_request_info = [dataforseo_client.ContentAnalysisSentimentAnalysisLiveRequestInfo()] # List[ContentAnalysisSentimentAnalysisLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.sentiment_analysis_live(content_analysis_sentiment_analysis_live_request_info=content_analysis_sentiment_analysis_live_request_info)
        print("The response of ContentAnalysisApi->sentiment_analysis_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContentAnalysisApi->sentiment_analysis_live: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**content_analysis_sentiment_analysis_live_request_info** | [**List[ContentAnalysisSentimentAnalysisLiveRequestInfo]**](ContentAnalysisSentimentAnalysisLiveRequestInfo.md)|  | [optional]

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
**200** | Successful operation |  -  |

   

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")