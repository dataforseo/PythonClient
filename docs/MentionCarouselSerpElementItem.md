# MentionCarouselSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**items** | [**List[MentionCarouselElement]**](MentionCarouselElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.mention_carousel_serp_element_item import MentionCarouselSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of MentionCarouselSerpElementItem from a JSON string
mention_carousel_serp_element_item_instance = MentionCarouselSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(MentionCarouselSerpElementItem.to_json())

# convert the object into a dict
mention_carousel_serp_element_item_dict = mention_carousel_serp_element_item_instance.to_dict()
# create an instance of MentionCarouselSerpElementItem from a dict
mention_carousel_serp_element_item_from_dict = MentionCarouselSerpElementItem.from_dict(mention_carousel_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


