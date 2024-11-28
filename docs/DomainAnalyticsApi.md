# dataforseo_client.DomainAnalyticsApi

All URIs are relative to *https://api.dataforseo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_analytics_errors**](DomainAnalyticsApi.md#domain_analytics_errors) | **POST** /v3/domain_analytics/errors | 
[**domain_analytics_id_list**](DomainAnalyticsApi.md#domain_analytics_id_list) | **POST** /v3/domain_analytics/id_list | 
[**domain_analytics_technologies_languages**](DomainAnalyticsApi.md#domain_analytics_technologies_languages) | **GET** /v3/domain_analytics/technologies/languages | 
[**domain_analytics_technologies_locations**](DomainAnalyticsApi.md#domain_analytics_technologies_locations) | **GET** /v3/domain_analytics/technologies/locations | 
[**technologies_aggregation_technologies_live**](DomainAnalyticsApi.md#technologies_aggregation_technologies_live) | **POST** /v3/domain_analytics/technologies/aggregation_technologies/live | 
[**technologies_available_filters**](DomainAnalyticsApi.md#technologies_available_filters) | **GET** /v3/domain_analytics/technologies/available_filters | 
[**technologies_domain_technologies_live**](DomainAnalyticsApi.md#technologies_domain_technologies_live) | **POST** /v3/domain_analytics/technologies/domain_technologies/live | 
[**technologies_domains_by_html_terms_live**](DomainAnalyticsApi.md#technologies_domains_by_html_terms_live) | **POST** /v3/domain_analytics/technologies/domains_by_html_terms/live | 
[**technologies_domains_by_technology_live**](DomainAnalyticsApi.md#technologies_domains_by_technology_live) | **POST** /v3/domain_analytics/technologies/domains_by_technology/live | 
[**technologies_technologies**](DomainAnalyticsApi.md#technologies_technologies) | **GET** /v3/domain_analytics/technologies/technologies | 
[**technologies_technologies_summary_live**](DomainAnalyticsApi.md#technologies_technologies_summary_live) | **POST** /v3/domain_analytics/technologies/technologies_summary/live | 
[**technologies_technology_stats_live**](DomainAnalyticsApi.md#technologies_technology_stats_live) | **POST** /v3/domain_analytics/technologies/technology_stats/live | 
[**whois_available_filters**](DomainAnalyticsApi.md#whois_available_filters) | **GET** /v3/domain_analytics/whois/available_filters | 
[**whois_overview_live**](DomainAnalyticsApi.md#whois_overview_live) | **POST** /v3/domain_analytics/whois/overview/live | 


# **domain_analytics_errors**
> DomainAnalyticsErrorsResponseInfo domain_analytics_errors(domain_analytics_errors_request_info=domain_analytics_errors_request_info)



By calling this endpoint you will receive information about the Domain Analytics API tasks that returned an error within the past 7 days. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/errors/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_errors_request_info import DomainAnalyticsErrorsRequestInfo
from dataforseo_client.models.domain_analytics_errors_response_info import DomainAnalyticsErrorsResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)
    domain_analytics_errors_request_info = [dataforseo_client.DomainAnalyticsErrorsRequestInfo()] # List[DomainAnalyticsErrorsRequestInfo] |  (optional)

    try:
        api_response = api_instance.domain_analytics_errors(domain_analytics_errors_request_info=domain_analytics_errors_request_info)
        print("The response of DomainAnalyticsApi->domain_analytics_errors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->domain_analytics_errors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_analytics_errors_request_info** | [**List[DomainAnalyticsErrorsRequestInfo]**](DomainAnalyticsErrorsRequestInfo.md)|  | [optional] 

### Return type

[**DomainAnalyticsErrorsResponseInfo**](DomainAnalyticsErrorsResponseInfo.md)

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

# **domain_analytics_id_list**
> DomainAnalyticsIdListResponseInfo domain_analytics_id_list(domain_analytics_id_list_request_info=domain_analytics_id_list_request_info)



This endpoint is designed to provide you with the list of IDs and metadata of the completed Domain Analytics tasks during the specified period. You will get all task IDs that were made including successful, uncompleted, and tasks that responded as errors. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/id_list/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_id_list_request_info import DomainAnalyticsIdListRequestInfo
from dataforseo_client.models.domain_analytics_id_list_response_info import DomainAnalyticsIdListResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)
    domain_analytics_id_list_request_info = [dataforseo_client.DomainAnalyticsIdListRequestInfo()] # List[DomainAnalyticsIdListRequestInfo] |  (optional)

    try:
        api_response = api_instance.domain_analytics_id_list(domain_analytics_id_list_request_info=domain_analytics_id_list_request_info)
        print("The response of DomainAnalyticsApi->domain_analytics_id_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->domain_analytics_id_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_analytics_id_list_request_info** | [**List[DomainAnalyticsIdListRequestInfo]**](DomainAnalyticsIdListRequestInfo.md)|  | [optional] 

### Return type

[**DomainAnalyticsIdListResponseInfo**](DomainAnalyticsIdListResponseInfo.md)

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

# **domain_analytics_technologies_languages**
> DomainAnalyticsTechnologiesLanguagesResponseInfo domain_analytics_technologies_languages()



You will receive the list of languages by calling this API.   As a response of the API server, you will receive JSON-encoded data containing a tasks array with the information specific to the set tasks. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/technologies/languages/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_technologies_languages_response_info import DomainAnalyticsTechnologiesLanguagesResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)

    try:
        api_response = api_instance.domain_analytics_technologies_languages()
        print("The response of DomainAnalyticsApi->domain_analytics_technologies_languages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->domain_analytics_technologies_languages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainAnalyticsTechnologiesLanguagesResponseInfo**](DomainAnalyticsTechnologiesLanguagesResponseInfo.md)

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

# **domain_analytics_technologies_locations**
> DomainAnalyticsTechnologiesLocationsResponseInfo domain_analytics_technologies_locations()



You will receive the list of locations by this API call. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/technologies/locations/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_technologies_locations_response_info import DomainAnalyticsTechnologiesLocationsResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)

    try:
        api_response = api_instance.domain_analytics_technologies_locations()
        print("The response of DomainAnalyticsApi->domain_analytics_technologies_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->domain_analytics_technologies_locations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainAnalyticsTechnologiesLocationsResponseInfo**](DomainAnalyticsTechnologiesLocationsResponseInfo.md)

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

# **technologies_aggregation_technologies_live**
> DomainAnalyticsTechnologiesAggregationTechnologiesLiveResponseInfo technologies_aggregation_technologies_live(domain_analytics_technologies_aggregation_technologies_live_request_info=domain_analytics_technologies_aggregation_technologies_live_request_info)



‌‌ The Aggregation Technologies endpoint will provide you with a list of the most popular technologies websites use alongside the technologies you specify. Alternatively, you can specify technology categories or groups to obtain wider stats. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/technologies/aggregation_technologies/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_technologies_aggregation_technologies_live_request_info import DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo
from dataforseo_client.models.domain_analytics_technologies_aggregation_technologies_live_response_info import DomainAnalyticsTechnologiesAggregationTechnologiesLiveResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)
    domain_analytics_technologies_aggregation_technologies_live_request_info = [dataforseo_client.DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo()] # List[DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.technologies_aggregation_technologies_live(domain_analytics_technologies_aggregation_technologies_live_request_info=domain_analytics_technologies_aggregation_technologies_live_request_info)
        print("The response of DomainAnalyticsApi->technologies_aggregation_technologies_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->technologies_aggregation_technologies_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_analytics_technologies_aggregation_technologies_live_request_info** | [**List[DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo]**](DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo.md)|  | [optional] 

### Return type

[**DomainAnalyticsTechnologiesAggregationTechnologiesLiveResponseInfo**](DomainAnalyticsTechnologiesAggregationTechnologiesLiveResponseInfo.md)

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

# **technologies_available_filters**
> DomainAnalyticsTechnologiesAvailableFiltersResponseInfo technologies_available_filters()



‌‌ Here you will find all the necessary information about filters that can be used with Domain Analytics Technologies API endpoints. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/technologies/filters/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_technologies_available_filters_response_info import DomainAnalyticsTechnologiesAvailableFiltersResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)

    try:
        api_response = api_instance.technologies_available_filters()
        print("The response of DomainAnalyticsApi->technologies_available_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->technologies_available_filters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainAnalyticsTechnologiesAvailableFiltersResponseInfo**](DomainAnalyticsTechnologiesAvailableFiltersResponseInfo.md)

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

# **technologies_domain_technologies_live**
> DomainAnalyticsTechnologiesDomainTechnologiesLiveResponseInfo technologies_domain_technologies_live(domain_analytics_technologies_domain_technologies_live_request_info=domain_analytics_technologies_domain_technologies_live_request_info)



‌‌ Using this endpoint you will get a list of technologies used in a particular domain. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/technologies/domain_technologies/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_technologies_domain_technologies_live_request_info import DomainAnalyticsTechnologiesDomainTechnologiesLiveRequestInfo
from dataforseo_client.models.domain_analytics_technologies_domain_technologies_live_response_info import DomainAnalyticsTechnologiesDomainTechnologiesLiveResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)
    domain_analytics_technologies_domain_technologies_live_request_info = [dataforseo_client.DomainAnalyticsTechnologiesDomainTechnologiesLiveRequestInfo()] # List[DomainAnalyticsTechnologiesDomainTechnologiesLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.technologies_domain_technologies_live(domain_analytics_technologies_domain_technologies_live_request_info=domain_analytics_technologies_domain_technologies_live_request_info)
        print("The response of DomainAnalyticsApi->technologies_domain_technologies_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->technologies_domain_technologies_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_analytics_technologies_domain_technologies_live_request_info** | [**List[DomainAnalyticsTechnologiesDomainTechnologiesLiveRequestInfo]**](DomainAnalyticsTechnologiesDomainTechnologiesLiveRequestInfo.md)|  | [optional] 

### Return type

[**DomainAnalyticsTechnologiesDomainTechnologiesLiveResponseInfo**](DomainAnalyticsTechnologiesDomainTechnologiesLiveResponseInfo.md)

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

# **technologies_domains_by_html_terms_live**
> DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveResponseInfo technologies_domains_by_html_terms_live(domain_analytics_technologies_domains_by_html_terms_live_request_info=domain_analytics_technologies_domains_by_html_terms_live_request_info)



‌‌ This endpoint provides domains based on the HTML terms they use on their homepage. In addition to the list of domains, you will also get their technology profiles, the country and language they belong to, and other related data. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/technologies/domains_by_html_terms/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_technologies_domains_by_html_terms_live_request_info import DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo
from dataforseo_client.models.domain_analytics_technologies_domains_by_html_terms_live_response_info import DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)
    domain_analytics_technologies_domains_by_html_terms_live_request_info = [dataforseo_client.DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo()] # List[DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.technologies_domains_by_html_terms_live(domain_analytics_technologies_domains_by_html_terms_live_request_info=domain_analytics_technologies_domains_by_html_terms_live_request_info)
        print("The response of DomainAnalyticsApi->technologies_domains_by_html_terms_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->technologies_domains_by_html_terms_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_analytics_technologies_domains_by_html_terms_live_request_info** | [**List[DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo]**](DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo.md)|  | [optional] 

### Return type

[**DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveResponseInfo**](DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveResponseInfo.md)

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

# **technologies_domains_by_technology_live**
> DomainAnalyticsTechnologiesDomainsByTechnologyLiveResponseInfo technologies_domains_by_technology_live(domain_analytics_technologies_domains_by_technology_live_request_info=domain_analytics_technologies_domains_by_technology_live_request_info)



‌‌ This endpoint provides domains based on the technology they use. In addition to the list of domains, you will also get their technology profiles, the country and language they belong to, and other related data. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/technologies/domains_by_technology/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_technologies_domains_by_technology_live_request_info import DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo
from dataforseo_client.models.domain_analytics_technologies_domains_by_technology_live_response_info import DomainAnalyticsTechnologiesDomainsByTechnologyLiveResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)
    domain_analytics_technologies_domains_by_technology_live_request_info = [dataforseo_client.DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo()] # List[DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.technologies_domains_by_technology_live(domain_analytics_technologies_domains_by_technology_live_request_info=domain_analytics_technologies_domains_by_technology_live_request_info)
        print("The response of DomainAnalyticsApi->technologies_domains_by_technology_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->technologies_domains_by_technology_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_analytics_technologies_domains_by_technology_live_request_info** | [**List[DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo]**](DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo.md)|  | [optional] 

### Return type

[**DomainAnalyticsTechnologiesDomainsByTechnologyLiveResponseInfo**](DomainAnalyticsTechnologiesDomainsByTechnologyLiveResponseInfo.md)

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

# **technologies_technologies**
> DomainAnalyticsTechnologiesTechnologiesResponseInfo technologies_technologies()



This endpoint will provide you with the full list of available technologies structured by technology groups and categories each particular technology belongs to. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/technologies/technologies/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_technologies_technologies_response_info import DomainAnalyticsTechnologiesTechnologiesResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)

    try:
        api_response = api_instance.technologies_technologies()
        print("The response of DomainAnalyticsApi->technologies_technologies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->technologies_technologies: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainAnalyticsTechnologiesTechnologiesResponseInfo**](DomainAnalyticsTechnologiesTechnologiesResponseInfo.md)

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

# **technologies_technologies_summary_live**
> DomainAnalyticsTechnologiesTechnologiesSummaryLiveResponseInfo technologies_technologies_summary_live(domain_analytics_technologies_technologies_summary_live_request_info=domain_analytics_technologies_technologies_summary_live_request_info)



‌‌ The Technologies Summary endpoint will provide you with the number of domains across different countries and languages that use the specified technology names, technology groups, or technology categories. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/technologies/technologies_summary/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_technologies_technologies_summary_live_request_info import DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo
from dataforseo_client.models.domain_analytics_technologies_technologies_summary_live_response_info import DomainAnalyticsTechnologiesTechnologiesSummaryLiveResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)
    domain_analytics_technologies_technologies_summary_live_request_info = [dataforseo_client.DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo()] # List[DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.technologies_technologies_summary_live(domain_analytics_technologies_technologies_summary_live_request_info=domain_analytics_technologies_technologies_summary_live_request_info)
        print("The response of DomainAnalyticsApi->technologies_technologies_summary_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->technologies_technologies_summary_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_analytics_technologies_technologies_summary_live_request_info** | [**List[DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo]**](DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo.md)|  | [optional] 

### Return type

[**DomainAnalyticsTechnologiesTechnologiesSummaryLiveResponseInfo**](DomainAnalyticsTechnologiesTechnologiesSummaryLiveResponseInfo.md)

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

# **technologies_technology_stats_live**
> DomainAnalyticsTechnologiesTechnologyStatsLiveResponseInfo technologies_technology_stats_live(domain_analytics_technologies_technology_stats_live_request_info=domain_analytics_technologies_technology_stats_live_request_info)



‌‌ The Technology Stats endpoint will provide you with historical data on the number of domains across different countries and languages that use the specified technology. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/technologies/technology_stats/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_technologies_technology_stats_live_request_info import DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo
from dataforseo_client.models.domain_analytics_technologies_technology_stats_live_response_info import DomainAnalyticsTechnologiesTechnologyStatsLiveResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)
    domain_analytics_technologies_technology_stats_live_request_info = [dataforseo_client.DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo()] # List[DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.technologies_technology_stats_live(domain_analytics_technologies_technology_stats_live_request_info=domain_analytics_technologies_technology_stats_live_request_info)
        print("The response of DomainAnalyticsApi->technologies_technology_stats_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->technologies_technology_stats_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_analytics_technologies_technology_stats_live_request_info** | [**List[DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo]**](DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo.md)|  | [optional] 

### Return type

[**DomainAnalyticsTechnologiesTechnologyStatsLiveResponseInfo**](DomainAnalyticsTechnologiesTechnologyStatsLiveResponseInfo.md)

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

# **whois_available_filters**
> DomainAnalyticsWhoisAvailableFiltersResponseInfo whois_available_filters()



‌‌ Here you will find all the necessary information about filters that can be used with Domain Analytics Whois API. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/whois/filters/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_whois_available_filters_response_info import DomainAnalyticsWhoisAvailableFiltersResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)

    try:
        api_response = api_instance.whois_available_filters()
        print("The response of DomainAnalyticsApi->whois_available_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->whois_available_filters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DomainAnalyticsWhoisAvailableFiltersResponseInfo**](DomainAnalyticsWhoisAvailableFiltersResponseInfo.md)

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

# **whois_overview_live**
> DomainAnalyticsWhoisOverviewLiveResponseInfo whois_overview_live(domain_analytics_whois_overview_live_request_info=domain_analytics_whois_overview_live_request_info)



‌ This endpoint will provide you with Whois data enriched with backlink stats, and ranking and traffic info from organic and paid search results. Using this endpoint you will be able to get all these data for the domains matching the parameters you specify in the request. for more info please visit 'https://docs.dataforseo.com/v3/domain_analytics/whois/overview/live/?bash'

### Example

* Basic Authentication (basicAuth):

```python
import dataforseo_client
from dataforseo_client.models.domain_analytics_whois_overview_live_request_info import DomainAnalyticsWhoisOverviewLiveRequestInfo
from dataforseo_client.models.domain_analytics_whois_overview_live_response_info import DomainAnalyticsWhoisOverviewLiveResponseInfo
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
    api_instance = dataforseo_client.DomainAnalyticsApi(api_client)
    domain_analytics_whois_overview_live_request_info = [dataforseo_client.DomainAnalyticsWhoisOverviewLiveRequestInfo()] # List[DomainAnalyticsWhoisOverviewLiveRequestInfo] |  (optional)

    try:
        api_response = api_instance.whois_overview_live(domain_analytics_whois_overview_live_request_info=domain_analytics_whois_overview_live_request_info)
        print("The response of DomainAnalyticsApi->whois_overview_live:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainAnalyticsApi->whois_overview_live: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_analytics_whois_overview_live_request_info** | [**List[DomainAnalyticsWhoisOverviewLiveRequestInfo]**](DomainAnalyticsWhoisOverviewLiveRequestInfo.md)|  | [optional] 

### Return type

[**DomainAnalyticsWhoisOverviewLiveResponseInfo**](DomainAnalyticsWhoisOverviewLiveResponseInfo.md)

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

