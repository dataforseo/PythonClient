# AppDataApi

Knowledge base for `AppDataApi` (`dataforseo_client.api.app_data_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

Mobile application data from app stores such as Google Play and the App Store: app search results, top charts and collections, detailed app information and user reviews, plus a searchable database of app listings.

Results are collected for the requested location and language, the same way a store user would see them.

## Use it when you need

- Which apps rank in a store for a search query (app store optimization, competitor discovery).
- Which apps are in top charts or collections of a category.
- Details of a specific app: description, rating, installs, price, developer, versions.
- User reviews of an app for review monitoring, sentiment or product feedback analysis.
- Apps that match a category or text, found in a database without querying the store.

## Use another API when

- You need keywords an app ranks for, app competitors or app keyword gaps: `DataforseoLabsApi`.
- You need physical products on marketplaces: `MerchantApi`.

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### google_app_searches_task_post

`POST /v3/app_data/google/app_searches/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.models.app_data_google_app_searches_task_post_request_info import AppDataGoogleAppSearchesTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    app_data_api = AppDataApi(api_client)

    response = app_data_api.google_app_searches_task_post([AppDataGoogleAppSearchesTaskPostRequestInfo(
        keyword="vpn",
        location_code=2840,
        language_code="en",
        depth=30,
    )]
    )
```

### google_app_searches_task_get_advanced

`GET /v3/app_data/google/app_searches/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    app_data_api = AppDataApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = app_data_api.google_app_searches_task_get_advanced(id)
```

### apple_app_searches_task_get_advanced

`GET /v3/app_data/apple/app_searches/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    app_data_api = AppDataApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = app_data_api.apple_app_searches_task_get_advanced(id)
```

### apple_app_searches_task_post

`POST /v3/app_data/apple/app_searches/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.models.app_data_apple_app_searches_task_post_request_info import AppDataAppleAppSearchesTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    app_data_api = AppDataApi(api_client)

    response = app_data_api.apple_app_searches_task_post([AppDataAppleAppSearchesTaskPostRequestInfo(
        keyword="vpn",
        location_code=2840,
        language_code="en",
        depth=200,
    )]
    )
```

### google_app_info_task_get_advanced

`GET /v3/app_data/google/app_info/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    app_data_api = AppDataApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = app_data_api.google_app_info_task_get_advanced(id)
```

### google_app_info_task_post

`POST /v3/app_data/google/app_info/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.models.app_data_google_app_info_task_post_request_info import AppDataGoogleAppInfoTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    app_data_api = AppDataApi(api_client)

    response = app_data_api.google_app_info_task_post([AppDataGoogleAppInfoTaskPostRequestInfo(
        app_id="org.telegram.messenger",
        location_code=2840,
        language_code="en",
    )]
    )
```

### apple_app_info_task_get_advanced

`GET /v3/app_data/apple/app_info/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    app_data_api = AppDataApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = app_data_api.apple_app_info_task_get_advanced(id)
```

### apple_app_info_task_post

`POST /v3/app_data/apple/app_info/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.models.app_data_apple_app_info_task_post_request_info import AppDataAppleAppInfoTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    app_data_api = AppDataApi(api_client)

    response = app_data_api.apple_app_info_task_post([AppDataAppleAppInfoTaskPostRequestInfo(
        app_id="835599320",
        location_code=2840,
        language_code="en",
    )]
    )
```

### google_app_reviews_task_post

`POST /v3/app_data/google/app_reviews/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi
from dataforseo_client.models.app_data_google_app_reviews_task_post_request_info import AppDataGoogleAppReviewsTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    app_data_api = AppDataApi(api_client)

    response = app_data_api.google_app_reviews_task_post([AppDataGoogleAppReviewsTaskPostRequestInfo(
        app_id="org.telegram.messenger",
        location_code=2840,
        language_code="en",
        depth=150,
    )]
    )
```

### google_app_reviews_task_get_advanced

`GET /v3/app_data/google/app_reviews/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.app_data_api import AppDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    app_data_api = AppDataApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = app_data_api.google_app_reviews_task_get_advanced(id)
```

## Endpoints

All methods of `AppDataApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `app_data_id_list` | POST | `/v3/app_data/id_list` |
| `app_data_errors` | POST | `/v3/app_data/errors` |
| `google_categories` | GET | `/v3/app_data/google/categories` |
| `app_data_google_locations` | GET | `/v3/app_data/google/locations` |
| `app_data_google_locations_country` | GET | `/v3/app_data/google/locations/{country}` |
| `app_data_google_languages` | GET | `/v3/app_data/google/languages` |
| `google_app_searches_task_post` | POST | `/v3/app_data/google/app_searches/task_post` |
| `google_app_searches_tasks_ready` | GET | `/v3/app_data/google/app_searches/tasks_ready` |
| `app_data_tasks_ready` | GET | `/v3/app_data/tasks_ready` |
| `google_app_searches_task_get_advanced` | GET | `/v3/app_data/google/app_searches/task_get/advanced/{id}` |
| `google_app_searches_task_get_html` | GET | `/v3/app_data/google/app_searches/task_get/html/{id}` |
| `google_app_list_task_post` | POST | `/v3/app_data/google/app_list/task_post` |
| `google_app_list_tasks_ready` | GET | `/v3/app_data/google/app_list/tasks_ready` |
| `google_app_list_task_get_advanced` | GET | `/v3/app_data/google/app_list/task_get/advanced/{id}` |
| `google_app_list_task_get_html` | GET | `/v3/app_data/google/app_list/task_get/html/{id}` |
| `google_app_info_task_post` | POST | `/v3/app_data/google/app_info/task_post` |
| `google_app_info_tasks_ready` | GET | `/v3/app_data/google/app_info/tasks_ready` |
| `google_app_info_task_get_advanced` | GET | `/v3/app_data/google/app_info/task_get/advanced/{id}` |
| `google_app_info_task_get_html` | GET | `/v3/app_data/google/app_info/task_get/html/{id}` |
| `google_app_reviews_task_post` | POST | `/v3/app_data/google/app_reviews/task_post` |
| `google_app_reviews_tasks_ready` | GET | `/v3/app_data/google/app_reviews/tasks_ready` |
| `google_app_reviews_task_get_advanced` | GET | `/v3/app_data/google/app_reviews/task_get/advanced/{id}` |
| `google_app_reviews_task_get_html` | GET | `/v3/app_data/google/app_reviews/task_get/html/{id}` |
| `google_app_listings_categories` | GET | `/v3/app_data/google/app_listings/categories` |
| `google_app_listings_search_live` | POST | `/v3/app_data/google/app_listings/search/live` |
| `apple_categories` | GET | `/v3/app_data/apple/categories` |
| `apple_locations` | GET | `/v3/app_data/apple/locations` |
| `apple_languages` | GET | `/v3/app_data/apple/languages` |
| `apple_app_searches_task_post` | POST | `/v3/app_data/apple/app_searches/task_post` |
| `apple_app_searches_tasks_ready` | GET | `/v3/app_data/apple/app_searches/tasks_ready` |
| `apple_app_searches_task_get_advanced` | GET | `/v3/app_data/apple/app_searches/task_get/advanced/{id}` |
| `apple_app_info_task_post` | POST | `/v3/app_data/apple/app_info/task_post` |
| `apple_app_info_tasks_ready` | GET | `/v3/app_data/apple/app_info/tasks_ready` |
| `apple_app_info_task_get_advanced` | GET | `/v3/app_data/apple/app_info/task_get/advanced/{id}` |
| `apple_app_list_task_post` | POST | `/v3/app_data/apple/app_list/task_post` |
| `apple_app_list_tasks_ready` | GET | `/v3/app_data/apple/app_list/tasks_ready` |
| `apple_app_list_task_get_advanced` | GET | `/v3/app_data/apple/app_list/task_get/advanced/{id}` |
| `apple_app_reviews_task_post` | POST | `/v3/app_data/apple/app_reviews/task_post` |
| `apple_app_reviews_tasks_ready` | GET | `/v3/app_data/apple/app_reviews/tasks_ready` |
| `apple_app_reviews_task_get_advanced` | GET | `/v3/app_data/apple/app_reviews/task_get/advanced/{id}` |
| `apple_app_listings_categories` | GET | `/v3/app_data/apple/app_listings/categories` |
| `apple_app_listings_search_live` | POST | `/v3/app_data/apple/app_listings/search/live` |