# AppendixContentAnalysisLimitsRatesDataInfo


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

## Example

```python
from dataforseo_client.models.appendix_content_analysis_limits_rates_data_info import AppendixContentAnalysisLimitsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixContentAnalysisLimitsRatesDataInfo from a JSON string
appendix_content_analysis_limits_rates_data_info_instance = AppendixContentAnalysisLimitsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixContentAnalysisLimitsRatesDataInfo.to_json())

# convert the object into a dict
appendix_content_analysis_limits_rates_data_info_dict = appendix_content_analysis_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixContentAnalysisLimitsRatesDataInfo from a dict
appendix_content_analysis_limits_rates_data_info_from_dict = AppendixContentAnalysisLimitsRatesDataInfo.from_dict(appendix_content_analysis_limits_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


