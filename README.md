## OVERVIEW

There is a Python client to call DataForSeo API.

DataForSEO API uses REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

Client contains 12 sections (aka API):
- Serp ([source](https://docs.dataforseo.com/v3/serp/overview/?bash))
- KeywordsData ([source](https://docs.dataforseo.com/v3/keywords_data/overview/?bash))
- DomainAnalytics ([source](https://docs.dataforseo.com/v3/domain_analytics/overview/?bash))
- DataforseoLabs ([source](https://docs.dataforseo.com/v3/dataforseo_labs/overview/?bash))
- Backlinks ([source](https://docs.dataforseo.com/v3/backlinks/overview/?bash))
- OnPage ([source](https://docs.dataforseo.com/v3/on_page/overview/?bash))
- ContentAnalysis ([source](https://docs.dataforseo.com/v3/content_analysis/overview/?bash))
- ContentGeneration ([source](https://docs.dataforseo.com/v3/content_generation/overview/?bash))
- Merchant ([source](https://docs.dataforseo.com/v3/merchant/overview/?bash))
- AppData ([source](https://docs.dataforseo.com/v3/app_data/overview/?bash))
- BusinessData ([source](https://docs.dataforseo.com/v3/business_data/overview/?bash))
- Appendix ([source](https://docs.dataforseo.com/v3/appendix/user_data/?bash))

API Contains 2 types of requests:
1) Live (Simple HTTP request/response message)
2) Task-Based (Where you need to send a 'Task' entity to execute, waiting until the 'Task' status is ready and getting the 'Task' result in a special endpoint. Usually, it represents in 3 endpoints 'TaskPost', 'TaskReady' and 'TaskGet')

For more details - please follow [here](https://docs.dataforseo.com/v3/?bash)

## YAML Spec

Our API description is based on openAPI [syntax](https://spec.openapis.org/oas/v3.1.0) in YAML format. The YAML file attached to the project [here](./openapi_specification.yaml)

## Documentation
Code Objects documentation in .md format was also generated using 'openapi-generator-cli' and placed [here](./docs)

## Code generation

Code generated with using [openapi generator cli](https://openapi-generator.tech/docs/installation/)

## install package from nuget.org

```bash
pip install dataforseo-client 
```

## Examples of usage

Example of live request
```python
from __future__ import print_function
import time

import dataforseo_client
from dataforseo_client.rest import ApiException
from pprint import pprint
import asyncio
# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration()
configuration.username = 'USERNAME'
configuration.password = 'PASSWORD'

with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = dataforseo_client.SerpApi(api_client)


    try:

        api_response = serp_api.google_organic_live_advanced([dataforseo_client.SerpTaskRequestInfo(
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
from __future__ import print_function
import time

import dataforseo_client
from dataforseo_client.rest import ApiException
from pprint import pprint
import asyncio
# Configure HTTP basic authorization: basicAuth
configuration = dataforseo_client.Configuration()
configuration.username = 'USERNAME'
configuration.password = 'PASSWORD'


def GoogleOrganicTaskReady(id):
    result = serp_api.google_organic_tasks_ready()
    return any(any(xx.id == id for xx in x.result) for x in result.tasks)


with dataforseo_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    serp_api = dataforseo_client.SerpApi(api_client)


    try:

        task_post = serp_api.google_organic_task_post([dataforseo_client.SerpTaskRequestInfo(
            language_name="English",
            location_name="United States",
            keyword="albert einstein"
        )])

        task_id = task_post.tasks[0].id

        start_time = time.time()

        while GoogleOrganicTaskReady(task_id) and (time.time() - start_time) < 60:
           asyncio.sleep(1) 

        api_response = serp_api.google_organic_task_get_advanced(id=task_id)
        
        pprint(api_response)
    
    except ApiException as e:
        print("Exception: %s\n" % e)
```
