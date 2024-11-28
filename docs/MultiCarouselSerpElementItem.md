# MultiCarouselSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[MultiCarouselElement]**](MultiCarouselElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.multi_carousel_serp_element_item import MultiCarouselSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of MultiCarouselSerpElementItem from a JSON string
multi_carousel_serp_element_item_instance = MultiCarouselSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(MultiCarouselSerpElementItem.to_json())

# convert the object into a dict
multi_carousel_serp_element_item_dict = multi_carousel_serp_element_item_instance.to_dict()
# create an instance of MultiCarouselSerpElementItem from a dict
multi_carousel_serp_element_item_from_dict = MultiCarouselSerpElementItem.from_dict(multi_carousel_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


