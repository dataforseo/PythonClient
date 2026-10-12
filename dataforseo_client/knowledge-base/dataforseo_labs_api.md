# DataforseoLabsApi

Knowledge base for `DataforseoLabsApi` (`dataforseo_client.api.dataforseo_labs_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

Keyword research, competitor analysis and search analytics from DataForSEO's own databases of keywords, search results and rankings, for search engines and platforms such as Google, Amazon, Google Play and the App Store.

Because the data is precomputed, one request can cover many keywords or domains, return historical data and combine metrics (search volume, keyword difficulty, search intent, rankings, estimated traffic) without crawling search results on demand.

## Use it when you need

- Keyword research: ideas, suggestions and related keywords for a topic, with their search volume, difficulty and intent.
- The keywords a domain, page, product or app ranks for, its positions and estimated traffic, now and in the past.
- Competitors of a domain, product or app in search, and the keywords they share or do not share (keyword gap).
- Market-level views: top searches, keyword categories, rankings across many domains at once.

## Use another API when

- You need live, exact search results for a specific query right now: `SerpApi`.
- You need search volume and CPC as reported by an advertising platform, ad traffic forecasts or trends: `KeywordsDataApi`.
- You need backlinks and link-based authority: `BacklinksApi`.
- You need AI search visibility rather than classic search: `AiOptimizationApi`.

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### google_ranked_keywords_live

`POST /v3/dataforseo_labs/google/ranked_keywords/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.models.dataforseo_labs_google_ranked_keywords_live_request_info import DataforseoLabsGoogleRankedKeywordsLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    dataforseo_labs_api = DataforseoLabsApi(api_client)

    response = dataforseo_labs_api.google_ranked_keywords_live([DataforseoLabsGoogleRankedKeywordsLiveRequestInfo(
        target="dataforseo.com",
        language_name="English",
        location_name="United States",
        load_rank_absolute=True,
        limit=3,
    )]
    )
```

### google_keyword_suggestions_live

`POST /v3/dataforseo_labs/google/keyword_suggestions/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.models.dataforseo_labs_google_keyword_suggestions_live_request_info import DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    dataforseo_labs_api = DataforseoLabsApi(api_client)

    response = dataforseo_labs_api.google_keyword_suggestions_live([DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo(
        keyword="phone",
        location_code=2840,
        language_code="en",
        include_serp_info=True,
        include_seed_keyword=True,
        limit=1,
    )]
    )
```

### google_domain_intersection_live

`POST /v3/dataforseo_labs/google/domain_intersection/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.models.dataforseo_labs_google_domain_intersection_live_request_info import DataforseoLabsGoogleDomainIntersectionLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    dataforseo_labs_api = DataforseoLabsApi(api_client)

    response = dataforseo_labs_api.google_domain_intersection_live([DataforseoLabsGoogleDomainIntersectionLiveRequestInfo(
        target_1="mom.com",
        target_2="quora.com",
        language_code="en",
        location_code=2840,
        include_serp_info=True,
        limit=3,
    )]
    )
```

### google_keyword_overview_live

`POST /v3/dataforseo_labs/google/keyword_overview/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.models.dataforseo_labs_google_keyword_overview_live_request_info import DataforseoLabsGoogleKeywordOverviewLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    dataforseo_labs_api = DataforseoLabsApi(api_client)

    response = dataforseo_labs_api.google_keyword_overview_live([DataforseoLabsGoogleKeywordOverviewLiveRequestInfo(
        language_code="en",
        location_code=2840,
        include_clickstream_data=True,
        include_serp_info=True,
        keywords=[
            "iphone",
        ],
    )]
    )
```

### google_historical_serps_live

`POST /v3/dataforseo_labs/google/historical_serps/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.models.dataforseo_labs_google_historical_serps_live_request_info import DataforseoLabsGoogleHistoricalSerpsLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    dataforseo_labs_api = DataforseoLabsApi(api_client)

    response = dataforseo_labs_api.google_historical_serps_live([DataforseoLabsGoogleHistoricalSerpsLiveRequestInfo(
        keyword="albert einstein",
        location_code=2840,
        language_code="en",
    )]
    )
```

### google_related_keywords_live

`POST /v3/dataforseo_labs/google/related_keywords/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.models.dataforseo_labs_google_related_keywords_live_request_info import DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    dataforseo_labs_api = DataforseoLabsApi(api_client)

    response = dataforseo_labs_api.google_related_keywords_live([DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo(
        keyword="phone",
        language_name="English",
        location_code=2840,
        limit=3,
    )]
    )
```

### google_domain_rank_overview_live

`POST /v3/dataforseo_labs/google/domain_rank_overview/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.models.dataforseo_labs_google_domain_rank_overview_live_request_info import DataforseoLabsGoogleDomainRankOverviewLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    dataforseo_labs_api = DataforseoLabsApi(api_client)

    response = dataforseo_labs_api.google_domain_rank_overview_live([DataforseoLabsGoogleDomainRankOverviewLiveRequestInfo(
        target="dataforseo.com",
        language_name="English",
        location_code=2840,
    )]
    )
```

### google_search_intent_live

`POST /v3/dataforseo_labs/google/search_intent/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.models.dataforseo_labs_google_search_intent_live_request_info import DataforseoLabsGoogleSearchIntentLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    dataforseo_labs_api = DataforseoLabsApi(api_client)

    response = dataforseo_labs_api.google_search_intent_live([DataforseoLabsGoogleSearchIntentLiveRequestInfo(
        keywords=[
            "login page",
            "audi a7",
            "elon musk",
            "milk store new york",
        ],
    )]
    )
```

### google_categories_for_domain_live

`POST /v3/dataforseo_labs/google/categories_for_domain/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.dataforseo_labs_api import DataforseoLabsApi
from dataforseo_client.models.dataforseo_labs_google_categories_for_domain_live_request_info import DataforseoLabsGoogleCategoriesForDomainLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    dataforseo_labs_api = DataforseoLabsApi(api_client)

    response = dataforseo_labs_api.google_categories_for_domain_live([DataforseoLabsGoogleCategoriesForDomainLiveRequestInfo(
        target="dataforseo.com",
        language_code="en",
        location_name="United States",
        item_types=[
            "paid",
            "organic",
            "featured_snippet",
            "local_pack",
        ],
        limit=3,
    )]
    )
```

## Endpoints

All methods of `DataforseoLabsApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `dataforseo_labs_id_list` | POST | `/v3/dataforseo_labs/id_list` |
| `status` | GET | `/v3/dataforseo_labs/status` |
| `dataforseo_labs_errors` | POST | `/v3/dataforseo_labs/errors` |
| `available_filters` | GET | `/v3/dataforseo_labs/available_filters` |
| `locations_and_languages` | GET | `/v3/dataforseo_labs/locations_and_languages` |
| `categories` | GET | `/v3/dataforseo_labs/categories` |
| `google_available_history` | GET | `/v3/dataforseo_labs/google/available_history` |
| `google_keywords_for_site_live` | POST | `/v3/dataforseo_labs/google/keywords_for_site/live` |
| `google_related_keywords_live` | POST | `/v3/dataforseo_labs/google/related_keywords/live` |
| `google_keyword_suggestions_live` | POST | `/v3/dataforseo_labs/google/keyword_suggestions/live` |
| `google_keyword_ideas_live` | POST | `/v3/dataforseo_labs/google/keyword_ideas/live` |
| `google_bulk_keyword_difficulty_live` | POST | `/v3/dataforseo_labs/google/bulk_keyword_difficulty/live` |
| `google_search_intent_live` | POST | `/v3/dataforseo_labs/google/search_intent/live` |
| `google_categories_for_keywords_languages` | GET | `/v3/dataforseo_labs/google/categories_for_keywords/languages` |
| `google_categories_for_domain_live` | POST | `/v3/dataforseo_labs/google/categories_for_domain/live` |
| `google_categories_for_keywords_live` | POST | `/v3/dataforseo_labs/google/categories_for_keywords/live` |
| `google_keywords_for_categories_live` | POST | `/v3/dataforseo_labs/google/keywords_for_categories/live` |
| `google_domain_metrics_by_categories_live` | POST | `/v3/dataforseo_labs/google/domain_metrics_by_categories/live` |
| `google_top_searches_live` | POST | `/v3/dataforseo_labs/google/top_searches/live` |
| `google_ranked_keywords_live` | POST | `/v3/dataforseo_labs/google/ranked_keywords/live` |
| `google_serp_competitors_live` | POST | `/v3/dataforseo_labs/google/serp_competitors/live` |
| `google_competitors_domain_live` | POST | `/v3/dataforseo_labs/google/competitors_domain/live` |
| `google_domain_intersection_live` | POST | `/v3/dataforseo_labs/google/domain_intersection/live` |
| `google_subdomains_live` | POST | `/v3/dataforseo_labs/google/subdomains/live` |
| `google_relevant_pages_live` | POST | `/v3/dataforseo_labs/google/relevant_pages/live` |
| `google_domain_rank_overview_live` | POST | `/v3/dataforseo_labs/google/domain_rank_overview/live` |
| `google_historical_serps_live` | POST | `/v3/dataforseo_labs/google/historical_serps/live` |
| `google_historical_rank_overview_live` | POST | `/v3/dataforseo_labs/google/historical_rank_overview/live` |
| `google_page_intersection_live` | POST | `/v3/dataforseo_labs/google/page_intersection/live` |
| `google_historical_search_volume_live` | POST | `/v3/dataforseo_labs/google/historical_search_volume/live` |
| `google_bulk_traffic_estimation_live` | POST | `/v3/dataforseo_labs/google/bulk_traffic_estimation/live` |
| `google_historical_bulk_traffic_estimation_live` | POST | `/v3/dataforseo_labs/google/historical_bulk_traffic_estimation/live` |
| `google_historical_keyword_data_live` | POST | `/v3/dataforseo_labs/google/historical_keyword_data/live` |
| `google_keyword_overview_live` | POST | `/v3/dataforseo_labs/google/keyword_overview/live` |
| `amazon_bulk_search_volume_live` | POST | `/v3/dataforseo_labs/amazon/bulk_search_volume/live` |
| `amazon_related_keywords_live` | POST | `/v3/dataforseo_labs/amazon/related_keywords/live` |
| `amazon_ranked_keywords_live` | POST | `/v3/dataforseo_labs/amazon/ranked_keywords/live` |
| `amazon_product_rank_overview_live` | POST | `/v3/dataforseo_labs/amazon/product_rank_overview/live` |
| `amazon_product_competitors_live` | POST | `/v3/dataforseo_labs/amazon/product_competitors/live` |
| `amazon_product_keyword_intersections_live` | POST | `/v3/dataforseo_labs/amazon/product_keyword_intersections/live` |
| `google_bulk_app_metrics_live` | POST | `/v3/dataforseo_labs/google/bulk_app_metrics/live` |
| `google_keywords_for_app_live` | POST | `/v3/dataforseo_labs/google/keywords_for_app/live` |
| `google_app_competitors_live` | POST | `/v3/dataforseo_labs/google/app_competitors/live` |
| `google_app_intersection_live` | POST | `/v3/dataforseo_labs/google/app_intersection/live` |
| `apple_bulk_app_metrics_live` | POST | `/v3/dataforseo_labs/apple/bulk_app_metrics/live` |
| `apple_keywords_for_app_live` | POST | `/v3/dataforseo_labs/apple/keywords_for_app/live` |
| `apple_app_competitors_live` | POST | `/v3/dataforseo_labs/apple/app_competitors/live` |
| `apple_app_intersection_live` | POST | `/v3/dataforseo_labs/apple/app_intersection/live` |