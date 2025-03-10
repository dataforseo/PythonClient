# MentionCarouselDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**items** | [**List[MentionCarouselElement]**](MentionCarouselElement.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.mention_carousel_dataforseo_labs_serp_element_item import MentionCarouselDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of MentionCarouselDataforseoLabsSerpElementItem from a JSON string
mention_carousel_dataforseo_labs_serp_element_item_instance = MentionCarouselDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(MentionCarouselDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
mention_carousel_dataforseo_labs_serp_element_item_dict = mention_carousel_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of MentionCarouselDataforseoLabsSerpElementItem from a dict
mention_carousel_dataforseo_labs_serp_element_item_from_dict = MentionCarouselDataforseoLabsSerpElementItem.from_dict(mention_carousel_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


