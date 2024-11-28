# AppendixContentAnalysisDayStatisticsRatesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**summary** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**sentiment_analysis** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**rating_distribution** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**phrase_trends** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**category_trends** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**locations** | **float** |  | [optional] 
**languages** | **float** |  | [optional] 
**categories** | **float** |  | [optional] 
**errors** | **float** |  | [optional] 
**available_filters** | **float** |  | [optional] 
**id_list** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_content_analysis_day_statistics_rates_data import AppendixContentAnalysisDayStatisticsRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixContentAnalysisDayStatisticsRatesData from a JSON string
appendix_content_analysis_day_statistics_rates_data_instance = AppendixContentAnalysisDayStatisticsRatesData.from_json(json)
# print the JSON string representation of the object
print(AppendixContentAnalysisDayStatisticsRatesData.to_json())

# convert the object into a dict
appendix_content_analysis_day_statistics_rates_data_dict = appendix_content_analysis_day_statistics_rates_data_instance.to_dict()
# create an instance of AppendixContentAnalysisDayStatisticsRatesData from a dict
appendix_content_analysis_day_statistics_rates_data_from_dict = AppendixContentAnalysisDayStatisticsRatesData.from_dict(appendix_content_analysis_day_statistics_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


