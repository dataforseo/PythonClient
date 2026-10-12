# MerchantApi

Knowledge base for `MerchantApi` (`dataforseo_client.api.merchant_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

E-commerce data from marketplaces and shopping search engines such as Amazon and Google Shopping: product listings for a search query, product details, product variations, sellers and their offers, with prices, ratings, reviews count and paid placements.

Results are collected for the requested location and language, the same way a real shopper would see them, and are returned as parsed data or raw HTML.

## Use it when you need

- Which products appear for a search query on a marketplace, in which order, and which of them are sponsored.
- Details of a specific product: description, specifications, price, rating, variations.
- Who sells a product and at what price and conditions, for price monitoring and competitor analysis.

## Use another API when

- You need keyword metrics or ranked keywords for marketplace products: `DataforseoLabsApi`.
- You need shopping elements that appear inside regular search results: `SerpApi`.
- You need mobile apps rather than products: `AppDataApi`.

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### google_sellers_task_get_advanced

`GET /v3/merchant/google/sellers/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    merchant_api = MerchantApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = merchant_api.google_sellers_task_get_advanced(id)
```

### google_sellers_task_post

`POST /v3/merchant/google/sellers/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.models.merchant_google_sellers_task_post_request_info import MerchantGoogleSellersTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    merchant_api = MerchantApi(api_client)

    response = merchant_api.google_sellers_task_post([MerchantGoogleSellersTaskPostRequestInfo(
        language_code="en",
        location_code=2840,
        product_id="1113158713975221117",
    )]
    )
```

### google_products_task_get_advanced

`GET /v3/merchant/google/products/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    merchant_api = MerchantApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = merchant_api.google_products_task_get_advanced(id)
```

### google_products_task_post

`POST /v3/merchant/google/products/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.models.merchant_google_products_task_post_request_info import MerchantGoogleProductsTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    merchant_api = MerchantApi(api_client)

    response = merchant_api.google_products_task_post([MerchantGoogleProductsTaskPostRequestInfo(
        language_code="en",
        location_code=2840,
        keyword="iphone",
        price_min=5,
    )]
    )
```

### amazon_products_task_get_advanced

`GET /v3/merchant/amazon/products/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    merchant_api = MerchantApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = merchant_api.amazon_products_task_get_advanced(id)
```

### amazon_products_task_post

`POST /v3/merchant/amazon/products/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.models.merchant_amazon_products_task_post_request_info import MerchantAmazonProductsTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    merchant_api = MerchantApi(api_client)

    response = merchant_api.amazon_products_task_post([MerchantAmazonProductsTaskPostRequestInfo(
        language_code="en_US",
        location_code=2840,
        keyword="shoes",
    )]
    )
```

### google_product_info_task_get_advanced

`GET /v3/merchant/google/product_info/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    merchant_api = MerchantApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = merchant_api.google_product_info_task_get_advanced(id)
```

### google_product_info_task_post

`POST /v3/merchant/google/product_info/task_post`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi
from dataforseo_client.models.merchant_google_product_info_task_post_request_info import MerchantGoogleProductInfoTaskPostRequestInfo

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    merchant_api = MerchantApi(api_client)

    response = merchant_api.google_product_info_task_post([MerchantGoogleProductInfoTaskPostRequestInfo(
        language_code="en",
        location_code=2840,
        product_id="1113158713975221117",
    )]
    )
```

### amazon_sellers_task_get_advanced

`GET /v3/merchant/amazon/sellers/task_get/advanced/{id}`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.merchant_api import MerchantApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    merchant_api = MerchantApi(api_client)

    id = "00000000-0000-0000-0000-000000000000"
    response = merchant_api.amazon_sellers_task_get_advanced(id)
```

## Endpoints

All methods of `MerchantApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `merchant_id_list` | POST | `/v3/merchant/id_list` |
| `merchant_errors` | POST | `/v3/merchant/errors` |
| `merchant_google_languages` | GET | `/v3/merchant/google/languages` |
| `merchant_google_locations` | GET | `/v3/merchant/google/locations` |
| `merchant_google_locations_country` | GET | `/v3/merchant/google/locations/{country}` |
| `google_products_task_post` | POST | `/v3/merchant/google/products/task_post` |
| `google_products_tasks_ready` | GET | `/v3/merchant/google/products/tasks_ready` |
| `merchant_tasks_ready` | GET | `/v3/merchant/tasks_ready` |
| `google_products_task_get_advanced` | GET | `/v3/merchant/google/products/task_get/advanced/{id}` |
| `google_products_task_get_html` | GET | `/v3/merchant/google/products/task_get/html/{id}` |
| `google_sellers_task_post` | POST | `/v3/merchant/google/sellers/task_post` |
| `google_sellers_tasks_ready` | GET | `/v3/merchant/google/sellers/tasks_ready` |
| `google_sellers_task_get_advanced` | GET | `/v3/merchant/google/sellers/task_get/advanced/{id}` |
| `google_product_info_task_post` | POST | `/v3/merchant/google/product_info/task_post` |
| `google_product_info_tasks_ready` | GET | `/v3/merchant/google/product_info/tasks_ready` |
| `google_product_info_task_get_advanced` | GET | `/v3/merchant/google/product_info/task_get/advanced/{id}` |
| `google_sellers_ad_url` | GET | `/v3/merchant/google/sellers/ad_url/{shop_ad_aclk}` |
| `amazon_locations` | GET | `/v3/merchant/amazon/locations` |
| `amazon_locations_country` | GET | `/v3/merchant/amazon/locations/{country}` |
| `amazon_languages` | GET | `/v3/merchant/amazon/languages` |
| `amazon_products_task_post` | POST | `/v3/merchant/amazon/products/task_post` |
| `amazon_products_tasks_ready` | GET | `/v3/merchant/amazon/products/tasks_ready` |
| `amazon_products_task_get_advanced` | GET | `/v3/merchant/amazon/products/task_get/advanced/{id}` |
| `amazon_products_live_advanced` | POST | `/v3/merchant/amazon/products/live/advanced` |
| `amazon_products_task_get_html` | GET | `/v3/merchant/amazon/products/task_get/html/{id}` |
| `amazon_products_live_html` | POST | `/v3/merchant/amazon/products/live/html` |
| `amazon_asin_task_post` | POST | `/v3/merchant/amazon/asin/task_post` |
| `amazon_asin_tasks_ready` | GET | `/v3/merchant/amazon/asin/tasks_ready` |
| `amazon_asin_task_get_advanced` | GET | `/v3/merchant/amazon/asin/task_get/advanced/{id}` |
| `amazon_asin_live_advanced` | POST | `/v3/merchant/amazon/asin/live/advanced` |
| `amazon_asin_task_get_html` | GET | `/v3/merchant/amazon/asin/task_get/html/{id}` |
| `amazon_asin_live_html` | POST | `/v3/merchant/amazon/asin/live/html` |
| `amazon_sellers_task_post` | POST | `/v3/merchant/amazon/sellers/task_post` |
| `amazon_sellers_tasks_ready` | GET | `/v3/merchant/amazon/sellers/tasks_ready` |
| `amazon_sellers_task_get_advanced` | GET | `/v3/merchant/amazon/sellers/task_get/advanced/{id}` |
| `amazon_sellers_live_advanced` | POST | `/v3/merchant/amazon/sellers/live/advanced` |
| `amazon_sellers_task_get_html` | GET | `/v3/merchant/amazon/sellers/task_get/html/{id}` |
| `amazon_sellers_live_html` | POST | `/v3/merchant/amazon/sellers/live/html` |