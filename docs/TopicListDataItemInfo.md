[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# TopicListDataItemInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic_id** | **str** | unique topic identifier in Google Trends | [optional]
**topic_title** | **str** | title of the topic | [optional]
**topic_type** | **str** | type of the topic represents the general type of the topic | [optional]
**value** | **str** | search term popularity represents the popularity of the topic. Scoring is on a relative scale where a value of 100 is the most commonly searched topic and a value of 50 is a topic searched half as often as the most popular term, and so on. | [optional]

## Example

```python
from dataforseo_client.models.topic_list_data_item_info import TopicListDataItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TopicListDataItemInfo from a JSON string
topic_list_data_item_info_instance = TopicListDataItemInfo.from_json(json)
# print the JSON string representation of the object
print TopicListDataItemInfo.to_json()

# convert the object into a dict
topic_list_data_item_info_dict = topic_list_data_item_info_instance.to_dict()
# create an instance of TopicListDataItemInfo from a dict
topic_list_data_item_info_form_dict = topic_list_data_item_info.from_dict(topic_list_data_item_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")