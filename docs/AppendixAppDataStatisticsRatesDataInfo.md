# AppendixAppDataStatisticsRatesDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_info** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**app_list** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**app_reviews** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**app_searches** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**errors** | **float** |  | [optional] 
**languages** | **float** |  | [optional] 
**locations** | **float** |  | [optional] 
**categories** | **float** |  | [optional] 
**tasks_ready** | **float** |  | [optional] 
**app_listings** | [**AppendixBusinessListingsBusinessDataLimitsRatesDataInfo**](AppendixBusinessListingsBusinessDataLimitsRatesDataInfo.md) |  | [optional] 
**id_list** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_app_data_statistics_rates_data_info import AppendixAppDataStatisticsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixAppDataStatisticsRatesDataInfo from a JSON string
appendix_app_data_statistics_rates_data_info_instance = AppendixAppDataStatisticsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixAppDataStatisticsRatesDataInfo.to_json()

# convert the object into a dict
appendix_app_data_statistics_rates_data_info_dict = appendix_app_data_statistics_rates_data_info_instance.to_dict()
# create an instance of AppendixAppDataStatisticsRatesDataInfo from a dict
appendix_app_data_statistics_rates_data_info_form_dict = appendix_app_data_statistics_rates_data_info.from_dict(appendix_app_data_statistics_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


