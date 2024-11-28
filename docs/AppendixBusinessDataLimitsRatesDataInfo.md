# AppendixBusinessDataLimitsRatesDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google** | [**AppendixBusinessDataGoogleInfo**](AppendixBusinessDataGoogleInfo.md) |  | [optional] 
**locations** | **float** |  | [optional] 
**languages** | **float** |  | [optional] 
**errors** | **float** |  | [optional] 
**yelp** | [**AppendixBusinessDataDayLimitsRatesDataInfo**](AppendixBusinessDataDayLimitsRatesDataInfo.md) |  | [optional] 
**social_media** | [**AppendixSocialMediaBusinessDataLimitsRatesDataInfo**](AppendixSocialMediaBusinessDataLimitsRatesDataInfo.md) |  | [optional] 
**tripadvisor** | [**AppendixBusinessDataDayLimitsRatesDataInfo**](AppendixBusinessDataDayLimitsRatesDataInfo.md) |  | [optional] 
**trustpilot** | [**AppendixBusinessDataDayLimitsRatesDataInfo**](AppendixBusinessDataDayLimitsRatesDataInfo.md) |  | [optional] 
**business_listings** | [**AppendixBusinessListingsBusinessDataLimitsRatesDataInfo**](AppendixBusinessListingsBusinessDataLimitsRatesDataInfo.md) |  | [optional] 
**tasks_ready** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_business_data_limits_rates_data_info import AppendixBusinessDataLimitsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixBusinessDataLimitsRatesDataInfo from a JSON string
appendix_business_data_limits_rates_data_info_instance = AppendixBusinessDataLimitsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixBusinessDataLimitsRatesDataInfo.to_json())

# convert the object into a dict
appendix_business_data_limits_rates_data_info_dict = appendix_business_data_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixBusinessDataLimitsRatesDataInfo from a dict
appendix_business_data_limits_rates_data_info_from_dict = AppendixBusinessDataLimitsRatesDataInfo.from_dict(appendix_business_data_limits_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


