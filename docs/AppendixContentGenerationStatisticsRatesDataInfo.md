# AppendixContentGenerationStatisticsRatesDataInfo


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
from dataforseo_client.models.appendix_content_generation_statistics_rates_data_info import AppendixContentGenerationStatisticsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixContentGenerationStatisticsRatesDataInfo from a JSON string
appendix_content_generation_statistics_rates_data_info_instance = AppendixContentGenerationStatisticsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixContentGenerationStatisticsRatesDataInfo.to_json()

# convert the object into a dict
appendix_content_generation_statistics_rates_data_info_dict = appendix_content_generation_statistics_rates_data_info_instance.to_dict()
# create an instance of AppendixContentGenerationStatisticsRatesDataInfo from a dict
appendix_content_generation_statistics_rates_data_info_form_dict = appendix_content_generation_statistics_rates_data_info.from_dict(appendix_content_generation_statistics_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


