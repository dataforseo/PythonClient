# MultiCarouselElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the row | [optional] 
**multi_carousel_snippets** | [**List[CarouselElement]**](CarouselElement.md) | multi_carousel_snippet results | [optional] 

## Example

```python
from dataforseo_client.models.multi_carousel_element import MultiCarouselElement

# TODO update the JSON string below
json = "{}"
# create an instance of MultiCarouselElement from a JSON string
multi_carousel_element_instance = MultiCarouselElement.from_json(json)
# print the JSON string representation of the object
print MultiCarouselElement.to_json()

# convert the object into a dict
multi_carousel_element_dict = multi_carousel_element_instance.to_dict()
# create an instance of MultiCarouselElement from a dict
multi_carousel_element_form_dict = multi_carousel_element.from_dict(multi_carousel_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


