# History


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | year | [optional] 
**month** | **int** | month | [optional] 
**keyword_info** | [**KeywordInfo**](KeywordInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.history import History

# TODO update the JSON string below
json = "{}"
# create an instance of History from a JSON string
history_instance = History.from_json(json)
# print the JSON string representation of the object
print(History.to_json())

# convert the object into a dict
history_dict = history_instance.to_dict()
# create an instance of History from a dict
history_from_dict = History.from_dict(history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


