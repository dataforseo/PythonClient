# MentionCarouselElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of the row | [optional] 
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**mentioned_in** | [**List[LinkElement]**](LinkElement.md) | additional elements in the mention_carousel item | [optional] 

## Example

```python
from dataforseo_client.models.mention_carousel_element import MentionCarouselElement

# TODO update the JSON string below
json = "{}"
# create an instance of MentionCarouselElement from a JSON string
mention_carousel_element_instance = MentionCarouselElement.from_json(json)
# print the JSON string representation of the object
print MentionCarouselElement.to_json()

# convert the object into a dict
mention_carousel_element_dict = mention_carousel_element_instance.to_dict()
# create an instance of MentionCarouselElement from a dict
mention_carousel_element_form_dict = mention_carousel_element.from_dict(mention_carousel_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


