---
name: dataforseo-python-client
description: Use the DataForSEO Python client (pip package dataforseo-client, module dataforseo_client) to call DataForSEO API v3 (SERP, Keywords Data, DataForSEO Labs, Backlinks, OnPage, AI Optimization, etc.). Read this before exploring the code; it explains the layout, naming rules and how to find an endpoint without reading the huge generated files.
---

# DataForSEO Python client

Generated, typed (pydantic v2) Python client for DataForSEO API v3.
Every API endpoint is one method; every request/response body is one model class.

- Package: `pip install dataforseo-client`, import as `dataforseo_client`
- HTTP: `urllib3`, synchronous
- Base URL: `https://api.dataforseo.com` (sandbox with free dummy data: `https://sandbox.dataforseo.com`)
- Auth: HTTP Basic with the DataForSEO API login and password (not the dashboard password)

## Do not read generated code in full

The client is generated from an OpenAPI spec and is very large (thousands of model files, `api/*_api.py` files up to ~1 MB, very long field descriptions in every model). Never open files whole. Derive names with the rules below and use targeted search (grep) only to confirm them.

## Knowledge base: start here

`knowledge-base/` (next to this file) has one Markdown file per API section, i.e. per class in `api/`. Each file explains what data the section provides and when to use another section instead, gives ready-to-run examples and lists every endpoint with its method name. Open only the file of the section you need: it is much cheaper than searching the generated code.

| API class | Use it for |
|---|---|
| [`SerpApi`](knowledge-base/serp_api.md) | Search engine results pages (SERP) collected on request: what a search engine shows for a query in a given location, language and device, from engines such as Google, Bing, YouTube, Yahoo and others, including search verticals such as maps, news, images, jobs and AI search modes. |
| [`DataforseoLabsApi`](knowledge-base/dataforseo_labs_api.md) | Keyword research, competitor analysis and search analytics from DataForSEO's own databases of keywords, search results and rankings, for search engines and platforms such as Google, Amazon, Google Play and the App Store. |
| [`DomainAnalyticsApi`](knowledge-base/domain_analytics_api.md) | Information about websites as such: the technologies a site is built with (CMS, analytics, frameworks, advertising and other tools), which sites use a given technology, statistics of technology usage, and domain registration (Whois) data enriched with search and backlink metrics. |
| [`KeywordsDataApi`](knowledge-base/keywords_data_api.md) | Keyword metrics from advertising platforms and trend services: search volume, cost per click, competition and their monthly dynamics, keyword ideas, ad traffic forecasts and keyword popularity trends, from sources such as Google Ads, Bing Ads, Google Trends, DataForSEO Trends and clickstream data. |
| [`BacklinksApi`](knowledge-base/backlinks_api.md) | Backlink data for any domain, subdomain or web page from DataForSEO's continuously updated link index: inbound links, referring domains, pages and networks, anchor texts, link-based authority (rank) and spam score, how the link profile changes over time, and how it compares with other sites. |
| [`AiOptimizationApi`](knowledge-base/ai_optimization_api.md) | Data for AI search optimization (GEO): answers of large language models such as ChatGPT, Claude, Gemini and Perplexity to your prompts, results scraped from the web interfaces of AI assistants, search volume of keywords in AI tools, and how often brands, domains and pages are mentioned in AI-generated answers. |
| [`OnPageApi`](knowledge-base/on_page_api.md) | Technical SEO audit of websites with a configurable crawler: crawl a site and get per-page checks, resources, internal and external links, duplicates, redirects, indexability issues, keyword density and page speed data; or analyze individual pages instantly, extract their content, take screenshots and run Google Lighthouse. |
| [`ContentAnalysisApi`](knowledge-base/content_analysis_api.md) | Brand monitoring and sentiment analysis across the web: pages that mention (cite) a keyword or brand, with the sentiment polarity and emotional connotations of each mention, content ratings and categories, and aggregated trends of mentions over time. |
| [`MerchantApi`](knowledge-base/merchant_api.md) | E-commerce data from marketplaces and shopping search engines such as Amazon and Google Shopping: product listings for a search query, product details, product variations, sellers and their offers, with prices, ratings, reviews count and paid placements. |
| [`AppDataApi`](knowledge-base/app_data_api.md) | Mobile application data from app stores such as Google Play and the App Store: app search results, top charts and collections, detailed app information and user reviews, plus a searchable database of app listings. |
| [`BusinessDataApi`](knowledge-base/business_data_api.md) | Publicly available data about businesses and local places: business profiles, reviews, questions and answers, hotel data and a database of business listings, from sources such as Google, Trustpilot and Tripadvisor. |
| [`AppendixApi`](knowledge-base/appendix_api.md) | Account and service information that applies to the whole DataForSEO API rather than to a data source: account balance, spending, limits and prices, the current status of the APIs, the list of error codes, and re-sending webhooks (pingbacks and postbacks) of completed tasks. |

## Layout

Paths are relative to the `dataforseo_client` package (a top-level folder in the repository; after `pip install` it is `site-packages/dataforseo_client/`, where copies of this file and of `knowledge-base/` also live):

```
configuration.py                 Configuration (credentials, host, proxy, ssl, retries)
api_client.py                    ApiClient (HTTP transport, context manager)
exceptions.py                    ApiException and subclasses
api/<section>_api.py             one class per API section, one method per endpoint
models/<class_name>.py           one pydantic model per file (snake_case file, PascalCase class)
knowledge-base/<section>_api.md  per-section guide with examples (see above)
```

## Naming rules (derive names instead of searching)

Endpoint path `/v3/<section>/<rest>` maps to:

| What | Rule | Example for `/v3/serp/google/organic/live/advanced` |
|---|---|---|
| API class / module | `<Section>Api` in `api/<section>_api.py` | `SerpApi` in `dataforseo_client.api.serp_api` |
| Method | snake_case of `<rest>` (usually) | `google_organic_live_advanced` |
| Request model | `<Section><Rest>RequestInfo` | `SerpGoogleOrganicLiveAdvancedRequestInfo` |
| Response model | `<Section><Rest>ResponseInfo` | `SerpGoogleOrganicLiveAdvancedResponseInfo` |
| Task item | `<Section><Rest>TaskInfo` | `SerpGoogleOrganicLiveAdvancedTaskInfo` |
| Result item | `<Section><Rest>ResultInfo` | `SerpGoogleOrganicLiveAdvancedResultInfo` |
| Model module | snake_case of class name | `dataforseo_client.models.serp_google_organic_live_advanced_request_info` |

Model names follow the rule strictly. Method names sometimes keep the section prefix (e.g. `dataforseo_labs_id_list`), so confirm the method with one search (the pattern also matches a prefixed name):

```bash
grep -n "def [a-z_]*google_organic_live_advanced(" api/serp_api.py
```

Model fields and their descriptions (required/optional, allowed values, limits) are in `Field(description=...)`. The lines are very long, so list field names first and then grep only the fields you need:

```bash
grep -oE "^    [a-z_0-9]+:" models/serp_google_organic_live_advanced_request_info.py   # field names
grep -n "^    location_code:" models/serp_google_organic_live_advanced_request_info.py  # one field with description
```

## Method shapes

- `POST` endpoints: `x(list_optional_x_request_info: List[XRequestInfo]) -> XResponseInfo`, the body is always a list of tasks. Pass it positionally.
- `GET` endpoints: `x() -> XResponseInfo` or `x(id)` (task id for `task_get_*`, `country` for locations etc.).
- Every method also has `x_with_http_info(...)` (returns `ApiResponse` with `status_code`, `headers`, `data`) and `x_without_preload_content(...)` (raw urllib3 response).
- Every method accepts `_request_timeout` (seconds or `(connect, read)` tuple) and `_headers`.

## Setup

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi

configuration = dfs_config.Configuration(username="API_LOGIN", password="API_PASSWORD")
# sandbox: dfs_config.Configuration(host="https://sandbox.dataforseo.com", username=..., password=...)

with dfs_api_provider.ApiClient(configuration) as api_client:
    serp_api = SerpApi(api_client)
    ...
```

Create one `ApiClient` and reuse it for all section classes.

## Live request (result in the same call)

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.serp_google_organic_live_advanced_request_info import SerpGoogleOrganicLiveAdvancedRequestInfo
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')
with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    try:

        api_response = serp_api.google_organic_live_advanced([SerpGoogleOrganicLiveAdvancedRequestInfo(
            language_name="English",
            location_name="United States",
            keyword="albert einstein"
        )])
        
        pprint(api_response)
    
    except ApiException as e:
        print("Exception: %s\n" % e)
```

## Task-based request (post -> wait -> get)

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.serp_google_organic_task_post_request_info import SerpGoogleOrganicTaskPostRequestInfo
from pprint import pprint
import time

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')

def GoogleOrganicTaskReady(id):
    result = serp_api.google_organic_tasks_ready()
    return any(any(xx.id == id for xx in (x.result or [])) for x in (result.tasks or []))

with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    try:

        task_post = serp_api.google_organic_task_post([SerpGoogleOrganicTaskPostRequestInfo(
            language_name="English",
            location_name="United States",
            keyword="albert einstein"
        )])

        task_id = task_post.tasks[0].id

        start_time = time.time()

        while GoogleOrganicTaskReady(task_id) is not True and (time.time() - start_time) < 60:
            time.sleep(1)

        api_response = serp_api.google_organic_task_get_advanced(id=task_id)
        
        pprint(api_response)
    
    except ApiException as e:
        print("Exception: %s\n" % e)
```

Instead of polling you can set `postback_url` / `pingback_url` in the task request.

## Response envelope (same for every endpoint)

```
XResponseInfo
  version, status_code, status_message, time, cost, tasks_count, tasks_error
  tasks: List[XTaskInfo]
    XTaskInfo
      id, status_code, status_message, time, cost, result_count, path, data (echo of the request)
      result: List[XResultInfo]   # endpoint specific payload, often with items
```

- `status_code == 20000` means OK (both top-level and per task); `20100` = task created; `4xxxx`/`5xxxx` = errors. Always check the per-task `status_code`: the HTTP status is usually 200 even when a task failed.
- All fields are `Optional`; guard lists with `or []`.
- Models are pydantic: `to_dict()`, `to_json()`, `from_dict()`, `from_json()` are available.

## Polymorphic items

Lists like `items` are typed as a base class (e.g. `BaseSerpApiElementItem`) and deserialized into concrete subclasses by the JSON `type` field (`organic` -> `OrganicSerpElementItem`, `paid` -> `PaidSerpElementItem`, `featured_snippet` -> `FeaturedSnippetSerpElementItem`, ...). Use `isinstance`. The mapping is in `__discriminator_value_class_map` of the base model file; grep there instead of reading it.

## Errors

`dataforseo_client.exceptions` (also re-exported from `dataforseo_client.rest`): `ApiException` with `status`, `reason`, `body`, `headers`; subclasses `BadRequestException` (400), `UnauthorizedException` (401), `ForbiddenException` (403), `NotFoundException` (404), `ServiceException` (5xx). Client-side validation errors raise pydantic `ValidationError`.

## Useful facts

- Location / language codes: `location_code=2840` (United States), `language_code="en"`. Full lists come from endpoints like `SerpApi.google_locations()` / `google_languages()` (and similar per section).
- Most Live endpoints accept one task per request; Task POST endpoints accept many tasks (up to 100) in one call.
- `task_get_*` has several variants (`regular`, `advanced`, `html`); use the one matching the data you need.
- Field semantics, allowed values and limits: the `description` of the model field (it comes from the official API docs).

## External documentation (last resort)

Use https://dataforseo.com/llms.txt only when this file, the knowledge base or generated code do not answer the question (for example pricing, account limits or endpoint behaviour that is not described locally). Everything needed to write client code is already in this library.

`llms.txt` is a large (~200 KB) index of links to per-endpoint Markdown pages (`https://docs.dataforseo.com/v3/...md`). Do not read it whole: search it for the endpoint path or name and fetch only the linked page.