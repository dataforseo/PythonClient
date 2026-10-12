# BusinessDataApi

Knowledge base for `BusinessDataApi` (`dataforseo_client.api.business_data_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

Publicly available data about businesses and local places: business profiles, reviews, questions and answers, hotel data and a database of business listings, from sources such as Google, Trustpilot and Tripadvisor.

## Use it when you need

- Details of a business profile: address, phone, website, hours, categories, rating, attributes and posts.
- Reviews of a business on Google or review platforms, for reputation monitoring and sentiment analysis.
- Questions and answers about a place, or hotel search results with prices and hotel details.
- Lists of businesses by category, location, rating and other attributes (lead generation, local market research).

## Use another API when

- You need local rankings in search or maps results for a query: `SerpApi`.
- You need web-wide brand mentions rather than reviews: `ContentAnalysisApi`.
- You need products and sellers on marketplaces: `MerchantApi`.

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### google_my_business_info_task_get

`GET /v3/business_data/google/my_business_info/task_get/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    business_data_api = BusinessDataApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = business_data_api.google_my_business_info_task_get(id)
```

### google_my_business_info_task_post

`POST /v3/business_data/google/my_business_info/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.models.business_data_google_my_business_info_task_post_request_info import BusinessDataGoogleMyBusinessInfoTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    business_data_api = BusinessDataApi(api_client)

    response = business_data_api.google_my_business_info_task_post([BusinessDataGoogleMyBusinessInfoTaskPostRequestInfo(
        language_code="en",
        location_name="New York,New York,United States",
        keyword="RustyBrick, Inc.",
    )]
    )
```

### google_reviews_tasks_ready

`GET /v3/business_data/google/reviews/tasks_ready`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    business_data_api = BusinessDataApi(api_client)

    response = business_data_api.google_reviews_tasks_ready()
```

### google_reviews_task_get

`GET /v3/business_data/google/reviews/task_get/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    business_data_api = BusinessDataApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = business_data_api.google_reviews_task_get(id)
```

### google_reviews_task_post

`POST /v3/business_data/google/reviews/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.models.business_data_google_reviews_task_post_request_info import BusinessDataGoogleReviewsTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    business_data_api = BusinessDataApi(api_client)

    response = business_data_api.google_reviews_task_post([BusinessDataGoogleReviewsTaskPostRequestInfo(
        location_name="London,England,United Kingdom",
        language_name="English",
        keyword="hedonism wines",
        depth=50,
        sort_by="highest_rating",
    )]
    )
```

### google_hotel_info_task_get_advanced

`GET /v3/business_data/google/hotel_info/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    business_data_api = BusinessDataApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = business_data_api.google_hotel_info_task_get_advanced(id)
```

### google_hotel_info_task_post

`POST /v3/business_data/google/hotel_info/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.models.business_data_google_hotel_info_task_post_request_info import BusinessDataGoogleHotelInfoTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    business_data_api = BusinessDataApi(api_client)

    response = business_data_api.google_hotel_info_task_post([BusinessDataGoogleHotelInfoTaskPostRequestInfo(
        language_code="en",
        location_name="New York,New York,United States",
        hotel_identifier="ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE",
        tag="some_string_123",
        postback_url="https://your-server.com/postbackscript.php",
        postback_data="advanced",
    )]
    )
```

### google_my_business_info_live

`POST /v3/business_data/google/my_business_info/live`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi
from dataforseo_client.models.business_data_google_my_business_info_live_request_info import BusinessDataGoogleMyBusinessInfoLiveRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    business_data_api = BusinessDataApi(api_client)

    response = business_data_api.google_my_business_info_live([BusinessDataGoogleMyBusinessInfoLiveRequestInfo(
        language_code="en",
        location_name="New York,New York,United States",
        keyword="RustyBrick, Inc.",
    )]
    )
```

### google_my_business_info_tasks_ready

`GET /v3/business_data/google/my_business_info/tasks_ready`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.business_data_api import BusinessDataApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    business_data_api = BusinessDataApi(api_client)

    response = business_data_api.google_my_business_info_tasks_ready()
```

## Endpoints

All methods of `BusinessDataApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `business_data_id_list` | POST | `/v3/business_data/id_list` |
| `business_data_errors` | POST | `/v3/business_data/errors` |
| `business_listings_locations` | GET | `/v3/business_data/business_listings/locations` |
| `business_listings_categories` | GET | `/v3/business_data/business_listings/categories` |
| `business_listings_available_filters` | GET | `/v3/business_data/business_listings/available_filters` |
| `business_listings_search_live` | POST | `/v3/business_data/business_listings/search/live` |
| `business_listings_categories_aggregation_live` | POST | `/v3/business_data/business_listings/categories_aggregation/live` |
| `business_data_google_locations` | GET | `/v3/business_data/google/locations` |
| `business_data_google_locations_country` | GET | `/v3/business_data/google/locations/{country}` |
| `business_data_google_languages` | GET | `/v3/business_data/google/languages` |
| `google_my_business_info_task_post` | POST | `/v3/business_data/google/my_business_info/task_post` |
| `google_my_business_info_tasks_ready` | GET | `/v3/business_data/google/my_business_info/tasks_ready` |
| `business_data_tasks_ready` | GET | `/v3/business_data/tasks_ready` |
| `google_my_business_info_task_get` | GET | `/v3/business_data/google/my_business_info/task_get/{id}` |
| `google_my_business_info_live` | POST | `/v3/business_data/google/my_business_info/live` |
| `google_my_business_updates_task_post` | POST | `/v3/business_data/google/my_business_updates/task_post` |
| `google_my_business_updates_tasks_ready` | GET | `/v3/business_data/google/my_business_updates/tasks_ready` |
| `google_my_business_updates_task_get` | GET | `/v3/business_data/google/my_business_updates/task_get/{id}` |
| `google_hotel_searches_task_post` | POST | `/v3/business_data/google/hotel_searches/task_post` |
| `google_hotel_searches_tasks_ready` | GET | `/v3/business_data/google/hotel_searches/tasks_ready` |
| `google_hotel_searches_task_get` | GET | `/v3/business_data/google/hotel_searches/task_get/{id}` |
| `google_hotel_searches_live` | POST | `/v3/business_data/google/hotel_searches/live` |
| `google_hotel_info_task_post` | POST | `/v3/business_data/google/hotel_info/task_post` |
| `google_hotel_info_tasks_ready` | GET | `/v3/business_data/google/hotel_info/tasks_ready` |
| `google_hotel_info_task_get_advanced` | GET | `/v3/business_data/google/hotel_info/task_get/advanced/{id}` |
| `google_hotel_info_task_get_html` | GET | `/v3/business_data/google/hotel_info/task_get/html/{id}` |
| `google_hotel_info_live_advanced` | POST | `/v3/business_data/google/hotel_info/live/advanced` |
| `google_hotel_info_live_html` | POST | `/v3/business_data/google/hotel_info/live/html` |
| `google_reviews_task_post` | POST | `/v3/business_data/google/reviews/task_post` |
| `google_reviews_tasks_ready` | GET | `/v3/business_data/google/reviews/tasks_ready` |
| `google_reviews_task_get` | GET | `/v3/business_data/google/reviews/task_get/{id}` |
| `google_extended_reviews_task_post` | POST | `/v3/business_data/google/extended_reviews/task_post` |
| `google_extended_reviews_tasks_ready` | GET | `/v3/business_data/google/extended_reviews/tasks_ready` |
| `google_extended_reviews_task_get` | GET | `/v3/business_data/google/extended_reviews/task_get/{id}` |
| `google_questions_and_answers_task_post` | POST | `/v3/business_data/google/questions_and_answers/task_post` |
| `google_questions_and_answers_tasks_ready` | GET | `/v3/business_data/google/questions_and_answers/tasks_ready` |
| `google_questions_and_answers_task_get` | GET | `/v3/business_data/google/questions_and_answers/task_get/{id}` |
| `google_questions_and_answers_live` | POST | `/v3/business_data/google/questions_and_answers/live` |
| `trustpilot_search_task_post` | POST | `/v3/business_data/trustpilot/search/task_post` |
| `trustpilot_search_tasks_ready` | GET | `/v3/business_data/trustpilot/search/tasks_ready` |
| `trustpilot_search_task_get` | GET | `/v3/business_data/trustpilot/search/task_get/{id}` |
| `trustpilot_reviews_task_post` | POST | `/v3/business_data/trustpilot/reviews/task_post` |
| `trustpilot_reviews_tasks_ready` | GET | `/v3/business_data/trustpilot/reviews/tasks_ready` |
| `trustpilot_reviews_task_get` | GET | `/v3/business_data/trustpilot/reviews/task_get/{id}` |
| `tripadvisor_locations` | GET | `/v3/business_data/tripadvisor/locations` |
| `tripadvisor_locations_country` | GET | `/v3/business_data/tripadvisor/locations/{country}` |
| `tripadvisor_languages` | GET | `/v3/business_data/tripadvisor/languages` |
| `tripadvisor_search_task_post` | POST | `/v3/business_data/tripadvisor/search/task_post` |
| `tripadvisor_search_tasks_ready` | GET | `/v3/business_data/tripadvisor/search/tasks_ready` |
| `tripadvisor_search_task_get` | GET | `/v3/business_data/tripadvisor/search/task_get/{id}` |
| `tripadvisor_reviews_task_post` | POST | `/v3/business_data/tripadvisor/reviews/task_post` |
| `tripadvisor_reviews_tasks_ready` | GET | `/v3/business_data/tripadvisor/reviews/tasks_ready` |
| `tripadvisor_reviews_task_get` | GET | `/v3/business_data/tripadvisor/reviews/task_get/{id}` |