# JobsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the row | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**author** | **str** | author | [optional] 
**job_posted_time** | **str** | the time when the job was posted | [optional] 
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**contract_type** | **str** | contract type | [optional] 
**salary** | **str** | salary | [optional] 
**url** | **str** | URL | [optional] 

## Example

```python
from dataforseo_client.models.jobs_element import JobsElement

# TODO update the JSON string below
json = "{}"
# create an instance of JobsElement from a JSON string
jobs_element_instance = JobsElement.from_json(json)
# print the JSON string representation of the object
print JobsElement.to_json()

# convert the object into a dict
jobs_element_dict = jobs_element_instance.to_dict()
# create an instance of JobsElement from a dict
jobs_element_form_dict = jobs_element.from_dict(jobs_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


