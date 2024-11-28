# GoogleTrendsTopicsListElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TrendsTopicListDataInfo**](TrendsTopicListDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.google_trends_topics_list_element_item import GoogleTrendsTopicsListElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleTrendsTopicsListElementItem from a JSON string
google_trends_topics_list_element_item_instance = GoogleTrendsTopicsListElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleTrendsTopicsListElementItem.to_json())

# convert the object into a dict
google_trends_topics_list_element_item_dict = google_trends_topics_list_element_item_instance.to_dict()
# create an instance of GoogleTrendsTopicsListElementItem from a dict
google_trends_topics_list_element_item_from_dict = GoogleTrendsTopicsListElementItem.from_dict(google_trends_topics_list_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


