# DiscussionsAndForumsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**url** | **str** | URL | [optional] 
**domain** | **str** | website domain | [optional] 
**source** | **str** | source of the element indicates the source of information included in the top_stories_element | [optional] 
**description** | **str** | description | [optional] 
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**posts_count** | **int** | number of posts from the discussion on the related source | [optional] 

## Example

```python
from dataforseo_client.models.discussions_and_forums_element import DiscussionsAndForumsElement

# TODO update the JSON string below
json = "{}"
# create an instance of DiscussionsAndForumsElement from a JSON string
discussions_and_forums_element_instance = DiscussionsAndForumsElement.from_json(json)
# print the JSON string representation of the object
print(DiscussionsAndForumsElement.to_json())

# convert the object into a dict
discussions_and_forums_element_dict = discussions_and_forums_element_instance.to_dict()
# create an instance of DiscussionsAndForumsElement from a dict
discussions_and_forums_element_form_dict = discussions_and_forums_element.from_dict(discussions_and_forums_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


