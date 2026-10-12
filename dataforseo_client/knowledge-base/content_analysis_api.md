# ContentAnalysisApi

Knowledge base for `ContentAnalysisApi` (`dataforseo_client.api.content_analysis_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

Brand monitoring and sentiment analysis across the web: pages that mention (cite) a keyword or brand, with the sentiment polarity and emotional connotations of each mention, content ratings and categories, and aggregated trends of mentions over time.

## Use it when you need

- Where and how a brand, product, person or topic is mentioned on the web: news, blogs, forums, reviews and other pages.
- Whether mentions are positive, negative or neutral, and which emotions they carry.
- An aggregated picture of mentions: top sources, countries, languages, page types and content categories.
- How the volume and sentiment of mentions change over time for a keyword or a content category.

## Use another API when

- You need links pointing to a site rather than text mentions: `BacklinksApi`.
- You need mentions in AI assistant answers: `AiOptimizationApi`.
- You need reviews of a specific business on review platforms: `BusinessDataApi`.

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### search_live

`POST /v3/content_analysis/search/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.models.content_analysis_search_live_request_info import ContentAnalysisSearchLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    content_analysis_api = ContentAnalysisApi(api_client)

    response = content_analysis_api.search_live([ContentAnalysisSearchLiveRequestInfo(
        keyword_fields={
            "snippet": "logitech",
        },
        keyword="logitech",
        page_type=[
            "ecommerce",
            "news",
            "blogs",
            "message-boards",
            "organization",
        ],
        search_mode="as_is",
        filters=[
            "main_domain",
            "=",
            "reviewfinder.ca",
        ],
        order_by=[
            "content_info.sentiment_connotations.anger,desc",
        ],
        limit=10,
    )]
    )
```

### content_analysis_summary_live

`POST /v3/content_analysis/summary/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.models.content_analysis_summary_live_request_info import ContentAnalysisSummaryLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    content_analysis_api = ContentAnalysisApi(api_client)

    response = content_analysis_api.content_analysis_summary_live([ContentAnalysisSummaryLiveRequestInfo(
        keyword="logitech",
        page_type=[
            "ecommerce",
            "news",
            "blogs",
            "message-boards",
            "organization",
        ],
        internal_list_limit=8,
        positive_connotation_threshold=0.5,
    )]
    )
```

### phrase_trends_live

`POST /v3/content_analysis/phrase_trends/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.models.content_analysis_phrase_trends_live_request_info import ContentAnalysisPhraseTrendsLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    content_analysis_api = ContentAnalysisApi(api_client)

    response = content_analysis_api.phrase_trends_live([ContentAnalysisPhraseTrendsLiveRequestInfo(
        keyword="logitech",
        search_mode="as_is",
        date_group="month",
    )]
    )
```

### content_analysis_id_list

`POST /v3/content_analysis/id_list`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.models.content_analysis_id_list_request_info import ContentAnalysisIdListRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    content_analysis_api = ContentAnalysisApi(api_client)

    response = content_analysis_api.content_analysis_id_list([ContentAnalysisIdListRequestInfo(
        limit=10,
        include_metadata=True,
    )]
    )
```

### sentiment_analysis_live

`POST /v3/content_analysis/sentiment_analysis/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.models.content_analysis_sentiment_analysis_live_request_info import ContentAnalysisSentimentAnalysisLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    content_analysis_api = ContentAnalysisApi(api_client)

    response = content_analysis_api.sentiment_analysis_live([ContentAnalysisSentimentAnalysisLiveRequestInfo(
        keyword="logitech",
        internal_list_limit=1,
    )]
    )
```

### rating_distribution_live

`POST /v3/content_analysis/rating_distribution/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.models.content_analysis_rating_distribution_live_request_info import ContentAnalysisRatingDistributionLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    content_analysis_api = ContentAnalysisApi(api_client)

    response = content_analysis_api.rating_distribution_live([ContentAnalysisRatingDistributionLiveRequestInfo(
        keyword="logitech",
        search_mode="as_is",
        internal_list_limit=10,
    )]
    )
```

### languages

`GET /v3/content_analysis/languages`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    content_analysis_api = ContentAnalysisApi(api_client)

    response = content_analysis_api.languages()
```

### content_analysis_categories

`GET /v3/content_analysis/categories`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    content_analysis_api = ContentAnalysisApi(api_client)

    response = content_analysis_api.content_analysis_categories()
```

### locations

`GET /v3/content_analysis/locations`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    content_analysis_api = ContentAnalysisApi(api_client)

    response = content_analysis_api.locations()
```

### category_trends_live

`POST /v3/content_analysis/category_trends/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.content_analysis_api import ContentAnalysisApi
from dataforseo_client.models.content_analysis_category_trends_live_request_info import ContentAnalysisCategoryTrendsLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    content_analysis_api = ContentAnalysisApi(api_client)

    response = content_analysis_api.category_trends_live([ContentAnalysisCategoryTrendsLiveRequestInfo(
        category_code=10994,
        search_mode="as_is",
        date_group="month",
    )]
    )
```

## Endpoints

All methods of `ContentAnalysisApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `content_analysis_id_list` | POST | `/v3/content_analysis/id_list` |
| `content_analysis_available_filters` | GET | `/v3/content_analysis/available_filters` |
| `locations` | GET | `/v3/content_analysis/locations` |
| `languages` | GET | `/v3/content_analysis/languages` |
| `content_analysis_categories` | GET | `/v3/content_analysis/categories` |
| `search_live` | POST | `/v3/content_analysis/search/live` |
| `content_analysis_summary_live` | POST | `/v3/content_analysis/summary/live` |
| `sentiment_analysis_live` | POST | `/v3/content_analysis/sentiment_analysis/live` |
| `rating_distribution_live` | POST | `/v3/content_analysis/rating_distribution/live` |
| `phrase_trends_live` | POST | `/v3/content_analysis/phrase_trends/live` |
| `category_trends_live` | POST | `/v3/content_analysis/category_trends/live` |