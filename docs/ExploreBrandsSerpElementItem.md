# ExploreBrandsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**items** | [**List[ExploreBrandsElement]**](ExploreBrandsElement.md) | contains results featured in the ‘hotels_pack’ element of SERP | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.explore_brands_serp_element_item import ExploreBrandsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ExploreBrandsSerpElementItem from a JSON string
explore_brands_serp_element_item_instance = ExploreBrandsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print ExploreBrandsSerpElementItem.to_json()

# convert the object into a dict
explore_brands_serp_element_item_dict = explore_brands_serp_element_item_instance.to_dict()
# create an instance of ExploreBrandsSerpElementItem from a dict
explore_brands_serp_element_item_form_dict = explore_brands_serp_element_item.from_dict(explore_brands_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


