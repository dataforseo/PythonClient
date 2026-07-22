# AiOptimizationApi

All URIs are relative to *https://api.dataforseo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
[**chatGptLlmScraperLocations**](AiOptimizationApi.md#chatGptLlmScraperLocations) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/locations  |
[**chatGptLlmScraperLocationsCountry**](AiOptimizationApi.md#chatGptLlmScraperLocationsCountry) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/locations/{country}  |
[**chatGptLlmScraperLanguages**](AiOptimizationApi.md#chatGptLlmScraperLanguages) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/languages  |
[**chatGptLlmScraperTaskPost**](AiOptimizationApi.md#chatGptLlmScraperTaskPost) | **POST**  /v3/ai_optimization/chat_gpt/llm_scraper/task_post  |
[**chatGptLlmScraperTasksReady**](AiOptimizationApi.md#chatGptLlmScraperTasksReady) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/tasks_ready  |
[**chatGptLlmScraperTaskGetAdvanced**](AiOptimizationApi.md#chatGptLlmScraperTaskGetAdvanced) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/task_get/advanced/{id}  |
[**chatGptLlmScraperTaskGetHtml**](AiOptimizationApi.md#chatGptLlmScraperTaskGetHtml) | **GET**  /v3/ai_optimization/chat_gpt/llm_scraper/task_get/html/{id}  |
[**chatGptLlmScraperLiveAdvanced**](AiOptimizationApi.md#chatGptLlmScraperLiveAdvanced) | **POST**  /v3/ai_optimization/chat_gpt/llm_scraper/live/advanced  |
[**chatGptLlmScraperLiveHtml**](AiOptimizationApi.md#chatGptLlmScraperLiveHtml) | **POST**  /v3/ai_optimization/chat_gpt/llm_scraper/live/html  |
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
[**geminiLlmScraperLocations**](AiOptimizationApi.md#geminiLlmScraperLocations) | **GET**  /v3/ai_optimization/gemini/llm_scraper/locations  |
[**geminiLlmScraperLanguages**](AiOptimizationApi.md#geminiLlmScraperLanguages) | **GET**  /v3/ai_optimization/gemini/llm_scraper/languages  |
[**geminiLlmScraperTaskPost**](AiOptimizationApi.md#geminiLlmScraperTaskPost) | **POST**  /v3/ai_optimization/gemini/llm_scraper/task_post  |
[**geminiLlmScraperTasksReady**](AiOptimizationApi.md#geminiLlmScraperTasksReady) | **GET**  /v3/ai_optimization/gemini/llm_scraper/tasks_ready  |
[**geminiLlmScraperTaskGetAdvanced**](AiOptimizationApi.md#geminiLlmScraperTaskGetAdvanced) | **GET**  /v3/ai_optimization/gemini/llm_scraper/task_get/advanced/{id}  |
[**geminiLlmScraperTaskGetHtml**](AiOptimizationApi.md#geminiLlmScraperTaskGetHtml) | **GET**  /v3/ai_optimization/gemini/llm_scraper/task_get/html/{id}  |
[**geminiLlmScraperLiveAdvanced**](AiOptimizationApi.md#geminiLlmScraperLiveAdvanced) | **POST**  /v3/ai_optimization/gemini/llm_scraper/live/advanced  |
[**geminiLlmScraperLiveHtml**](AiOptimizationApi.md#geminiLlmScraperLiveHtml) | **POST**  /v3/ai_optimization/gemini/llm_scraper/live/html  |
[**perplexityLlmResponsesModels**](AiOptimizationApi.md#perplexityLlmResponsesModels) | **GET**  /v3/ai_optimization/perplexity/llm_responses/models  |
[**perplexityLlmResponsesLive**](AiOptimizationApi.md#perplexityLlmResponsesLive) | **POST**  /v3/ai_optimization/perplexity/llm_responses/live  |
[**aiKeywordDataAvailableFilters**](AiOptimizationApi.md#aiKeywordDataAvailableFilters) | **GET**  /v3/ai_optimization/ai_keyword_data/available_filters  |
[**aiKeywordDataLocationsAndLanguages**](AiOptimizationApi.md#aiKeywordDataLocationsAndLanguages) | **GET**  /v3/ai_optimization/ai_keyword_data/locations_and_languages  |
[**aiKeywordDataKeywordsSearchVolumeLive**](AiOptimizationApi.md#aiKeywordDataKeywordsSearchVolumeLive) | **POST**  /v3/ai_optimization/ai_keyword_data/keywords_search_volume/live  |
[**llmMentionsAvailableFilters**](AiOptimizationApi.md#llmMentionsAvailableFilters) | **GET**  /v3/ai_optimization/llm_mentions/available_filters  |
[**llmMentionsLocationsAndLanguages**](AiOptimizationApi.md#llmMentionsLocationsAndLanguages) | **GET**  /v3/ai_optimization/llm_mentions/locations_and_languages  |
[**llmMentionsSearchMentionsLive**](AiOptimizationApi.md#llmMentionsSearchMentionsLive) | **POST**  /v3/ai_optimization/llm_mentions/search_mentions/live  |
[**llmMentionsTargetMetricsLive**](AiOptimizationApi.md#llmMentionsTargetMetricsLive) | **POST**  /v3/ai_optimization/llm_mentions/target_metrics/live  |
[**llmMentionsMultiTargetMetricsLive**](AiOptimizationApi.md#llmMentionsMultiTargetMetricsLive) | **POST**  /v3/ai_optimization/llm_mentions/multi_target_metrics/live  |
[**llmMentionsTopMentionedDomainsLive**](AiOptimizationApi.md#llmMentionsTopMentionedDomainsLive) | **POST**  /v3/ai_optimization/llm_mentions/top_mentioned_domains/live  |
[**llmMentionsTopMentionedPagesLive**](AiOptimizationApi.md#llmMentionsTopMentionedPagesLive) | **POST**  /v3/ai_optimization/llm_mentions/top_mentioned_pages/live  |
[**llmMentionsTopMentionedBrandsLive**](AiOptimizationApi.md#llmMentionsTopMentionedBrandsLive) | **POST**  /v3/ai_optimization/llm_mentions/top_mentioned_brands/live  |
[**llmMentionsTopMentionedBrandCategoriesLive**](AiOptimizationApi.md#llmMentionsTopMentionedBrandCategoriesLive) | **POST**  /v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live  |
[**llmMentionsTargetMetricsLiteLive**](AiOptimizationApi.md#llmMentionsTargetMetricsLiteLive) | **POST**  /v3/ai_optimization/llm_mentions/target_metrics_lite/live  |
[**llmMentionsTopMentionedDomainsLiteLive**](AiOptimizationApi.md#llmMentionsTopMentionedDomainsLiteLive) | **POST**  /v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live  |
[**llmMentionsTopMentionedPagesLiteLive**](AiOptimizationApi.md#llmMentionsTopMentionedPagesLiteLive) | **POST**  /v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live  |
[**llmMentionsTopMentionedBrandsLiteLive**](AiOptimizationApi.md#llmMentionsTopMentionedBrandsLiteLive) | **POST**  /v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live  |
[**llmMentionsTopMentionedBrandCategoriesLiteLive**](AiOptimizationApi.md#llmMentionsTopMentionedBrandCategoriesLiteLive) | **POST**  /v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live  |
[**llmMentionsHistoricalLive**](AiOptimizationApi.md#llmMentionsHistoricalLive) | **POST**  /v3/ai_optimization/llm_mentions/historical/live  |
[**llmMentionsTimeseriesDeltaLive**](AiOptimizationApi.md#llmMentionsTimeseriesDeltaLive) | **POST**  /v3/ai_optimization/llm_mentions/timeseries_delta/live  |
[**llmMentionsTimeseriesNewLostLive**](AiOptimizationApi.md#llmMentionsTimeseriesNewLostLive) | **POST**  /v3/ai_optimization/llm_mentions/timeseries_new_lost/live  |

<a id="chatGptLlmScraperLocations"></a>
# **chatGptLlmScraperLocations**
> AiOptimizationChatGptLlmScraperLocationsResponseInfo chatGptLlmScraperLocations()


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

        response = ai_optimization_api.chat_gpt_llm_scraper_locations()
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

<a id="chatGptLlmScraperLocationsCountry"></a>
# **chatGptLlmScraperLocationsCountry**
> AiOptimizationChatGptLlmScraperLocationsCountryResponseInfo chatGptLlmScraperLocationsCountry()


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
        response = ai_optimization_api.chat_gpt_llm_scraper_locations_country(country)
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

<a id="chatGptLlmScraperLanguages"></a>
# **chatGptLlmScraperLanguages**
> AiOptimizationChatGptLlmScraperLanguagesResponseInfo chatGptLlmScraperLanguages()


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

        response = ai_optimization_api.chat_gpt_llm_scraper_languages()
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
                language_code="en",
                location_code=2840,
                keyword="what is chatgpt",
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

<a id="chatGptLlmScraperLiveAdvanced"></a>
# **chatGptLlmScraperLiveAdvanced**
> AiOptimizationChatGptLlmScraperLiveAdvancedResponseInfo chatGptLlmScraperLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_chat_gpt_llm_scraper_live_advanced_request_info import List[Optional[AiOptimizationChatGptLlmScraperLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.chat_gpt_llm_scraper_live_advanced([AiOptimizationChatGptLlmScraperLiveAdvancedRequestInfo(
                language_code="en",
                location_code=2840,
                keyword="albert einstein",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationChatGptLlmScraperLiveAdvancedRequestInfo]]&gt;**](List[Optional[AiOptimizationChatGptLlmScraperLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationChatGptLlmScraperLiveAdvancedResponseInfo**](AiOptimizationChatGptLlmScraperLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="chatGptLlmScraperLiveHtml"></a>
# **chatGptLlmScraperLiveHtml**
> AiOptimizationChatGptLlmScraperLiveHtmlResponseInfo chatGptLlmScraperLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_chat_gpt_llm_scraper_live_html_request_info import List[Optional[AiOptimizationChatGptLlmScraperLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.chat_gpt_llm_scraper_live_html([AiOptimizationChatGptLlmScraperLiveHtmlRequestInfo(
                language_code="en",
                location_code=2840,
                keyword="albert einstein",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationChatGptLlmScraperLiveHtmlRequestInfo]]&gt;**](List[Optional[AiOptimizationChatGptLlmScraperLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationChatGptLlmScraperLiveHtmlResponseInfo**](AiOptimizationChatGptLlmScraperLiveHtmlResponseInfo.md)

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
                max_output_tokens=200,
                temperature=0.3,
                top_p=0.5,
                model_name="gpt-4.1-mini",
                web_search=True,
                web_search_country_iso_code="FR",
                web_search_city="Paris",
                user_prompt="provide information on how relevant the amusement park business is in France now",
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
                model_name="gpt-4.1-mini",
                user_prompt="provide information on how relevant the amusement park business is in France now",
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
                max_output_tokens=200,
                model_name="claude-opus-4-0",
                temperature=0.3,
                web_search=True,
                web_search_country_iso_code="FR",
                user_prompt="provide information on how relevant the amusement park business is in France now",
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
                max_output_tokens=1024,
                temperature=0.3,
                web_search_country_iso_code="FR",
                model_name="claude-sonnet-4-0",
                web_search=True,
                user_prompt="provide information on how relevant the amusement park business is in France now",
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
                model_name="gemini-2.5-flash",
                user_prompt="provide information on how relevant the amusement park business is in France now",
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
                max_output_tokens=200,
                temperature=0.3,
                top_p=0.5,
                model_name="gemini-2.5-flash",
                web_search=True,
                user_prompt="provide information on how relevant the amusement park business is in France now",
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

<a id="geminiLlmScraperLocations"></a>
# **geminiLlmScraperLocations**
> AiOptimizationGeminiLlmScraperLocationsResponseInfo geminiLlmScraperLocations()


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

        response = ai_optimization_api.gemini_llm_scraper_locations()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationGeminiLlmScraperLocationsResponseInfo**](AiOptimizationGeminiLlmScraperLocationsResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmScraperLanguages"></a>
# **geminiLlmScraperLanguages**
> AiOptimizationGeminiLlmScraperLanguagesResponseInfo geminiLlmScraperLanguages()


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

        response = ai_optimization_api.gemini_llm_scraper_languages()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationGeminiLlmScraperLanguagesResponseInfo**](AiOptimizationGeminiLlmScraperLanguagesResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmScraperTaskPost"></a>
# **geminiLlmScraperTaskPost**
> AiOptimizationGeminiLlmScraperTaskPostResponseInfo geminiLlmScraperTaskPost()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_gemini_llm_scraper_task_post_request_info import List[Optional[AiOptimizationGeminiLlmScraperTaskPostRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.gemini_llm_scraper_task_post([AiOptimizationGeminiLlmScraperTaskPostRequestInfo(
                language_code="en",
                location_code=2840,
                keyword="albert einstein",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationGeminiLlmScraperTaskPostRequestInfo]]&gt;**](List[Optional[AiOptimizationGeminiLlmScraperTaskPostRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationGeminiLlmScraperTaskPostResponseInfo**](AiOptimizationGeminiLlmScraperTaskPostResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmScraperTasksReady"></a>
# **geminiLlmScraperTasksReady**
> AiOptimizationGeminiLlmScraperTasksReadyResponseInfo geminiLlmScraperTasksReady()


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

        response = ai_optimization_api.gemini_llm_scraper_tasks_ready()
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationGeminiLlmScraperTasksReadyResponseInfo**](AiOptimizationGeminiLlmScraperTasksReadyResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmScraperTaskGetAdvanced"></a>
# **geminiLlmScraperTaskGetAdvanced**
> AiOptimizationGeminiLlmScraperTaskGetAdvancedResponseInfo geminiLlmScraperTaskGetAdvanced()


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
        response = ai_optimization_api.gemini_llm_scraper_task_get_advanced(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationGeminiLlmScraperTaskGetAdvancedResponseInfo**](AiOptimizationGeminiLlmScraperTaskGetAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmScraperTaskGetHtml"></a>
# **geminiLlmScraperTaskGetHtml**
> AiOptimizationGeminiLlmScraperTaskGetHtmlResponseInfo geminiLlmScraperTaskGetHtml()


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
        response = ai_optimization_api.gemini_llm_scraper_task_get_html(id)
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters


    
        This endpoint does not need any parameter.
    


### Return type

[**AiOptimizationGeminiLlmScraperTaskGetHtmlResponseInfo**](AiOptimizationGeminiLlmScraperTaskGetHtmlResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmScraperLiveAdvanced"></a>
# **geminiLlmScraperLiveAdvanced**
> AiOptimizationGeminiLlmScraperLiveAdvancedResponseInfo geminiLlmScraperLiveAdvanced()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_gemini_llm_scraper_live_advanced_request_info import List[Optional[AiOptimizationGeminiLlmScraperLiveAdvancedRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.gemini_llm_scraper_live_advanced([AiOptimizationGeminiLlmScraperLiveAdvancedRequestInfo(
                language_code="en",
                location_code=2840,
                keyword="albert einstein",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationGeminiLlmScraperLiveAdvancedRequestInfo]]&gt;**](List[Optional[AiOptimizationGeminiLlmScraperLiveAdvancedRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationGeminiLlmScraperLiveAdvancedResponseInfo**](AiOptimizationGeminiLlmScraperLiveAdvancedResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="geminiLlmScraperLiveHtml"></a>
# **geminiLlmScraperLiveHtml**
> AiOptimizationGeminiLlmScraperLiveHtmlResponseInfo geminiLlmScraperLiveHtml()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_gemini_llm_scraper_live_html_request_info import List[Optional[AiOptimizationGeminiLlmScraperLiveHtmlRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.gemini_llm_scraper_live_html([AiOptimizationGeminiLlmScraperLiveHtmlRequestInfo(
                language_code="en",
                location_code=2840,
                keyword="albert einstein",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationGeminiLlmScraperLiveHtmlRequestInfo]]&gt;**](List[Optional[AiOptimizationGeminiLlmScraperLiveHtmlRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationGeminiLlmScraperLiveHtmlResponseInfo**](AiOptimizationGeminiLlmScraperLiveHtmlResponseInfo.md)

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
                max_output_tokens=200,
                temperature=0.3,
                top_p=0.5,
                web_search_country_iso_code="FR",
                model_name="sonar",
                user_prompt="provide information on how relevant the amusement park business is in France now",
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

<a id="aiKeywordDataLocationsAndLanguages"></a>
# **aiKeywordDataLocationsAndLanguages**
> AiOptimizationAiKeywordDataLocationsAndLanguagesResponseInfo aiKeywordDataLocationsAndLanguages()


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

        response = ai_optimization_api.ai_keyword_data_locations_and_languages()
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
                language_name="English",
                location_code=2840,
                keywords=[
                    "iphone",
                    "seo",
                    ],
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

<a id="llmMentionsLocationsAndLanguages"></a>
# **llmMentionsLocationsAndLanguages**
> AiOptimizationLlmMentionsLocationsAndLanguagesResponseInfo llmMentionsLocationsAndLanguages()


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

        response = ai_optimization_api.llm_mentions_locations_and_languages()
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

<a id="llmMentionsSearchMentionsLive"></a>
# **llmMentionsSearchMentionsLive**
> AiOptimizationLlmMentionsSearchMentionsLiveResponseInfo llmMentionsSearchMentionsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_search_mentions_live_request_info import List[Optional[AiOptimizationLlmMentionsSearchMentionsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_search_mentions_live([AiOptimizationLlmMentionsSearchMentionsLiveRequestInfo(
                language_name="English",
                location_code=2840,
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        domain="dataforseo.com",
                        search_filter="exclude",
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    ],
                platform="google",
                filters=[
                    ,
                    ],
                order_by=[
                    "ai_search_volume,desc",
                    ],
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
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsSearchMentionsLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsSearchMentionsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsSearchMentionsLiveResponseInfo**](AiOptimizationLlmMentionsSearchMentionsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTargetMetricsLive"></a>
# **llmMentionsTargetMetricsLive**
> AiOptimizationLlmMentionsTargetMetricsLiveResponseInfo llmMentionsTargetMetricsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_target_metrics_live_request_info import List[Optional[AiOptimizationLlmMentionsTargetMetricsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_target_metrics_live([AiOptimizationLlmMentionsTargetMetricsLiveRequestInfo(
                language_code="en",
                location_code=2840,
                platform="chat_gpt",
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        domain="en.wikipedia.org",
                        search_filter="exclude",
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    ],
                initial_dataset_filters=[
                    ,
                    ],
                internal_list_limit=10,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTargetMetricsLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTargetMetricsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTargetMetricsLiveResponseInfo**](AiOptimizationLlmMentionsTargetMetricsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsMultiTargetMetricsLive"></a>
# **llmMentionsMultiTargetMetricsLive**
> AiOptimizationLlmMentionsMultiTargetMetricsLiveResponseInfo llmMentionsMultiTargetMetricsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_multi_target_metrics_live_request_info import List[Optional[AiOptimizationLlmMentionsMultiTargetMetricsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_multi_target_metrics_live([AiOptimizationLlmMentionsMultiTargetMetricsLiveRequestInfo(
                language_code="en",
                location_code=2840,
                platform="google",
                targets=[
                    AiOptimizationLLmMentionsMultiTargetMetricsRequestInfo(
                        key="chat_gpt",
                        target=,
                    ),
                    AiOptimizationLLmMentionsMultiTargetMetricsRequestInfo(
                        key="claude",
                        target=,
                    ),
                    AiOptimizationLLmMentionsMultiTargetMetricsRequestInfo(
                        key="gemini",
                        target=,
                    ),
                    AiOptimizationLLmMentionsMultiTargetMetricsRequestInfo(
                        key="perplexity",
                        target=,
                    ),
                    ],
                initial_dataset_filters=[
                    ,
                    ],
                internal_list_limit=5,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsMultiTargetMetricsLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsMultiTargetMetricsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsMultiTargetMetricsLiveResponseInfo**](AiOptimizationLlmMentionsMultiTargetMetricsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTopMentionedDomainsLive"></a>
# **llmMentionsTopMentionedDomainsLive**
> AiOptimizationLlmMentionsTopMentionedDomainsLiveResponseInfo llmMentionsTopMentionedDomainsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_top_mentioned_domains_live_request_info import List[Optional[AiOptimizationLlmMentionsTopMentionedDomainsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_top_mentioned_domains_live([AiOptimizationLlmMentionsTopMentionedDomainsLiveRequestInfo(
                language_code="en",
                location_code=2840,
                platform="chat_gpt",
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="auto",
                        search_scope=,
                        match_type="partial_match",
                    ),
                    ],
                links_scope="sources",
                initial_dataset_filters=[
                    ,
                    ],
                limit=3,
                internal_list_limit=2,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTopMentionedDomainsLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTopMentionedDomainsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTopMentionedDomainsLiveResponseInfo**](AiOptimizationLlmMentionsTopMentionedDomainsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTopMentionedPagesLive"></a>
# **llmMentionsTopMentionedPagesLive**
> AiOptimizationLlmMentionsTopMentionedPagesLiveResponseInfo llmMentionsTopMentionedPagesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_top_mentioned_pages_live_request_info import List[Optional[AiOptimizationLlmMentionsTopMentionedPagesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_top_mentioned_pages_live([AiOptimizationLlmMentionsTopMentionedPagesLiveRequestInfo(
                language_code="en",
                location_code=2840,
                platform="chat_gpt",
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="auto",
                        search_scope=,
                        match_type="partial_match",
                    ),
                    ],
                links_scope="sources",
                initial_dataset_filters=[
                    ,
                    ],
                limit=3,
                internal_list_limit=2,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTopMentionedPagesLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTopMentionedPagesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTopMentionedPagesLiveResponseInfo**](AiOptimizationLlmMentionsTopMentionedPagesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTopMentionedBrandsLive"></a>
# **llmMentionsTopMentionedBrandsLive**
> AiOptimizationLlmMentionsTopMentionedBrandsLiveResponseInfo llmMentionsTopMentionedBrandsLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_top_mentioned_brands_live_request_info import List[Optional[AiOptimizationLlmMentionsTopMentionedBrandsLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_top_mentioned_brands_live([AiOptimizationLlmMentionsTopMentionedBrandsLiveRequestInfo(
                language_code="en",
                location_code=2840,
                platform="chat_gpt",
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="auto",
                        search_scope=,
                        match_type="partial_match",
                    ),
                    ],
                initial_dataset_filters=[
                    ,
                    ],
                limit=3,
                internal_list_limit=2,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTopMentionedBrandsLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTopMentionedBrandsLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTopMentionedBrandsLiveResponseInfo**](AiOptimizationLlmMentionsTopMentionedBrandsLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTopMentionedBrandCategoriesLive"></a>
# **llmMentionsTopMentionedBrandCategoriesLive**
> AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiveResponseInfo llmMentionsTopMentionedBrandCategoriesLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_top_mentioned_brand_categories_live_request_info import List[Optional[AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_top_mentioned_brand_categories_live([AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiveRequestInfo(
                language_code="en",
                location_code=2840,
                platform="chat_gpt",
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="auto",
                        search_scope=,
                        match_type="partial_match",
                    ),
                    ],
                initial_dataset_filters=[
                    ,
                    ],
                limit=3,
                internal_list_limit=2,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiveResponseInfo**](AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTargetMetricsLiteLive"></a>
# **llmMentionsTargetMetricsLiteLive**
> AiOptimizationLlmMentionsTargetMetricsLiteLiveResponseInfo llmMentionsTargetMetricsLiteLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_target_metrics_lite_live_request_info import List[Optional[AiOptimizationLlmMentionsTargetMetricsLiteLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_target_metrics_lite_live([AiOptimizationLlmMentionsTargetMetricsLiteLiveRequestInfo(
                language_code="es",
                location_code=2840,
                platform="google",
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        domain="en.wikipedia.org",
                        search_filter="exclude",
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    ],
                initial_dataset_filters=[
                    ,
                    ],
                limit=6,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTargetMetricsLiteLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTargetMetricsLiteLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTargetMetricsLiteLiveResponseInfo**](AiOptimizationLlmMentionsTargetMetricsLiteLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTopMentionedDomainsLiteLive"></a>
# **llmMentionsTopMentionedDomainsLiteLive**
> AiOptimizationLlmMentionsTopMentionedDomainsLiteLiveResponseInfo llmMentionsTopMentionedDomainsLiteLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_top_mentioned_domains_lite_live_request_info import List[Optional[AiOptimizationLlmMentionsTopMentionedDomainsLiteLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_top_mentioned_domains_lite_live([AiOptimizationLlmMentionsTopMentionedDomainsLiteLiveRequestInfo(
                language_code="en",
                location_code=2840,
                platform="chat_gpt",
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="auto",
                        search_scope=,
                        match_type="partial_match",
                    ),
                    ],
                links_scope="sources",
                initial_dataset_filters=[
                    ,
                    ],
                limit=3,
                internal_list_limit=2,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTopMentionedDomainsLiteLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTopMentionedDomainsLiteLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTopMentionedDomainsLiteLiveResponseInfo**](AiOptimizationLlmMentionsTopMentionedDomainsLiteLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTopMentionedPagesLiteLive"></a>
# **llmMentionsTopMentionedPagesLiteLive**
> AiOptimizationLlmMentionsTopMentionedPagesLiteLiveResponseInfo llmMentionsTopMentionedPagesLiteLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_top_mentioned_pages_lite_live_request_info import List[Optional[AiOptimizationLlmMentionsTopMentionedPagesLiteLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_top_mentioned_pages_lite_live([AiOptimizationLlmMentionsTopMentionedPagesLiteLiveRequestInfo(
                language_code="en",
                location_code=2840,
                platform="chat_gpt",
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="auto",
                        search_scope=,
                        match_type="partial_match",
                    ),
                    ],
                links_scope="sources",
                initial_dataset_filters=[
                    ,
                    ],
                limit=3,
                internal_list_limit=2,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTopMentionedPagesLiteLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTopMentionedPagesLiteLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTopMentionedPagesLiteLiveResponseInfo**](AiOptimizationLlmMentionsTopMentionedPagesLiteLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTopMentionedBrandsLiteLive"></a>
# **llmMentionsTopMentionedBrandsLiteLive**
> AiOptimizationLlmMentionsTopMentionedBrandsLiteLiveResponseInfo llmMentionsTopMentionedBrandsLiteLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_top_mentioned_brands_lite_live_request_info import List[Optional[AiOptimizationLlmMentionsTopMentionedBrandsLiteLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_top_mentioned_brands_lite_live([AiOptimizationLlmMentionsTopMentionedBrandsLiteLiveRequestInfo(
                language_code="en",
                location_code=2840,
                platform="chat_gpt",
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="auto",
                        search_scope=,
                        match_type="partial_match",
                    ),
                    ],
                initial_dataset_filters=[
                    ,
                    ],
                limit=3,
                internal_list_limit=2,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTopMentionedBrandsLiteLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTopMentionedBrandsLiteLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTopMentionedBrandsLiteLiveResponseInfo**](AiOptimizationLlmMentionsTopMentionedBrandsLiteLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTopMentionedBrandCategoriesLiteLive"></a>
# **llmMentionsTopMentionedBrandCategoriesLiteLive**
> AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiteLiveResponseInfo llmMentionsTopMentionedBrandCategoriesLiteLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_top_mentioned_brand_categories_lite_live_request_info import List[Optional[AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiteLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_top_mentioned_brand_categories_lite_live([AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiteLiveRequestInfo(
                language_code="en",
                location_code=2840,
                platform="chat_gpt",
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="auto",
                        search_scope=,
                        match_type="partial_match",
                    ),
                    ],
                initial_dataset_filters=[
                    ,
                    ],
                limit=3,
                internal_list_limit=2,
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiteLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiteLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiteLiveResponseInfo**](AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiteLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsHistoricalLive"></a>
# **llmMentionsHistoricalLive**
> AiOptimizationLlmMentionsHistoricalLiveResponseInfo llmMentionsHistoricalLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_historical_live_request_info import List[Optional[AiOptimizationLlmMentionsHistoricalLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_historical_live([AiOptimizationLlmMentionsHistoricalLiveRequestInfo(
                language_code="es",
                location_code=2840,
                platform="google",
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        domain="en.wikipedia.org",
                        search_filter="exclude",
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
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
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsHistoricalLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsHistoricalLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsHistoricalLiveResponseInfo**](AiOptimizationLlmMentionsHistoricalLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTimeseriesDeltaLive"></a>
# **llmMentionsTimeseriesDeltaLive**
> AiOptimizationLlmMentionsTimeseriesDeltaLiveResponseInfo llmMentionsTimeseriesDeltaLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_timeseries_delta_live_request_info import List[Optional[AiOptimizationLlmMentionsTimeseriesDeltaLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_timeseries_delta_live([AiOptimizationLlmMentionsTimeseriesDeltaLiveRequestInfo(
                language_name="English",
                location_code=2840,
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        domain="dataforseo.com",
                        search_filter="exclude",
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="bmw",
                        search_scope=,
                    ),
                    ],
                platform="google",
                group_range="month",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTimeseriesDeltaLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTimeseriesDeltaLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTimeseriesDeltaLiveResponseInfo**](AiOptimizationLlmMentionsTimeseriesDeltaLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="llmMentionsTimeseriesNewLostLive"></a>
# **llmMentionsTimeseriesNewLostLive**
> AiOptimizationLlmMentionsTimeseriesNewLostLiveResponseInfo llmMentionsTimeseriesNewLostLive()


### Example
```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.list_optional_ai_optimization_llm_mentions_timeseries_new_lost_live_request_info import List[Optional[AiOptimizationLlmMentionsTimeseriesNewLostLiveRequestInfo]]

from pprint import pprint
try:
    # Configure HTTP basic authorization: basicAuth
    configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



    with dfs_api_provider.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        ai_optimization_api = AiOptimizationApi(api_client)

        response = ai_optimization_api.llm_mentions_timeseries_new_lost_live([AiOptimizationLlmMentionsTimeseriesNewLostLiveRequestInfo(
                language_name="English",
                location_code=2840,
                target=[
                    BaseAiOptimizationLLmMentionsTargetElement(
                        domain="dataforseo.com",
                        search_filter="exclude",
                    ),
                    BaseAiOptimizationLLmMentionsTargetElement(
                        keyword="serp",
                        search_scope=,
                    ),
                    ],
                platform="google",
                group_range="month",
        )]
        )
except ApiException as e:
    print("Exception: %s\n" % e)
```

### Parameters

    | Name | Type | Description  | Notes |
    |------------- | ------------- | ------------- | -------------|
    | **** | [**List&lt;List[Optional[AiOptimizationLlmMentionsTimeseriesNewLostLiveRequestInfo]]&gt;**](List[Optional[AiOptimizationLlmMentionsTimeseriesNewLostLiveRequestInfo]].md)|  | [optional] |



### Return type

[**AiOptimizationLlmMentionsTimeseriesNewLostLiveResponseInfo**](AiOptimizationLlmMentionsTimeseriesNewLostLiveResponseInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |