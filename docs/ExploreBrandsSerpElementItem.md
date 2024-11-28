# ExploreBrandsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**items** | [**List[ExploreBrandsElement]**](ExploreBrandsElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.explore_brands_serp_element_item import ExploreBrandsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExploreBrandsSerpElementItem from a JSON string
explore_brands_serp_element_item_instance = ExploreBrandsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(ExploreBrandsSerpElementItem.to_json())

# convert the object into a dict
explore_brands_serp_element_item_dict = explore_brands_serp_element_item_instance.to_dict()
# create an instance of ExploreBrandsSerpElementItem from a dict
explore_brands_serp_element_item_from_dict = ExploreBrandsSerpElementItem.from_dict(explore_brands_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


