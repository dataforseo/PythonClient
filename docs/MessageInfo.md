# MessageInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **str** | level of error can take the following values: fatal, error, warning, info | [optional] 
**message** | **str** | message associated with an error message providing the details of the detected error | [optional] 

## Example

```python
from dataforseo_client.models.message_info import MessageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MessageInfo from a JSON string
message_info_instance = MessageInfo.from_json(json)
# print the JSON string representation of the object
print(MessageInfo.to_json())

# convert the object into a dict
message_info_dict = message_info_instance.to_dict()
# create an instance of MessageInfo from a dict
message_info_from_dict = MessageInfo.from_dict(message_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


