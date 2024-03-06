[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# MentionCarouselDataforseoLabsSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional]
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | the XPath of the element | [optional]
**title** | **str** | title of the result in SERP | [optional]
**items** | [**List[MentionCarouselElement]**](MentionCarouselElement.md) | elements of search results found in SERP | [optional]

## Example

```python
from dataforseo_client.models.mention_carousel_dataforseo_labs_serp_element_item import MentionCarouselDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of MentionCarouselDataforseoLabsSerpElementItem from a JSON string
mention_carousel_dataforseo_labs_serp_element_item_instance = MentionCarouselDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print MentionCarouselDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
mention_carousel_dataforseo_labs_serp_element_item_dict = mention_carousel_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of MentionCarouselDataforseoLabsSerpElementItem from a dict
mention_carousel_dataforseo_labs_serp_element_item_form_dict = mention_carousel_dataforseo_labs_serp_element_item.from_dict(mention_carousel_dataforseo_labs_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")