# HotelsPackDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the item | [optional] 
**date_from** | **str** | starting date of stay in the format “year-month-date” example: 2019-11-15 | [optional] 
**date_to** | **str** | ending date of stay in the format “year-month-date” example: 2019-11-17 | [optional] 
**items** | [**List[HotelsPackElement]**](HotelsPackElement.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.hotels_pack_dataforseo_labs_serp_element_item import HotelsPackDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of HotelsPackDataforseoLabsSerpElementItem from a JSON string
hotels_pack_dataforseo_labs_serp_element_item_instance = HotelsPackDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print HotelsPackDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
hotels_pack_dataforseo_labs_serp_element_item_dict = hotels_pack_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of HotelsPackDataforseoLabsSerpElementItem from a dict
hotels_pack_dataforseo_labs_serp_element_item_form_dict = hotels_pack_dataforseo_labs_serp_element_item.from_dict(hotels_pack_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


