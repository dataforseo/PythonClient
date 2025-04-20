# AppendixStatisticsRatesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | [**AppendixDayStatisticsRatesData**](AppendixDayStatisticsRatesData.md) |  | [optional] 
**minute** | [**AppendixMinuteStatisticsRatesData**](AppendixMinuteStatisticsRatesData.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_statistics_rates_data import AppendixStatisticsRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixStatisticsRatesData from a JSON string
appendix_statistics_rates_data_instance = AppendixStatisticsRatesData.from_json(json)
# print the JSON string representation of the object
print(AppendixStatisticsRatesData.to_json())

# convert the object into a dict
appendix_statistics_rates_data_dict = appendix_statistics_rates_data_instance.to_dict()
# create an instance of AppendixStatisticsRatesData from a dict
appendix_statistics_rates_data_from_dict = AppendixStatisticsRatesData.from_dict(appendix_statistics_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


