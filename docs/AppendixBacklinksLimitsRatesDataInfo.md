# AppendixBacklinksLimitsRatesDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**history** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**content_duplicates** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**domain_intersection** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**backlinks** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**domain_pages** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**anchors** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**referring_domains** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**page_intersection** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**referring_networks** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**bulk_ranks** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**bulk_backlinks** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**bulk_new_lost_backlinks** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**bulk_new_lost_referring_domains** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**bulk_referring_domains** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**errors** | **float** |  | [optional] 
**domain_pages_summary** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**timeseries_summary** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**timeseries_new_lost_summary** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 
**competitors** | [**AppendixFunctionInfo**](AppendixFunctionInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_backlinks_limits_rates_data_info import AppendixBacklinksLimitsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixBacklinksLimitsRatesDataInfo from a JSON string
appendix_backlinks_limits_rates_data_info_instance = AppendixBacklinksLimitsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixBacklinksLimitsRatesDataInfo.to_json()

# convert the object into a dict
appendix_backlinks_limits_rates_data_info_dict = appendix_backlinks_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixBacklinksLimitsRatesDataInfo from a dict
appendix_backlinks_limits_rates_data_info_form_dict = appendix_backlinks_limits_rates_data_info.from_dict(appendix_backlinks_limits_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


