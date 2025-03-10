# CarouselDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**items** | [**List[CarouselElement]**](CarouselElement.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.carousel_dataforseo_labs_serp_element_item import CarouselDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of CarouselDataforseoLabsSerpElementItem from a JSON string
carousel_dataforseo_labs_serp_element_item_instance = CarouselDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(CarouselDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
carousel_dataforseo_labs_serp_element_item_dict = carousel_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of CarouselDataforseoLabsSerpElementItem from a dict
carousel_dataforseo_labs_serp_element_item_from_dict = CarouselDataforseoLabsSerpElementItem.from_dict(carousel_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


