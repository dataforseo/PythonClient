# AppendixSerpPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tasks_fixed** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**errors** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**jobs** | [**AppendixKeywordsKeywordsDataPriceDataInfo**](AppendixKeywordsKeywordsDataPriceDataInfo.md) |  | [optional] 
**languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**live** | [**AppendixSerpPriceDataInfo**](AppendixSerpPriceDataInfo.md) |  | [optional] 
**locations** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**screenshot** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**task_get** | [**AppendixSerpPriceDataInfo**](AppendixSerpPriceDataInfo.md) |  | [optional] 
**task_post** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**tasks_ready** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_serp_price_data import AppendixSerpPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixSerpPriceData from a JSON string
appendix_serp_price_data_instance = AppendixSerpPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixSerpPriceData.to_json())

# convert the object into a dict
appendix_serp_price_data_dict = appendix_serp_price_data_instance.to_dict()
# create an instance of AppendixSerpPriceData from a dict
appendix_serp_price_data_form_dict = appendix_serp_price_data.from_dict(appendix_serp_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


