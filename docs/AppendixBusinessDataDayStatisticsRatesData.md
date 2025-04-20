# AppendixBusinessDataDayStatisticsRatesData


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
**available_filters** | **float** |  | [optional] 
**id_list** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_business_data_day_statistics_rates_data import AppendixBusinessDataDayStatisticsRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixBusinessDataDayStatisticsRatesData from a JSON string
appendix_business_data_day_statistics_rates_data_instance = AppendixBusinessDataDayStatisticsRatesData.from_json(json)
# print the JSON string representation of the object
print(AppendixBusinessDataDayStatisticsRatesData.to_json())

# convert the object into a dict
appendix_business_data_day_statistics_rates_data_dict = appendix_business_data_day_statistics_rates_data_instance.to_dict()
# create an instance of AppendixBusinessDataDayStatisticsRatesData from a dict
appendix_business_data_day_statistics_rates_data_from_dict = AppendixBusinessDataDayStatisticsRatesData.from_dict(appendix_business_data_day_statistics_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


