# JobsDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | relevant URL | [optional] 
**items** | [**List[JobsElement]**](JobsElement.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.jobs_dataforseo_labs_serp_element_item import JobsDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of JobsDataforseoLabsSerpElementItem from a JSON string
jobs_dataforseo_labs_serp_element_item_instance = JobsDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(JobsDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
jobs_dataforseo_labs_serp_element_item_dict = jobs_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of JobsDataforseoLabsSerpElementItem from a dict
jobs_dataforseo_labs_serp_element_item_from_dict = JobsDataforseoLabsSerpElementItem.from_dict(jobs_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


