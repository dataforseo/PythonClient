# ResponseDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** | author of the response | [optional] 
**title** | **str** | title of the response in this case, will equal null | [optional] 
**text** | **str** | content of the response | [optional] 
**timestamp** | **str** | date and time when the response was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”; example: 2019-11-15 12:57:46 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.response_data_info import ResponseDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDataInfo from a JSON string
response_data_info_instance = ResponseDataInfo.from_json(json)
# print the JSON string representation of the object
print ResponseDataInfo.to_json()

# convert the object into a dict
response_data_info_dict = response_data_info_instance.to_dict()
# create an instance of ResponseDataInfo from a dict
response_data_info_form_dict = response_data_info.from_dict(response_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


