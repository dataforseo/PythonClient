# BacklinksApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**backlinksIdList**](BacklinksApi.md#backlinksIdList) | **POST**  /v3/backlinks/id_list  |
[**backlinksErrors**](BacklinksApi.md#backlinksErrors) | **POST**  /v3/backlinks/errors  |
[**backlinksAvailableFilters**](BacklinksApi.md#backlinksAvailableFilters) | **GET**  /v3/backlinks/available_filters  |
[**index**](BacklinksApi.md#index) | **GET**  /v3/backlinks/index  |
[**summaryLive**](BacklinksApi.md#summaryLive) | **POST**  /v3/backlinks/summary/live  |
[**historyLive**](BacklinksApi.md#historyLive) | **POST**  /v3/backlinks/history/live  |
[**backlinksLive**](BacklinksApi.md#backlinksLive) | **POST**  /v3/backlinks/backlinks/live  |
[**anchorsLive**](BacklinksApi.md#anchorsLive) | **POST**  /v3/backlinks/anchors/live  |
[**domainPagesLive**](BacklinksApi.md#domainPagesLive) | **POST**  /v3/backlinks/domain_pages/live  |
[**domainPagesSummaryLive**](BacklinksApi.md#domainPagesSummaryLive) | **POST**  /v3/backlinks/domain_pages_summary/live  |
[**referringDomainsLive**](BacklinksApi.md#referringDomainsLive) | **POST**  /v3/backlinks/referring_domains/live  |
[**referringNetworksLive**](BacklinksApi.md#referringNetworksLive) | **POST**  /v3/backlinks/referring_networks/live  |
[**competitorsLive**](BacklinksApi.md#competitorsLive) | **POST**  /v3/backlinks/competitors/live  |
[**domainIntersectionLive**](BacklinksApi.md#domainIntersectionLive) | **POST**  /v3/backlinks/domain_intersection/live  |
[**pageIntersectionLive**](BacklinksApi.md#pageIntersectionLive) | **POST**  /v3/backlinks/page_intersection/live  |
[**timeseriesSummaryLive**](BacklinksApi.md#timeseriesSummaryLive) | **POST**  /v3/backlinks/timeseries_summary/live  |
[**timeseriesNewLostSummaryLive**](BacklinksApi.md#timeseriesNewLostSummaryLive) | **POST**  /v3/backlinks/timeseries_new_lost_summary/live  |
[**bulkRanksLive**](BacklinksApi.md#bulkRanksLive) | **POST**  /v3/backlinks/bulk_ranks/live  |
[**bulkBacklinksLive**](BacklinksApi.md#bulkBacklinksLive) | **POST**  /v3/backlinks/bulk_backlinks/live  |
[**bulkSpamScoreLive**](BacklinksApi.md#bulkSpamScoreLive) | **POST**  /v3/backlinks/bulk_spam_score/live  |
[**bulkReferringDomainsLive**](BacklinksApi.md#bulkReferringDomainsLive) | **POST**  /v3/backlinks/bulk_referring_domains/live  |
[**bulkNewLostBacklinksLive**](BacklinksApi.md#bulkNewLostBacklinksLive) | **POST**  /v3/backlinks/bulk_new_lost_backlinks/live  |
[**bulkNewLostReferringDomainsLive**](BacklinksApi.md#bulkNewLostReferringDomainsLive) | **POST**  /v3/backlinks/bulk_new_lost_referring_domains/live  |
[**bulkPagesSummaryLive**](BacklinksApi.md#bulkPagesSummaryLive) | **POST**  /v3/backlinks/bulk_pages_summary/live  |

<a id="backlinksIdList"></a>
# **backlinksIdList**
> BacklinksIdListResponseInfo backlinksIdList()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_id_list_request_info import List[Optional[BacklinksIdListRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.backlinks_id_list([BacklinksIdListRequestInfo(
                datetime_from="2025-01-18 03:39:12 +00:00",
                datetime_to="2025-03-18 03:39:12 +00:00",
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
    | **** | [**List&lt;List[Optional[BacklinksIdListRequestInfo]]&gt;**](List[Optional[BacklinksIdListRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="backlinksErrors"></a>
# **backlinksErrors**
> BacklinksErrorsResponseInfo backlinksErrors()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_errors_request_info import List[Optional[BacklinksErrorsRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.backlinks_errors([BacklinksErrorsRequestInfo(
                limit=10,
                offset=0,
                filtered_function="backlinks/content_duplicates",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksErrorsRequestInfo]]&gt;**](List[Optional[BacklinksErrorsRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="backlinksAvailableFilters"></a>
# **backlinksAvailableFilters**
> BacklinksAvailableFiltersResponseInfo backlinksAvailableFilters()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.backlinks_available_filters()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BacklinksAvailableFiltersResponseInfo**](BacklinksAvailableFiltersResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="index"></a>
# **index**
> BacklinksIndexResponseInfo index()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.index()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**BacklinksIndexResponseInfo**](BacklinksIndexResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="summaryLive"></a>
# **summaryLive**
> BacklinksSummaryLiveResponseInfo summaryLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_summary_live_request_info import List[Optional[BacklinksSummaryLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.summary_live([BacklinksSummaryLiveRequestInfo(
                target="explodingtopics.com",
                include_subdomains=True,
                internal_list_limit=10,
                backlinks_status_type="all",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksSummaryLiveRequestInfo]]&gt;**](List[Optional[BacklinksSummaryLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="historyLive"></a>
# **historyLive**
> BacklinksHistoryLiveResponseInfo historyLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_history_live_request_info import List[Optional[BacklinksHistoryLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.history_live([BacklinksHistoryLiveRequestInfo(
                target="cnn.com",
                date_from="2020-01-01",
                date_to="2021-01-01",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksHistoryLiveRequestInfo]]&gt;**](List[Optional[BacklinksHistoryLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="backlinksLive"></a>
# **backlinksLive**
> BacklinksBacklinksLiveResponseInfo backlinksLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_backlinks_live_request_info import List[Optional[BacklinksBacklinksLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.backlinks_live([BacklinksBacklinksLiveRequestInfo(
                target="forbes.com",
                mode="as_is",
                limit=5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksBacklinksLiveRequestInfo]]&gt;**](List[Optional[BacklinksBacklinksLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="anchorsLive"></a>
# **anchorsLive**
> BacklinksAnchorsLiveResponseInfo anchorsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_anchors_live_request_info import List[Optional[BacklinksAnchorsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.anchors_live([BacklinksAnchorsLiveRequestInfo(
                target="forbes.com",
                limit=4,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksAnchorsLiveRequestInfo]]&gt;**](List[Optional[BacklinksAnchorsLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="domainPagesLive"></a>
# **domainPagesLive**
> BacklinksDomainPagesLiveResponseInfo domainPagesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_domain_pages_live_request_info import List[Optional[BacklinksDomainPagesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.domain_pages_live([BacklinksDomainPagesLiveRequestInfo(
                target="forbes.com",
                limit=5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksDomainPagesLiveRequestInfo]]&gt;**](List[Optional[BacklinksDomainPagesLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="domainPagesSummaryLive"></a>
# **domainPagesSummaryLive**
> BacklinksDomainPagesSummaryLiveResponseInfo domainPagesSummaryLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_domain_pages_summary_live_request_info import List[Optional[BacklinksDomainPagesSummaryLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.domain_pages_summary_live([BacklinksDomainPagesSummaryLiveRequestInfo(
                target="forbes.com",
                limit=4,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksDomainPagesSummaryLiveRequestInfo]]&gt;**](List[Optional[BacklinksDomainPagesSummaryLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="referringDomainsLive"></a>
# **referringDomainsLive**
> BacklinksReferringDomainsLiveResponseInfo referringDomainsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_referring_domains_live_request_info import List[Optional[BacklinksReferringDomainsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.referring_domains_live([BacklinksReferringDomainsLiveRequestInfo(
                target="backlinko.com",
                limit=5,
                exclude_internal_backlinks=True,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksReferringDomainsLiveRequestInfo]]&gt;**](List[Optional[BacklinksReferringDomainsLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="referringNetworksLive"></a>
# **referringNetworksLive**
> BacklinksReferringNetworksLiveResponseInfo referringNetworksLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_referring_networks_live_request_info import List[Optional[BacklinksReferringNetworksLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.referring_networks_live([BacklinksReferringNetworksLiveRequestInfo(
                target="backlinko.com",
                network_address_type="subnet",
                limit=5,
                exclude_internal_backlinks=True,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksReferringNetworksLiveRequestInfo]]&gt;**](List[Optional[BacklinksReferringNetworksLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="competitorsLive"></a>
# **competitorsLive**
> BacklinksCompetitorsLiveResponseInfo competitorsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_competitors_live_request_info import List[Optional[BacklinksCompetitorsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.competitors_live([BacklinksCompetitorsLiveRequestInfo(
                target="dataforseo.com",
                limit=5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksCompetitorsLiveRequestInfo]]&gt;**](List[Optional[BacklinksCompetitorsLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="domainIntersectionLive"></a>
# **domainIntersectionLive**
> BacklinksDomainIntersectionLiveResponseInfo domainIntersectionLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_domain_intersection_live_request_info import List[Optional[BacklinksDomainIntersectionLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.domain_intersection_live([BacklinksDomainIntersectionLiveRequestInfo(
                targets={
                        "1": "moz.com",
                        "2": "ahrefs.com",
                    },
                exclude_targets=[
                        "semrush.com",
                    ],
                limit=5,
                include_subdomains=False,
                exclude_internal_backlinks=True,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksDomainIntersectionLiveRequestInfo]]&gt;**](List[Optional[BacklinksDomainIntersectionLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="pageIntersectionLive"></a>
# **pageIntersectionLive**
> BacklinksPageIntersectionLiveResponseInfo pageIntersectionLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_page_intersection_live_request_info import List[Optional[BacklinksPageIntersectionLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.page_intersection_live([BacklinksPageIntersectionLiveRequestInfo(
                targets={
                        "1": "football.com",
                        "2": "fifa.com",
                    },
                exclude_targets=[
                        "skysports.com",
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
    | **** | [**List&lt;List[Optional[BacklinksPageIntersectionLiveRequestInfo]]&gt;**](List[Optional[BacklinksPageIntersectionLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="timeseriesSummaryLive"></a>
# **timeseriesSummaryLive**
> BacklinksTimeseriesSummaryLiveResponseInfo timeseriesSummaryLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_timeseries_summary_live_request_info import List[Optional[BacklinksTimeseriesSummaryLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.timeseries_summary_live([BacklinksTimeseriesSummaryLiveRequestInfo(
                target="dataforseo.com",
                date_from="2021-12-01",
                date_to="2022-02-01",
                group_range="month",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksTimeseriesSummaryLiveRequestInfo]]&gt;**](List[Optional[BacklinksTimeseriesSummaryLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="timeseriesNewLostSummaryLive"></a>
# **timeseriesNewLostSummaryLive**
> BacklinksTimeseriesNewLostSummaryLiveResponseInfo timeseriesNewLostSummaryLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_timeseries_new_lost_summary_live_request_info import List[Optional[BacklinksTimeseriesNewLostSummaryLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.timeseries_new_lost_summary_live([BacklinksTimeseriesNewLostSummaryLiveRequestInfo(
                target="dataforseo.com",
                date_from="2021-12-01",
                date_to="2022-02-01",
                group_range="month",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksTimeseriesNewLostSummaryLiveRequestInfo]]&gt;**](List[Optional[BacklinksTimeseriesNewLostSummaryLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="bulkRanksLive"></a>
# **bulkRanksLive**
> BacklinksBulkRanksLiveResponseInfo bulkRanksLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_bulk_ranks_live_request_info import List[Optional[BacklinksBulkRanksLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.bulk_ranks_live([BacklinksBulkRanksLiveRequestInfo(
                targets=[
                        "forbes.com",
                        "cnn.com",
                        "bbc.com",
                        "yelp.com",
                        "https://www.apple.com/iphone/",
                        "https://ahrefs.com/blog/",
                        "ibm.com",
                        "https://variety.com/",
                        "https://stackoverflow.com/",
                        "www.trustpilot.com",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksBulkRanksLiveRequestInfo]]&gt;**](List[Optional[BacklinksBulkRanksLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="bulkBacklinksLive"></a>
# **bulkBacklinksLive**
> BacklinksBulkBacklinksLiveResponseInfo bulkBacklinksLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_bulk_backlinks_live_request_info import List[Optional[BacklinksBulkBacklinksLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.bulk_backlinks_live([BacklinksBulkBacklinksLiveRequestInfo(
                targets=[
                        "forbes.com",
                        "cnn.com",
                        "bbc.com",
                        "yelp.com",
                        "https://www.apple.com/iphone/",
                        "https://ahrefs.com/blog/",
                        "ibm.com",
                        "https://variety.com/",
                        "https://stackoverflow.com/",
                        "www.trustpilot.com",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksBulkBacklinksLiveRequestInfo]]&gt;**](List[Optional[BacklinksBulkBacklinksLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="bulkSpamScoreLive"></a>
# **bulkSpamScoreLive**
> BacklinksBulkSpamScoreLiveResponseInfo bulkSpamScoreLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_bulk_spam_score_live_request_info import List[Optional[BacklinksBulkSpamScoreLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.bulk_spam_score_live([BacklinksBulkSpamScoreLiveRequestInfo(
                targets=[
                        "forbes.com",
                        "cnn.com",
                        "bbc.com",
                        "yelp.com",
                        "https://www.apple.com/iphone/",
                        "https://ahrefs.com/blog/",
                        "ibm.com",
                        "https://variety.com/",
                        "https://stackoverflow.com/",
                        "www.trustpilot.com",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksBulkSpamScoreLiveRequestInfo]]&gt;**](List[Optional[BacklinksBulkSpamScoreLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="bulkReferringDomainsLive"></a>
# **bulkReferringDomainsLive**
> BacklinksBulkReferringDomainsLiveResponseInfo bulkReferringDomainsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_bulk_referring_domains_live_request_info import List[Optional[BacklinksBulkReferringDomainsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.bulk_referring_domains_live([BacklinksBulkReferringDomainsLiveRequestInfo(
                targets=[
                        "forbes.com",
                        "cnn.com",
                        "bbc.com",
                        "yelp.com",
                        "https://www.apple.com/iphone/",
                        "https://ahrefs.com/blog/",
                        "ibm.com",
                        "https://variety.com/",
                        "https://stackoverflow.com/",
                        "www.trustpilot.com",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksBulkReferringDomainsLiveRequestInfo]]&gt;**](List[Optional[BacklinksBulkReferringDomainsLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="bulkNewLostBacklinksLive"></a>
# **bulkNewLostBacklinksLive**
> BacklinksBulkNewLostBacklinksLiveResponseInfo bulkNewLostBacklinksLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_bulk_new_lost_backlinks_live_request_info import List[Optional[BacklinksBulkNewLostBacklinksLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.bulk_new_lost_backlinks_live([BacklinksBulkNewLostBacklinksLiveRequestInfo(
                targets=[
                        "forbes.com",
                        "cnn.com",
                        "bbc.com",
                        "yelp.com",
                        "https://www.apple.com/iphone/",
                        "https://ahrefs.com/blog/",
                        "ibm.com",
                        "https://variety.com/",
                        "https://stackoverflow.com/",
                        "www.trustpilot.com",
                    ],
                date_from="2021-01-01",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksBulkNewLostBacklinksLiveRequestInfo]]&gt;**](List[Optional[BacklinksBulkNewLostBacklinksLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="bulkNewLostReferringDomainsLive"></a>
# **bulkNewLostReferringDomainsLive**
> BacklinksBulkNewLostReferringDomainsLiveResponseInfo bulkNewLostReferringDomainsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_bulk_new_lost_referring_domains_live_request_info import List[Optional[BacklinksBulkNewLostReferringDomainsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.bulk_new_lost_referring_domains_live([BacklinksBulkNewLostReferringDomainsLiveRequestInfo(
                targets=[
                        "forbes.com",
                        "cnn.com",
                        "bbc.com",
                        "yelp.com",
                        "https://www.apple.com/iphone/",
                        "https://ahrefs.com/blog/",
                        "ibm.com",
                        "https://variety.com/",
                        "https://stackoverflow.com/",
                        "www.trustpilot.com",
                    ],
                date_from="2023-09-01",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksBulkNewLostReferringDomainsLiveRequestInfo]]&gt;**](List[Optional[BacklinksBulkNewLostReferringDomainsLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="bulkPagesSummaryLive"></a>
# **bulkPagesSummaryLive**
> BacklinksBulkPagesSummaryLiveResponseInfo bulkPagesSummaryLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_backlinks_bulk_pages_summary_live_request_info import List[Optional[BacklinksBulkPagesSummaryLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        backlinks_api = BacklinksApi(api_client)

        response = backlinks_api.bulk_pages_summary_live([BacklinksBulkPagesSummaryLiveRequestInfo(
                targets=[
                        "https://dataforseo.com/solutions",
                        "https://dataforseo.com/about-us",
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[BacklinksBulkPagesSummaryLiveRequestInfo]]&gt;**](List[Optional[BacklinksBulkPagesSummaryLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |