## OVERVIEW

This is a Python client providing you, as a developer, with a tool for obtaining the necessary data from DataForSEO APIs. You don't have to figure out how to make a request and process a response - all that is readily available in this client.

[![GitHub issues](https://img.shields.io/github/issues/dataforseo/PythonClient.svg)](https://github.com/dataforseo/PythonClient/issues)
[![GitHub license](https://img.shields.io/github/license/dataforseo/PythonClient.svg)](https://github.com/dataforseo/PythonClient)

DataForSEO API uses REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows using our API with almost any programming language.

Client contains 13 sections (aka APIs):

- AI Optimization API (source docs | api docs)
- SERP ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/SerpApi.md) | [api docs](https://docs.dataforseo.com/v3/serp/overview/?bash))
- Keywords Data ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/KeywordsDataApi.md) | [api docs](https://docs.dataforseo.com/v3/keywords_data/overview/?bash))
- Domain Analytics ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/DomainAnalyticsApi.md) | [api docs](https://docs.dataforseo.com/v3/domain_analytics/overview/?bash))
- DataForSEO Labs ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/DataforseoLabsApi.md) | [api docs](https://docs.dataforseo.com/v3/dataforseo_labs/overview/?bash))
- Backlinks ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/BacklinksApi.md) | [api docs](https://docs.dataforseo.com/v3/backlinks/overview/?bash))
- OnPage ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/OnPageApi.md) | [api docs](https://docs.dataforseo.com/v3/on_page/overview/?bash))
- Content Analysis ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/ContentAnalysisApi.md) | [api docs](https://docs.dataforseo.com/v3/content_analysis/overview/?bash))
- Content Generation ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/ContentGenerationApi.md) | [api docs](https://docs.dataforseo.com/v3/content_generation/overview/?bash))
- Merchant ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/MerchantApi.md) | [api docs](https://docs.dataforseo.com/v3/merchant/overview/?bash))
- AppData ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/AppDataApi.md) | [api docs](https://docs.dataforseo.com/v3/app_data/overview/?bash))
- Business Data ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/BusinessDataApi.md) | [api docs](https://docs.dataforseo.com/v3/business_data/overview/?bash))
- Appendix ([source docs](https://github.com/dataforseo/PythonClient/blob/master/docs/AppendixApi.md) | [api docs](https://docs.dataforseo.com/v3/appendix/user_data/?bash))

API Contains 2 types of requests:

1) Live (Simple HTTP request/response message)
2) Task-based (Requires sending a 'Task' entity to execute, waiting until the 'Task' status is ready, and getting the 'Task' result in a special endpoint. Usually, it is represented by 3 types of endpoints: 'TaskPost', 'TaskReady', and 'TaskGet')
   For more details - please follow [here](https://docs.dataforseo.com/v3/?bash)

## YAML Spec

Our API description is based on the OpenAPI [syntax](https://spec.openapis.org/oas/v3.1.0) in YAML format. The YAML file attached to the project [here](https://github.com/dataforseo/OpenApiDocumentation)

## Documentation
The documentation for code objects, formatted in Markdown (.md) is available [here](https://github.com/dataforseo/PythonClient/blob/master/docs/). Official documentation for DataForSEO API is available [here](https://docs.dataforseo.com/v3/?bash).

## Code generation

Code generated using the [openapi generator cli](https://openapi-generator.tech/docs/installation/)

## Install package from nuget.org

```bash
pip install dataforseo-client 
```

## Examples of usage

Example of live request
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

Example of Task-Based request

```python
from dataforseo_client import configuration as dfs_config, api_client as dfs_api_provider
from dataforseo_client.api.serp_api import SerpApi
from dataforseo_client.rest import ApiException
from dataforseo_client.models.serp_task_request_info import SerpTaskRequestInfo
from pprint import pprint
import asyncio
import time

# Configure HTTP basic authorization: basicAuth
configuration = dfs_config.Configuration(username='USERNAME',password='PASSWORD')

def GoogleOrganicTaskReady(id):
    result = serp_api.google_organic_tasks_ready()
    return any(any(xx.id == id for xx in x.result) for x in result.tasks)

with dfs_api_provider.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = SerpApi(api_client)

    try:

        task_post = serp_api.google_organic_task_post([SerpTaskRequestInfo(
            language_name="English",
            location_name="United States",
            keyword="albert einstein"
        )])

        task_id = task_post.tasks[0].id

        start_time = time.time()

        while GoogleOrganicTaskReady(task_id) is not True and (time.time() - start_time) < 60:
           asyncio.sleep(1) 

        api_response = serp_api.google_organic_task_get_advanced(id=task_id)
        
        pprint(api_response)
    
    except ApiException as e:
        print("Exception: %s\n" % e)
```
