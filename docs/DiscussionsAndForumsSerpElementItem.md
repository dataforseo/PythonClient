# DiscussionsAndForumsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**items** | [**List[DiscussionsAndForumsElement]**](DiscussionsAndForumsElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.discussions_and_forums_serp_element_item import DiscussionsAndForumsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsAndForumsSerpElementItem from a JSON string
discussions_and_forums_serp_element_item_instance = DiscussionsAndForumsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print DiscussionsAndForumsSerpElementItem.to_json()

# convert the object into a dict
discussions_and_forums_serp_element_item_dict = discussions_and_forums_serp_element_item_instance.to_dict()
# create an instance of DiscussionsAndForumsSerpElementItem from a dict
discussions_and_forums_serp_element_item_form_dict = discussions_and_forums_serp_element_item.from_dict(discussions_and_forums_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


