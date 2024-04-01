# AppendixUserDataResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | your login | [optional] 
**timezone** | **str** | your time zone can be set in your profile settings | [optional] 
**rates** | [**AppendixRatesData**](AppendixRatesData.md) |  | [optional] 
**money** | [**AppendixMoneyData**](AppendixMoneyData.md) |  | [optional] 
**price** | [**AppendixPriceData**](AppendixPriceData.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_user_data_result_info import AppendixUserDataResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixUserDataResultInfo from a JSON string
appendix_user_data_result_info_instance = AppendixUserDataResultInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixUserDataResultInfo.to_json())

# convert the object into a dict
appendix_user_data_result_info_dict = appendix_user_data_result_info_instance.to_dict()
# create an instance of AppendixUserDataResultInfo from a dict
appendix_user_data_result_info_form_dict = appendix_user_data_result_info.from_dict(appendix_user_data_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


