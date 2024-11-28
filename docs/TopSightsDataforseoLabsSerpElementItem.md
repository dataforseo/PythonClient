# TopSightsDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**items** | [**List[TopSightsElement]**](TopSightsElement.md) | elements of search results found in SERP | [optional] 

## Example

```python
from dataforseo_client.models.top_sights_dataforseo_labs_serp_element_item import TopSightsDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of TopSightsDataforseoLabsSerpElementItem from a JSON string
top_sights_dataforseo_labs_serp_element_item_instance = TopSightsDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(TopSightsDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
top_sights_dataforseo_labs_serp_element_item_dict = top_sights_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of TopSightsDataforseoLabsSerpElementItem from a dict
top_sights_dataforseo_labs_serp_element_item_from_dict = TopSightsDataforseoLabsSerpElementItem.from_dict(top_sights_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


