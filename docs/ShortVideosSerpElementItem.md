[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ShortVideosSerpElementItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional]
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional]
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional]
**xpath** | **str** | the XPath of the element | [optional]
**title** | **str** | title of a given link element | [optional]
**items** | [**List[ShortVideosElement]**](ShortVideosElement.md) | contains results featured in the ‘hotels_pack’ element of SERP | [optional]
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional]

## Example

```python
from dataforseo_client.models.short_videos_serp_element_item import ShortVideosSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShortVideosSerpElementItem from a JSON string
short_videos_serp_element_item_instance = ShortVideosSerpElementItem.from_json(json)
# print the JSON string representation of the object
print ShortVideosSerpElementItem.to_json()

# convert the object into a dict
short_videos_serp_element_item_dict = short_videos_serp_element_item_instance.to_dict()
# create an instance of ShortVideosSerpElementItem from a dict
short_videos_serp_element_item_form_dict = short_videos_serp_element_item.from_dict(short_videos_serp_element_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")