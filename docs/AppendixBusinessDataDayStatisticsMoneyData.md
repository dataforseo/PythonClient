# AppendixBusinessDataDayStatisticsMoneyData


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
**refund_money** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_business_data_day_statistics_money_data import AppendixBusinessDataDayStatisticsMoneyData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixBusinessDataDayStatisticsMoneyData from a JSON string
appendix_business_data_day_statistics_money_data_instance = AppendixBusinessDataDayStatisticsMoneyData.from_json(json)
# print the JSON string representation of the object
print AppendixBusinessDataDayStatisticsMoneyData.to_json()

# convert the object into a dict
appendix_business_data_day_statistics_money_data_dict = appendix_business_data_day_statistics_money_data_instance.to_dict()
# create an instance of AppendixBusinessDataDayStatisticsMoneyData from a dict
appendix_business_data_day_statistics_money_data_form_dict = appendix_business_data_day_statistics_money_data.from_dict(appendix_business_data_day_statistics_money_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


