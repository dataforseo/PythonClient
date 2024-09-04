# AppendixMinuteStatisticsMoneyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serp** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional] 
**total** | **float** | total amount of money deposited to your account | [optional] 
**total_serp** | **float** |  | [optional] 
**keywords_data** | [**AppendixKeywordsDatasRatesDataInfo**](AppendixKeywordsDatasRatesDataInfo.md) |  | [optional] 
**total_keywords_data** | **float** |  | [optional] 
**appendix** | [**AppendixAppendixsRatesDataInfo**](AppendixAppendixsRatesDataInfo.md) |  | [optional] 
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
**value** | **str** | time period for grouping day in the yyyy-MM-dd format minute in the yyyy-MM-dd HH:mm format | [optional] 

## Example

```python
from dataforseo_client.models.appendix_minute_statistics_money_data import AppendixMinuteStatisticsMoneyData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixMinuteStatisticsMoneyData from a JSON string
appendix_minute_statistics_money_data_instance = AppendixMinuteStatisticsMoneyData.from_json(json)
# print the JSON string representation of the object
print AppendixMinuteStatisticsMoneyData.to_json()

# convert the object into a dict
appendix_minute_statistics_money_data_dict = appendix_minute_statistics_money_data_instance.to_dict()
# create an instance of AppendixMinuteStatisticsMoneyData from a dict
appendix_minute_statistics_money_data_form_dict = appendix_minute_statistics_money_data.from_dict(appendix_minute_statistics_money_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


