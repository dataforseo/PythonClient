# AiOptimizationApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**aiOptimizationChatGptLlmScraperLocations**](AiOptimizationApi.md#aiOptimizationChatGptLlmScraperLocations) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/locations  |
[**aiOptimizationChatGptLlmScraperLocationsCountry**](AiOptimizationApi.md#aiOptimizationChatGptLlmScraperLocationsCountry) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/locations/{country}  |
[**aiOptimizationChatGptLlmScraperLanguages**](AiOptimizationApi.md#aiOptimizationChatGptLlmScraperLanguages) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/languages  |
[**chatGptLlmScraperTaskPost**](AiOptimizationApi.md#chatGptLlmScraperTaskPost) | **POST**  /v3/ai_optimization/chat_gpt/llm_scraper/task_post  |
[**chatGptLlmScraperTasksReady**](AiOptimizationApi.md#chatGptLlmScraperTasksReady) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/tasks_ready  |
[**chatGptLlmScraperTaskGetAdvanced**](AiOptimizationApi.md#chatGptLlmScraperTaskGetAdvanced) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/task_get/advanced/{id}  |
[**chatGptLlmScraperTaskGetHtml**](AiOptimizationApi.md#chatGptLlmScraperTaskGetHtml) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/task_get/html/{id}  |
[**aiOptimizationLlmMentionsLocationsAndLanguages**](AiOptimizationApi.md#aiOptimizationLlmMentionsLocationsAndLanguages) | **GET**  /v3/ai_optimization/llm_mentions/locations_and_languages  |
[**llmMentionsAvailableFilters**](AiOptimizationApi.md#llmMentionsAvailableFilters) | **GET**  /v3/ai_optimization/llm_mentions/available_filters  |
[**llmMentionsSearchLive**](AiOptimizationApi.md#llmMentionsSearchLive) | **POST**  /v3/ai_optimization/llm_mentions/search/live  |
[**llmMentionsTopPagesLive**](AiOptimizationApi.md#llmMentionsTopPagesLive) | **POST**  /v3/ai_optimization/llm_mentions/top_pages/live  |
[**llmMentionsTopDomainsLive**](AiOptimizationApi.md#llmMentionsTopDomainsLive) | **POST**  /v3/ai_optimization/llm_mentions/top_domains/live  |
[**llmMentionsAggregatedMetricsLive**](AiOptimizationApi.md#llmMentionsAggregatedMetricsLive) | **POST**  /v3/ai_optimization/llm_mentions/aggregated_metrics/live  |
[**llmMentionsCrossAggregatedMetricsLive**](AiOptimizationApi.md#llmMentionsCrossAggregatedMetricsLive) | **POST**  /v3/ai_optimization/llm_mentions/cross_aggregated_metrics/live  |
[**chatGptLlmResponsesModels**](AiOptimizationApi.md#chatGptLlmResponsesModels) | **GET**  /v3/ai_optimization/chat_gpt/llm_responses/models  |
[**chatGptLlmResponsesLive**](AiOptimizationApi.md#chatGptLlmResponsesLive) | **POST**  /v3/ai_optimization/chat_gpt/llm_responses/live  |
[**chatGptLlmResponsesTaskPost**](AiOptimizationApi.md#chatGptLlmResponsesTaskPost) | **POST**  /v3/ai_optimization/chat_gpt/llm_responses/task_post  |
[**chatGptLlmResponsesTasksReady**](AiOptimizationApi.md#chatGptLlmResponsesTasksReady) | **GET**  /v3/ai_optimization/chat_gpt/llm_responses/tasks_ready  |
[**chatGptLlmResponsesTaskGet**](AiOptimizationApi.md#chatGptLlmResponsesTaskGet) | **GET**  /v3/ai_optimization/chat_gpt/llm_responses/task_get/{id}  |
[**claudeLlmResponsesModels**](AiOptimizationApi.md#claudeLlmResponsesModels) | **GET**  /v3/ai_optimization/claude/llm_responses/models  |
[**claudeLlmResponsesLive**](AiOptimizationApi.md#claudeLlmResponsesLive) | **POST**  /v3/ai_optimization/claude/llm_responses/live  |
[**claudeLlmResponsesTaskPost**](AiOptimizationApi.md#claudeLlmResponsesTaskPost) | **POST**  /v3/ai_optimization/claude/llm_responses/task_post  |
[**claudeLlmResponsesTasksReady**](AiOptimizationApi.md#claudeLlmResponsesTasksReady) | **GET**  /v3/ai_optimization/claude/llm_responses/tasks_ready  |
[**claudeLlmResponsesTaskGet**](AiOptimizationApi.md#claudeLlmResponsesTaskGet) | **GET**  /v3/ai_optimization/claude/llm_responses/task_get/{id}  |
[**geminiLlmResponsesModels**](AiOptimizationApi.md#geminiLlmResponsesModels) | **GET**  /v3/ai_optimization/gemini/llm_responses/models  |
[**geminiLlmResponsesTaskPost**](AiOptimizationApi.md#geminiLlmResponsesTaskPost) | **POST**  /v3/ai_optimization/gemini/llm_responses/task_post  |
[**geminiLlmResponsesTasksReady**](AiOptimizationApi.md#geminiLlmResponsesTasksReady) | **GET**  /v3/ai_optimization/gemini/llm_responses/tasks_ready  |
[**geminiLlmResponsesTaskGet**](AiOptimizationApi.md#geminiLlmResponsesTaskGet) | **GET**  /v3/ai_optimization/gemini/llm_responses/task_get/{id}  |
[**geminiLlmResponsesLive**](AiOptimizationApi.md#geminiLlmResponsesLive) | **POST**  /v3/ai_optimization/gemini/llm_responses/live  |
[**perplexityLlmResponsesModels**](AiOptimizationApi.md#perplexityLlmResponsesModels) | **GET**  /v3/ai_optimization/perplexity/llm_responses/models  |
[**perplexityLlmResponsesLive**](AiOptimizationApi.md#perplexityLlmResponsesLive) | **POST**  /v3/ai_optimization/perplexity/llm_responses/live  |
[**aiKeywordDataAvailableFilters**](AiOptimizationApi.md#aiKeywordDataAvailableFilters) | **GET**  /v3/ai_optimization/ai_keyword_data/available_filters  |
[**aiOptimizationAiKeywordDataLocationsAndLanguages**](AiOptimizationApi.md#aiOptimizationAiKeywordDataLocationsAndLanguages) | **GET**  /v3/ai_optimization/ai_keyword_data/locations_and_languages  |
[**aiKeywordDataKeywordsSearchVolumeLive**](AiOptimizationApi.md#aiKeywordDataKeywordsSearchVolumeLive) | **POST**  /v3/ai_optimization/ai_keyword_data/keywords_search_volume/live  |

<a id="aiOptimizationChatGptLlmScraperLocations"></a>
# **aiOptimizationChatGptLlmScraperLocations**
> AiOptimizationChatGptLlmScraperLocationsResponseInfo aiOptimizationChatGptLlmScraperLocations()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.ai_optimization_chat_gpt_llm_scraper_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperLocationsResponseInfo**](AiOptimizationChatGptLlmScraperLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiOptimizationChatGptLlmScraperLocationsCountry"></a>
# **aiOptimizationChatGptLlmScraperLocationsCountry**
> AiOptimizationChatGptLlmScraperLocationsCountryResponseInfo aiOptimizationChatGptLlmScraperLocationsCountry()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        country = "us"
        response = ai_optimization_api.ai_optimization_chat_gpt_llm_scraper_locations_country(country)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperLocationsCountryResponseInfo**](AiOptimizationChatGptLlmScraperLocationsCountryResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiOptimizationChatGptLlmScraperLanguages"></a>
# **aiOptimizationChatGptLlmScraperLanguages**
> AiOptimizationChatGptLlmScraperLanguagesResponseInfo aiOptimizationChatGptLlmScraperLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.ai_optimization_chat_gpt_llm_scraper_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperLanguagesResponseInfo**](AiOptimizationChatGptLlmScraperLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmScraperTaskPost"></a>
# **chatGptLlmScraperTaskPost**
> AiOptimizationChatGptLlmScraperTaskPostResponseInfo chatGptLlmScraperTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_chat_gpt_llm_scraper_task_post_request_info import List[Optional[AiOptimizationChatGptLlmScraperTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.chat_gpt_llm_scraper_task_post([AiOptimizationChatGptLlmScraperTaskPostRequestInfo(
                keyword="what is chatgpt",
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
    | **** | [**List&lt;List[Optional[AiOptimizationChatGptLlmScraperTaskPostRequestInfo]]&gt;**](List[Optional[AiOptimizationChatGptLlmScraperTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationChatGptLlmScraperTaskPostResponseInfo**](AiOptimizationChatGptLlmScraperTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmScraperTasksReady"></a>
# **chatGptLlmScraperTasksReady**
> AiOptimizationChatGptLlmScraperTasksReadyResponseInfo chatGptLlmScraperTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.chat_gpt_llm_scraper_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperTasksReadyResponseInfo**](AiOptimizationChatGptLlmScraperTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmScraperTaskGetAdvanced"></a>
# **chatGptLlmScraperTaskGetAdvanced**
> AiOptimizationChatGptLlmScraperTaskGetAdvancedResponseInfo chatGptLlmScraperTaskGetAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = ai_optimization_api.chat_gpt_llm_scraper_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperTaskGetAdvancedResponseInfo**](AiOptimizationChatGptLlmScraperTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmScraperTaskGetHtml"></a>
# **chatGptLlmScraperTaskGetHtml**
> AiOptimizationChatGptLlmScraperTaskGetHtmlResponseInfo chatGptLlmScraperTaskGetHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = ai_optimization_api.chat_gpt_llm_scraper_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmScraperTaskGetHtmlResponseInfo**](AiOptimizationChatGptLlmScraperTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiOptimizationLlmMentionsLocationsAndLanguages"></a>
# **aiOptimizationLlmMentionsLocationsAndLanguages**
> AiOptimizationLlmMentionsLocationsAndLanguagesResponseInfo aiOptimizationLlmMentionsLocationsAndLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.ai_optimization_llm_mentions_locations_and_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationLlmMentionsLocationsAndLanguagesResponseInfo**](AiOptimizationLlmMentionsLocationsAndLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsAvailableFilters"></a>
# **llmMentionsAvailableFilters**
> AiOptimizationLlmMentionsAvailableFiltersResponseInfo llmMentionsAvailableFilters()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_available_filters()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationLlmMentionsAvailableFiltersResponseInfo**](AiOptimizationLlmMentionsAvailableFiltersResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsSearchLive"></a>
# **llmMentionsSearchLive**
> AiOptimizationLlmMentionsSearchLiveResponseInfo llmMentionsSearchLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_search_live_request_info import List[Optional[AiOptimizationLlmMentionsSearchLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_search_live([AiOptimizationLlmMentionsSearchLiveRequestInfo(
                target=[
                    AiOptimizationLLmMentionsDomainElement(
                        domain="dataforseo.com",
                        search_filter="exclude",
                    ),
                    AiOptimizationLLmMentionsKeywordElement(
                        keyword="bmw",
                        search_scope=[ "answer"],
                    ),
                    ],
                location_code=2840,
                language_name="English",
                platform="google",
                offset=0,
                limit=3,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsSearchLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsSearchLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsSearchLiveResponseInfo**](AiOptimizationLlmMentionsSearchLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTopPagesLive"></a>
# **llmMentionsTopPagesLive**
> AiOptimizationLlmMentionsTopPagesLiveResponseInfo llmMentionsTopPagesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_top_pages_live_request_info import List[Optional[AiOptimizationLlmMentionsTopPagesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_top_pages_live([AiOptimizationLlmMentionsTopPagesLiveRequestInfo(
                target=[
                    AiOptimizationLLmMentionsKeywordElement(
                        keyword="bmw",
                        search_scope=[ "answer"],
                    ),
                    AiOptimizationLLmMentionsKeywordElement(
                        keyword="auto",
                        search_scope=[ "question"],
                        match_type="partial_match",
                    ),
                    ],
                location_code=2840,
                language_code="en",
                platform="google",
                links_scope="sources",
                items_list_limit=3,
                internal_list_limit=2,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTopPagesLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTopPagesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTopPagesLiveResponseInfo**](AiOptimizationLlmMentionsTopPagesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTopDomainsLive"></a>
# **llmMentionsTopDomainsLive**
> AiOptimizationLlmMentionsTopDomainsLiveResponseInfo llmMentionsTopDomainsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_top_domains_live_request_info import List[Optional[AiOptimizationLlmMentionsTopDomainsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_top_domains_live([AiOptimizationLlmMentionsTopDomainsLiveRequestInfo(
                target=[
                    AiOptimizationLLmMentionsKeywordElement(
                        keyword="bmw",
                        search_scope=["answer"],
                    ),
                    AiOptimizationLLmMentionsKeywordElement(
                        keyword="auto",
                        search_scope=["question"],
                        match_type="partial_match",
                    ),
                    ],
                location_code=2840,
                language_code="en",
                platform="chat_gpt",
                links_scope="sources",
                items_list_limit=3,
                internal_list_limit=2,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTopDomainsLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTopDomainsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTopDomainsLiveResponseInfo**](AiOptimizationLlmMentionsTopDomainsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsAggregatedMetricsLive"></a>
# **llmMentionsAggregatedMetricsLive**
> AiOptimizationLlmMentionsAggregatedMetricsLiveResponseInfo llmMentionsAggregatedMetricsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_aggregated_metrics_live_request_info import List[Optional[AiOptimizationLlmMentionsAggregatedMetricsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_aggregated_metrics_live([AiOptimizationLlmMentionsAggregatedMetricsLiveRequestInfo(
                target=[
                    AiOptimizationLLmMentionsDomainElement(
                        domain="en.wikipedia.org",
                        search_filter="exclude",
                    ),
                    AiOptimizationLLmMentionsKeywordElement(
                        keyword="bmw",
                        search_scope=[ "answer"],
                    ),
                    ],
                location_code=2840,
                language_code="es",
                platform="google",
                internal_list_limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsAggregatedMetricsLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsAggregatedMetricsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsAggregatedMetricsLiveResponseInfo**](AiOptimizationLlmMentionsAggregatedMetricsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsCrossAggregatedMetricsLive"></a>
# **llmMentionsCrossAggregatedMetricsLive**
> AiOptimizationLlmMentionsCrossAggregatedMetricsLiveResponseInfo llmMentionsCrossAggregatedMetricsLive()

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsCrossAggregatedMetricsLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsCrossAggregatedMetricsLiveRequestInfo]].md)|  | [optional] |

### Return type

[**AiOptimizationLlmMentionsCrossAggregatedMetricsLiveResponseInfo**](AiOptimizationLlmMentionsCrossAggregatedMetricsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmResponsesModels"></a>
# **chatGptLlmResponsesModels**
> AiOptimizationChatGptLlmResponsesModelsResponseInfo chatGptLlmResponsesModels()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.chat_gpt_llm_responses_models()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmResponsesModelsResponseInfo**](AiOptimizationChatGptLlmResponsesModelsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmResponsesLive"></a>
# **chatGptLlmResponsesLive**
> AiOptimizationChatGptLlmResponsesLiveResponseInfo chatGptLlmResponsesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_chat_gpt_llm_responses_live_request_info import List[Optional[AiOptimizationChatGptLlmResponsesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.chat_gpt_llm_responses_live([AiOptimizationChatGptLlmResponsesLiveRequestInfo(
                user_prompt="provide information on how relevant the amusement park business is in France now",
                model_name="gpt-4.1-mini",
                max_output_tokens=200,
                temperature=0.3,
                top_p=0.5,
                web_search=True,
                web_search_country_iso_code="FR",
                web_search_city="Paris",
                system_message="communicate as if we are in a business meeting",
                message_chain=[
                    LlmMessageChainItem(
                        role="user",
                        message="Hello, what’s up?",
                    ),
                    LlmMessageChainItem(
                        role="ai",
                        message="Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
                    ),
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationChatGptLlmResponsesLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationChatGptLlmResponsesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationChatGptLlmResponsesLiveResponseInfo**](AiOptimizationChatGptLlmResponsesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmResponsesTaskPost"></a>
# **chatGptLlmResponsesTaskPost**
> AiOptimizationChatGptLlmResponsesTaskPostResponseInfo chatGptLlmResponsesTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_chat_gpt_llm_responses_task_post_request_info import List[Optional[AiOptimizationChatGptLlmResponsesTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.chat_gpt_llm_responses_task_post([AiOptimizationChatGptLlmResponsesTaskPostRequestInfo(
                user_prompt="provide information on how relevant the amusement park business is in France now",
                model_name="gpt-4.1-mini",
                system_message="communicate as if we are in a business meeting",
                message_chain=[
                    LlmMessageChainItem(
                        role="user",
                        message="Hello, what’s up?",
                    ),
                    LlmMessageChainItem(
                        role="ai",
                        message="Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
                    ),
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationChatGptLlmResponsesTaskPostRequestInfo]]&gt;**](List[Optional[AiOptimizationChatGptLlmResponsesTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationChatGptLlmResponsesTaskPostResponseInfo**](AiOptimizationChatGptLlmResponsesTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmResponsesTasksReady"></a>
# **chatGptLlmResponsesTasksReady**
> AiOptimizationChatGptLlmResponsesTasksReadyResponseInfo chatGptLlmResponsesTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.chat_gpt_llm_responses_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmResponsesTasksReadyResponseInfo**](AiOptimizationChatGptLlmResponsesTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmResponsesTaskGet"></a>
# **chatGptLlmResponsesTaskGet**
> AiOptimizationChatGptLlmResponsesTaskGetResponseInfo chatGptLlmResponsesTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = ai_optimization_api.chat_gpt_llm_responses_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationChatGptLlmResponsesTaskGetResponseInfo**](AiOptimizationChatGptLlmResponsesTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="claudeLlmResponsesModels"></a>
# **claudeLlmResponsesModels**
> AiOptimizationClaudeLlmResponsesModelsResponseInfo claudeLlmResponsesModels()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.claude_llm_responses_models()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationClaudeLlmResponsesModelsResponseInfo**](AiOptimizationClaudeLlmResponsesModelsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="claudeLlmResponsesLive"></a>
# **claudeLlmResponsesLive**
> AiOptimizationClaudeLlmResponsesLiveResponseInfo claudeLlmResponsesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_claude_llm_responses_live_request_info import List[Optional[AiOptimizationClaudeLlmResponsesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.claude_llm_responses_live([AiOptimizationClaudeLlmResponsesLiveRequestInfo(
                user_prompt="provide information on how relevant the amusement park business is in France now",
                model_name="claude-opus-4-0",
                max_output_tokens=200,
                temperature=0.3,
                top_p=0.5,
                web_search=True,
                web_search_country_iso_code="FR",
                system_message="communicate as if we are in a business meeting",
                message_chain=[
                    LlmMessageChainItem(
                        role="user",
                        message="Hello, what’s up?",
                    ),
                    LlmMessageChainItem(
                        role="ai",
                        message="Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
                    ),
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationClaudeLlmResponsesLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationClaudeLlmResponsesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationClaudeLlmResponsesLiveResponseInfo**](AiOptimizationClaudeLlmResponsesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="claudeLlmResponsesTaskPost"></a>
# **claudeLlmResponsesTaskPost**
> AiOptimizationClaudeLlmResponsesTaskPostResponseInfo claudeLlmResponsesTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_claude_llm_responses_task_post_request_info import List[Optional[AiOptimizationClaudeLlmResponsesTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.claude_llm_responses_task_post([AiOptimizationClaudeLlmResponsesTaskPostRequestInfo(
                user_prompt="provide information on how relevant the amusement park business is in France now",
                model_name="claude-sonnet-4-0",
                max_output_tokens=1024,
                temperature=0.3,
                top_p=0.5,
                web_search=True,
                web_search_country_iso_code="FR",
                system_message="communicate as if we are in a business meeting",
                message_chain=[
                    LlmMessageChainItem(
                        role="user",
                        message="Hello, what’s up?",
                    ),
                    LlmMessageChainItem(
                        role="ai",
                        message="Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
                    ),
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationClaudeLlmResponsesTaskPostRequestInfo]]&gt;**](List[Optional[AiOptimizationClaudeLlmResponsesTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationClaudeLlmResponsesTaskPostResponseInfo**](AiOptimizationClaudeLlmResponsesTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="claudeLlmResponsesTasksReady"></a>
# **claudeLlmResponsesTasksReady**
> AiOptimizationClaudeLlmResponsesTasksReadyResponseInfo claudeLlmResponsesTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.claude_llm_responses_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationClaudeLlmResponsesTasksReadyResponseInfo**](AiOptimizationClaudeLlmResponsesTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="claudeLlmResponsesTaskGet"></a>
# **claudeLlmResponsesTaskGet**
> AiOptimizationClaudeLlmResponsesTaskGetResponseInfo claudeLlmResponsesTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = ai_optimization_api.claude_llm_responses_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationClaudeLlmResponsesTaskGetResponseInfo**](AiOptimizationClaudeLlmResponsesTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmResponsesModels"></a>
# **geminiLlmResponsesModels**
> AiOptimizationGeminiLlmResponsesModelsResponseInfo geminiLlmResponsesModels()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.gemini_llm_responses_models()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationGeminiLlmResponsesModelsResponseInfo**](AiOptimizationGeminiLlmResponsesModelsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmResponsesTaskPost"></a>
# **geminiLlmResponsesTaskPost**
> AiOptimizationGeminiLlmResponsesTaskPostResponseInfo geminiLlmResponsesTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_gemini_llm_responses_task_post_request_info import List[Optional[AiOptimizationGeminiLlmResponsesTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.gemini_llm_responses_task_post([AiOptimizationGeminiLlmResponsesTaskPostRequestInfo(
                user_prompt="provide information on how relevant the amusement park business is in France now",
                model_name="gemini-2.5-flash",
                system_message="communicate as if we are in a business meeting",
                message_chain=[
                    LlmMessageChainItem(
                        role="user",
                        message="Hello, what’s up?",
                    ),
                    LlmMessageChainItem(
                        role="ai",
                        message="Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
                    ),
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationGeminiLlmResponsesTaskPostRequestInfo]]&gt;**](List[Optional[AiOptimizationGeminiLlmResponsesTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationGeminiLlmResponsesTaskPostResponseInfo**](AiOptimizationGeminiLlmResponsesTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmResponsesTasksReady"></a>
# **geminiLlmResponsesTasksReady**
> AiOptimizationGeminiLlmResponsesTasksReadyResponseInfo geminiLlmResponsesTasksReady()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.gemini_llm_responses_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationGeminiLlmResponsesTasksReadyResponseInfo**](AiOptimizationGeminiLlmResponsesTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmResponsesTaskGet"></a>
# **geminiLlmResponsesTaskGet**
> AiOptimizationGeminiLlmResponsesTaskGetResponseInfo geminiLlmResponsesTaskGet()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        id = "00000000-0000-0000-0000-000000000000"
        response = ai_optimization_api.gemini_llm_responses_task_get(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationGeminiLlmResponsesTaskGetResponseInfo**](AiOptimizationGeminiLlmResponsesTaskGetResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmResponsesLive"></a>
# **geminiLlmResponsesLive**
> AiOptimizationGeminiLlmResponsesLiveResponseInfo geminiLlmResponsesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_gemini_llm_responses_live_request_info import List[Optional[AiOptimizationGeminiLlmResponsesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.gemini_llm_responses_live([AiOptimizationGeminiLlmResponsesLiveRequestInfo(
                user_prompt="provide information on how relevant the amusement park business is in France now",
                model_name="gemini-2.5-flash",
                max_output_tokens=200,
                temperature=0.3,
                top_p=0.5,
                web_search=True,
                system_message="communicate as if we are in a business meeting",
                message_chain=[
                    LlmMessageChainItem(
                        role="user",
                        message="Hello, what’s up?",
                    ),
                    LlmMessageChainItem(
                        role="ai",
                        message="Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
                    ),
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationGeminiLlmResponsesLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationGeminiLlmResponsesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationGeminiLlmResponsesLiveResponseInfo**](AiOptimizationGeminiLlmResponsesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="perplexityLlmResponsesModels"></a>
# **perplexityLlmResponsesModels**
> AiOptimizationPerplexityLlmResponsesModelsResponseInfo perplexityLlmResponsesModels()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.perplexity_llm_responses_models()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationPerplexityLlmResponsesModelsResponseInfo**](AiOptimizationPerplexityLlmResponsesModelsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="perplexityLlmResponsesLive"></a>
# **perplexityLlmResponsesLive**
> AiOptimizationPerplexityLlmResponsesLiveResponseInfo perplexityLlmResponsesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_perplexity_llm_responses_live_request_info import List[Optional[AiOptimizationPerplexityLlmResponsesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.perplexity_llm_responses_live([AiOptimizationPerplexityLlmResponsesLiveRequestInfo(
                user_prompt="provide information on how relevant the amusement park business is in France now",
                model_name="sonar-reasoning",
                max_output_tokens=200,
                temperature=0.3,
                top_p=0.5,
                web_search_country_iso_code="FR",
                system_message="communicate as if we are in a business meeting",
                message_chain=[
                    LlmMessageChainItem(
                        role="user",
                        message="Hello, what’s up?",
                    ),
                    LlmMessageChainItem(
                        role="ai",
                        message="Hello! I’m doing well, thank you. How can I assist you today? Are there any specific topics or projects you’d like to discuss in our meeting?",
                    ),
                    ],
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationPerplexityLlmResponsesLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationPerplexityLlmResponsesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationPerplexityLlmResponsesLiveResponseInfo**](AiOptimizationPerplexityLlmResponsesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiKeywordDataAvailableFilters"></a>
# **aiKeywordDataAvailableFilters**
> AiOptimizationAiKeywordDataAvailableFiltersResponseInfo aiKeywordDataAvailableFilters()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.ai_keyword_data_available_filters()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationAiKeywordDataAvailableFiltersResponseInfo**](AiOptimizationAiKeywordDataAvailableFiltersResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiOptimizationAiKeywordDataLocationsAndLanguages"></a>
# **aiOptimizationAiKeywordDataLocationsAndLanguages**
> AiOptimizationAiKeywordDataLocationsAndLanguagesResponseInfo aiOptimizationAiKeywordDataLocationsAndLanguages()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.ai_optimization_ai_keyword_data_locations_and_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationAiKeywordDataLocationsAndLanguagesResponseInfo**](AiOptimizationAiKeywordDataLocationsAndLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="aiKeywordDataKeywordsSearchVolumeLive"></a>
# **aiKeywordDataKeywordsSearchVolumeLive**
> AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveResponseInfo aiKeywordDataKeywordsSearchVolumeLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_ai_keyword_data_keywords_search_volume_live_request_info import List[Optional[AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.ai_keyword_data_keywords_search_volume_live([AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveRequestInfo(
                keywords=[
                    "iphone",
                    "seo",
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
    | **** | [**List&lt;List[Optional[AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveResponseInfo**](AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |