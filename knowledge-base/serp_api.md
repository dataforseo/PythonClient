# SerpApi

Knowledge base for `SerpApi` (`dataforseo_client.api.serp_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

Search engine results pages (SERP) collected on request: what a search engine shows for a query in a given location, language and device, from engines such as Google, Bing, YouTube, Yahoo and others, including search verticals such as maps, news, images, jobs and AI search modes.

Results are collected at the moment of the request and emulate a real, non-personalized user in the chosen location. They are returned either as parsed, typed elements of the page (organic results, ads, featured snippets, AI answers, local packs, videos and other SERP features) or as raw HTML.

## Use it when you need

- The current ranking of a website, page or product for a keyword in a specific location, language or device (rank tracking).
- The composition of a results page: which SERP features appear and what they contain.
- Fresh results of a search vertical: local businesses on maps, news articles, images, videos, autocomplete suggestions and similar.
- Search results as a raw input for your own processing (parsing, screenshots, summaries).

## Use another API when

- You need keyword metrics such as search volume, CPC or difficulty: `KeywordsDataApi` or `DataforseoLabsApi`.
- You need many keywords or domains at once, historical rankings or the keywords a domain ranks for, without crawling each SERP: `DataforseoLabsApi`.
- You need marketplace product data (Amazon, Google Shopping): `MerchantApi`; app store data: `AppDataApi`; business profiles and reviews: `BusinessDataApi`.
- You need answers of LLM chat assistants rather than search engines: `AiOptimizationApi`.

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### google_organic_task_post

`POST /v3/serp/google/organic/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.models.serp_google_organic_task_post_request_info import SerpGoogleOrganicTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    response = serp_api.google_organic_task_post([SerpGoogleOrganicTaskPostRequestInfo(
        language_code="en",
        location_code=2840,
        keyword="albert einstein",
    )]
    )
```

### google_organic_task_get_advanced

`GET /v3/serp/google/organic/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = serp_api.google_organic_task_get_advanced(id)
```

### google_organic_task_get_html

`GET /v3/serp/google/organic/task_get/html/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = serp_api.google_organic_task_get_html(id)
```

### google_maps_task_get_advanced

`GET /v3/serp/google/maps/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = serp_api.google_maps_task_get_advanced(id)
```

### google_maps_task_post

`POST /v3/serp/google/maps/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.models.serp_google_maps_task_post_request_info import SerpGoogleMapsTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    response = serp_api.google_maps_task_post([SerpGoogleMapsTaskPostRequestInfo(
        language_code="en",
        location_code=2840,
        keyword="albert einstein",
    )]
    )
```

### google_organic_task_get_regular

`GET /v3/serp/google/organic/task_get/regular/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = serp_api.google_organic_task_get_regular(id)
```

### google_organic_live_advanced

`POST /v3/serp/google/organic/live/advanced`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.models.serp_google_organic_live_advanced_request_info import SerpGoogleOrganicLiveAdvancedRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    response = serp_api.google_organic_live_advanced([SerpGoogleOrganicLiveAdvancedRequestInfo(
        language_code="en",
        location_code=2840,
        keyword="albert einstein",
        calculate_rectangles=True,
    )]
    )
```

### google_organic_tasks_ready

`GET /v3/serp/google/organic/tasks_ready`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    response = serp_api.google_organic_tasks_ready()
```

### google_ai_mode_task_post

`POST /v3/serp/google/ai_mode/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.models.serp_google_ai_mode_task_post_request_info import SerpGoogleAiModeTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    response = serp_api.google_ai_mode_task_post([SerpGoogleAiModeTaskPostRequestInfo(
        language_code="en",
        location_code=2840,
        keyword="what is google ai mode",
    )]
    )
```

## Endpoints

All methods of `SerpApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `id_list` | POST | `/v3/serp/id_list` |
| `errors` | POST | `/v3/serp/errors` |
| `screenshot` | POST | `/v3/serp/screenshot` |
| `ai_summary` | POST | `/v3/serp/ai_summary` |
| `google_locations` | GET | `/v3/serp/google/locations` |
| `google_locations_country` | GET | `/v3/serp/google/locations/{country}` |
| `google_languages` | GET | `/v3/serp/google/languages` |
| `google_organic_task_post` | POST | `/v3/serp/google/organic/task_post` |
| `google_organic_tasks_ready` | GET | `/v3/serp/google/organic/tasks_ready` |
| `tasks_ready` | GET | `/v3/serp/tasks_ready` |
| `google_organic_tasks_fixed` | GET | `/v3/serp/google/organic/tasks_fixed` |
| `google_organic_task_get_regular` | GET | `/v3/serp/google/organic/task_get/regular/{id}` |
| `google_organic_task_get_advanced` | GET | `/v3/serp/google/organic/task_get/advanced/{id}` |
| `google_organic_task_get_html` | GET | `/v3/serp/google/organic/task_get/html/{id}` |
| `google_organic_live_regular` | POST | `/v3/serp/google/organic/live/regular` |
| `google_organic_live_advanced` | POST | `/v3/serp/google/organic/live/advanced` |
| `google_organic_live_html` | POST | `/v3/serp/google/organic/live/html` |
| `google_ai_mode_languages` | GET | `/v3/serp/google/ai_mode/languages` |
| `google_ai_mode_task_post` | POST | `/v3/serp/google/ai_mode/task_post` |
| `google_ai_mode_tasks_ready` | GET | `/v3/serp/google/ai_mode/tasks_ready` |
| `google_ai_mode_tasks_fixed` | GET | `/v3/serp/google/ai_mode/tasks_fixed` |
| `google_ai_mode_task_get_advanced` | GET | `/v3/serp/google/ai_mode/task_get/advanced/{id}` |
| `google_ai_mode_task_get_html` | GET | `/v3/serp/google/ai_mode/task_get/html/{id}` |
| `google_ai_mode_live_advanced` | POST | `/v3/serp/google/ai_mode/live/advanced` |
| `google_ai_mode_live_html` | POST | `/v3/serp/google/ai_mode/live/html` |
| `google_maps_task_post` | POST | `/v3/serp/google/maps/task_post` |
| `google_maps_tasks_ready` | GET | `/v3/serp/google/maps/tasks_ready` |
| `google_maps_tasks_fixed` | GET | `/v3/serp/google/maps/tasks_fixed` |
| `google_maps_task_get_advanced` | GET | `/v3/serp/google/maps/task_get/advanced/{id}` |
| `google_maps_live_advanced` | POST | `/v3/serp/google/maps/live/advanced` |
| `google_local_finder_task_post` | POST | `/v3/serp/google/local_finder/task_post` |
| `google_local_finder_tasks_ready` | GET | `/v3/serp/google/local_finder/tasks_ready` |
| `google_local_finder_tasks_fixed` | GET | `/v3/serp/google/local_finder/tasks_fixed` |
| `google_local_finder_task_get_advanced` | GET | `/v3/serp/google/local_finder/task_get/advanced/{id}` |
| `google_local_finder_task_get_html` | GET | `/v3/serp/google/local_finder/task_get/html/{id}` |
| `google_local_finder_live_advanced` | POST | `/v3/serp/google/local_finder/live/advanced` |
| `google_local_finder_live_html` | POST | `/v3/serp/google/local_finder/live/html` |
| `google_news_task_post` | POST | `/v3/serp/google/news/task_post` |
| `google_news_tasks_ready` | GET | `/v3/serp/google/news/tasks_ready` |
| `google_news_tasks_fixed` | GET | `/v3/serp/google/news/tasks_fixed` |
| `google_news_task_get_advanced` | GET | `/v3/serp/google/news/task_get/advanced/{id}` |
| `google_news_task_get_html` | GET | `/v3/serp/google/news/task_get/html/{id}` |
| `google_news_live_advanced` | POST | `/v3/serp/google/news/live/advanced` |
| `google_news_live_html` | POST | `/v3/serp/google/news/live/html` |
| `google_images_task_post` | POST | `/v3/serp/google/images/task_post` |
| `google_images_tasks_ready` | GET | `/v3/serp/google/images/tasks_ready` |
| `google_images_tasks_fixed` | GET | `/v3/serp/google/images/tasks_fixed` |
| `google_images_task_get_advanced` | GET | `/v3/serp/google/images/task_get/advanced/{id}` |
| `google_images_task_get_html` | GET | `/v3/serp/google/images/task_get/html/{id}` |
| `google_images_live_advanced` | POST | `/v3/serp/google/images/live/advanced` |
| `google_images_live_html` | POST | `/v3/serp/google/images/live/html` |
| `google_search_by_image_task_post` | POST | `/v3/serp/google/search_by_image/task_post` |
| `google_search_by_image_tasks_ready` | GET | `/v3/serp/google/search_by_image/tasks_ready` |
| `google_search_by_image_tasks_fixed` | GET | `/v3/serp/google/search_by_image/tasks_fixed` |
| `google_search_by_image_task_get_advanced` | GET | `/v3/serp/google/search_by_image/task_get/advanced/{id}` |
| `google_jobs_task_post` | POST | `/v3/serp/google/jobs/task_post` |
| `google_jobs_tasks_ready` | GET | `/v3/serp/google/jobs/tasks_ready` |
| `google_jobs_tasks_fixed` | GET | `/v3/serp/google/jobs/tasks_fixed` |
| `google_jobs_task_get_advanced` | GET | `/v3/serp/google/jobs/task_get/advanced/{id}` |
| `google_jobs_task_get_html` | GET | `/v3/serp/google/jobs/task_get/html/{id}` |
| `google_autocomplete_task_post` | POST | `/v3/serp/google/autocomplete/task_post` |
| `google_autocomplete_tasks_ready` | GET | `/v3/serp/google/autocomplete/tasks_ready` |
| `google_autocomplete_tasks_fixed` | GET | `/v3/serp/google/autocomplete/tasks_fixed` |
| `google_autocomplete_task_get_advanced` | GET | `/v3/serp/google/autocomplete/task_get/advanced/{id}` |
| `google_autocomplete_live_advanced` | POST | `/v3/serp/google/autocomplete/live/advanced` |
| `google_dataset_search_task_post` | POST | `/v3/serp/google/dataset_search/task_post` |
| `google_dataset_search_tasks_ready` | GET | `/v3/serp/google/dataset_search/tasks_ready` |
| `google_dataset_search_tasks_fixed` | GET | `/v3/serp/google/dataset_search/tasks_fixed` |
| `google_dataset_search_task_get_advanced` | GET | `/v3/serp/google/dataset_search/task_get/advanced/{id}` |
| `google_dataset_search_live_advanced` | POST | `/v3/serp/google/dataset_search/live/advanced` |
| `google_dataset_info_task_post` | POST | `/v3/serp/google/dataset_info/task_post` |
| `google_dataset_info_tasks_ready` | GET | `/v3/serp/google/dataset_info/tasks_ready` |
| `google_dataset_info_tasks_fixed` | GET | `/v3/serp/google/dataset_info/tasks_fixed` |
| `google_dataset_info_task_get_advanced` | GET | `/v3/serp/google/dataset_info/task_get/advanced/{id}` |
| `google_dataset_info_live_advanced` | POST | `/v3/serp/google/dataset_info/live/advanced` |
| `google_ads_advertisers_locations` | GET | `/v3/serp/google/ads_advertisers/locations` |
| `google_ads_advertisers_task_post` | POST | `/v3/serp/google/ads_advertisers/task_post` |
| `google_ads_advertisers_tasks_ready` | GET | `/v3/serp/google/ads_advertisers/tasks_ready` |
| `google_ads_advertisers_task_get_advanced` | GET | `/v3/serp/google/ads_advertisers/task_get/advanced/{id}` |
| `google_ads_search_locations` | GET | `/v3/serp/google/ads_search/locations` |
| `google_ads_search_task_post` | POST | `/v3/serp/google/ads_search/task_post` |
| `google_ads_search_tasks_ready` | GET | `/v3/serp/google/ads_search/tasks_ready` |
| `google_ads_search_task_get_advanced` | GET | `/v3/serp/google/ads_search/task_get/advanced/{id}` |
| `bing_locations` | GET | `/v3/serp/bing/locations` |
| `bing_locations_country` | GET | `/v3/serp/bing/locations/{country}` |
| `bing_languages` | GET | `/v3/serp/bing/languages` |
| `bing_organic_task_post` | POST | `/v3/serp/bing/organic/task_post` |
| `bing_organic_tasks_ready` | GET | `/v3/serp/bing/organic/tasks_ready` |
| `bing_organic_tasks_fixed` | GET | `/v3/serp/bing/organic/tasks_fixed` |
| `bing_organic_task_get_regular` | GET | `/v3/serp/bing/organic/task_get/regular/{id}` |
| `bing_organic_task_get_advanced` | GET | `/v3/serp/bing/organic/task_get/advanced/{id}` |
| `bing_organic_task_get_html` | GET | `/v3/serp/bing/organic/task_get/html/{id}` |
| `bing_organic_live_regular` | POST | `/v3/serp/bing/organic/live/regular` |
| `bing_organic_live_advanced` | POST | `/v3/serp/bing/organic/live/advanced` |
| `bing_organic_live_html` | POST | `/v3/serp/bing/organic/live/html` |
| `youtube_locations` | GET | `/v3/serp/youtube/locations` |
| `youtube_locations_country` | GET | `/v3/serp/youtube/locations/{country}` |
| `youtube_languages` | GET | `/v3/serp/youtube/languages` |
| `youtube_video_info_task_post` | POST | `/v3/serp/youtube/video_info/task_post` |
| `youtube_video_info_tasks_ready` | GET | `/v3/serp/youtube/video_info/tasks_ready` |
| `youtube_video_info_tasks_fixed` | GET | `/v3/serp/youtube/video_info/tasks_fixed` |
| `youtube_video_info_task_get_advanced` | GET | `/v3/serp/youtube/video_info/task_get/advanced/{id}` |
| `youtube_video_info_live_advanced` | POST | `/v3/serp/youtube/video_info/live/advanced` |
| `youtube_organic_task_post` | POST | `/v3/serp/youtube/organic/task_post` |
| `youtube_organic_tasks_ready` | GET | `/v3/serp/youtube/organic/tasks_ready` |
| `youtube_organic_tasks_fixed` | GET | `/v3/serp/youtube/organic/tasks_fixed` |
| `youtube_organic_task_get_advanced` | GET | `/v3/serp/youtube/organic/task_get/advanced/{id}` |
| `youtube_organic_live_advanced` | POST | `/v3/serp/youtube/organic/live/advanced` |
| `youtube_video_subtitles_task_post` | POST | `/v3/serp/youtube/video_subtitles/task_post` |
| `youtube_video_subtitles_tasks_ready` | GET | `/v3/serp/youtube/video_subtitles/tasks_ready` |
| `youtube_video_subtitles_tasks_fixed` | GET | `/v3/serp/youtube/video_subtitles/tasks_fixed` |
| `youtube_video_subtitles_task_get_advanced` | GET | `/v3/serp/youtube/video_subtitles/task_get/advanced/{id}` |
| `youtube_video_subtitles_live_advanced` | POST | `/v3/serp/youtube/video_subtitles/live/advanced` |
| `youtube_video_comments_task_post` | POST | `/v3/serp/youtube/video_comments/task_post` |
| `youtube_video_comments_tasks_ready` | GET | `/v3/serp/youtube/video_comments/tasks_ready` |
| `youtube_video_comments_tasks_fixed` | GET | `/v3/serp/youtube/video_comments/tasks_fixed` |
| `youtube_video_comments_task_get_advanced` | GET | `/v3/serp/youtube/video_comments/task_get/advanced/{id}` |
| `youtube_video_comments_live_advanced` | POST | `/v3/serp/youtube/video_comments/live/advanced` |
| `yahoo_locations` | GET | `/v3/serp/yahoo/locations` |
| `yahoo_locations_country` | GET | `/v3/serp/yahoo/locations/{country}` |
| `yahoo_languages` | GET | `/v3/serp/yahoo/languages` |
| `yahoo_organic_task_post` | POST | `/v3/serp/yahoo/organic/task_post` |
| `yahoo_organic_tasks_ready` | GET | `/v3/serp/yahoo/organic/tasks_ready` |
| `yahoo_organic_tasks_fixed` | GET | `/v3/serp/yahoo/organic/tasks_fixed` |
| `yahoo_organic_task_get_regular` | GET | `/v3/serp/yahoo/organic/task_get/regular/{id}` |
| `yahoo_organic_task_get_advanced` | GET | `/v3/serp/yahoo/organic/task_get/advanced/{id}` |
| `yahoo_organic_task_get_html` | GET | `/v3/serp/yahoo/organic/task_get/html/{id}` |
| `yahoo_organic_live_regular` | POST | `/v3/serp/yahoo/organic/live/regular` |
| `yahoo_organic_live_advanced` | POST | `/v3/serp/yahoo/organic/live/advanced` |
| `yahoo_organic_live_html` | POST | `/v3/serp/yahoo/organic/live/html` |
| `baidu_locations` | GET | `/v3/serp/baidu/locations` |
| `baidu_locations_country` | GET | `/v3/serp/baidu/locations/{country}` |
| `baidu_languages` | GET | `/v3/serp/baidu/languages` |
| `baidu_organic_task_post` | POST | `/v3/serp/baidu/organic/task_post` |
| `baidu_organic_tasks_ready` | GET | `/v3/serp/baidu/organic/tasks_ready` |
| `baidu_organic_tasks_fixed` | GET | `/v3/serp/baidu/organic/tasks_fixed` |
| `baidu_organic_task_get_regular` | GET | `/v3/serp/baidu/organic/task_get/regular/{id}` |
| `baidu_organic_task_get_advanced` | GET | `/v3/serp/baidu/organic/task_get/advanced/{id}` |
| `baidu_organic_task_get_html` | GET | `/v3/serp/baidu/organic/task_get/html/{id}` |
| `naver_organic_task_post` | POST | `/v3/serp/naver/organic/task_post` |
| `naver_organic_tasks_ready` | GET | `/v3/serp/naver/organic/tasks_ready` |
| `naver_organic_tasks_fixed` | GET | `/v3/serp/naver/organic/tasks_fixed` |
| `naver_organic_task_get_regular` | GET | `/v3/serp/naver/organic/task_get/regular/{id}` |
| `naver_organic_task_get_advanced` | GET | `/v3/serp/naver/organic/task_get/advanced/{id}` |
| `naver_organic_task_get_html` | GET | `/v3/serp/naver/organic/task_get/html/{id}` |
| `seznam_locations` | GET | `/v3/serp/seznam/locations` |
| `seznam_locations_country` | GET | `/v3/serp/seznam/locations/{country}` |
| `seznam_languages` | GET | `/v3/serp/seznam/languages` |
| `seznam_organic_task_post` | POST | `/v3/serp/seznam/organic/task_post` |
| `seznam_organic_tasks_ready` | GET | `/v3/serp/seznam/organic/tasks_ready` |
| `seznam_organic_tasks_fixed` | GET | `/v3/serp/seznam/organic/tasks_fixed` |
| `seznam_organic_task_get_regular` | GET | `/v3/serp/seznam/organic/task_get/regular/{id}` |
| `seznam_organic_task_get_advanced` | GET | `/v3/serp/seznam/organic/task_get/advanced/{id}` |
| `seznam_organic_task_get_html` | GET | `/v3/serp/seznam/organic/task_get/html/{id}` |
| `google_finance_explore_task_post` | POST | `/v3/serp/google/finance_explore/task_post` |
| `google_finance_explore_tasks_ready` | GET | `/v3/serp/google/finance_explore/tasks_ready` |
| `google_finance_explore_task_get_advanced` | GET | `/v3/serp/google/finance_explore/task_get/advanced/{id}` |
| `google_finance_explore_task_get_html` | GET | `/v3/serp/google/finance_explore/task_get/html/{id}` |
| `google_finance_explore_live_advanced` | POST | `/v3/serp/google/finance_explore/live/advanced` |
| `google_finance_explore_live_html` | POST | `/v3/serp/google/finance_explore/live/html` |
| `google_finance_markets_task_post` | POST | `/v3/serp/google/finance_markets/task_post` |
| `google_finance_markets_tasks_ready` | GET | `/v3/serp/google/finance_markets/tasks_ready` |
| `google_finance_markets_task_get_advanced` | GET | `/v3/serp/google/finance_markets/task_get/advanced/{id}` |
| `google_finance_markets_task_get_html` | GET | `/v3/serp/google/finance_markets/task_get/html/{id}` |
| `google_finance_markets_live_advanced` | POST | `/v3/serp/google/finance_markets/live/advanced` |
| `google_finance_markets_live_html` | POST | `/v3/serp/google/finance_markets/live/html` |
| `google_finance_quote_task_post` | POST | `/v3/serp/google/finance_quote/task_post` |
| `google_finance_quote_tasks_ready` | GET | `/v3/serp/google/finance_quote/tasks_ready` |
| `google_finance_quote_task_get_advanced` | GET | `/v3/serp/google/finance_quote/task_get/advanced/{id}` |
| `google_finance_quote_task_get_html` | GET | `/v3/serp/google/finance_quote/task_get/html/{id}` |
| `google_finance_quote_live_advanced` | POST | `/v3/serp/google/finance_quote/live/advanced` |
| `google_finance_quote_live_html` | POST | `/v3/serp/google/finance_quote/live/html` |
| `google_finance_ticker_search_task_post` | POST | `/v3/serp/google/finance_ticker_search/task_post` |
| `google_finance_ticker_search_tasks_ready` | GET | `/v3/serp/google/finance_ticker_search/tasks_ready` |
| `google_finance_ticker_search_task_get_advanced` | GET | `/v3/serp/google/finance_ticker_search/task_get/advanced/{id}` |
| `google_finance_ticker_search_live_advanced` | POST | `/v3/serp/google/finance_ticker_search/live/advanced` |