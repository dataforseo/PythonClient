# MicrodataFieldsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | field name name of the data field | [optional] 
**types** | **List[Optional[str]]** | parent microdata types for a full list of available types, please visit schema.org | [optional] 
**value** | **str** | microdata value microdata value specified on a target web page | [optional] 
**test_results** | [**List[MessageInfo]**](MessageInfo.md) | list of microdata types | [optional] 
**fields** | [**List[MicrodataFieldsInfo]**](MicrodataFieldsInfo.md) | microdata fields an array of objects containing data fields related to the certain microdata type | [optional] 

## Example

```python
from dataforseo_client.models.microdata_fields_info import MicrodataFieldsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodataFieldsInfo from a JSON string
microdata_fields_info_instance = MicrodataFieldsInfo.from_json(json)
# print the JSON string representation of the object
print(MicrodataFieldsInfo.to_json())

# convert the object into a dict
microdata_fields_info_dict = microdata_fields_info_instance.to_dict()
# create an instance of MicrodataFieldsInfo from a dict
microdata_fields_info_from_dict = MicrodataFieldsInfo.from_dict(microdata_fields_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


