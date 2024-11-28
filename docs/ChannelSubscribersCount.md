# ChannelSubscribersCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayed_count** | **str** | displayed subscriber count subscriber count as displayed on YouTube | [optional] 
**count** | **int** | subscriber count | [optional] 

## Example

```python
from dataforseo_client.models.channel_subscribers_count import ChannelSubscribersCount

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelSubscribersCount from a JSON string
channel_subscribers_count_instance = ChannelSubscribersCount.from_json(json)
# print the JSON string representation of the object
print(ChannelSubscribersCount.to_json())

# convert the object into a dict
channel_subscribers_count_dict = channel_subscribers_count_instance.to_dict()
# create an instance of ChannelSubscribersCount from a dict
channel_subscribers_count_from_dict = ChannelSubscribersCount.from_dict(channel_subscribers_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


