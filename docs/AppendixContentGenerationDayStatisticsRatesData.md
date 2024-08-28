# AppendixContentGenerationDayStatisticsRatesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generate** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**generate_meta_tags** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**generate_text** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**paraphrase** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**check_grammar** | [**AppendixContentGenerationDayLimitsRatesDataInfo**](AppendixContentGenerationDayLimitsRatesDataInfo.md) |  | [optional] 
**text_summary** | [**AppendixContentGenerationDayLimitsRatesDataInfo**](AppendixContentGenerationDayLimitsRatesDataInfo.md) |  | [optional] 
**generate_sub_topics** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**grammar_rules** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_content_generation_day_statistics_rates_data import AppendixContentGenerationDayStatisticsRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixContentGenerationDayStatisticsRatesData from a JSON string
appendix_content_generation_day_statistics_rates_data_instance = AppendixContentGenerationDayStatisticsRatesData.from_json(json)
# print the JSON string representation of the object
print AppendixContentGenerationDayStatisticsRatesData.to_json()

# convert the object into a dict
appendix_content_generation_day_statistics_rates_data_dict = appendix_content_generation_day_statistics_rates_data_instance.to_dict()
# create an instance of AppendixContentGenerationDayStatisticsRatesData from a dict
appendix_content_generation_day_statistics_rates_data_form_dict = appendix_content_generation_day_statistics_rates_data.from_dict(appendix_content_generation_day_statistics_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


