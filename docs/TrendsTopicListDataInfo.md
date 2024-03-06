[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# TrendsTopicListDataInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top** | [**List[TopicListDataItemInfo]**](TopicListDataItemInfo.md) | the most popular related topics represents the list of the most popular related topics | [optional]
**rising** | [**List[TopicListDataItemInfo]**](TopicListDataItemInfo.md) | emerging related topics represents the list of related topics with the biggest increase in search frequency since the last time period | [optional]

## Example

```python
from dataforseo_client.models.trends_topic_list_data_info import TrendsTopicListDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TrendsTopicListDataInfo from a JSON string
trends_topic_list_data_info_instance = TrendsTopicListDataInfo.from_json(json)
# print the JSON string representation of the object
print TrendsTopicListDataInfo.to_json()

# convert the object into a dict
trends_topic_list_data_info_dict = trends_topic_list_data_info_instance.to_dict()
# create an instance of TrendsTopicListDataInfo from a dict
trends_topic_list_data_info_form_dict = trends_topic_list_data_info.from_dict(trends_topic_list_data_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")