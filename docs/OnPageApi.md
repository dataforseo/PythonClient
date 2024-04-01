# dataforseo_client.OnPageApi

All URIs are relative to *https://api.dataforseo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_parsing**](OnPageApi.md#content_parsing) | **POST** /v3/on_page/content_parsing | 
[**content_parsing_live**](OnPageApi.md#content_parsing_live) | **POST** /v3/on_page/content_parsing/live | 
[**duplicate_content**](OnPageApi.md#duplicate_content) | **POST** /v3/on_page/duplicate_content | 
[**duplicate_tags**](OnPageApi.md#duplicate_tags) | **POST** /v3/on_page/duplicate_tags | 
[**force_stop**](OnPageApi.md#force_stop) | **POST** /v3/on_page/force_stop | 
[**instant_pages**](OnPageApi.md#instant_pages) | **POST** /v3/on_page/instant_pages | 
[**keyword_density**](OnPageApi.md#keyword_density) | **POST** /v3/on_page/keyword_density | 
[**lighthouse_audits**](OnPageApi.md#lighthouse_audits) | **GET** /v3/on_page/lighthouse/audits | 
[**lighthouse_live_json**](OnPageApi.md#lighthouse_live_json) | **POST** /v3/on_page/lighthouse/live/json | 
[**lighthouse_task_get_json**](OnPageApi.md#lighthouse_task_get_json) | **GET** /v3/on_page/lighthouse/task_get/json/{id} | 
[**lighthouse_task_post**](OnPageApi.md#lighthouse_task_post) | **POST** /v3/on_page/lighthouse/task_post | 
[**lighthouse_tasks_ready**](OnPageApi.md#lighthouse_tasks_ready) | **GET** /v3/on_page/lighthouse/tasks_ready | 
[**lighthouse_versions**](OnPageApi.md#lighthouse_versions) | **GET** /v3/on_page/lighthouse/versions | 
[**links**](OnPageApi.md#links) | **POST** /v3/on_page/links | 
[**microdata**](OnPageApi.md#microdata) | **POST** /v3/on_page/microdata | 
[**non_indexable**](OnPageApi.md#non_indexable) | **POST** /v3/on_page/non_indexable | 
[**on_page_available_filters**](OnPageApi.md#on_page_available_filters) | **GET** /v3/on_page/available_filters | 
[**on_page_errors**](OnPageApi.md#on_page_errors) | **POST** /v3/on_page/errors | 
[**on_page_id_list**](OnPageApi.md#on_page_id_list) | **POST** /v3/on_page/id_list | 
[**on_page_lighthouse_languages**](OnPageApi.md#on_page_lighthouse_languages) | **GET** /v3/on_page/lighthouse/languages | 
[**page_screenshot**](OnPageApi.md#page_screenshot) | **POST** /v3/on_page/page_screenshot | 
[**pages**](OnPageApi.md#pages) | **POST** /v3/on_page/pages | 
[**pages_by_resource**](OnPageApi.md#pages_by_resource) | **POST** /v3/on_page/pages_by_resource | 
[**raw_html**](OnPageApi.md#raw_html) | **POST** /v3/on_page/raw_html | 
[**redirect_chains**](OnPageApi.md#redirect_chains) | **POST** /v3/on_page/redirect_chains | 
[**resources**](OnPageApi.md#resources) | **POST** /v3/on_page/resources | 
[**summary**](OnPageApi.md#summary) | **GET** /v3/on_page/summary/{id} | 
[**task_post**](OnPageApi.md#task_post) | **POST** /v3/on_page/task_post | 
[**tasks_ready**](OnPageApi.md#tasks_ready) | **GET** /v3/on_page/tasks_ready | 
[**waterfall**](OnPageApi.md#waterfall) | **POST** /v3/on_page/waterfall | 


# **content_parsing**
> OnPageContentParsingResponseInfo content_parsing(on_page_content_parsing_request_info=on_page_content_parsing_request_info)



‌‌ This endpoint allows parsing the content on any page you specify and will return the structured content of the target page, including link URLs, anchors, headings, and textual content. for more info please visit 'https://docs.dataforseo.com/v3/on_page/content_parsing/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_content_parsing_request_info import OnPageContentParsingRequestInfo
from dataforseo_client.models.on_page_content_parsing_response_info import OnPageContentParsingResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_content_parsing_request_info = [dataforseo_client.OnPageContentParsingRequestInfo()] # List[OnPageContentParsingRequestInfo] |  (optional)

    try:
        api_response = api_instance.content_parsing(on_page_content_parsing_request_info=on_page_content_parsing_request_info)
        print("The response of OnPageApi->content_parsing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->content_parsing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_content_parsing_request_info** | [**List[OnPageContentParsingRequestInfo]**](OnPageContentParsingRequestInfo.md)|  | [optional] 

### Return type

[**OnPageContentParsingResponseInfo**](OnPageContentParsingResponseInfo.md)

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

# **content_parsing_live**
> OnPageContentParsingLiveResponseInfo content_parsing_live(on_page_content_parsing_live_request_info=on_page_content_parsing_live_request_info)



‌‌ This endpoint allows parsing the content on any page you specify and will return the structured content of the target page, including link URLs, anchors, headings, and textual content. for more info please visit 'https://docs.dataforseo.com/v3/on_page/content_parsing/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_content_parsing_live_request_info import OnPageContentParsingLiveRequestInfo
from dataforseo_client.models.on_page_content_parsing_live_response_info import OnPageContentParsingLiveResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_content_parsing_live_request_info = [dataforseo_client.OnPageContentParsingLiveRequestInfo()] # List[OnPageContentParsingLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.content_parsing_live(on_page_content_parsing_live_request_info=on_page_content_parsing_live_request_info)
        print("The response of OnPageApi->content_parsing_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->content_parsing_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_content_parsing_live_request_info** | [**List[OnPageContentParsingLiveRequestInfo]**](OnPageContentParsingLiveRequestInfo.md)|  | [optional] 

### Return type

[**OnPageContentParsingLiveResponseInfo**](OnPageContentParsingLiveResponseInfo.md)

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

# **duplicate_content**
> OnPageDuplicateContentResponseInfo duplicate_content(on_page_duplicate_content_request_info=on_page_duplicate_content_request_info)



‌‌ This endpoint returns a list of pages that have content similar to the page specified in the request. The response also contains data related to page performance and the similarity index that indicates how similar the compared pages are. for more info please visit 'https://docs.dataforseo.com/v3/on_page/duplicate_content/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_duplicate_content_request_info import OnPageDuplicateContentRequestInfo
from dataforseo_client.models.on_page_duplicate_content_response_info import OnPageDuplicateContentResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_duplicate_content_request_info = [dataforseo_client.OnPageDuplicateContentRequestInfo()] # List[OnPageDuplicateContentRequestInfo] |  (optional)

    try:
        api_response = api_instance.duplicate_content(on_page_duplicate_content_request_info=on_page_duplicate_content_request_info)
        print("The response of OnPageApi->duplicate_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->duplicate_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_duplicate_content_request_info** | [**List[OnPageDuplicateContentRequestInfo]**](OnPageDuplicateContentRequestInfo.md)|  | [optional] 

### Return type

[**OnPageDuplicateContentResponseInfo**](OnPageDuplicateContentResponseInfo.md)

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

# **duplicate_tags**
> OnPageDuplicateTagsResponseInfo duplicate_tags(on_page_duplicate_tags_request_info=on_page_duplicate_tags_request_info)



‌‌ This endpoint returns a list of pages that contain duplicate title or description tags. The response also contains data related to page performance. for more info please visit 'https://docs.dataforseo.com/v3/on_page/duplicate_tags/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_duplicate_tags_request_info import OnPageDuplicateTagsRequestInfo
from dataforseo_client.models.on_page_duplicate_tags_response_info import OnPageDuplicateTagsResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_duplicate_tags_request_info = [dataforseo_client.OnPageDuplicateTagsRequestInfo()] # List[OnPageDuplicateTagsRequestInfo] |  (optional)

    try:
        api_response = api_instance.duplicate_tags(on_page_duplicate_tags_request_info=on_page_duplicate_tags_request_info)
        print("The response of OnPageApi->duplicate_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->duplicate_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_duplicate_tags_request_info** | [**List[OnPageDuplicateTagsRequestInfo]**](OnPageDuplicateTagsRequestInfo.md)|  | [optional] 

### Return type

[**OnPageDuplicateTagsResponseInfo**](OnPageDuplicateTagsResponseInfo.md)

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

# **force_stop**
> OnPageForceStopResponseInfo force_stop(on_page_force_stop_request_info=on_page_force_stop_request_info)



‌‌ This endpoint is designed to force stop the crawl process of websites you specified in a task. The execution of all the tasks associated with the IDs indicated in your request to this endpoint will be stopped. You will still be able to obtain the data on pages that have been scanned until the crawling process was stopped. for more info please visit 'https://docs.dataforseo.com/v3/on_page/force_stop/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_force_stop_request_info import OnPageForceStopRequestInfo
from dataforseo_client.models.on_page_force_stop_response_info import OnPageForceStopResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_force_stop_request_info = [dataforseo_client.OnPageForceStopRequestInfo()] # List[OnPageForceStopRequestInfo] |  (optional)

    try:
        api_response = api_instance.force_stop(on_page_force_stop_request_info=on_page_force_stop_request_info)
        print("The response of OnPageApi->force_stop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->force_stop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_force_stop_request_info** | [**List[OnPageForceStopRequestInfo]**](OnPageForceStopRequestInfo.md)|  | [optional] 

### Return type

[**OnPageForceStopResponseInfo**](OnPageForceStopResponseInfo.md)

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

# **instant_pages**
> OnPageInstantPagesResponseInfo instant_pages(on_page_instant_pages_request_info=on_page_instant_pages_request_info)



‌‌ Using this function you will get page-specific data with detailed information on how well a particular page is optimized for organic search. for more info please visit 'https://docs.dataforseo.com/v3/on_page/instant_pages/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_instant_pages_request_info import OnPageInstantPagesRequestInfo
from dataforseo_client.models.on_page_instant_pages_response_info import OnPageInstantPagesResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_instant_pages_request_info = [dataforseo_client.OnPageInstantPagesRequestInfo()] # List[OnPageInstantPagesRequestInfo] |  (optional)

    try:
        api_response = api_instance.instant_pages(on_page_instant_pages_request_info=on_page_instant_pages_request_info)
        print("The response of OnPageApi->instant_pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->instant_pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_instant_pages_request_info** | [**List[OnPageInstantPagesRequestInfo]**](OnPageInstantPagesRequestInfo.md)|  | [optional] 

### Return type

[**OnPageInstantPagesResponseInfo**](OnPageInstantPagesResponseInfo.md)

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

# **keyword_density**
> OnPageKeywordDensityResponseInfo keyword_density(on_page_keyword_density_request_info=on_page_keyword_density_request_info)



‌‌ This endpoint will provide you with keyword density and keyword frequency data for terms appearing on the specified website or web page. You can filter and sort the data that will be retrieved with this API call. for more info please visit 'https://docs.dataforseo.com/v3/on_page/keyword_density/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_keyword_density_request_info import OnPageKeywordDensityRequestInfo
from dataforseo_client.models.on_page_keyword_density_response_info import OnPageKeywordDensityResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_keyword_density_request_info = [dataforseo_client.OnPageKeywordDensityRequestInfo()] # List[OnPageKeywordDensityRequestInfo] |  (optional)

    try:
        api_response = api_instance.keyword_density(on_page_keyword_density_request_info=on_page_keyword_density_request_info)
        print("The response of OnPageApi->keyword_density:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->keyword_density: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_keyword_density_request_info** | [**List[OnPageKeywordDensityRequestInfo]**](OnPageKeywordDensityRequestInfo.md)|  | [optional] 

### Return type

[**OnPageKeywordDensityResponseInfo**](OnPageKeywordDensityResponseInfo.md)

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

# **lighthouse_audits**
> OnPageLighthouseAuditsResponseInfo lighthouse_audits()



The OnPage Lighthouse API is based on Google’s open-source Lighthouse project and provides data on the quality of web pages. for more info please visit 'https://docs.dataforseo.com/v3/on_page/lighthouse/audits/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_lighthouse_audits_response_info import OnPageLighthouseAuditsResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)

    try:
        api_response = api_instance.lighthouse_audits()
        print("The response of OnPageApi->lighthouse_audits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->lighthouse_audits: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OnPageLighthouseAuditsResponseInfo**](OnPageLighthouseAuditsResponseInfo.md)

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

# **lighthouse_live_json**
> OnPageLighthouseLiveJsonResponseInfo lighthouse_live_json(on_page_lighthouse_live_json_request_info=on_page_lighthouse_live_json_request_info)



‌The OnPage Lighthouse API is based on Google’s open-source Lighthouse project for measuring the quality of web pages and web apps. for more info please visit 'https://docs.dataforseo.com/v3/on_page/lighthouse/live/json/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_lighthouse_live_json_request_info import OnPageLighthouseLiveJsonRequestInfo
from dataforseo_client.models.on_page_lighthouse_live_json_response_info import OnPageLighthouseLiveJsonResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_lighthouse_live_json_request_info = [dataforseo_client.OnPageLighthouseLiveJsonRequestInfo()] # List[OnPageLighthouseLiveJsonRequestInfo] |  (optional)

    try:
        api_response = api_instance.lighthouse_live_json(on_page_lighthouse_live_json_request_info=on_page_lighthouse_live_json_request_info)
        print("The response of OnPageApi->lighthouse_live_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->lighthouse_live_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_lighthouse_live_json_request_info** | [**List[OnPageLighthouseLiveJsonRequestInfo]**](OnPageLighthouseLiveJsonRequestInfo.md)|  | [optional] 

### Return type

[**OnPageLighthouseLiveJsonResponseInfo**](OnPageLighthouseLiveJsonResponseInfo.md)

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

# **lighthouse_task_get_json**
> OnPageLighthouseTaskGetJsonResponseInfo lighthouse_task_get_json(id)



‌ The OnPage Lighthouse API is based on Google’s open-source Lighthouse project for measuring the quality of web pages and web apps. This endpoint will provide you with the results of Lighthouse Audit. Use the id received in the response of your Task POST request to get the results. The response will include data about all categories and audits specified in the Task POST. By default, the response will include all available data about the webpage including its performance, accessibility, progressive web apps, SEO, and compliance with best practices. for more info please visit 'https://docs.dataforseo.com/v3/on_page/lighthouse/task_get/json/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_lighthouse_task_get_json_response_info import OnPageLighthouseTaskGetJsonResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    id = '00000000-0000-0000-0000-000000000000' # str | task identifier required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04”

    try:
        api_response = api_instance.lighthouse_task_get_json(id)
        print("The response of OnPageApi->lighthouse_task_get_json:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->lighthouse_task_get_json: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| task identifier required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04” | 

### Return type

[**OnPageLighthouseTaskGetJsonResponseInfo**](OnPageLighthouseTaskGetJsonResponseInfo.md)

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

# **lighthouse_task_post**
> OnPageLighthouseTaskPostResponseInfo lighthouse_task_post(on_page_lighthouse_task_post_request_info=on_page_lighthouse_task_post_request_info)



‌The OnPage Lighthouse API is based on Google’s open-source Lighthouse project for measuring the quality of web pages and web apps. for more info please visit 'https://docs.dataforseo.com/v3/on_page/lighthouse/task_post/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_lighthouse_task_post_request_info import OnPageLighthouseTaskPostRequestInfo
from dataforseo_client.models.on_page_lighthouse_task_post_response_info import OnPageLighthouseTaskPostResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_lighthouse_task_post_request_info = [dataforseo_client.OnPageLighthouseTaskPostRequestInfo()] # List[OnPageLighthouseTaskPostRequestInfo] |  (optional)

    try:
        api_response = api_instance.lighthouse_task_post(on_page_lighthouse_task_post_request_info=on_page_lighthouse_task_post_request_info)
        print("The response of OnPageApi->lighthouse_task_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->lighthouse_task_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_lighthouse_task_post_request_info** | [**List[OnPageLighthouseTaskPostRequestInfo]**](OnPageLighthouseTaskPostRequestInfo.md)|  | [optional] 

### Return type

[**OnPageLighthouseTaskPostResponseInfo**](OnPageLighthouseTaskPostResponseInfo.md)

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

# **lighthouse_tasks_ready**
> OnPageLighthouseTasksReadyResponseInfo lighthouse_tasks_ready()



‌ The ‘Tasks Ready’ endpoint is designed to provide you with the list of completed tasks, which haven’t been collected yet. If you use the Standard method without specifying the postback_url, you can receive the list of id for all completed tasks using this endpoint. Then, you can collect the results using the ‘Task GET’ endpoint. for more info please visit 'https://docs.dataforseo.com/v3/on_page/lighthouse/tasks_ready/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_lighthouse_tasks_ready_response_info import OnPageLighthouseTasksReadyResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)

    try:
        api_response = api_instance.lighthouse_tasks_ready()
        print("The response of OnPageApi->lighthouse_tasks_ready:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->lighthouse_tasks_ready: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OnPageLighthouseTasksReadyResponseInfo**](OnPageLighthouseTasksReadyResponseInfo.md)

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

# **lighthouse_versions**
> OnPageLighthouseVersionsResponseInfo lighthouse_versions()



OnPage Lighthouse API is based on Google’s open-source Lighthouse project and provides data on the quality of web pages. for more info please visit 'https://docs.dataforseo.com/v3/on_page/lighthouse/versions/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_lighthouse_versions_response_info import OnPageLighthouseVersionsResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)

    try:
        api_response = api_instance.lighthouse_versions()
        print("The response of OnPageApi->lighthouse_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->lighthouse_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OnPageLighthouseVersionsResponseInfo**](OnPageLighthouseVersionsResponseInfo.md)

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

# **links**
> OnPageLinksResponseInfo links(on_page_links_request_info=on_page_links_request_info)



‌‌ This endpoint will provide you with a list of internal and external links detected on a target website. The following link types are supported: anchor, image, link, canonical, meta, alternate, redirect. for more info please visit 'https://docs.dataforseo.com/v3/on_page/links/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_links_request_info import OnPageLinksRequestInfo
from dataforseo_client.models.on_page_links_response_info import OnPageLinksResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_links_request_info = [dataforseo_client.OnPageLinksRequestInfo()] # List[OnPageLinksRequestInfo] |  (optional)

    try:
        api_response = api_instance.links(on_page_links_request_info=on_page_links_request_info)
        print("The response of OnPageApi->links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->links: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_links_request_info** | [**List[OnPageLinksRequestInfo]**](OnPageLinksRequestInfo.md)|  | [optional] 

### Return type

[**OnPageLinksResponseInfo**](OnPageLinksResponseInfo.md)

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

# **microdata**
> OnPageMicrodataResponseInfo microdata(on_page_microdata_request_info=on_page_microdata_request_info)



‌‌ This endpoint is designed to validate structured JSON-LD data and Microdata. Using this function you will obtain microdata available on the specified page of the target website and detailed results of its validation. To use this endpoint, set the validate_micromarkup parameter to true in the POST request to OnPage API. for more info please visit 'https://docs.dataforseo.com/v3/on_page/microdata/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_microdata_request_info import OnPageMicrodataRequestInfo
from dataforseo_client.models.on_page_microdata_response_info import OnPageMicrodataResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_microdata_request_info = [dataforseo_client.OnPageMicrodataRequestInfo()] # List[OnPageMicrodataRequestInfo] |  (optional)

    try:
        api_response = api_instance.microdata(on_page_microdata_request_info=on_page_microdata_request_info)
        print("The response of OnPageApi->microdata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->microdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_microdata_request_info** | [**List[OnPageMicrodataRequestInfo]**](OnPageMicrodataRequestInfo.md)|  | [optional] 

### Return type

[**OnPageMicrodataResponseInfo**](OnPageMicrodataResponseInfo.md)

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

# **non_indexable**
> OnPageNonIndexableResponseInfo non_indexable(on_page_non_indexable_request_info=on_page_non_indexable_request_info)



‌‌ This endpoint returns a list of pages that are blocked from being indexed by Google and other search engines by robots.txt, HTTP headers, or meta tags settings. for more info please visit 'https://docs.dataforseo.com/v3/on_page/non_indexable/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_non_indexable_request_info import OnPageNonIndexableRequestInfo
from dataforseo_client.models.on_page_non_indexable_response_info import OnPageNonIndexableResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_non_indexable_request_info = [dataforseo_client.OnPageNonIndexableRequestInfo()] # List[OnPageNonIndexableRequestInfo] |  (optional)

    try:
        api_response = api_instance.non_indexable(on_page_non_indexable_request_info=on_page_non_indexable_request_info)
        print("The response of OnPageApi->non_indexable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->non_indexable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_non_indexable_request_info** | [**List[OnPageNonIndexableRequestInfo]**](OnPageNonIndexableRequestInfo.md)|  | [optional] 

### Return type

[**OnPageNonIndexableResponseInfo**](OnPageNonIndexableResponseInfo.md)

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

# **on_page_available_filters**
> OnPageAvailableFiltersResponseInfo on_page_available_filters()



OnPage API supports plenty of customizable crawling parameters that allow you to adapt the extraction of website data to your requirements and modify the thresholds for various performance indicators. ‌‌ Here you will find all the necessary information about filters and thresholds that can be used with DataForSEO OnPage API endpoints. for more info please visit 'https://docs.dataforseo.com/v3/on_page/filters_and_thresholds/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_available_filters_response_info import OnPageAvailableFiltersResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)

    try:
        api_response = api_instance.on_page_available_filters()
        print("The response of OnPageApi->on_page_available_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->on_page_available_filters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OnPageAvailableFiltersResponseInfo**](OnPageAvailableFiltersResponseInfo.md)

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

# **on_page_errors**
> OnPageErrorsResponseInfo on_page_errors(on_page_errors_request_info=on_page_errors_request_info)



By calling this endpoint you will receive information about the OnPage API tasks that returned an error within the past 24 hours. for more info please visit 'https://docs.dataforseo.com/v3/on_page/errors/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_errors_request_info import OnPageErrorsRequestInfo
from dataforseo_client.models.on_page_errors_response_info import OnPageErrorsResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_errors_request_info = [dataforseo_client.OnPageErrorsRequestInfo()] # List[OnPageErrorsRequestInfo] |  (optional)

    try:
        api_response = api_instance.on_page_errors(on_page_errors_request_info=on_page_errors_request_info)
        print("The response of OnPageApi->on_page_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->on_page_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_errors_request_info** | [**List[OnPageErrorsRequestInfo]**](OnPageErrorsRequestInfo.md)|  | [optional] 

### Return type

[**OnPageErrorsResponseInfo**](OnPageErrorsResponseInfo.md)

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

# **on_page_id_list**
> OnPageIdListResponseInfo on_page_id_list(on_page_id_list_request_info=on_page_id_list_request_info)



This endpoint is designed to provide you with the list of IDs and metadata of the completed On Page tasks during the specified period. You will get all task IDs that were made including successful, uncompleted, and tasks that responded as errors. for more info please visit 'https://docs.dataforseo.com/v3/on_page/id_list/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_id_list_request_info import OnPageIdListRequestInfo
from dataforseo_client.models.on_page_id_list_response_info import OnPageIdListResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_id_list_request_info = [dataforseo_client.OnPageIdListRequestInfo()] # List[OnPageIdListRequestInfo] |  (optional)

    try:
        api_response = api_instance.on_page_id_list(on_page_id_list_request_info=on_page_id_list_request_info)
        print("The response of OnPageApi->on_page_id_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->on_page_id_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_id_list_request_info** | [**List[OnPageIdListRequestInfo]**](OnPageIdListRequestInfo.md)|  | [optional] 

### Return type

[**OnPageIdListResponseInfo**](OnPageIdListResponseInfo.md)

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

# **on_page_lighthouse_languages**
> OnPageLighthouseLanguagesResponseInfo on_page_lighthouse_languages()



You will receive the list of languages by calling this API.   As a response of the API server, you will receive JSON-encoded data containing a tasks array with the information specific to the set tasks. for more info please visit 'https://docs.dataforseo.com/v3/on_page/lighthouse/languages/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_lighthouse_languages_response_info import OnPageLighthouseLanguagesResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)

    try:
        api_response = api_instance.on_page_lighthouse_languages()
        print("The response of OnPageApi->on_page_lighthouse_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->on_page_lighthouse_languages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OnPageLighthouseLanguagesResponseInfo**](OnPageLighthouseLanguagesResponseInfo.md)

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

# **page_screenshot**
> OnPagePageScreenshotResponseInfo page_screenshot(on_page_page_screenshot_request_info=on_page_page_screenshot_request_info)



‌‌ Using this endpoint, you can capture a full high-quality screenshot of any webpage. In this way, you can review the target page as the DataForSEO crawler and Googlebot see it. for more info please visit 'https://docs.dataforseo.com/v3/on_page/page_screenshot/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_page_screenshot_request_info import OnPagePageScreenshotRequestInfo
from dataforseo_client.models.on_page_page_screenshot_response_info import OnPagePageScreenshotResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_page_screenshot_request_info = [dataforseo_client.OnPagePageScreenshotRequestInfo()] # List[OnPagePageScreenshotRequestInfo] |  (optional)

    try:
        api_response = api_instance.page_screenshot(on_page_page_screenshot_request_info=on_page_page_screenshot_request_info)
        print("The response of OnPageApi->page_screenshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->page_screenshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_page_screenshot_request_info** | [**List[OnPagePageScreenshotRequestInfo]**](OnPagePageScreenshotRequestInfo.md)|  | [optional] 

### Return type

[**OnPagePageScreenshotResponseInfo**](OnPagePageScreenshotResponseInfo.md)

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

# **pages**
> OnPagePagesResponseInfo pages(on_page_pages_request_info=on_page_pages_request_info)



‌‌ This endpoint returns a list of crawled pages with on-page check-ups and other metrics related to the page performance. Using this function you will get page-specific data with detailed information on how well your pages are optimized for search. for more info please visit 'https://docs.dataforseo.com/v3/on_page/pages/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_pages_request_info import OnPagePagesRequestInfo
from dataforseo_client.models.on_page_pages_response_info import OnPagePagesResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_pages_request_info = [dataforseo_client.OnPagePagesRequestInfo()] # List[OnPagePagesRequestInfo] |  (optional)

    try:
        api_response = api_instance.pages(on_page_pages_request_info=on_page_pages_request_info)
        print("The response of OnPageApi->pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_pages_request_info** | [**List[OnPagePagesRequestInfo]**](OnPagePagesRequestInfo.md)|  | [optional] 

### Return type

[**OnPagePagesResponseInfo**](OnPagePagesResponseInfo.md)

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

# **pages_by_resource**
> OnPagePagesByResourceResponseInfo pages_by_resource(on_page_pages_by_resource_request_info=on_page_pages_by_resource_request_info)



‌‌ This endpoint will return the list of pages where a specific resource is located. Using this function you will also get the data related to the pages that contain a specified resource. You can get the URL of a resource using the Resources endpoint. for more info please visit 'https://docs.dataforseo.com/v3/on_page/page_by_resource/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_pages_by_resource_request_info import OnPagePagesByResourceRequestInfo
from dataforseo_client.models.on_page_pages_by_resource_response_info import OnPagePagesByResourceResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_pages_by_resource_request_info = [dataforseo_client.OnPagePagesByResourceRequestInfo()] # List[OnPagePagesByResourceRequestInfo] |  (optional)

    try:
        api_response = api_instance.pages_by_resource(on_page_pages_by_resource_request_info=on_page_pages_by_resource_request_info)
        print("The response of OnPageApi->pages_by_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->pages_by_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_pages_by_resource_request_info** | [**List[OnPagePagesByResourceRequestInfo]**](OnPagePagesByResourceRequestInfo.md)|  | [optional] 

### Return type

[**OnPagePagesByResourceResponseInfo**](OnPagePagesByResourceResponseInfo.md)

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

# **raw_html**
> OnPageRawHtmlResponseInfo raw_html(on_page_raw_html_request_info=on_page_raw_html_request_info)



‌‌ This endpoint returns the HTML of a page you indicate in the request. for more info please visit 'https://docs.dataforseo.com/v3/on_page/raw_html/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_raw_html_request_info import OnPageRawHtmlRequestInfo
from dataforseo_client.models.on_page_raw_html_response_info import OnPageRawHtmlResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_raw_html_request_info = [dataforseo_client.OnPageRawHtmlRequestInfo()] # List[OnPageRawHtmlRequestInfo] |  (optional)

    try:
        api_response = api_instance.raw_html(on_page_raw_html_request_info=on_page_raw_html_request_info)
        print("The response of OnPageApi->raw_html:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->raw_html: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_raw_html_request_info** | [**List[OnPageRawHtmlRequestInfo]**](OnPageRawHtmlRequestInfo.md)|  | [optional] 

### Return type

[**OnPageRawHtmlResponseInfo**](OnPageRawHtmlResponseInfo.md)

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

# **redirect_chains**
> OnPageRedirectChainsResponseInfo redirect_chains(on_page_redirect_chains_request_info=on_page_redirect_chains_request_info)



‌‌ Redirect chains occur when there are at least two redirects between the initial URL and the destination URL. For example, if page A redirects to page B which redirects to page C, such a series of redirects is considered a redirect chain. Sometimes, if page B redirects back to page A, the redirect chain becomes closed and is considered a redirect loop. for more info please visit 'https://docs.dataforseo.com/v3/on_page/redirect_chains/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_redirect_chains_request_info import OnPageRedirectChainsRequestInfo
from dataforseo_client.models.on_page_redirect_chains_response_info import OnPageRedirectChainsResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_redirect_chains_request_info = [dataforseo_client.OnPageRedirectChainsRequestInfo()] # List[OnPageRedirectChainsRequestInfo] |  (optional)

    try:
        api_response = api_instance.redirect_chains(on_page_redirect_chains_request_info=on_page_redirect_chains_request_info)
        print("The response of OnPageApi->redirect_chains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->redirect_chains: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_redirect_chains_request_info** | [**List[OnPageRedirectChainsRequestInfo]**](OnPageRedirectChainsRequestInfo.md)|  | [optional] 

### Return type

[**OnPageRedirectChainsResponseInfo**](OnPageRedirectChainsResponseInfo.md)

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

# **resources**
> OnPageResourcesResponseInfo resources(on_page_resources_request_info=on_page_resources_request_info)



‌‌ This endpoint will provide you with a list of resources, including images, scripts, stylesheets, and broken elements. You will get a detailed overview of every resource found on the crawled pages. for more info please visit 'https://docs.dataforseo.com/v3/on_page/resources/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_resources_request_info import OnPageResourcesRequestInfo
from dataforseo_client.models.on_page_resources_response_info import OnPageResourcesResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_resources_request_info = [dataforseo_client.OnPageResourcesRequestInfo()] # List[OnPageResourcesRequestInfo] |  (optional)

    try:
        api_response = api_instance.resources(on_page_resources_request_info=on_page_resources_request_info)
        print("The response of OnPageApi->resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_resources_request_info** | [**List[OnPageResourcesRequestInfo]**](OnPageResourcesRequestInfo.md)|  | [optional] 

### Return type

[**OnPageResourcesResponseInfo**](OnPageResourcesResponseInfo.md)

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

# **summary**
> OnPageSummaryResponseInfo summary(id)



‌ Using this function, you can get the overall information on a website as well as drill down into exact on-page issues of a website that has been scanned. As a result, you will know what functions to use for receiving detailed data for each of the found issues. for more info please visit 'https://docs.dataforseo.com/v3/on_page/summary/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_summary_response_info import OnPageSummaryResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    id = '00000000-0000-0000-0000-000000000000' # str | task identifier required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04”

    try:
        api_response = api_instance.summary(id)
        print("The response of OnPageApi->summary:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->summary: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| task identifier required field you can get this ID in the response of the Task POST endpoint example: “07131248-1535-0216-1000-17384017ad04” | 

### Return type

[**OnPageSummaryResponseInfo**](OnPageSummaryResponseInfo.md)

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

# **task_post**
> OnPageTaskPostResponseInfo task_post(on_page_task_request_info=on_page_task_request_info)



‌ OnPage API checks websites for 60+ customizable on-page parameters defines and displays all found flaws and opportunities for optimization so that you can easily fix them. It checks meta tags, duplicate content, image tags, response codes, and other parameters on every page. You can find the full list of OnPage API check-up parameters in the Pages section. for more info please visit 'https://docs.dataforseo.com/v3/on_page/task_post/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_task_post_response_info import OnPageTaskPostResponseInfo
from dataforseo_client.models.on_page_task_request_info import OnPageTaskRequestInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_task_request_info = [dataforseo_client.OnPageTaskRequestInfo()] # List[OnPageTaskRequestInfo] |  (optional)

    try:
        api_response = api_instance.task_post(on_page_task_request_info=on_page_task_request_info)
        print("The response of OnPageApi->task_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->task_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_task_request_info** | [**List[OnPageTaskRequestInfo]**](OnPageTaskRequestInfo.md)|  | [optional] 

### Return type

[**OnPageTaskPostResponseInfo**](OnPageTaskPostResponseInfo.md)

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

# **tasks_ready**
> OnPageTasksReadyResponseInfo tasks_ready()



‌ The ‘Tasks Ready’ endpoint is designed to provide you with a list of completed tasks, which results haven’t been collected yet. for more info please visit 'https://docs.dataforseo.com/v3/on_page-tasks_ready/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_tasks_ready_response_info import OnPageTasksReadyResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)

    try:
        api_response = api_instance.tasks_ready()
        print("The response of OnPageApi->tasks_ready:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->tasks_ready: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OnPageTasksReadyResponseInfo**](OnPageTasksReadyResponseInfo.md)

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

# **waterfall**
> OnPageWaterfallResponseInfo waterfall(on_page_waterfall_request_info=on_page_waterfall_request_info)



‌‌ This endpoint is designed to provide you with the page speed insights. Using this function you can get detailed information about the page loading time, time to secure connection, the time it takes to load page resources, and so on. for more info please visit 'https://docs.dataforseo.com/v3/on_page/waterfall/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.on_page_waterfall_request_info import OnPageWaterfallRequestInfo
from dataforseo_client.models.on_page_waterfall_response_info import OnPageWaterfallResponseInfo
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
    api_instance = dataforseo_client.OnPageApi(api_client)
    on_page_waterfall_request_info = [dataforseo_client.OnPageWaterfallRequestInfo()] # List[OnPageWaterfallRequestInfo] |  (optional)

    try:
        api_response = api_instance.waterfall(on_page_waterfall_request_info=on_page_waterfall_request_info)
        print("The response of OnPageApi->waterfall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OnPageApi->waterfall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **on_page_waterfall_request_info** | [**List[OnPageWaterfallRequestInfo]**](OnPageWaterfallRequestInfo.md)|  | [optional] 

### Return type

[**OnPageWaterfallResponseInfo**](OnPageWaterfallResponseInfo.md)

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

