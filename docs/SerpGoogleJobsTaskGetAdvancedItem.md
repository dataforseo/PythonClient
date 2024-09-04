# SerpGoogleJobsTaskGetAdvancedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**job_id** | **str** | ID of the job on Google Jobs | [optional] 
**title** | **str** | title of the job | [optional] 
**employer_name** | **str** | name of the employer | [optional] 
**employer_url** | **str** | URL to the employer’s website | [optional] 
**employer_image_url** | **str** | URL to the image used in the job posting | [optional] 
**location** | **str** | location for which the job vacancy is posted | [optional] 
**source_name** | **str** | original source of the job vacancy | [optional] 
**source_url** | **str** | URL to the original source of the job vacancy | [optional] 
**salary** | **str** | the salary indicated in the job vacancy if the salary isn’t indicated, this field will equal null | [optional] 
**contract_type** | **str** | employment contract type | [optional] 
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**time_ago** | **str** | indicates how long ago the job vacancy was posted | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.serp_google_jobs_task_get_advanced_item import SerpGoogleJobsTaskGetAdvancedItem

# TODO update the JSON string below
json = "{}"
# create an instance of SerpGoogleJobsTaskGetAdvancedItem from a JSON string
serp_google_jobs_task_get_advanced_item_instance = SerpGoogleJobsTaskGetAdvancedItem.from_json(json)
# print the JSON string representation of the object
print SerpGoogleJobsTaskGetAdvancedItem.to_json()

# convert the object into a dict
serp_google_jobs_task_get_advanced_item_dict = serp_google_jobs_task_get_advanced_item_instance.to_dict()
# create an instance of SerpGoogleJobsTaskGetAdvancedItem from a dict
serp_google_jobs_task_get_advanced_item_form_dict = serp_google_jobs_task_get_advanced_item.from_dict(serp_google_jobs_task_get_advanced_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


