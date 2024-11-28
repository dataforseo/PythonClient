# CarouselElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**subtitle** | **str** | subtitle of the element | [optional] 
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional] 

## Example

```python
from dataforseo_client.models.carousel_element import CarouselElement

# TODO update the JSON string below
json = "{}"
# create an instance of CarouselElement from a JSON string
carousel_element_instance = CarouselElement.from_json(json)
# print the JSON string representation of the object
print(CarouselElement.to_json())

# convert the object into a dict
carousel_element_dict = carousel_element_instance.to_dict()
# create an instance of CarouselElement from a dict
carousel_element_from_dict = CarouselElement.from_dict(carousel_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


