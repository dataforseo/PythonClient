# HotelsPackElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional] 
**title** | **str** | title of a given link element | [optional] 
**description** | **str** | description | [optional] 
**hotel_identifier** | **str** | unique hotel identifier unique hotel identifier assigned by Google; example: \&quot;CgoIjaeSlI6CnNpVEAE\&quot; | [optional] 
**domain** | **str** | website domain | [optional] 
**url** | **str** | URL | [optional] 
**is_paid** | **bool** | indicates whether the element is an ad | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.hotels_pack_element import HotelsPackElement

# TODO update the JSON string below
json = "{}"
# create an instance of HotelsPackElement from a JSON string
hotels_pack_element_instance = HotelsPackElement.from_json(json)
# print the JSON string representation of the object
print(HotelsPackElement.to_json())

# convert the object into a dict
hotels_pack_element_dict = hotels_pack_element_instance.to_dict()
# create an instance of HotelsPackElement from a dict
hotels_pack_element_from_dict = HotelsPackElement.from_dict(hotels_pack_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


