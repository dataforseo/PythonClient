# TopStoriesSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**items** | [**List[TopStoriesElement]**](TopStoriesElement.md) | contains arrays of specific images | [optional] 

## Example

```python
from dataforseo_client.models.top_stories_serp_element_item import TopStoriesSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of TopStoriesSerpElementItem from a JSON string
top_stories_serp_element_item_instance = TopStoriesSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(TopStoriesSerpElementItem.to_json())

# convert the object into a dict
top_stories_serp_element_item_dict = top_stories_serp_element_item_instance.to_dict()
# create an instance of TopStoriesSerpElementItem from a dict
top_stories_serp_element_item_from_dict = TopStoriesSerpElementItem.from_dict(top_stories_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


