# BacklinksApi

Knowledge base for `BacklinksApi` (`dataforseo_client.api.backlinks_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

Backlink data for any domain, subdomain or web page from DataForSEO's continuously updated link index: inbound links, referring domains, pages and networks, anchor texts, link-based authority (rank) and spam score, how the link profile changes over time, and how it compares with other sites.

Data is returned immediately from the index and can be filtered, sorted and paged. Many metrics are also available in bulk for large lists of targets.

## Use it when you need

- An overview of a site's link profile and authority.
- Detailed lists of backlinks, referring domains or anchors of a target, filtered by attributes such as dofollow, first seen date or authority.
- New and lost links over time, or the history of a link profile.
- Link building and competitive research: sites with similar link profiles, or domains that link to competitors but not to you.
- Quick authority or spam checks for many domains or URLs at once.

## Use another API when

- You need search rankings, keywords or traffic of a site: `DataforseoLabsApi` or `SerpApi`.
- You need a technical audit of a site, including its internal and outgoing links: `OnPageApi`.
- You need mentions of a brand without a link: `ContentAnalysisApi` (web) or `AiOptimizationApi` (AI answers).

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### backlinks_live

`POST /v3/backlinks/backlinks/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.models.backlinks_backlinks_live_request_info import BacklinksBacklinksLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    backlinks_api = BacklinksApi(api_client)

    response = backlinks_api.backlinks_live([BacklinksBacklinksLiveRequestInfo(
        target="forbes.com",
        mode="as_is",
        filters=[
            "dofollow",
            "=",
            True,
        ],
        limit=5,
    )]
    )
```

### summary_live

`POST /v3/backlinks/summary/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.models.backlinks_summary_live_request_info import BacklinksSummaryLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    backlinks_api = BacklinksApi(api_client)

    response = backlinks_api.summary_live([BacklinksSummaryLiveRequestInfo(
        target="explodingtopics.com",
        internal_list_limit=10,
        include_subdomains=True,
        backlinks_filters=[
            "dofollow",
            "=",
            True,
        ],
        backlinks_status_type="all",
    )]
    )
```

### referring_domains_live

`POST /v3/backlinks/referring_domains/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.models.backlinks_referring_domains_live_request_info import BacklinksReferringDomainsLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    backlinks_api = BacklinksApi(api_client)

    response = backlinks_api.referring_domains_live([BacklinksReferringDomainsLiveRequestInfo(
        target="backlinko.com",
        limit=5,
        order_by=[
            "rank,desc",
        ],
        exclude_internal_backlinks=True,
        backlinks_filters=[
            "dofollow",
            "=",
            True,
        ],
        filters=[
            "backlinks",
            ">",
            100,
        ],
    )]
    )
```

### bulk_ranks_live

`POST /v3/backlinks/bulk_ranks/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.models.backlinks_bulk_ranks_live_request_info import BacklinksBulkRanksLiveRequestInfo

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
```

### anchors_live

`POST /v3/backlinks/anchors/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.models.backlinks_anchors_live_request_info import BacklinksAnchorsLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    backlinks_api = BacklinksApi(api_client)

    response = backlinks_api.anchors_live([BacklinksAnchorsLiveRequestInfo(
        target="forbes.com",
        limit=4,
        order_by=[
            "backlinks,desc",
        ],
        filters=[
            "anchor",
            "like",
            "%news%",
        ],
    )]
    )
```

### bulk_referring_domains_live

`POST /v3/backlinks/bulk_referring_domains/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.models.backlinks_bulk_referring_domains_live_request_info import BacklinksBulkReferringDomainsLiveRequestInfo

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
```

### bulk_pages_summary_live

`POST /v3/backlinks/bulk_pages_summary/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.models.backlinks_bulk_pages_summary_live_request_info import BacklinksBulkPagesSummaryLiveRequestInfo

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
```

### history_live

`POST /v3/backlinks/history/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.models.backlinks_history_live_request_info import BacklinksHistoryLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    backlinks_api = BacklinksApi(api_client)

    response = backlinks_api.history_live([BacklinksHistoryLiveRequestInfo(
        target="cnn.com",
    )]
    )
```

### bulk_backlinks_live

`POST /v3/backlinks/bulk_backlinks/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.backlinks_api import BacklinksApi
from dataforseo_client.models.backlinks_bulk_backlinks_live_request_info import BacklinksBulkBacklinksLiveRequestInfo

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
```

## Endpoints

All methods of `BacklinksApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `backlinks_id_list` | POST | `/v3/backlinks/id_list` |
| `backlinks_errors` | POST | `/v3/backlinks/errors` |
| `backlinks_available_filters` | GET | `/v3/backlinks/available_filters` |
| `index` | GET | `/v3/backlinks/index` |
| `summary_live` | POST | `/v3/backlinks/summary/live` |
| `history_live` | POST | `/v3/backlinks/history/live` |
| `backlinks_live` | POST | `/v3/backlinks/backlinks/live` |
| `anchors_live` | POST | `/v3/backlinks/anchors/live` |
| `domain_pages_live` | POST | `/v3/backlinks/domain_pages/live` |
| `domain_pages_summary_live` | POST | `/v3/backlinks/domain_pages_summary/live` |
| `referring_domains_live` | POST | `/v3/backlinks/referring_domains/live` |
| `referring_networks_live` | POST | `/v3/backlinks/referring_networks/live` |
| `competitors_live` | POST | `/v3/backlinks/competitors/live` |
| `domain_intersection_live` | POST | `/v3/backlinks/domain_intersection/live` |
| `page_intersection_live` | POST | `/v3/backlinks/page_intersection/live` |
| `timeseries_summary_live` | POST | `/v3/backlinks/timeseries_summary/live` |
| `timeseries_new_lost_summary_live` | POST | `/v3/backlinks/timeseries_new_lost_summary/live` |
| `bulk_ranks_live` | POST | `/v3/backlinks/bulk_ranks/live` |
| `bulk_backlinks_live` | POST | `/v3/backlinks/bulk_backlinks/live` |
| `bulk_spam_score_live` | POST | `/v3/backlinks/bulk_spam_score/live` |
| `bulk_referring_domains_live` | POST | `/v3/backlinks/bulk_referring_domains/live` |
| `bulk_new_lost_backlinks_live` | POST | `/v3/backlinks/bulk_new_lost_backlinks/live` |
| `bulk_new_lost_referring_domains_live` | POST | `/v3/backlinks/bulk_new_lost_referring_domains/live` |
| `bulk_pages_summary_live` | POST | `/v3/backlinks/bulk_pages_summary/live` |