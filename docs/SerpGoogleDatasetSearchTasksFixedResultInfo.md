[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# SerpGoogleDatasetSearchTasksFixedResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | task identifier of the completed task unique task identifier in our system in the UUID format | [optional]
**se** | **str** | search engine specified when setting the task | [optional]
**se_type** | **str** | type of search engine can take the following values: dataset_search | [optional]
**date_fixed** | **str** | date when the task was fixed (in the UTC format) | [optional]
**tag** | **str** | user-defined task identifier | [optional]
**endpoint_regular** | **str** | URL for collecting the results of the SERP Regular task if SERP Regular is not supported in the specified endpoint, the value will be null | [optional]
**endpoint_advanced** | **str** | URL for collecting the results of the SERP Advanced task if SERP Advanced is not supported in the specified endpoint, the value will be null | [optional]
**endpoint_html** | **str** | URL for collecting the results of the SERP HTML task if SERP HTML is not supported in the specified endpoint, the value will be null | [optional]

## Example

```python
from dataforseo_client.models.serp_google_dataset_search_tasks_fixed_result_info import SerpGoogleDatasetSearchTasksFixedResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleDatasetSearchTasksFixedResultInfo from a JSON string
serp_google_dataset_search_tasks_fixed_result_info_instance = SerpGoogleDatasetSearchTasksFixedResultInfo.from_json(json)
# print the JSON string representation of the object
print SerpGoogleDatasetSearchTasksFixedResultInfo.to_json()

# convert the object into a dict
serp_google_dataset_search_tasks_fixed_result_info_dict = serp_google_dataset_search_tasks_fixed_result_info_instance.to_dict()
# create an instance of SerpGoogleDatasetSearchTasksFixedResultInfo from a dict
serp_google_dataset_search_tasks_fixed_result_info_form_dict = serp_google_dataset_search_tasks_fixed_result_info.from_dict(serp_google_dataset_search_tasks_fixed_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")