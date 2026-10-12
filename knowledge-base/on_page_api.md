# OnPageApi

Knowledge base for `OnPageApi` (`dataforseo_client.api.on_page_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

Technical SEO audit of websites with a configurable crawler: crawl a site and get per-page checks, resources, internal and external links, duplicates, redirects, indexability issues, keyword density and page speed data; or analyze individual pages instantly, extract their content, take screenshots and run Google Lighthouse.

A full site audit is a crawl task: it is started once and its reports can be read while the crawl is running or after it finishes. Single-page analysis returns results immediately.

## Use it when you need

- A site health check: broken pages and resources, duplicate titles, descriptions or content, redirect chains, pages blocked from indexing and other on-page issues.
- The structure of a site: its pages, resources and the links between them.
- On-page data of a single URL: meta tags, headings, checks, parsed main content or the raw HTML.
- Performance, accessibility and best-practice scores of a page.

## Use another API when

- You need inbound links from other sites: `BacklinksApi`.
- You need how pages rank in search: `SerpApi` or `DataforseoLabsApi`.
- You need which technologies a site uses: `DomainAnalyticsApi`.

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### instant_pages

`POST /v3/on_page/instant_pages`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.models.on_page_instant_pages_request_info import OnPageInstantPagesRequestInfo

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
```

### raw_html

`POST /v3/on_page/raw_html`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.models.on_page_raw_html_request_info import OnPageRawHtmlRequestInfo

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
```

### summary

`GET /v3/on_page/summary/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    on_page_api = OnPageApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = on_page_api.summary(id)
```

### pages

`POST /v3/on_page/pages`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.models.on_page_pages_request_info import OnPagePagesRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    on_page_api = OnPageApi(api_client)

    response = on_page_api.pages([OnPagePagesRequestInfo(
        id="07281559-0695-0216-0000-c269be8b7592",
        filters=[
            [
                "resource_type",
                "=",
                "html",
            ],
            "and",
            [
                "meta.scripts_count",
                ">",
                40,
            ],
        ],
        order_by=[
            "meta.content.plain_text_word_count,desc",
        ],
        limit=10,
    )]
    )
```

### content_parsing_live

`POST /v3/on_page/content_parsing/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.models.on_page_content_parsing_live_request_info import OnPageContentParsingLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    on_page_api = OnPageApi(api_client)

    response = on_page_api.content_parsing_live([OnPageContentParsingLiveRequestInfo(
        url="https://dataforseo.com/blog/a-versatile-alternative-to-google-trends-exploring-the-power-of-dataforseo-trends-api",
    )]
    )
```

### task_post

`POST /v3/on_page/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.models.on_page_task_post_request_info import OnPageTaskPostRequestInfo

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
```

### links

`POST /v3/on_page/links`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.models.on_page_links_request_info import OnPageLinksRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    on_page_api = OnPageApi(api_client)

    response = on_page_api.links([OnPageLinksRequestInfo(
        id="07281559-0695-0216-0000-c269be8b7592",
        page_from="/apis/google-trends-api",
        filters=[
            [
                "dofollow",
                "=",
                True,
            ],
            "and",
            [
                "direction",
                "=",
                "external",
            ],
        ],
        limit=10,
    )]
    )
```

### microdata

`POST /v3/on_page/microdata`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi
from dataforseo_client.models.on_page_microdata_request_info import OnPageMicrodataRequestInfo

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
```

### on_page_tasks_ready

`GET /v3/on_page/tasks_ready`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.on_page_api import OnPageApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    on_page_api = OnPageApi(api_client)

    response = on_page_api.on_page_tasks_ready()
```

## Endpoints

All methods of `OnPageApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `on_page_id_list` | POST | `/v3/on_page/id_list` |
| `on_page_errors` | POST | `/v3/on_page/errors` |
| `force_stop` | POST | `/v3/on_page/force_stop` |
| `on_page_available_filters` | GET | `/v3/on_page/available_filters` |
| `task_post` | POST | `/v3/on_page/task_post` |
| `on_page_tasks_ready` | GET | `/v3/on_page/tasks_ready` |
| `summary` | GET | `/v3/on_page/summary/{id}` |
| `pages` | POST | `/v3/on_page/pages` |
| `pages_by_resource` | POST | `/v3/on_page/pages_by_resource` |
| `resources` | POST | `/v3/on_page/resources` |
| `duplicate_tags` | POST | `/v3/on_page/duplicate_tags` |
| `duplicate_content` | POST | `/v3/on_page/duplicate_content` |
| `links` | POST | `/v3/on_page/links` |
| `redirect_chains` | POST | `/v3/on_page/redirect_chains` |
| `non_indexable` | POST | `/v3/on_page/non_indexable` |
| `waterfall` | POST | `/v3/on_page/waterfall` |
| `keyword_density` | POST | `/v3/on_page/keyword_density` |
| `microdata` | POST | `/v3/on_page/microdata` |
| `uncrawlable_resources` | POST | `/v3/on_page/uncrawlable_resources` |
| `raw_html` | POST | `/v3/on_page/raw_html` |
| `page_screenshot` | POST | `/v3/on_page/page_screenshot` |
| `content_parsing` | POST | `/v3/on_page/content_parsing` |
| `content_parsing_live` | POST | `/v3/on_page/content_parsing/live` |
| `instant_pages` | POST | `/v3/on_page/instant_pages` |
| `lighthouse_languages` | GET | `/v3/on_page/lighthouse/languages` |
| `lighthouse_audits` | GET | `/v3/on_page/lighthouse/audits` |
| `lighthouse_versions` | GET | `/v3/on_page/lighthouse/versions` |
| `lighthouse_task_post` | POST | `/v3/on_page/lighthouse/task_post` |
| `lighthouse_tasks_ready` | GET | `/v3/on_page/lighthouse/tasks_ready` |
| `lighthouse_task_get_json` | GET | `/v3/on_page/lighthouse/task_get/json/{id}` |
| `lighthouse_live_json` | POST | `/v3/on_page/lighthouse/live/json` |