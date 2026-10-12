# DomainAnalyticsApi

Knowledge base for `DomainAnalyticsApi` (`dataforseo_client.api.domain_analytics_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

Information about websites as such: the technologies a site is built with (CMS, analytics, frameworks, advertising and other tools), which sites use a given technology, statistics of technology usage, and domain registration (Whois) data enriched with search and backlink metrics.

## Use it when you need

- The technology profile of a website.
- Lists of websites that use a technology or contain certain terms in their HTML, for lead generation or market research, filtered by country, language or popularity.
- Market share and adoption trends of technologies.
- Domain registration details (registrar, creation, update and expiration dates), for example to find expiring domains, together with traffic and backlink indicators.

## Use another API when

- You need the content, technical SEO health or performance of a website's pages: `OnPageApi`.
- You need a website's backlinks: `BacklinksApi`; its keywords, rankings or traffic estimates: `DataforseoLabsApi`.

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### technologies_domain_technologies_live

`POST /v3/domain_analytics/technologies/domain_technologies/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.domain_analytics_api import DomainAnalyticsApi
from dataforseo_client.models.domain_analytics_technologies_domain_technologies_live_request_info import DomainAnalyticsTechnologiesDomainTechnologiesLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    domain_analytics_api = DomainAnalyticsApi(api_client)

    response = domain_analytics_api.technologies_domain_technologies_live([DomainAnalyticsTechnologiesDomainTechnologiesLiveRequestInfo(
        target="dataforseo.com",
    )]
    )
```

### whois_overview_live

`POST /v3/domain_analytics/whois/overview/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.domain_analytics_api import DomainAnalyticsApi
from dataforseo_client.models.domain_analytics_whois_overview_live_request_info import DomainAnalyticsWhoisOverviewLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    domain_analytics_api = DomainAnalyticsApi(api_client)

    response = domain_analytics_api.whois_overview_live([DomainAnalyticsWhoisOverviewLiveRequestInfo(
        limit=2,
        filters=[
            [
                "epp_status_codes",
                "in",
                [
                    "client_transfer_prohibited",
                    "client_update_prohibited",
                ],
            ],
        ],
    )]
    )
```

### technologies_domains_by_technology_live

`POST /v3/domain_analytics/technologies/domains_by_technology/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.domain_analytics_api import DomainAnalyticsApi
from dataforseo_client.models.domain_analytics_technologies_domains_by_technology_live_request_info import DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    domain_analytics_api = DomainAnalyticsApi(api_client)

    response = domain_analytics_api.technologies_domains_by_technology_live([DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo(
        technologies=[
            "Nginx",
        ],
        filters=[
            [
                "country_iso_code",
                "=",
                "US",
            ],
            "and",
            [
                "domain_rank",
                ">",
                800,
            ],
        ],
        order_by=[
            "last_visited,desc",
        ],
        limit=10,
    )]
    )
```

### domain_analytics_id_list

`POST /v3/domain_analytics/id_list`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.domain_analytics_api import DomainAnalyticsApi
from dataforseo_client.models.domain_analytics_id_list_request_info import DomainAnalyticsIdListRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    domain_analytics_api = DomainAnalyticsApi(api_client)

    response = domain_analytics_api.domain_analytics_id_list([DomainAnalyticsIdListRequestInfo(
        limit=10,
        include_metadata=True,
    )]
    )
```

### technologies_domains_by_html_terms_live

`POST /v3/domain_analytics/technologies/domains_by_html_terms/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.domain_analytics_api import DomainAnalyticsApi
from dataforseo_client.models.domain_analytics_technologies_domains_by_html_terms_live_request_info import DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    domain_analytics_api = DomainAnalyticsApi(api_client)

    response = domain_analytics_api.technologies_domains_by_html_terms_live([DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo(
        search_terms=[
            "data-attrid",
        ],
        order_by=[
            "last_visited,desc",
        ],
        limit=10,
        offset=0,
    )]
    )
```

### technologies_technologies

`GET /v3/domain_analytics/technologies/technologies`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.domain_analytics_api import DomainAnalyticsApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    domain_analytics_api = DomainAnalyticsApi(api_client)

    response = domain_analytics_api.technologies_technologies()
```

### technologies_aggregation_technologies_live

`POST /v3/domain_analytics/technologies/aggregation_technologies/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.domain_analytics_api import DomainAnalyticsApi
from dataforseo_client.models.domain_analytics_technologies_aggregation_technologies_live_request_info import DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    domain_analytics_api = DomainAnalyticsApi(api_client)

    response = domain_analytics_api.technologies_aggregation_technologies_live([DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo(
        mode="entry",
        technology="Nginx",
        keyword="WordPress",
        filters=[
            [
                "country_iso_code",
                "=",
                "US",
            ],
            "and",
            [
                "domain_rank",
                ">",
                800,
            ],
        ],
        order_by=[
            "groups_count,desc",
        ],
        limit=10,
    )]
    )
```

### technologies_technologies_summary_live

`POST /v3/domain_analytics/technologies/technologies_summary/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.domain_analytics_api import DomainAnalyticsApi
from dataforseo_client.models.domain_analytics_technologies_technologies_summary_live_request_info import DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    domain_analytics_api = DomainAnalyticsApi(api_client)

    response = domain_analytics_api.technologies_technologies_summary_live([DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo(
        mode="entry",
        technologies=[
            "Ngi",
        ],
        keywords=[
            "WordPress",
        ],
        filters=[
            [
                "country_iso_code",
                "=",
                "US",
            ],
            "and",
            [
                "domain_rank",
                ">",
                800,
            ],
        ],
    )]
    )
```

### technologies_locations

`GET /v3/domain_analytics/technologies/locations`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.domain_analytics_api import DomainAnalyticsApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    domain_analytics_api = DomainAnalyticsApi(api_client)

    response = domain_analytics_api.technologies_locations()
```

### technologies_technology_stats_live

`POST /v3/domain_analytics/technologies/technology_stats/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.domain_analytics_api import DomainAnalyticsApi
from dataforseo_client.models.domain_analytics_technologies_technology_stats_live_request_info import DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    domain_analytics_api = DomainAnalyticsApi(api_client)

    response = domain_analytics_api.technologies_technology_stats_live([DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo(
        technology="jQuery",
    )]
    )
```

## Endpoints

All methods of `DomainAnalyticsApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `domain_analytics_id_list` | POST | `/v3/domain_analytics/id_list` |
| `domain_analytics_errors` | POST | `/v3/domain_analytics/errors` |
| `technologies_available_filters` | GET | `/v3/domain_analytics/technologies/available_filters` |
| `technologies_locations` | GET | `/v3/domain_analytics/technologies/locations` |
| `technologies_languages` | GET | `/v3/domain_analytics/technologies/languages` |
| `technologies_technologies` | GET | `/v3/domain_analytics/technologies/technologies` |
| `technologies_aggregation_technologies_live` | POST | `/v3/domain_analytics/technologies/aggregation_technologies/live` |
| `technologies_technologies_summary_live` | POST | `/v3/domain_analytics/technologies/technologies_summary/live` |
| `technologies_technology_stats_live` | POST | `/v3/domain_analytics/technologies/technology_stats/live` |
| `technologies_domains_by_technology_live` | POST | `/v3/domain_analytics/technologies/domains_by_technology/live` |
| `technologies_domains_by_html_terms_live` | POST | `/v3/domain_analytics/technologies/domains_by_html_terms/live` |
| `technologies_domain_technologies_live` | POST | `/v3/domain_analytics/technologies/domain_technologies/live` |
| `whois_available_filters` | GET | `/v3/domain_analytics/whois/available_filters` |
| `whois_overview_live` | POST | `/v3/domain_analytics/whois/overview/live` |