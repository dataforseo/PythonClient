# JobsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**url** | **str** | source URL | [optional] 
**items** | [**List[JobsElement]**](JobsElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.jobs_serp_element_item import JobsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of JobsSerpElementItem from a JSON string
jobs_serp_element_item_instance = JobsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print JobsSerpElementItem.to_json()

# convert the object into a dict
jobs_serp_element_item_dict = jobs_serp_element_item_instance.to_dict()
# create an instance of JobsSerpElementItem from a dict
jobs_serp_element_item_form_dict = jobs_serp_element_item.from_dict(jobs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


