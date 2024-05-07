# MultiCarouselSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values; positions of elements with different type values are omitted from rank_group; always equals 0 for desktop | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP always equals 0 for desktop | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**items** | [**List[MultiCarouselElement]**](MultiCarouselElement.md) | additional items present in the element if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.multi_carousel_serp_element_item import MultiCarouselSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of MultiCarouselSerpElementItem from a JSON string
multi_carousel_serp_element_item_instance = MultiCarouselSerpElementItem.from_json(json)
# print the JSON string representation of the object
print MultiCarouselSerpElementItem.to_json()

# convert the object into a dict
multi_carousel_serp_element_item_dict = multi_carousel_serp_element_item_instance.to_dict()
# create an instance of MultiCarouselSerpElementItem from a dict
multi_carousel_serp_element_item_form_dict = multi_carousel_serp_element_item.from_dict(multi_carousel_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


