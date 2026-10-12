# KeywordsDataApi

Knowledge base for `KeywordsDataApi` (`dataforseo_client.api.keywords_data_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

Keyword metrics from advertising platforms and trend services: search volume, cost per click, competition and their monthly dynamics, keyword ideas, ad traffic forecasts and keyword popularity trends, from sources such as Google Ads, Bing Ads, Google Trends, DataForSEO Trends and clickstream data.

The data comes from the original sources, so it follows their rules: advertising platforms do not return data for restricted topics, and trend services return relative popularity rather than absolute numbers.

## Use it when you need

- Search volume, CPC and competition for a known list of keywords, as reported by an advertising platform.
- Keyword ideas suggested by an advertising platform for a website or for seed keywords.
- A forecast of impressions, clicks and cost for a planned advertising campaign.
- How interest in a keyword or topic changes over time and across regions, or which related topics and queries are rising.

## Use another API when

- You do SEO-oriented keyword research (difficulty, search intent, keywords a domain ranks for, competitors) or need large volumes of keywords from a database: `DataforseoLabsApi`.
- You need how often keywords are asked in AI assistants: `AiOptimizationApi`.
- You need what the search results look like for a keyword: `SerpApi`.

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### google_trends_explore_task_get

`GET /v3/keywords_data/google_trends/explore/task_get/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    keywords_data_api = KeywordsDataApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = keywords_data_api.google_trends_explore_task_get(id)
```

### google_trends_explore_task_post

`POST /v3/keywords_data/google_trends/explore/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.models.keywords_data_google_trends_explore_task_post_request_info import KeywordsDataGoogleTrendsExploreTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    keywords_data_api = KeywordsDataApi(api_client)

    response = keywords_data_api.google_trends_explore_task_post([KeywordsDataGoogleTrendsExploreTaskPostRequestInfo(
        type="youtube",
        category_code=3,
        keywords=[
            "seo api",
            "rank api",
        ],
    )]
    )
```

### google_ads_search_volume_live

`POST /v3/keywords_data/google_ads/search_volume/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.models.keywords_data_google_ads_search_volume_live_request_info import KeywordsDataGoogleAdsSearchVolumeLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    keywords_data_api = KeywordsDataApi(api_client)

    response = keywords_data_api.google_ads_search_volume_live([KeywordsDataGoogleAdsSearchVolumeLiveRequestInfo(
        location_code=2840,
        keywords=[
            "buy laptop",
            "cheap laptops for sale",
            "purchase laptop",
        ],
        search_partners=True,
    )]
    )
```

### bing_search_volume_live

`POST /v3/keywords_data/bing/search_volume/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.models.keywords_data_bing_search_volume_live_request_info import KeywordsDataBingSearchVolumeLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    keywords_data_api = KeywordsDataApi(api_client)

    response = keywords_data_api.bing_search_volume_live([KeywordsDataBingSearchVolumeLiveRequestInfo(
        location_name="United States",
        language_code="en",
        keywords=[
            "tom and jerry",
            "silicon valley",
            "spider man",
        ],
    )]
    )
```

### google_trends_explore_live

`POST /v3/keywords_data/google_trends/explore/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.models.keywords_data_google_trends_explore_live_request_info import KeywordsDataGoogleTrendsExploreLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    keywords_data_api = KeywordsDataApi(api_client)

    response = keywords_data_api.google_trends_explore_live([KeywordsDataGoogleTrendsExploreLiveRequestInfo(
        location_name="United States",
        type="youtube",
        category_code=3,
        keywords=[
            "rugby",
            "cricket",
        ],
    )]
    )
```

### google_ads_search_volume_task_get

`GET /v3/keywords_data/google_ads/search_volume/task_get/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    keywords_data_api = KeywordsDataApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = keywords_data_api.google_ads_search_volume_task_get(id)
```

### google_ads_search_volume_task_post

`POST /v3/keywords_data/google_ads/search_volume/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi
from dataforseo_client.models.keywords_data_google_ads_search_volume_task_post_request_info import KeywordsDataGoogleAdsSearchVolumeTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    keywords_data_api = KeywordsDataApi(api_client)

    response = keywords_data_api.google_ads_search_volume_task_post([KeywordsDataGoogleAdsSearchVolumeTaskPostRequestInfo(
        location_name="United States",
        keywords=[
            "buy laptop",
            "cheap laptops for sale",
            "purchase laptop",
        ],
    )]
    )
```

### google_ads_search_volume_tasks_ready

`GET /v3/keywords_data/google_ads/search_volume/tasks_ready`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.keywords_data_api import KeywordsDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    keywords_data_api = KeywordsDataApi(api_client)

    response = keywords_data_api.google_ads_search_volume_tasks_ready()
```

## Endpoints

All methods of `KeywordsDataApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `keywords_data_id_list` | POST | `/v3/keywords_data/id_list` |
| `keywords_data_errors` | POST | `/v3/keywords_data/errors` |
| `google_ads_status` | GET | `/v3/keywords_data/google_ads/status` |
| `google_ads_locations` | GET | `/v3/keywords_data/google_ads/locations` |
| `google_ads_locations_country` | GET | `/v3/keywords_data/google_ads/locations/{country}` |
| `google_ads_languages` | GET | `/v3/keywords_data/google_ads/languages` |
| `google_ads_search_volume_task_post` | POST | `/v3/keywords_data/google_ads/search_volume/task_post` |
| `google_ads_search_volume_tasks_ready` | GET | `/v3/keywords_data/google_ads/search_volume/tasks_ready` |
| `google_ads_search_volume_task_get` | GET | `/v3/keywords_data/google_ads/search_volume/task_get/{id}` |
| `google_ads_search_volume_live` | POST | `/v3/keywords_data/google_ads/search_volume/live` |
| `google_ads_keywords_for_site_task_post` | POST | `/v3/keywords_data/google_ads/keywords_for_site/task_post` |
| `google_ads_keywords_for_site_tasks_ready` | GET | `/v3/keywords_data/google_ads/keywords_for_site/tasks_ready` |
| `google_ads_keywords_for_site_task_get` | GET | `/v3/keywords_data/google_ads/keywords_for_site/task_get/{id}` |
| `google_ads_keywords_for_site_live` | POST | `/v3/keywords_data/google_ads/keywords_for_site/live` |
| `google_ads_keywords_for_keywords_task_post` | POST | `/v3/keywords_data/google_ads/keywords_for_keywords/task_post` |
| `google_ads_keywords_for_keywords_tasks_ready` | GET | `/v3/keywords_data/google_ads/keywords_for_keywords/tasks_ready` |
| `google_ads_keywords_for_keywords_task_get` | GET | `/v3/keywords_data/google_ads/keywords_for_keywords/task_get/{id}` |
| `google_ads_keywords_for_keywords_live` | POST | `/v3/keywords_data/google_ads/keywords_for_keywords/live` |
| `google_ads_ad_traffic_by_keywords_task_post` | POST | `/v3/keywords_data/google_ads/ad_traffic_by_keywords/task_post` |
| `google_ads_ad_traffic_by_keywords_tasks_ready` | GET | `/v3/keywords_data/google_ads/ad_traffic_by_keywords/tasks_ready` |
| `google_ads_ad_traffic_by_keywords_task_get` | GET | `/v3/keywords_data/google_ads/ad_traffic_by_keywords/task_get/{id}` |
| `google_ads_ad_traffic_by_keywords_live` | POST | `/v3/keywords_data/google_ads/ad_traffic_by_keywords/live` |
| `google_trends_locations` | GET | `/v3/keywords_data/google_trends/locations` |
| `google_trends_locations_country` | GET | `/v3/keywords_data/google_trends/locations/{country}` |
| `google_trends_languages` | GET | `/v3/keywords_data/google_trends/languages` |
| `google_trends_categories` | GET | `/v3/keywords_data/google_trends/categories` |
| `google_trends_explore_task_post` | POST | `/v3/keywords_data/google_trends/explore/task_post` |
| `google_trends_explore_tasks_ready` | GET | `/v3/keywords_data/google_trends/explore/tasks_ready` |
| `google_trends_explore_task_get` | GET | `/v3/keywords_data/google_trends/explore/task_get/{id}` |
| `google_trends_explore_live` | POST | `/v3/keywords_data/google_trends/explore/live` |
| `dataforseo_trends_locations` | GET | `/v3/keywords_data/dataforseo_trends/locations` |
| `dataforseo_trends_locations_country` | GET | `/v3/keywords_data/dataforseo_trends/locations/{country}` |
| `dataforseo_trends_explore_live` | POST | `/v3/keywords_data/dataforseo_trends/explore/live` |
| `dataforseo_trends_subregion_interests_live` | POST | `/v3/keywords_data/dataforseo_trends/subregion_interests/live` |
| `dataforseo_trends_demography_live` | POST | `/v3/keywords_data/dataforseo_trends/demography/live` |
| `dataforseo_trends_merged_data_live` | POST | `/v3/keywords_data/dataforseo_trends/merged_data/live` |
| `keywords_data_bing_locations` | GET | `/v3/keywords_data/bing/locations` |
| `keywords_data_bing_languages` | GET | `/v3/keywords_data/bing/languages` |
| `bing_search_volume_task_post` | POST | `/v3/keywords_data/bing/search_volume/task_post` |
| `bing_search_volume_tasks_ready` | GET | `/v3/keywords_data/bing/search_volume/tasks_ready` |
| `bing_search_volume_task_get` | GET | `/v3/keywords_data/bing/search_volume/task_get/{id}` |
| `bing_search_volume_live` | POST | `/v3/keywords_data/bing/search_volume/live` |
| `bing_audience_estimation_job_functions` | GET | `/v3/keywords_data/bing/audience_estimation/job_functions` |
| `bing_audience_estimation_industries` | GET | `/v3/keywords_data/bing/audience_estimation/industries` |
| `bing_audience_estimation_task_post` | POST | `/v3/keywords_data/bing/audience_estimation/task_post` |
| `bing_audience_estimation_tasks_ready` | GET | `/v3/keywords_data/bing/audience_estimation/tasks_ready` |
| `bing_audience_estimation_task_get` | GET | `/v3/keywords_data/bing/audience_estimation/task_get/{id}` |
| `bing_audience_estimation_live` | POST | `/v3/keywords_data/bing/audience_estimation/live` |
| `bing_keywords_for_site_task_post` | POST | `/v3/keywords_data/bing/keywords_for_site/task_post` |
| `bing_keywords_for_site_tasks_ready` | GET | `/v3/keywords_data/bing/keywords_for_site/tasks_ready` |
| `bing_keywords_for_site_task_get` | GET | `/v3/keywords_data/bing/keywords_for_site/task_get/{id}` |
| `bing_keywords_for_site_live` | POST | `/v3/keywords_data/bing/keywords_for_site/live` |
| `bing_keywords_for_keywords_task_post` | POST | `/v3/keywords_data/bing/keywords_for_keywords/task_post` |
| `bing_keywords_for_keywords_tasks_ready` | GET | `/v3/keywords_data/bing/keywords_for_keywords/tasks_ready` |
| `bing_keywords_for_keywords_task_get` | GET | `/v3/keywords_data/bing/keywords_for_keywords/task_get/{id}` |
| `bing_keywords_for_keywords_live` | POST | `/v3/keywords_data/bing/keywords_for_keywords/live` |
| `bing_keyword_performance_locations_and_languages` | GET | `/v3/keywords_data/bing/keyword_performance/locations_and_languages` |
| `bing_keyword_performance_task_post` | POST | `/v3/keywords_data/bing/keyword_performance/task_post` |
| `bing_keyword_performance_tasks_ready` | GET | `/v3/keywords_data/bing/keyword_performance/tasks_ready` |
| `bing_keyword_performance_task_get` | GET | `/v3/keywords_data/bing/keyword_performance/task_get/{id}` |
| `bing_keyword_performance_live` | POST | `/v3/keywords_data/bing/keyword_performance/live` |
| `bing_search_volume_history_locations_and_languages` | GET | `/v3/keywords_data/bing/search_volume_history/locations_and_languages` |
| `bing_search_volume_history_task_post` | POST | `/v3/keywords_data/bing/search_volume_history/task_post` |
| `bing_search_volume_history_tasks_ready` | GET | `/v3/keywords_data/bing/search_volume_history/tasks_ready` |
| `bing_search_volume_history_task_get` | GET | `/v3/keywords_data/bing/search_volume_history/task_get/{id}` |
| `bing_search_volume_history_live` | POST | `/v3/keywords_data/bing/search_volume_history/live` |
| `clickstream_data_locations_and_languages` | GET | `/v3/keywords_data/clickstream_data/locations_and_languages` |
| `clickstream_data_dataforseo_search_volume_live` | POST | `/v3/keywords_data/clickstream_data/dataforseo_search_volume/live` |
| `clickstream_data_global_search_volume_live` | POST | `/v3/keywords_data/clickstream_data/global_search_volume/live` |
| `clickstream_data_bulk_search_volume_live` | POST | `/v3/keywords_data/clickstream_data/bulk_search_volume/live` |