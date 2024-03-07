[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsGoogleAppIntersectionLiveResponseInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | the current version of the API | [optional]
**status_code** | **int** | general status code you can find the full list of the response codes here | [optional]
**status_message** | **str** | general informational message you can find the full list of general informational messages here | [optional]
**time** | **str** | total execution time, seconds | [optional]
**cost** | **float** | total tasks cost, USD | [optional]
**tasks_count** | **int** | the number of tasks in the tasks array | [optional]
**tasks_error** | **int** | the number of tasks in the tasks array returned with an error | [optional]
**tasks** | [**List[DataforseoLabsGoogleAppIntersectionLiveTaskInfo]**](DataforseoLabsGoogleAppIntersectionLiveTaskInfo.md) | array of tasks | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_app_intersection_live_response_info import DataforseoLabsGoogleAppIntersectionLiveResponseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleAppIntersectionLiveResponseInfo from a JSON string
dataforseo_labs_google_app_intersection_live_response_info_instance = DataforseoLabsGoogleAppIntersectionLiveResponseInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleAppIntersectionLiveResponseInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_app_intersection_live_response_info_dict = dataforseo_labs_google_app_intersection_live_response_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleAppIntersectionLiveResponseInfo from a dict
dataforseo_labs_google_app_intersection_live_response_info_form_dict = dataforseo_labs_google_app_intersection_live_response_info.from_dict(dataforseo_labs_google_app_intersection_live_response_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")