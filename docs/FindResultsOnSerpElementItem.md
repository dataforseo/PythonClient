# FindResultsOnSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ShortVideosElement]**](ShortVideosElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.find_results_on_serp_element_item import FindResultsOnSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of FindResultsOnSerpElementItem from a JSON string
find_results_on_serp_element_item_instance = FindResultsOnSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(FindResultsOnSerpElementItem.to_json())

# convert the object into a dict
find_results_on_serp_element_item_dict = find_results_on_serp_element_item_instance.to_dict()
# create an instance of FindResultsOnSerpElementItem from a dict
find_results_on_serp_element_item_from_dict = FindResultsOnSerpElementItem.from_dict(find_results_on_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


