# AppendixBacklinksLimitsRatesDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**history** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**content_duplicates** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**domain_intersection** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**backlinks** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**domain_pages** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**anchors** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**referring_domains** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**page_intersection** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**referring_networks** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**bulk_ranks** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**bulk_backlinks** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**bulk_new_lost_backlinks** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**bulk_new_lost_referring_domains** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**bulk_referring_domains** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**errors** | **float** |  | [optional] 
**domain_pages_summary** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**timeseries_summary** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**timeseries_new_lost_summary** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**competitors** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 

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


