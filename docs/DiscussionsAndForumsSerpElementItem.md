# DiscussionsAndForumsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rank_group** | **int** | group rank in SERP position within a group of elements with identical type values; positions of elements with different type values are omitted from rank_group; always equals 0 for desktop | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP always equals 0 for desktop | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**items** | [**List[DiscussionsAndForumsElement]**](DiscussionsAndForumsElement.md) | additional items present in the element if there are none, equals null | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.discussions_and_forums_serp_element_item import DiscussionsAndForumsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsAndForumsSerpElementItem from a JSON string
discussions_and_forums_serp_element_item_instance = DiscussionsAndForumsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(DiscussionsAndForumsSerpElementItem.to_json())

# convert the object into a dict
discussions_and_forums_serp_element_item_dict = discussions_and_forums_serp_element_item_instance.to_dict()
# create an instance of DiscussionsAndForumsSerpElementItem from a dict
discussions_and_forums_serp_element_item_form_dict = discussions_and_forums_serp_element_item.from_dict(discussions_and_forums_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


