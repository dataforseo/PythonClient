# AppendixOnPagePriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**lighthouse** | [**AppendixLighthouseOnPagePriceData**](AppendixLighthouseOnPagePriceData.md) |  | [optional] 
**content_parsing** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**content_parsing_live** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**duplicate_content** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**duplicate_tags** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**instant_pages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**keyword_density** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**links** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**non_indexable** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**pages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**pages_by_resource** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**page_screenshot** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**raw_html** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**redirect_chains** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**resources** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**summary** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**task_post** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**tasks_ready** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**waterfall** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_on_page_price_data import AppendixOnPagePriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixOnPagePriceData from a JSON string
appendix_on_page_price_data_instance = AppendixOnPagePriceData.from_json(json)
# print the JSON string representation of the object
print AppendixOnPagePriceData.to_json()

# convert the object into a dict
appendix_on_page_price_data_dict = appendix_on_page_price_data_instance.to_dict()
# create an instance of AppendixOnPagePriceData from a dict
appendix_on_page_price_data_form_dict = appendix_on_page_price_data.from_dict(appendix_on_page_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


