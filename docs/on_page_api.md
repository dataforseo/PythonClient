# OnPageApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**onPageIdList**](OnPageApi.md#onPageIdList) | **POST**  /v3/on_page/id_list  |
[**onPageErrors**](OnPageApi.md#onPageErrors) | **POST**  /v3/on_page/errors  |
[**forceStop**](OnPageApi.md#forceStop) | **POST**  /v3/on_page/force_stop  |
[**onPageAvailableFilters**](OnPageApi.md#onPageAvailableFilters) | **GET**  /v3/on_page/available_filters  |
[**taskPost**](OnPageApi.md#taskPost) | **POST**  /v3/on_page/task_post  |
[**onPageTasksReady**](OnPageApi.md#onPageTasksReady) | **GET**  /v3/on_page/tasks_ready  |
[**summary**](OnPageApi.md#summary) | **GET**  /v3/on_page/summary/{id}  |
[**pages**](OnPageApi.md#pages) | **POST**  /v3/on_page/pages  |
[**pagesByResource**](OnPageApi.md#pagesByResource) | **POST**  /v3/on_page/pages_by_resource  |
[**resources**](OnPageApi.md#resources) | **POST**  /v3/on_page/resources  |
[**duplicateTags**](OnPageApi.md#duplicateTags) | **POST**  /v3/on_page/duplicate_tags  |
[**duplicateContent**](OnPageApi.md#duplicateContent) | **POST**  /v3/on_page/duplicate_content  |
[**links**](OnPageApi.md#links) | **POST**  /v3/on_page/links  |
[**redirectChains**](OnPageApi.md#redirectChains) | **POST**  /v3/on_page/redirect_chains  |
[**nonIndexable**](OnPageApi.md#nonIndexable) | **POST**  /v3/on_page/non_indexable  |
[**waterfall**](OnPageApi.md#waterfall) | **POST**  /v3/on_page/waterfall  |
[**keywordDensity**](OnPageApi.md#keywordDensity) | **POST**  /v3/on_page/keyword_density  |
[**microdata**](OnPageApi.md#microdata) | **POST**  /v3/on_page/microdata  |
[**rawHtml**](OnPageApi.md#rawHtml) | **POST**  /v3/on_page/raw_html  |
[**pageScreenshot**](OnPageApi.md#pageScreenshot) | **POST**  /v3/on_page/page_screenshot  |
[**contentParsing**](OnPageApi.md#contentParsing) | **POST**  /v3/on_page/content_parsing  |
[**contentParsingLive**](OnPageApi.md#contentParsingLive) | **POST**  /v3/on_page/content_parsing/live  |
[**instantPages**](OnPageApi.md#instantPages) | **POST**  /v3/on_page/instant_pages  |
[**onPageLighthouseLanguages**](OnPageApi.md#onPageLighthouseLanguages) | **GET**  /v3/on_page/lighthouse/languages  |
[**lighthouseAudits**](OnPageApi.md#lighthouseAudits) | **GET**  /v3/on_page/lighthouse/audits  |
[**lighthouseVersions**](OnPageApi.md#lighthouseVersions) | **GET**  /v3/on_page/lighthouse/versions  |
[**lighthouseTaskPost**](OnPageApi.md#lighthouseTaskPost) | **POST**  /v3/on_page/lighthouse/task_post  |
[**lighthouseTasksReady**](OnPageApi.md#lighthouseTasksReady) | **GET**  /v3/on_page/lighthouse/tasks_ready  |
[**lighthouseTaskGetJson**](OnPageApi.md#lighthouseTaskGetJson) | **GET**  /v3/on_page/lighthouse/task_get/json/{id}  |
[**lighthouseLiveJson**](OnPageApi.md#lighthouseLiveJson) | **POST**  /v3/on_page/lighthouse/live/json  |

<a id="onPageIdList"></a>
# **onPageIdList**
> OnPageIdListResponseInfo onPageIdList()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_id_list_request_info import List[Optional[OnPageIdListRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.on_page_id_list([OnPageIdListRequestInfo(
                datetime_from="2025-08-22 08:09:28 +00:00",
                datetime_to="2025-10-22 08:09:28 +00:00",
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
    | **** | [**List&lt;List[Optional[OnPageIdListRequestInfo]]&gt;**](List[Optional[OnPageIdListRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="onPageErrors"></a>
# **onPageErrors**
> OnPageErrorsResponseInfo onPageErrors()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_errors_request_info import List[Optional[OnPageErrorsRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.on_page_errors([OnPageErrorsRequestInfo(
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
    | **** | [**List&lt;List[Optional[OnPageErrorsRequestInfo]]&gt;**](List[Optional[OnPageErrorsRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="forceStop"></a>
# **forceStop**
> OnPageForceStopResponseInfo forceStop()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_force_stop_request_info import List[Optional[OnPageForceStopRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.force_stop([OnPageForceStopRequestInfo(
                id="08121600-1535-0216-0000-37b4c7a34453",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageForceStopRequestInfo]]&gt;**](List[Optional[OnPageForceStopRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="onPageAvailableFilters"></a>
# **onPageAvailableFilters**
> OnPageAvailableFiltersResponseInfo onPageAvailableFilters()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.on_page_available_filters()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**OnPageAvailableFiltersResponseInfo**](OnPageAvailableFiltersResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="taskPost"></a>
# **taskPost**
> OnPageTaskPostResponseInfo taskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_task_post_request_info import List[Optional[OnPageTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.task_post([OnPageTaskPostRequestInfo(
                target="dataforseo.com",
                max_crawl_pages=10,
                load_resources=True,
                enable_javascript=True,
                custom_js="meta = {}; meta.url = document.URL; meta;",
                tag="some_string_123",
                pingback_url="https://your-server.com/pingscript?id=$id&tag=$tag",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageTaskPostRequestInfo]]&gt;**](List[Optional[OnPageTaskPostRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="onPageTasksReady"></a>
# **onPageTasksReady**
> OnPageTasksReadyResponseInfo onPageTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.on_page_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**OnPageTasksReadyResponseInfo**](OnPageTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="summary"></a>
# **summary**
> OnPageSummaryResponseInfo summary()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = on_page_api.summary(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**OnPageSummaryResponseInfo**](OnPageSummaryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="pages"></a>
# **pages**
> OnPagePagesResponseInfo pages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_pages_request_info import List[Optional[OnPagePagesRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.pages([OnPagePagesRequestInfo(
                id="07281559-0695-0216-0000-c269be8b7592",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPagePagesRequestInfo]]&gt;**](List[Optional[OnPagePagesRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="pagesByResource"></a>
# **pagesByResource**
> OnPagePagesByResourceResponseInfo pagesByResource()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_pages_by_resource_request_info import List[Optional[OnPagePagesByResourceRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.pages_by_resource([OnPagePagesByResourceRequestInfo(
                id="02241700-1535-0216-0000-034137259bc1",
                url="https://www.etsy.com/about/jobs.workco2018.js?",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPagePagesByResourceRequestInfo]]&gt;**](List[Optional[OnPagePagesByResourceRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="resources"></a>
# **resources**
> OnPageResourcesResponseInfo resources()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_resources_request_info import List[Optional[OnPageResourcesRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.resources([OnPageResourcesRequestInfo(
                id="07281559-0695-0216-0000-c269be8b7592",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageResourcesRequestInfo]]&gt;**](List[Optional[OnPageResourcesRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="duplicateTags"></a>
# **duplicateTags**
> OnPageDuplicateTagsResponseInfo duplicateTags()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_duplicate_tags_request_info import List[Optional[OnPageDuplicateTagsRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.duplicate_tags([OnPageDuplicateTagsRequestInfo(
                id="07281559-0695-0216-0000-c269be8b7592",
                type="duplicate_description",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageDuplicateTagsRequestInfo]]&gt;**](List[Optional[OnPageDuplicateTagsRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="duplicateContent"></a>
# **duplicateContent**
> OnPageDuplicateContentResponseInfo duplicateContent()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_duplicate_content_request_info import List[Optional[OnPageDuplicateContentRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.duplicate_content([OnPageDuplicateContentRequestInfo(
                id="07281559-0695-0216-0000-c269be8b7592",
                url="https://www.etsy.com/",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageDuplicateContentRequestInfo]]&gt;**](List[Optional[OnPageDuplicateContentRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="links"></a>
# **links**
> OnPageLinksResponseInfo links()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_links_request_info import List[Optional[OnPageLinksRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.links([OnPageLinksRequestInfo(
                id="07281559-0695-0216-0000-c269be8b7592",
                page_from="/apis/google-trends-api",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageLinksRequestInfo]]&gt;**](List[Optional[OnPageLinksRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="redirectChains"></a>
# **redirectChains**
> OnPageRedirectChainsResponseInfo redirectChains()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_redirect_chains_request_info import List[Optional[OnPageRedirectChainsRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.redirect_chains([OnPageRedirectChainsRequestInfo(
                id="03051327-4536-0216-1000-3b458a2cfcca",
                url="https://test_rdr.dataforseo.com/a/",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageRedirectChainsRequestInfo]]&gt;**](List[Optional[OnPageRedirectChainsRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="nonIndexable"></a>
# **nonIndexable**
> OnPageNonIndexableResponseInfo nonIndexable()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_non_indexable_request_info import List[Optional[OnPageNonIndexableRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.non_indexable([OnPageNonIndexableRequestInfo(
                id="07281559-0695-0216-0000-c269be8b7592",
                limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageNonIndexableRequestInfo]]&gt;**](List[Optional[OnPageNonIndexableRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="waterfall"></a>
# **waterfall**
> OnPageWaterfallResponseInfo waterfall()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_waterfall_request_info import List[Optional[OnPageWaterfallRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.waterfall([OnPageWaterfallRequestInfo(
                id="08101204-0696-0216-0000-644a7b21a48a",
                url="https://dataforseo.com/tag/broken-links",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageWaterfallRequestInfo]]&gt;**](List[Optional[OnPageWaterfallRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="keywordDensity"></a>
# **keywordDensity**
> OnPageKeywordDensityResponseInfo keywordDensity()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_keyword_density_request_info import List[Optional[OnPageKeywordDensityRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.keyword_density([OnPageKeywordDensityRequestInfo(
                id="09101923-1535-0216-0000-2389a8854b70",
                keyword_length=2,
                url="https://dataforseo.com/",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageKeywordDensityRequestInfo]]&gt;**](List[Optional[OnPageKeywordDensityRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="microdata"></a>
# **microdata**
> OnPageMicrodataResponseInfo microdata()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_microdata_request_info import List[Optional[OnPageMicrodataRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.microdata([OnPageMicrodataRequestInfo(
                id="02241700-1535-0216-0000-034137259bc1",
                url="https://dataforseo.com/apis",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageMicrodataRequestInfo]]&gt;**](List[Optional[OnPageMicrodataRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="rawHtml"></a>
# **rawHtml**
> OnPageRawHtmlResponseInfo rawHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_raw_html_request_info import List[Optional[OnPageRawHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.raw_html([OnPageRawHtmlRequestInfo(
                id="07281559-0695-0216-0000-c269be8b7592",
                url="https://dataforseo.com/apis",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageRawHtmlRequestInfo]]&gt;**](List[Optional[OnPageRawHtmlRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="pageScreenshot"></a>
# **pageScreenshot**
> OnPagePageScreenshotResponseInfo pageScreenshot()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_page_screenshot_request_info import List[Optional[OnPagePageScreenshotRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.page_screenshot([OnPagePageScreenshotRequestInfo(
                url="https://dataforseo.com/apis",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPagePageScreenshotRequestInfo]]&gt;**](List[Optional[OnPagePageScreenshotRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="contentParsing"></a>
# **contentParsing**
> OnPageContentParsingResponseInfo contentParsing()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_content_parsing_request_info import List[Optional[OnPageContentParsingRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.content_parsing([OnPageContentParsingRequestInfo(
                url="https://dataforseo.com/blog/a-versatile-alternative-to-google-trends-exploring-the-power-of-dataforseo-trends-api",
                id="11161551-1535-0216-0000-500b3f307f92",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageContentParsingRequestInfo]]&gt;**](List[Optional[OnPageContentParsingRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="contentParsingLive"></a>
# **contentParsingLive**
> OnPageContentParsingLiveResponseInfo contentParsingLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_content_parsing_live_request_info import List[Optional[OnPageContentParsingLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.content_parsing_live([OnPageContentParsingLiveRequestInfo(
                url="https://dataforseo.com/blog/a-versatile-alternative-to-google-trends-exploring-the-power-of-dataforseo-trends-api",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageContentParsingLiveRequestInfo]]&gt;**](List[Optional[OnPageContentParsingLiveRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="instantPages"></a>
# **instantPages**
> OnPageInstantPagesResponseInfo instantPages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_instant_pages_request_info import List[Optional[OnPageInstantPagesRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.instant_pages([OnPageInstantPagesRequestInfo(
                url="https://dataforseo.com/blog",
                enable_javascript=True,
                custom_js="meta = {}; meta.url = document.URL; meta;",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageInstantPagesRequestInfo]]&gt;**](List[Optional[OnPageInstantPagesRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="onPageLighthouseLanguages"></a>
# **onPageLighthouseLanguages**
> OnPageLighthouseLanguagesResponseInfo onPageLighthouseLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.on_page_lighthouse_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**OnPageLighthouseLanguagesResponseInfo**](OnPageLighthouseLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="lighthouseAudits"></a>
# **lighthouseAudits**
> OnPageLighthouseAuditsResponseInfo lighthouseAudits()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.lighthouse_audits()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**OnPageLighthouseAuditsResponseInfo**](OnPageLighthouseAuditsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="lighthouseVersions"></a>
# **lighthouseVersions**
> OnPageLighthouseVersionsResponseInfo lighthouseVersions()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.lighthouse_versions()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**OnPageLighthouseVersionsResponseInfo**](OnPageLighthouseVersionsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="lighthouseTaskPost"></a>
# **lighthouseTaskPost**
> OnPageLighthouseTaskPostResponseInfo lighthouseTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_lighthouse_task_post_request_info import List[Optional[OnPageLighthouseTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.lighthouse_task_post([OnPageLighthouseTaskPostRequestInfo(
                url="https://dataforseo.com",
                for_mobile=True,
                tag="some_string_123",
                pingback_url="https://your-server.com/pingscript?id=$id&tag=$tag",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageLighthouseTaskPostRequestInfo]]&gt;**](List[Optional[OnPageLighthouseTaskPostRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |

<a id="lighthouseTasksReady"></a>
# **lighthouseTasksReady**
> OnPageLighthouseTasksReadyResponseInfo lighthouseTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.lighthouse_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**OnPageLighthouseTasksReadyResponseInfo**](OnPageLighthouseTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="lighthouseTaskGetJson"></a>
# **lighthouseTaskGetJson**
> OnPageLighthouseTaskGetJsonResponseInfo lighthouseTaskGetJson()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = on_page_api.lighthouse_task_get_json(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**OnPageLighthouseTaskGetJsonResponseInfo**](OnPageLighthouseTaskGetJsonResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="lighthouseLiveJson"></a>
# **lighthouseLiveJson**
> OnPageLighthouseLiveJsonResponseInfo lighthouseLiveJson()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_on_page_lighthouse_live_json_request_info import List[Optional[OnPageLighthouseLiveJsonRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        on_page_api = OnPageApi(api_client)

        response = on_page_api.lighthouse_live_json([OnPageLighthouseLiveJsonRequestInfo(
                url="https://dataforseo.com",
                for_mobile=True,
                tag="some_string_123",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[OnPageLighthouseLiveJsonRequestInfo]]&gt;**](List[Optional[OnPageLighthouseLiveJsonRequestInfo]].md)|  | [optional] |



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
| **200** | Successful operation |  -  |