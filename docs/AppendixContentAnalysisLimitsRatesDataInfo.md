# AppendixContentAnalysisLimitsRatesDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**summary** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**sentiment_analysis** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**rating_distribution** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**phrase_trends** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**category_trends** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
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
print AppendixContentAnalysisLimitsRatesDataInfo.to_json()

# convert the object into a dict
appendix_content_analysis_limits_rates_data_info_dict = appendix_content_analysis_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixContentAnalysisLimitsRatesDataInfo from a dict
appendix_content_analysis_limits_rates_data_info_form_dict = appendix_content_analysis_limits_rates_data_info.from_dict(appendix_content_analysis_limits_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


