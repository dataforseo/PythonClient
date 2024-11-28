# CarouselSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**items** | [**List[CarouselElement]**](CarouselElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.carousel_serp_element_item import CarouselSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of CarouselSerpElementItem from a JSON string
carousel_serp_element_item_instance = CarouselSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(CarouselSerpElementItem.to_json())

# convert the object into a dict
carousel_serp_element_item_dict = carousel_serp_element_item_instance.to_dict()
# create an instance of CarouselSerpElementItem from a dict
carousel_serp_element_item_from_dict = CarouselSerpElementItem.from_dict(carousel_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


