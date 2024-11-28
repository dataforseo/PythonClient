# AppendixBusinessDataGoogleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**my_business_info** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**my_business_updates** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**hotel_info** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**hotel_searches** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**reviews** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**questions_and_answers** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**extended_reviews** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_business_data_google_info import AppendixBusinessDataGoogleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixBusinessDataGoogleInfo from a JSON string
appendix_business_data_google_info_instance = AppendixBusinessDataGoogleInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixBusinessDataGoogleInfo.to_json())

# convert the object into a dict
appendix_business_data_google_info_dict = appendix_business_data_google_info_instance.to_dict()
# create an instance of AppendixBusinessDataGoogleInfo from a dict
appendix_business_data_google_info_from_dict = AppendixBusinessDataGoogleInfo.from_dict(appendix_business_data_google_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


