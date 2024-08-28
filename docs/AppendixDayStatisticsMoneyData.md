# AppendixDayStatisticsMoneyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serp** | [**AppendixSerpDayStatisticsMoneyData**](AppendixSerpDayStatisticsMoneyData.md) |  | [optional] 
**total** | **float** | total amount of money deposited to your account | [optional] 
**total_serp** | **float** |  | [optional] 
**keywords_data** | [**AppendixKeywordsDataDayStatisticsMoneyData**](AppendixKeywordsDataDayStatisticsMoneyData.md) |  | [optional] 
**total_keywords_data** | **float** |  | [optional] 
**appendix** | [**AppendixAppendixsRatesDataInfo**](AppendixAppendixsRatesDataInfo.md) |  | [optional] 
**total_appendix** | **float** |  | [optional] 
**dataforseo_labs** | [**AppendixDataforseoLabsDayStatisticsRatesData**](AppendixDataforseoLabsDayStatisticsRatesData.md) |  | [optional] 
**total_dataforseo_labs** | **float** |  | [optional] 
**domain_analytics** | [**AppendixDomainAnalyticsLimitsRatesDataInfo**](AppendixDomainAnalyticsLimitsRatesDataInfo.md) |  | [optional] 
**total_domain_analytics** | **float** |  | [optional] 
**merchant** | [**AppendixMerchantLimitsRatesDataInfo**](AppendixMerchantLimitsRatesDataInfo.md) |  | [optional] 
**total_merchant** | **float** |  | [optional] 
**on_page** | [**AppendixOnPageDayStatisticsMoneyData**](AppendixOnPageDayStatisticsMoneyData.md) |  | [optional] 
**total_on_page** | **float** |  | [optional] 
**business_data** | [**AppendixBusinessDataDayStatisticsMoneyData**](AppendixBusinessDataDayStatisticsMoneyData.md) |  | [optional] 
**total_business_data** | **float** |  | [optional] 
**backlinks** | [**AppendixBacklinksDayStatisticsRatesData**](AppendixBacklinksDayStatisticsRatesData.md) |  | [optional] 
**total_backlinks** | **float** |  | [optional] 
**app_data** | [**AppendixAppDataDayStatisticsMoneyData**](AppendixAppDataDayStatisticsMoneyData.md) |  | [optional] 
**total_app_data** | **float** |  | [optional] 
**content_analysis** | [**AppendixContentAnalysisLimitsRatesDataInfo**](AppendixContentAnalysisLimitsRatesDataInfo.md) |  | [optional] 
**total_content_analysis** | **float** |  | [optional] 
**content_generation** | [**AppendixContentGenerationLimitsRatesDataInfo**](AppendixContentGenerationLimitsRatesDataInfo.md) |  | [optional] 
**total_content_generation** | **float** |  | [optional] 
**value** | **str** | time period for grouping day in the yyyy-MM-dd format minute in the yyyy-MM-dd HH:mm format | [optional] 
**total_traffic_analytics** | **float** |  | [optional] 
**total_reviews** | **float** |  | [optional] 
**reviews** | [**AppendixJobsSerpLimitsRatesDataInfo**](AppendixJobsSerpLimitsRatesDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_day_statistics_money_data import AppendixDayStatisticsMoneyData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixDayStatisticsMoneyData from a JSON string
appendix_day_statistics_money_data_instance = AppendixDayStatisticsMoneyData.from_json(json)
# print the JSON string representation of the object
print AppendixDayStatisticsMoneyData.to_json()

# convert the object into a dict
appendix_day_statistics_money_data_dict = appendix_day_statistics_money_data_instance.to_dict()
# create an instance of AppendixDayStatisticsMoneyData from a dict
appendix_day_statistics_money_data_form_dict = appendix_day_statistics_money_data.from_dict(appendix_day_statistics_money_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


