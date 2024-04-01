# TechnologiesInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_ons** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**analytics** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**web_development** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**security** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**business_tools** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**sales** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**other** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**user_generated_content** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**privacy** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**servers** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**location** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**content** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**media** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**marketing** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**communication** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 
**utilities** | **Dict[str, Optional[List[Optional[str]]]]** |  | [optional] 

## Example

```python
from dataforseo_client.models.technologies_info import TechnologiesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TechnologiesInfo from a JSON string
technologies_info_instance = TechnologiesInfo.from_json(json)
# print the JSON string representation of the object
print(TechnologiesInfo.to_json())

# convert the object into a dict
technologies_info_dict = technologies_info_instance.to_dict()
# create an instance of TechnologiesInfo from a dict
technologies_info_form_dict = technologies_info.from_dict(technologies_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


