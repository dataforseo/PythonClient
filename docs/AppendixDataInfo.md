# AppendixDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serp** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**total** | **float** | total amount of money deposited to your account | [optional] 
**total_serp** | **float** |  | [optional] 
**keywords_data** | [**AppendixKeywordsDataDataInfo**](AppendixKeywordsDataDataInfo.md) |  | [optional] 
**total_keywords_data** | **float** |  | [optional] 
**appendix** | [**AppendixAppendixDataInfo**](AppendixAppendixDataInfo.md) |  | [optional] 
**total_appendix** | **float** |  | [optional] 
**dataforseo_labs** | [**AppendixDataforseoLabsLimitsRatesDataInfo**](AppendixDataforseoLabsLimitsRatesDataInfo.md) |  | [optional] 
**total_dataforseo_labs** | **float** |  | [optional] 
**domain_analytics** | [**AppendixDomainAnalyticsLimitsRatesDataInfo**](AppendixDomainAnalyticsLimitsRatesDataInfo.md) |  | [optional] 
**total_domain_analytics** | **float** |  | [optional] 
**merchant** | [**AppendixMerchantLimitsRatesDataInfo**](AppendixMerchantLimitsRatesDataInfo.md) |  | [optional] 
**total_merchant** | **float** |  | [optional] 
**on_page** | [**AppendixOnPageLimitsRatesDataInfo**](AppendixOnPageLimitsRatesDataInfo.md) |  | [optional] 
**total_on_page** | **float** |  | [optional] 
**business_data** | [**AppendixBusinessDataLimitsRatesDataInfo**](AppendixBusinessDataLimitsRatesDataInfo.md) |  | [optional] 
**total_business_data** | **float** |  | [optional] 
**backlinks** | [**AppendixBacklinksLimitsRatesDataInfo**](AppendixBacklinksLimitsRatesDataInfo.md) |  | [optional] 
**total_backlinks** | **float** |  | [optional] 
**app_data** | [**AppendixAppDataLimitsRatesDataInfo**](AppendixAppDataLimitsRatesDataInfo.md) |  | [optional] 
**total_app_data** | **float** |  | [optional] 
**content_analysis** | [**AppendixContentAnalysisLimitsRatesDataInfo**](AppendixContentAnalysisLimitsRatesDataInfo.md) |  | [optional] 
**total_content_analysis** | **float** |  | [optional] 
**content_generation** | [**AppendixContentGenerationLimitsRatesDataInfo**](AppendixContentGenerationLimitsRatesDataInfo.md) |  | [optional] 
**total_content_generation** | **float** |  | [optional] 
**total_traffic_analytics** | **float** |  | [optional] 
**traffic_analytics** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**total_reviews** | **float** |  | [optional] 
**reviews** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**total_social** | **float** |  | [optional] 
**social** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_data_info import AppendixDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixDataInfo from a JSON string
appendix_data_info_instance = AppendixDataInfo.from_json(json)
# print the JSON string representation of the object
print AppendixDataInfo.to_json()

# convert the object into a dict
appendix_data_info_dict = appendix_data_info_instance.to_dict()
# create an instance of AppendixDataInfo from a dict
appendix_data_info_form_dict = appendix_data_info.from_dict(appendix_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


