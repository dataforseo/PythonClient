# AppendixOnPageLimitsRatesDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_post** | **float** |  | [optional] 
**tasks_ready** | **float** |  | [optional] 
**summary** | **float** |  | [optional] 
**resources** | **float** |  | [optional] 
**pages** | **float** |  | [optional] 
**non_indexable** | **float** |  | [optional] 
**duplicate_tags** | **float** |  | [optional] 
**links** | **float** |  | [optional] 
**waterfall** | **float** |  | [optional] 
**errors** | **float** |  | [optional] 
**pages_by_resource** | **float** |  | [optional] 
**duplicate_content** | **float** |  | [optional] 
**raw_html** | **float** |  | [optional] 
**instant_pages** | **float** |  | [optional] 
**redirect_chains** | **float** |  | [optional] 
**lighthouse** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**keyword_density** | **float** |  | [optional] 
**page_screenshot** | **float** |  | [optional] 
**content_parsing** | **float** |  | [optional] 
**content_parsing_live** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_on_page_limits_rates_data_info import AppendixOnPageLimitsRatesDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixOnPageLimitsRatesDataInfo from a JSON string
appendix_on_page_limits_rates_data_info_instance = AppendixOnPageLimitsRatesDataInfo.from_json(json)
# print the JSON string representation of the object
print(AppendixOnPageLimitsRatesDataInfo.to_json())

# convert the object into a dict
appendix_on_page_limits_rates_data_info_dict = appendix_on_page_limits_rates_data_info_instance.to_dict()
# create an instance of AppendixOnPageLimitsRatesDataInfo from a dict
appendix_on_page_limits_rates_data_info_from_dict = AppendixOnPageLimitsRatesDataInfo.from_dict(appendix_on_page_limits_rates_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


