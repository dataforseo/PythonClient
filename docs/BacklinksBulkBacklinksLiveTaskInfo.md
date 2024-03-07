[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksBulkBacklinksLiveTaskInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier unique task identifier in our system in the UUID format | [optional]
**status_code** | **int** | status code of the task generated by DataForSEO, can be within the following range: 10000-60000 you can find the full list of the response codes here | [optional]
**status_message** | **str** | informational message of the task you can find the full list of general informational messages here | [optional]
**time** | **str** | execution time, seconds | [optional]
**cost** | **float** | total tasks cost, USD | [optional]
**result_count** | **int** | number of elements in the result array | [optional]
**path** | **List[Optional[str]]** | URL path | [optional]
**data** | **object** | contains the same parameters that you specified in the POST request | [optional]
**result** | [**List[BacklinksBulkBacklinksLiveResultInfo]**](BacklinksBulkBacklinksLiveResultInfo.md) | array of results | [optional]

## Example

```python
from dataforseo_client.models.backlinks_bulk_backlinks_live_task_info import BacklinksBulkBacklinksLiveTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkBacklinksLiveTaskInfo from a JSON string
backlinks_bulk_backlinks_live_task_info_instance = BacklinksBulkBacklinksLiveTaskInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksBulkBacklinksLiveTaskInfo.to_json()

# convert the object into a dict
backlinks_bulk_backlinks_live_task_info_dict = backlinks_bulk_backlinks_live_task_info_instance.to_dict()
# create an instance of BacklinksBulkBacklinksLiveTaskInfo from a dict
backlinks_bulk_backlinks_live_task_info_form_dict = backlinks_bulk_backlinks_live_task_info.from_dict(backlinks_bulk_backlinks_live_task_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")