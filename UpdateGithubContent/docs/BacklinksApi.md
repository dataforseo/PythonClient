# dataforseo_client.BacklinksApi

All URIs are relative to *https://api.dataforseo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anchors_live**](BacklinksApi.md#anchors_live) | **POST** /v3/backlinks/anchors/live | 
[**backlinks_available_filters**](BacklinksApi.md#backlinks_available_filters) | **GET** /v3/backlinks/available_filters | 
[**backlinks_errors**](BacklinksApi.md#backlinks_errors) | **POST** /v3/backlinks/errors | 
[**backlinks_id_list**](BacklinksApi.md#backlinks_id_list) | **POST** /v3/backlinks/id_list | 
[**backlinks_live**](BacklinksApi.md#backlinks_live) | **POST** /v3/backlinks/backlinks/live | 
[**bulk_backlinks_live**](BacklinksApi.md#bulk_backlinks_live) | **POST** /v3/backlinks/bulk_backlinks/live | 
[**bulk_new_lost_backlinks_live**](BacklinksApi.md#bulk_new_lost_backlinks_live) | **POST** /v3/backlinks/bulk_new_lost_backlinks/live | 
[**bulk_new_lost_referring_domains_live**](BacklinksApi.md#bulk_new_lost_referring_domains_live) | **POST** /v3/backlinks/bulk_new_lost_referring_domains/live | 
[**bulk_pages_summary_live**](BacklinksApi.md#bulk_pages_summary_live) | **POST** /v3/backlinks/bulk_pages_summary/live | 
[**bulk_ranks_live**](BacklinksApi.md#bulk_ranks_live) | **POST** /v3/backlinks/bulk_ranks/live | 
[**bulk_referring_domains_live**](BacklinksApi.md#bulk_referring_domains_live) | **POST** /v3/backlinks/bulk_referring_domains/live | 
[**bulk_spam_score_live**](BacklinksApi.md#bulk_spam_score_live) | **POST** /v3/backlinks/bulk_spam_score/live | 
[**competitors_live**](BacklinksApi.md#competitors_live) | **POST** /v3/backlinks/competitors/live | 
[**domain_intersection_live**](BacklinksApi.md#domain_intersection_live) | **POST** /v3/backlinks/domain_intersection/live | 
[**domain_pages_live**](BacklinksApi.md#domain_pages_live) | **POST** /v3/backlinks/domain_pages/live | 
[**domain_pages_summary_live**](BacklinksApi.md#domain_pages_summary_live) | **POST** /v3/backlinks/domain_pages_summary/live | 
[**history_live**](BacklinksApi.md#history_live) | **POST** /v3/backlinks/history/live | 
[**index**](BacklinksApi.md#index) | **GET** /v3/backlinks/index | 
[**page_intersection_live**](BacklinksApi.md#page_intersection_live) | **POST** /v3/backlinks/page_intersection/live | 
[**referring_domains_live**](BacklinksApi.md#referring_domains_live) | **POST** /v3/backlinks/referring_domains/live | 
[**referring_networks_live**](BacklinksApi.md#referring_networks_live) | **POST** /v3/backlinks/referring_networks/live | 
[**summary_live**](BacklinksApi.md#summary_live) | **POST** /v3/backlinks/summary/live | 
[**timeseries_new_lost_summary_live**](BacklinksApi.md#timeseries_new_lost_summary_live) | **POST** /v3/backlinks/timeseries_new_lost_summary/live | 
[**timeseries_summary_live**](BacklinksApi.md#timeseries_summary_live) | **POST** /v3/backlinks/timeseries_summary/live | 


# **anchors_live**
> BacklinksAnchorsLiveResponseInfo anchors_live(backlinks_anchors_live_request_info=backlinks_anchors_live_request_info)



‌‌ This endpoint will provide you with a detailed overview of anchors used when linking to the specified website with relevant backlink data for each of them. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/anchors/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_anchors_live_request_info import BacklinksAnchorsLiveRequestInfo
from dataforseo_client.models.backlinks_anchors_live_response_info import BacklinksAnchorsLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_anchors_live_request_info = [dataforseo_client.BacklinksAnchorsLiveRequestInfo()] # List[BacklinksAnchorsLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.anchors_live(backlinks_anchors_live_request_info=backlinks_anchors_live_request_info)
        print("The response of BacklinksApi->anchors_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->anchors_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_anchors_live_request_info** | [**List[BacklinksAnchorsLiveRequestInfo]**](BacklinksAnchorsLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksAnchorsLiveResponseInfo**](BacklinksAnchorsLiveResponseInfo.md)

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

# **backlinks_available_filters**
> BacklinksAvailableFiltersResponseInfo backlinks_available_filters()



Backlinks API features plenty of parameters that support custom filtration. By applying filters to your POST requests, you will be able to effortlessly extract data that matches your requirements. Note that we do not charge any fees for using data filtering or sorting rules. ‌‌ Here you will find all the necessary information about filters that can be used with DataForSEO Backlinks API endpoints. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/filters/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_available_filters_response_info import BacklinksAvailableFiltersResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)

    try:
        api_response = api_instance.backlinks_available_filters()
        print("The response of BacklinksApi->backlinks_available_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->backlinks_available_filters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BacklinksAvailableFiltersResponseInfo**](BacklinksAvailableFiltersResponseInfo.md)

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

# **backlinks_errors**
> BacklinksErrorsResponseInfo backlinks_errors(backlinks_errors_request_info=backlinks_errors_request_info)



By calling this endpoint you will receive information about the Backlinks API tasks that returned an error within the past 24 hours. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/errors/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_errors_request_info import BacklinksErrorsRequestInfo
from dataforseo_client.models.backlinks_errors_response_info import BacklinksErrorsResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_errors_request_info = [dataforseo_client.BacklinksErrorsRequestInfo()] # List[BacklinksErrorsRequestInfo] |  (optional)

    try:
        api_response = api_instance.backlinks_errors(backlinks_errors_request_info=backlinks_errors_request_info)
        print("The response of BacklinksApi->backlinks_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->backlinks_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_errors_request_info** | [**List[BacklinksErrorsRequestInfo]**](BacklinksErrorsRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksErrorsResponseInfo**](BacklinksErrorsResponseInfo.md)

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

# **backlinks_id_list**
> BacklinksIdListResponseInfo backlinks_id_list(backlinks_id_list_request_info=backlinks_id_list_request_info)



This endpoint is designed to provide you with the list of IDs and metadata of the completed Backlinks tasks during the specified period. You will get all task IDs that were made including successful, uncompleted, and tasks that responded as errors. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/id_list/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_id_list_request_info import BacklinksIdListRequestInfo
from dataforseo_client.models.backlinks_id_list_response_info import BacklinksIdListResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_id_list_request_info = [dataforseo_client.BacklinksIdListRequestInfo()] # List[BacklinksIdListRequestInfo] |  (optional)

    try:
        api_response = api_instance.backlinks_id_list(backlinks_id_list_request_info=backlinks_id_list_request_info)
        print("The response of BacklinksApi->backlinks_id_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->backlinks_id_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_id_list_request_info** | [**List[BacklinksIdListRequestInfo]**](BacklinksIdListRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksIdListResponseInfo**](BacklinksIdListResponseInfo.md)

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

# **backlinks_live**
> BacklinksBacklinksLiveResponseInfo backlinks_live(backlinks_backlinks_live_request_info=backlinks_backlinks_live_request_info)



‌ This endpoint will provide you with a list of backlinks and relevant data for the specified domain, subdomain, or webpage. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/backlinks/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_backlinks_live_request_info import BacklinksBacklinksLiveRequestInfo
from dataforseo_client.models.backlinks_backlinks_live_response_info import BacklinksBacklinksLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_backlinks_live_request_info = [dataforseo_client.BacklinksBacklinksLiveRequestInfo()] # List[BacklinksBacklinksLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.backlinks_live(backlinks_backlinks_live_request_info=backlinks_backlinks_live_request_info)
        print("The response of BacklinksApi->backlinks_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->backlinks_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_backlinks_live_request_info** | [**List[BacklinksBacklinksLiveRequestInfo]**](BacklinksBacklinksLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksBacklinksLiveResponseInfo**](BacklinksBacklinksLiveResponseInfo.md)

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

# **bulk_backlinks_live**
> BacklinksBulkBacklinksLiveResponseInfo bulk_backlinks_live(backlinks_bulk_backlinks_live_request_info=backlinks_bulk_backlinks_live_request_info)



‌ This endpoint will provide you with the number of backlinks pointing to domains, subdomains, and pages specified in the targets array. The returned numbers correspond to all live backlinks, that is, total number of referring links with all attributes (e.g., nofollow, noreferrer, ugc, sponsored etc) that were found during the latest check. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/bulk_backlinks/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_bulk_backlinks_live_request_info import BacklinksBulkBacklinksLiveRequestInfo
from dataforseo_client.models.backlinks_bulk_backlinks_live_response_info import BacklinksBulkBacklinksLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_bulk_backlinks_live_request_info = [dataforseo_client.BacklinksBulkBacklinksLiveRequestInfo()] # List[BacklinksBulkBacklinksLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.bulk_backlinks_live(backlinks_bulk_backlinks_live_request_info=backlinks_bulk_backlinks_live_request_info)
        print("The response of BacklinksApi->bulk_backlinks_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->bulk_backlinks_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_bulk_backlinks_live_request_info** | [**List[BacklinksBulkBacklinksLiveRequestInfo]**](BacklinksBulkBacklinksLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksBulkBacklinksLiveResponseInfo**](BacklinksBulkBacklinksLiveResponseInfo.md)

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

# **bulk_new_lost_backlinks_live**
> BacklinksBulkNewLostBacklinksLiveResponseInfo bulk_new_lost_backlinks_live(backlinks_bulk_new_lost_backlinks_live_request_info=backlinks_bulk_new_lost_backlinks_live_request_info)



‌ This endpoint will provide you with the number of new and lost backlinks for the domains, subdomains, and pages specified in the targets array. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/bulk_new_lost_backlinks/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_bulk_new_lost_backlinks_live_request_info import BacklinksBulkNewLostBacklinksLiveRequestInfo
from dataforseo_client.models.backlinks_bulk_new_lost_backlinks_live_response_info import BacklinksBulkNewLostBacklinksLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_bulk_new_lost_backlinks_live_request_info = [dataforseo_client.BacklinksBulkNewLostBacklinksLiveRequestInfo()] # List[BacklinksBulkNewLostBacklinksLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.bulk_new_lost_backlinks_live(backlinks_bulk_new_lost_backlinks_live_request_info=backlinks_bulk_new_lost_backlinks_live_request_info)
        print("The response of BacklinksApi->bulk_new_lost_backlinks_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->bulk_new_lost_backlinks_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_bulk_new_lost_backlinks_live_request_info** | [**List[BacklinksBulkNewLostBacklinksLiveRequestInfo]**](BacklinksBulkNewLostBacklinksLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksBulkNewLostBacklinksLiveResponseInfo**](BacklinksBulkNewLostBacklinksLiveResponseInfo.md)

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

# **bulk_new_lost_referring_domains_live**
> BacklinksBulkNewLostReferringDomainsLiveResponseInfo bulk_new_lost_referring_domains_live(backlinks_bulk_new_lost_referring_domains_live_request_info=backlinks_bulk_new_lost_referring_domains_live_request_info)



‌ This endpoint will provide you with the number of referring domains pointing to the domains, subdomains and pages specified in the targets array. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/bulk_new_lost_referring_domains/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_bulk_new_lost_referring_domains_live_request_info import BacklinksBulkNewLostReferringDomainsLiveRequestInfo
from dataforseo_client.models.backlinks_bulk_new_lost_referring_domains_live_response_info import BacklinksBulkNewLostReferringDomainsLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_bulk_new_lost_referring_domains_live_request_info = [dataforseo_client.BacklinksBulkNewLostReferringDomainsLiveRequestInfo()] # List[BacklinksBulkNewLostReferringDomainsLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.bulk_new_lost_referring_domains_live(backlinks_bulk_new_lost_referring_domains_live_request_info=backlinks_bulk_new_lost_referring_domains_live_request_info)
        print("The response of BacklinksApi->bulk_new_lost_referring_domains_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->bulk_new_lost_referring_domains_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_bulk_new_lost_referring_domains_live_request_info** | [**List[BacklinksBulkNewLostReferringDomainsLiveRequestInfo]**](BacklinksBulkNewLostReferringDomainsLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksBulkNewLostReferringDomainsLiveResponseInfo**](BacklinksBulkNewLostReferringDomainsLiveResponseInfo.md)

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

# **bulk_pages_summary_live**
> BacklinksBulkPagesSummaryLiveResponseInfo bulk_pages_summary_live(backlinks_bulk_pages_summary_live_request_info=backlinks_bulk_pages_summary_live_request_info)



This endpoint will provide you with a comprehensive overview of backlinks and related data for a bulk of up to 1000 pages, domains, or subdomains. If you indicate a single page as a target, you will get comprehensive summary data on all backlinks for that page. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/bulk_pages_summary/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_bulk_pages_summary_live_request_info import BacklinksBulkPagesSummaryLiveRequestInfo
from dataforseo_client.models.backlinks_bulk_pages_summary_live_response_info import BacklinksBulkPagesSummaryLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_bulk_pages_summary_live_request_info = [dataforseo_client.BacklinksBulkPagesSummaryLiveRequestInfo()] # List[BacklinksBulkPagesSummaryLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.bulk_pages_summary_live(backlinks_bulk_pages_summary_live_request_info=backlinks_bulk_pages_summary_live_request_info)
        print("The response of BacklinksApi->bulk_pages_summary_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->bulk_pages_summary_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_bulk_pages_summary_live_request_info** | [**List[BacklinksBulkPagesSummaryLiveRequestInfo]**](BacklinksBulkPagesSummaryLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksBulkPagesSummaryLiveResponseInfo**](BacklinksBulkPagesSummaryLiveResponseInfo.md)

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

# **bulk_ranks_live**
> BacklinksBulkRanksLiveResponseInfo bulk_ranks_live(backlinks_bulk_ranks_live_request_info=backlinks_bulk_ranks_live_request_info)



‌ This endpoint will provide you with rank scores of the domains, subdomains, and pages specified in the targets array. The score is based on the number of referring domains pointing to the specified domains, subdomains, or pages. rank values range from 0 (no backlinks detected) to 1,000 (highest rank). A similar scoring system is used in Google’s Page Rank algorithm. You can learn more about rank scores in this help center article for more info please visit 'https://docs.dataforseo.com/v3/backlinks/bulk_ranks/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_bulk_ranks_live_request_info import BacklinksBulkRanksLiveRequestInfo
from dataforseo_client.models.backlinks_bulk_ranks_live_response_info import BacklinksBulkRanksLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_bulk_ranks_live_request_info = [dataforseo_client.BacklinksBulkRanksLiveRequestInfo()] # List[BacklinksBulkRanksLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.bulk_ranks_live(backlinks_bulk_ranks_live_request_info=backlinks_bulk_ranks_live_request_info)
        print("The response of BacklinksApi->bulk_ranks_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->bulk_ranks_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_bulk_ranks_live_request_info** | [**List[BacklinksBulkRanksLiveRequestInfo]**](BacklinksBulkRanksLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksBulkRanksLiveResponseInfo**](BacklinksBulkRanksLiveResponseInfo.md)

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

# **bulk_referring_domains_live**
> BacklinksBulkReferringDomainsLiveResponseInfo bulk_referring_domains_live(backlinks_bulk_referring_domains_live_request_info=backlinks_bulk_referring_domains_live_request_info)



‌ This endpoint will provide you with the number of referring domains pointing to domains, subdomains, and pages specified in the targets array. The returned numbers are based on all live referring domains, that is, total number of domains pointing to the target with any type of backlinks (e.g., nofollow, noreferrer, ugc, sponsored etc) that were found during the latest check. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/bulk_referring_domains/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_bulk_referring_domains_live_request_info import BacklinksBulkReferringDomainsLiveRequestInfo
from dataforseo_client.models.backlinks_bulk_referring_domains_live_response_info import BacklinksBulkReferringDomainsLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_bulk_referring_domains_live_request_info = [dataforseo_client.BacklinksBulkReferringDomainsLiveRequestInfo()] # List[BacklinksBulkReferringDomainsLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.bulk_referring_domains_live(backlinks_bulk_referring_domains_live_request_info=backlinks_bulk_referring_domains_live_request_info)
        print("The response of BacklinksApi->bulk_referring_domains_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->bulk_referring_domains_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_bulk_referring_domains_live_request_info** | [**List[BacklinksBulkReferringDomainsLiveRequestInfo]**](BacklinksBulkReferringDomainsLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksBulkReferringDomainsLiveResponseInfo**](BacklinksBulkReferringDomainsLiveResponseInfo.md)

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

# **bulk_spam_score_live**
> BacklinksBulkSpamScoreLiveResponseInfo bulk_spam_score_live(backlinks_bulk_spam_score_live_request_info=backlinks_bulk_spam_score_live_request_info)



‌ This endpoint will provide you with spam scores of the domains, subdomains, and pages you specified in the targets array. Spam Score is DataForSEO’s proprietary metric that indicates how “spammy” your target is on a scale from 0 to 100. You can learn more about Spam Score, how it is calculated, and signals it takes into account in this help center article for more info please visit 'https://docs.dataforseo.com/v3/backlinks/bulk_spam_score/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_bulk_spam_score_live_request_info import BacklinksBulkSpamScoreLiveRequestInfo
from dataforseo_client.models.backlinks_bulk_spam_score_live_response_info import BacklinksBulkSpamScoreLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_bulk_spam_score_live_request_info = [dataforseo_client.BacklinksBulkSpamScoreLiveRequestInfo()] # List[BacklinksBulkSpamScoreLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.bulk_spam_score_live(backlinks_bulk_spam_score_live_request_info=backlinks_bulk_spam_score_live_request_info)
        print("The response of BacklinksApi->bulk_spam_score_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->bulk_spam_score_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_bulk_spam_score_live_request_info** | [**List[BacklinksBulkSpamScoreLiveRequestInfo]**](BacklinksBulkSpamScoreLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksBulkSpamScoreLiveResponseInfo**](BacklinksBulkSpamScoreLiveResponseInfo.md)

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

# **competitors_live**
> BacklinksCompetitorsLiveResponseInfo competitors_live(backlinks_competitors_live_request_info=backlinks_competitors_live_request_info)



‌‌ This endpoint will provide you with a list of competitors that share some part of the backlink profile with a target website, along with a number of backlink intersections and the rank of every competing website. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/competitors/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_competitors_live_request_info import BacklinksCompetitorsLiveRequestInfo
from dataforseo_client.models.backlinks_competitors_live_response_info import BacklinksCompetitorsLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_competitors_live_request_info = [dataforseo_client.BacklinksCompetitorsLiveRequestInfo()] # List[BacklinksCompetitorsLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.competitors_live(backlinks_competitors_live_request_info=backlinks_competitors_live_request_info)
        print("The response of BacklinksApi->competitors_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->competitors_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_competitors_live_request_info** | [**List[BacklinksCompetitorsLiveRequestInfo]**](BacklinksCompetitorsLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksCompetitorsLiveResponseInfo**](BacklinksCompetitorsLiveResponseInfo.md)

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

# **domain_intersection_live**
> BacklinksDomainIntersectionLiveResponseInfo domain_intersection_live(backlinks_domain_intersection_live_request_info=backlinks_domain_intersection_live_request_info)



‌ This endpoint will provide you with the list of domains pointing to the specified websites. This endpoint is especially useful for creating a Link Gap feature that shows what domains link to your competitors but do not link out to your website. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/domain_intersection/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_domain_intersection_live_request_info import BacklinksDomainIntersectionLiveRequestInfo
from dataforseo_client.models.backlinks_domain_intersection_live_response_info import BacklinksDomainIntersectionLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_domain_intersection_live_request_info = [dataforseo_client.BacklinksDomainIntersectionLiveRequestInfo()] # List[BacklinksDomainIntersectionLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.domain_intersection_live(backlinks_domain_intersection_live_request_info=backlinks_domain_intersection_live_request_info)
        print("The response of BacklinksApi->domain_intersection_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->domain_intersection_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_domain_intersection_live_request_info** | [**List[BacklinksDomainIntersectionLiveRequestInfo]**](BacklinksDomainIntersectionLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksDomainIntersectionLiveResponseInfo**](BacklinksDomainIntersectionLiveResponseInfo.md)

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

# **domain_pages_live**
> BacklinksDomainPagesLiveResponseInfo domain_pages_live(backlinks_domain_pages_live_request_info=backlinks_domain_pages_live_request_info)



‌‌ This endpoint will provide you with a detailed overview of domain pages with backlink data for each page. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/domain_pages/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_domain_pages_live_request_info import BacklinksDomainPagesLiveRequestInfo
from dataforseo_client.models.backlinks_domain_pages_live_response_info import BacklinksDomainPagesLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_domain_pages_live_request_info = [dataforseo_client.BacklinksDomainPagesLiveRequestInfo()] # List[BacklinksDomainPagesLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.domain_pages_live(backlinks_domain_pages_live_request_info=backlinks_domain_pages_live_request_info)
        print("The response of BacklinksApi->domain_pages_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->domain_pages_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_domain_pages_live_request_info** | [**List[BacklinksDomainPagesLiveRequestInfo]**](BacklinksDomainPagesLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksDomainPagesLiveResponseInfo**](BacklinksDomainPagesLiveResponseInfo.md)

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

# **domain_pages_summary_live**
> BacklinksDomainPagesSummaryLiveResponseInfo domain_pages_summary_live(backlinks_domain_pages_summary_live_request_info=backlinks_domain_pages_summary_live_request_info)



This endpoint will provide you with detailed summary data on all backlinks and related metrics for each page of the target domain or subdomain you specify. If you indicate a single page as a target, you will get comprehensive summary data on all backlinks for that page. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/domain_pages_summary/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_domain_pages_summary_live_request_info import BacklinksDomainPagesSummaryLiveRequestInfo
from dataforseo_client.models.backlinks_domain_pages_summary_live_response_info import BacklinksDomainPagesSummaryLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_domain_pages_summary_live_request_info = [dataforseo_client.BacklinksDomainPagesSummaryLiveRequestInfo()] # List[BacklinksDomainPagesSummaryLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.domain_pages_summary_live(backlinks_domain_pages_summary_live_request_info=backlinks_domain_pages_summary_live_request_info)
        print("The response of BacklinksApi->domain_pages_summary_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->domain_pages_summary_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_domain_pages_summary_live_request_info** | [**List[BacklinksDomainPagesSummaryLiveRequestInfo]**](BacklinksDomainPagesSummaryLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksDomainPagesSummaryLiveResponseInfo**](BacklinksDomainPagesSummaryLiveResponseInfo.md)

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

# **history_live**
> BacklinksHistoryLiveResponseInfo history_live(backlinks_history_live_request_info=backlinks_history_live_request_info)



‌ This endpoint will provide you with historical backlinks data back to the beginning of 2019. You can receive the number of backlinks a given domain had in a specific time period, the number of new & lost backlinks, referring domains, and more. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/history/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_history_live_request_info import BacklinksHistoryLiveRequestInfo
from dataforseo_client.models.backlinks_history_live_response_info import BacklinksHistoryLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_history_live_request_info = [dataforseo_client.BacklinksHistoryLiveRequestInfo()] # List[BacklinksHistoryLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.history_live(backlinks_history_live_request_info=backlinks_history_live_request_info)
        print("The response of BacklinksApi->history_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->history_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_history_live_request_info** | [**List[BacklinksHistoryLiveRequestInfo]**](BacklinksHistoryLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksHistoryLiveResponseInfo**](BacklinksHistoryLiveResponseInfo.md)

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

# **index**
> BacklinksIndexResponseInfo index()



‌ This endpoint will provide you with the total number of backlinks, domains, and pages our database contains for the moment when you make a request. You will also get stats for the last 12 months. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/index/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_index_response_info import BacklinksIndexResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)

    try:
        api_response = api_instance.index()
        print("The response of BacklinksApi->index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->index: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BacklinksIndexResponseInfo**](BacklinksIndexResponseInfo.md)

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

# **page_intersection_live**
> BacklinksPageIntersectionLiveResponseInfo page_intersection_live(backlinks_page_intersection_live_request_info=backlinks_page_intersection_live_request_info)



‌ This endpoint will provide you with the list of referring pages pointing to the specified targets. It is especially useful for finding the backlinks that point to your competitors but don’t point to your website. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/page_intersection/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_page_intersection_live_request_info import BacklinksPageIntersectionLiveRequestInfo
from dataforseo_client.models.backlinks_page_intersection_live_response_info import BacklinksPageIntersectionLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_page_intersection_live_request_info = [dataforseo_client.BacklinksPageIntersectionLiveRequestInfo()] # List[BacklinksPageIntersectionLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.page_intersection_live(backlinks_page_intersection_live_request_info=backlinks_page_intersection_live_request_info)
        print("The response of BacklinksApi->page_intersection_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->page_intersection_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_page_intersection_live_request_info** | [**List[BacklinksPageIntersectionLiveRequestInfo]**](BacklinksPageIntersectionLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksPageIntersectionLiveResponseInfo**](BacklinksPageIntersectionLiveResponseInfo.md)

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

# **referring_domains_live**
> BacklinksReferringDomainsLiveResponseInfo referring_domains_live(backlinks_referring_domains_live_request_info=backlinks_referring_domains_live_request_info)



‌‌ This endpoint will provide you with a detailed overview of referring domains pointing to the target you specify. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/referring_domains/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_referring_domains_live_request_info import BacklinksReferringDomainsLiveRequestInfo
from dataforseo_client.models.backlinks_referring_domains_live_response_info import BacklinksReferringDomainsLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_referring_domains_live_request_info = [dataforseo_client.BacklinksReferringDomainsLiveRequestInfo()] # List[BacklinksReferringDomainsLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.referring_domains_live(backlinks_referring_domains_live_request_info=backlinks_referring_domains_live_request_info)
        print("The response of BacklinksApi->referring_domains_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->referring_domains_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_referring_domains_live_request_info** | [**List[BacklinksReferringDomainsLiveRequestInfo]**](BacklinksReferringDomainsLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksReferringDomainsLiveResponseInfo**](BacklinksReferringDomainsLiveResponseInfo.md)

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

# **referring_networks_live**
> BacklinksReferringNetworksLiveResponseInfo referring_networks_live(backlinks_referring_networks_live_request_info=backlinks_referring_networks_live_request_info)



‌‌ This endpoint will provide you with a detailed overview of referring IPs and subnets pointing to the target you specify. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/referring_networks/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_referring_networks_live_request_info import BacklinksReferringNetworksLiveRequestInfo
from dataforseo_client.models.backlinks_referring_networks_live_response_info import BacklinksReferringNetworksLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_referring_networks_live_request_info = [dataforseo_client.BacklinksReferringNetworksLiveRequestInfo()] # List[BacklinksReferringNetworksLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.referring_networks_live(backlinks_referring_networks_live_request_info=backlinks_referring_networks_live_request_info)
        print("The response of BacklinksApi->referring_networks_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->referring_networks_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_referring_networks_live_request_info** | [**List[BacklinksReferringNetworksLiveRequestInfo]**](BacklinksReferringNetworksLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksReferringNetworksLiveResponseInfo**](BacklinksReferringNetworksLiveResponseInfo.md)

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

# **summary_live**
> BacklinksSummaryLiveResponseInfo summary_live(backlinks_summary_live_request_info=backlinks_summary_live_request_info)



‌ This endpoint will provide you with an overview of backlinks data available for a given domain, subdomain, or webpage. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/summary/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_summary_live_request_info import BacklinksSummaryLiveRequestInfo
from dataforseo_client.models.backlinks_summary_live_response_info import BacklinksSummaryLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_summary_live_request_info = [dataforseo_client.BacklinksSummaryLiveRequestInfo()] # List[BacklinksSummaryLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.summary_live(backlinks_summary_live_request_info=backlinks_summary_live_request_info)
        print("The response of BacklinksApi->summary_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->summary_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_summary_live_request_info** | [**List[BacklinksSummaryLiveRequestInfo]**](BacklinksSummaryLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksSummaryLiveResponseInfo**](BacklinksSummaryLiveResponseInfo.md)

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

# **timeseries_new_lost_summary_live**
> BacklinksTimeseriesNewLostSummaryLiveResponseInfo timeseries_new_lost_summary_live(backlinks_timeseries_new_lost_summary_live_request_info=backlinks_timeseries_new_lost_summary_live_request_info)



‌ This endpoint will provide you with the number of new and lost backlinks and referring domains for the domain specified in the target field. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/timeseries_new_lost_summary/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_timeseries_new_lost_summary_live_request_info import BacklinksTimeseriesNewLostSummaryLiveRequestInfo
from dataforseo_client.models.backlinks_timeseries_new_lost_summary_live_response_info import BacklinksTimeseriesNewLostSummaryLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_timeseries_new_lost_summary_live_request_info = [dataforseo_client.BacklinksTimeseriesNewLostSummaryLiveRequestInfo()] # List[BacklinksTimeseriesNewLostSummaryLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.timeseries_new_lost_summary_live(backlinks_timeseries_new_lost_summary_live_request_info=backlinks_timeseries_new_lost_summary_live_request_info)
        print("The response of BacklinksApi->timeseries_new_lost_summary_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->timeseries_new_lost_summary_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_timeseries_new_lost_summary_live_request_info** | [**List[BacklinksTimeseriesNewLostSummaryLiveRequestInfo]**](BacklinksTimeseriesNewLostSummaryLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksTimeseriesNewLostSummaryLiveResponseInfo**](BacklinksTimeseriesNewLostSummaryLiveResponseInfo.md)

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

# **timeseries_summary_live**
> BacklinksTimeseriesSummaryLiveResponseInfo timeseries_summary_live(backlinks_timeseries_summary_live_request_info=backlinks_timeseries_summary_live_request_info)



‌ This endpoint will provide you with an overview of backlink data for the target domain available during a period between the two indicated dates. Backlink metrics will be grouped by the time range that you define: day, week, month, or year. for more info please visit 'https://docs.dataforseo.com/v3/backlinks/timeseries_summary/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.backlinks_timeseries_summary_live_request_info import BacklinksTimeseriesSummaryLiveRequestInfo
from dataforseo_client.models.backlinks_timeseries_summary_live_response_info import BacklinksTimeseriesSummaryLiveResponseInfo
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
    api_instance = dataforseo_client.BacklinksApi(api_client)
    backlinks_timeseries_summary_live_request_info = [dataforseo_client.BacklinksTimeseriesSummaryLiveRequestInfo()] # List[BacklinksTimeseriesSummaryLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.timeseries_summary_live(backlinks_timeseries_summary_live_request_info=backlinks_timeseries_summary_live_request_info)
        print("The response of BacklinksApi->timeseries_summary_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BacklinksApi->timeseries_summary_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **backlinks_timeseries_summary_live_request_info** | [**List[BacklinksTimeseriesSummaryLiveRequestInfo]**](BacklinksTimeseriesSummaryLiveRequestInfo.md)|  | [optional] 

### Return type

[**BacklinksTimeseriesSummaryLiveResponseInfo**](BacklinksTimeseriesSummaryLiveResponseInfo.md)

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

