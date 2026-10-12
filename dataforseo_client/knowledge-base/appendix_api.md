# AppendixApi

Knowledge base for `AppendixApi` (`dataforseo_client.api.appendix_api`) of the DataForSEO Python client. Naming rules, the response envelope, polymorphic items and errors are described in [SKILL.md](../SKILL.md).

Account and service information that applies to the whole DataForSEO API rather than to a data source: account balance, spending, limits and prices, the current status of the APIs, the list of error codes, and re-sending webhooks (pingbacks and postbacks) of completed tasks.

## Use it when you need

- To check credentials and connectivity, or the remaining balance and limits before running a job.
- To find out whether a problem is on DataForSEO's side.
- The meaning of an error code returned in a response.
- To receive webhooks of finished tasks again, for example after your receiving endpoint was unavailable.

This section returns no SEO or marketing data; for that use the other API classes listed in SKILL.md.

## Examples

Generated from the API specification in the same way as the client tests. Replace `USERNAME` / `PASSWORD` with your API login and password.

### user_data

`GET /v3/appendix/user_data`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.appendix_api import AppendixApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    appendix_api = AppendixApi(api_client)

    response = appendix_api.user_data()
```

### appendix_status

`GET /v3/appendix/status`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.appendix_api import AppendixApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    appendix_api = AppendixApi(api_client)

    response = appendix_api.appendix_status()
```

### errors

`GET /v3/appendix/errors`

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.appendix_api import AppendixApi

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')



with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    appendix_api = AppendixApi(api_client)

    response = appendix_api.errors()
```

## Endpoints

All methods of `AppendixApi`. Request and response model names are derived from the path (see SKILL.md).

| Method | HTTP | Path |
|---|---|---|
| `user_data` | GET | `/v3/appendix/user_data` |
| `errors` | GET | `/v3/appendix/errors` |
| `webhook_resend` | POST | `/v3/appendix/webhook_resend` |
| `appendix_status` | GET | `/v3/appendix/status` |