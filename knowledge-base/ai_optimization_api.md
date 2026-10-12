# AiOptimizationApi

Knowledge base for `AiOptimizationApi` (`dataforseo_client.api.ai_optimization_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

Data for AI search optimization (GEO): answers of large language models such as ChatGPT, Claude, Gemini and Perplexity to your prompts, results scraped from the web interfaces of AI assistants, search volume of keywords in AI tools, and how often brands, domains and pages are mentioned in AI-generated answers.

## Use it when you need

- To send a prompt to an LLM through one API and get its answer, the sources it cites and the usage cost, for example to benchmark several models.
- What end users actually see in an AI assistant for a query, including cited sources and mentioned brands.
- How popular a keyword or topic is among AI assistant users.
- Brand visibility in AI answers: where a brand or domain is mentioned, for which queries, how often, compared with competitors and over time.

## Use another API when

- You need classic search engine results, including AI answers embedded in search results pages: `SerpApi`.
- You need keyword metrics for classic search: `KeywordsDataApi` or `DataforseoLabsApi`.
- You need brand mentions on regular web pages: `ContentAnalysisApi`.

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### gemini_llm_scraper_task_get_advanced

`GET /v3/ai_optimization/gemini/llm_scraper/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    ai_optimization_api = AiOptimizationApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = ai_optimization_api.gemini_llm_scraper_task_get_advanced(id)
```

### chat_gpt_llm_scraper_task_get_advanced

`GET /v3/ai_optimization/chat_gpt/llm_scraper/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    ai_optimization_api = AiOptimizationApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = ai_optimization_api.chat_gpt_llm_scraper_task_get_advanced(id)
```

### chat_gpt_llm_scraper_task_post

`POST /v3/ai_optimization/chat_gpt/llm_scraper/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.models.ai_optimization_chat_gpt_llm_scraper_task_post_request_info import AiOptimizationChatGptLlmScraperTaskPostRequestInfo

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
```

### gemini_llm_scraper_task_post

`POST /v3/ai_optimization/gemini/llm_scraper/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.models.ai_optimization_gemini_llm_scraper_task_post_request_info import AiOptimizationGeminiLlmScraperTaskPostRequestInfo

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
```

### chat_gpt_llm_scraper_tasks_ready

`GET /v3/ai_optimization/chat_gpt/llm_scraper/tasks_ready`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    ai_optimization_api = AiOptimizationApi(api_client)

    response = ai_optimization_api.chat_gpt_llm_scraper_tasks_ready()
```

### chat_gpt_llm_scraper_live_advanced

`POST /v3/ai_optimization/chat_gpt/llm_scraper/live/advanced`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.models.ai_optimization_chat_gpt_llm_scraper_live_advanced_request_info import AiOptimizationChatGptLlmScraperLiveAdvancedRequestInfo

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
```

### perplexity_llm_responses_live

`POST /v3/ai_optimization/perplexity/llm_responses/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.models.ai_optimization_perplexity_llm_responses_live_request_info import AiOptimizationPerplexityLlmResponsesLiveRequestInfo
from dataforseo_client.models.llm_message_chain_item import LlmMessageChainItem

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
```

### gemini_llm_scraper_live_advanced

`POST /v3/ai_optimization/gemini/llm_scraper/live/advanced`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.models.ai_optimization_gemini_llm_scraper_live_advanced_request_info import AiOptimizationGeminiLlmScraperLiveAdvancedRequestInfo

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
```

### chat_gpt_llm_responses_live

`POST /v3/ai_optimization/chat_gpt/llm_responses/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.ai_optimization_api import AiOptimizationApi
from dataforseo_client.models.ai_optimization_chat_gpt_llm_responses_live_request_info import AiOptimizationChatGptLlmResponsesLiveRequestInfo
from dataforseo_client.models.llm_message_chain_item import LlmMessageChainItem

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
```

## Endpoints

All methods of `AiOptimizationApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `chat_gpt_llm_scraper_locations` | GET | `/v3/ai_optimization/chat_gpt/llm_scraper/locations` |
| `chat_gpt_llm_scraper_locations_country` | GET | `/v3/ai_optimization/chat_gpt/llm_scraper/locations/{country}` |
| `chat_gpt_llm_scraper_languages` | GET | `/v3/ai_optimization/chat_gpt/llm_scraper/languages` |
| `chat_gpt_llm_scraper_task_post` | POST | `/v3/ai_optimization/chat_gpt/llm_scraper/task_post` |
| `chat_gpt_llm_scraper_tasks_ready` | GET | `/v3/ai_optimization/chat_gpt/llm_scraper/tasks_ready` |
| `chat_gpt_llm_scraper_task_get_advanced` | GET | `/v3/ai_optimization/chat_gpt/llm_scraper/task_get/advanced/{id}` |
| `chat_gpt_llm_scraper_task_get_html` | GET | `/v3/ai_optimization/chat_gpt/llm_scraper/task_get/html/{id}` |
| `chat_gpt_llm_scraper_live_advanced` | POST | `/v3/ai_optimization/chat_gpt/llm_scraper/live/advanced` |
| `chat_gpt_llm_scraper_live_html` | POST | `/v3/ai_optimization/chat_gpt/llm_scraper/live/html` |
| `chat_gpt_llm_responses_models` | GET | `/v3/ai_optimization/chat_gpt/llm_responses/models` |
| `chat_gpt_llm_responses_live` | POST | `/v3/ai_optimization/chat_gpt/llm_responses/live` |
| `chat_gpt_llm_responses_task_post` | POST | `/v3/ai_optimization/chat_gpt/llm_responses/task_post` |
| `chat_gpt_llm_responses_tasks_ready` | GET | `/v3/ai_optimization/chat_gpt/llm_responses/tasks_ready` |
| `chat_gpt_llm_responses_task_get` | GET | `/v3/ai_optimization/chat_gpt/llm_responses/task_get/{id}` |
| `claude_llm_responses_models` | GET | `/v3/ai_optimization/claude/llm_responses/models` |
| `claude_llm_responses_live` | POST | `/v3/ai_optimization/claude/llm_responses/live` |
| `claude_llm_responses_task_post` | POST | `/v3/ai_optimization/claude/llm_responses/task_post` |
| `claude_llm_responses_tasks_ready` | GET | `/v3/ai_optimization/claude/llm_responses/tasks_ready` |
| `claude_llm_responses_task_get` | GET | `/v3/ai_optimization/claude/llm_responses/task_get/{id}` |
| `gemini_llm_responses_models` | GET | `/v3/ai_optimization/gemini/llm_responses/models` |
| `gemini_llm_responses_task_post` | POST | `/v3/ai_optimization/gemini/llm_responses/task_post` |
| `gemini_llm_responses_tasks_ready` | GET | `/v3/ai_optimization/gemini/llm_responses/tasks_ready` |
| `gemini_llm_responses_task_get` | GET | `/v3/ai_optimization/gemini/llm_responses/task_get/{id}` |
| `gemini_llm_responses_live` | POST | `/v3/ai_optimization/gemini/llm_responses/live` |
| `perplexity_llm_responses_models` | GET | `/v3/ai_optimization/perplexity/llm_responses/models` |
| `perplexity_llm_responses_live` | POST | `/v3/ai_optimization/perplexity/llm_responses/live` |
| `gemini_llm_scraper_locations` | GET | `/v3/ai_optimization/gemini/llm_scraper/locations` |
| `gemini_llm_scraper_languages` | GET | `/v3/ai_optimization/gemini/llm_scraper/languages` |
| `gemini_llm_scraper_task_post` | POST | `/v3/ai_optimization/gemini/llm_scraper/task_post` |
| `gemini_llm_scraper_tasks_ready` | GET | `/v3/ai_optimization/gemini/llm_scraper/tasks_ready` |
| `gemini_llm_scraper_task_get_advanced` | GET | `/v3/ai_optimization/gemini/llm_scraper/task_get/advanced/{id}` |
| `gemini_llm_scraper_task_get_html` | GET | `/v3/ai_optimization/gemini/llm_scraper/task_get/html/{id}` |
| `gemini_llm_scraper_live_advanced` | POST | `/v3/ai_optimization/gemini/llm_scraper/live/advanced` |
| `gemini_llm_scraper_live_html` | POST | `/v3/ai_optimization/gemini/llm_scraper/live/html` |
| `ai_keyword_data_available_filters` | GET | `/v3/ai_optimization/ai_keyword_data/available_filters` |
| `ai_keyword_data_locations_and_languages` | GET | `/v3/ai_optimization/ai_keyword_data/locations_and_languages` |
| `ai_keyword_data_keywords_search_volume_live` | POST | `/v3/ai_optimization/ai_keyword_data/keywords_search_volume/live` |
| `llm_mentions_available_filters` | GET | `/v3/ai_optimization/llm_mentions/available_filters` |
| `llm_mentions_locations_and_languages` | GET | `/v3/ai_optimization/llm_mentions/locations_and_languages` |
| `llm_mentions_search_mentions_live` | POST | `/v3/ai_optimization/llm_mentions/search_mentions/live` |
| `llm_mentions_target_metrics_live` | POST | `/v3/ai_optimization/llm_mentions/target_metrics/live` |
| `llm_mentions_multi_target_metrics_live` | POST | `/v3/ai_optimization/llm_mentions/multi_target_metrics/live` |
| `llm_mentions_top_mentioned_domains_live` | POST | `/v3/ai_optimization/llm_mentions/top_mentioned_domains/live` |
| `llm_mentions_top_mentioned_pages_live` | POST | `/v3/ai_optimization/llm_mentions/top_mentioned_pages/live` |
| `llm_mentions_top_mentioned_brands_live` | POST | `/v3/ai_optimization/llm_mentions/top_mentioned_brands/live` |
| `llm_mentions_top_mentioned_brand_categories_live` | POST | `/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories/live` |
| `llm_mentions_target_metrics_lite_live` | POST | `/v3/ai_optimization/llm_mentions/target_metrics_lite/live` |
| `llm_mentions_top_mentioned_domains_lite_live` | POST | `/v3/ai_optimization/llm_mentions/top_mentioned_domains_lite/live` |
| `llm_mentions_top_mentioned_pages_lite_live` | POST | `/v3/ai_optimization/llm_mentions/top_mentioned_pages_lite/live` |
| `llm_mentions_top_mentioned_brands_lite_live` | POST | `/v3/ai_optimization/llm_mentions/top_mentioned_brands_lite/live` |
| `llm_mentions_top_mentioned_brand_categories_lite_live` | POST | `/v3/ai_optimization/llm_mentions/top_mentioned_brand_categories_lite/live` |
| `llm_mentions_historical_live` | POST | `/v3/ai_optimization/llm_mentions/historical/live` |
| `llm_mentions_timeseries_delta_live` | POST | `/v3/ai_optimization/llm_mentions/timeseries_delta/live` |
| `llm_mentions_timeseries_new_lost_live` | POST | `/v3/ai_optimization/llm_mentions/timeseries_new_lost/live` |