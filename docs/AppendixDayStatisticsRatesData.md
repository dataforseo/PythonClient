# AppendixDayStatisticsRatesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serp** | [**AppendixSerpDayStatisticsRatesData**](AppendixSerpDayStatisticsRatesData.md) |  | [optional] 
**total** | **float** | total amount of money deposited to your account | [optional] 
**total_serp** | **float** |  | [optional] 
**keywords_data** | [**AppendixKeywordsDataDayStatisticsRatesData**](AppendixKeywordsDataDayStatisticsRatesData.md) |  | [optional] 
**total_keywords_data** | **float** |  | [optional] 
**appendix** | [**AppendixAppendixDayStatisticsRatesData**](AppendixAppendixDayStatisticsRatesData.md) |  | [optional] 
**total_appendix** | **float** |  | [optional] 
**dataforseo_labs** | [**AppendixDataforseoLabsDayStatisticsRatesData**](AppendixDataforseoLabsDayStatisticsRatesData.md) |  | [optional] 
**total_dataforseo_labs** | **float** |  | [optional] 
**domain_analytics** | [**AppendixDomainAnalyticsDayStatisticsRatesData**](AppendixDomainAnalyticsDayStatisticsRatesData.md) |  | [optional] 
**total_domain_analytics** | **float** |  | [optional] 
**merchant** | [**AppendixMerchantDayStatisticsRatesData**](AppendixMerchantDayStatisticsRatesData.md) |  | [optional] 
**total_merchant** | **float** |  | [optional] 
**on_page** | [**AppendixOnPageDayStatisticsRatesData**](AppendixOnPageDayStatisticsRatesData.md) |  | [optional] 
**total_on_page** | **float** |  | [optional] 
**business_data** | [**AppendixBusinessDataDayStatisticsRatesData**](AppendixBusinessDataDayStatisticsRatesData.md) |  | [optional] 
**total_business_data** | **float** |  | [optional] 
**backlinks** | [**AppendixBacklinksDayStatisticsRatesData**](AppendixBacklinksDayStatisticsRatesData.md) |  | [optional] 
**total_backlinks** | **float** |  | [optional] 
**app_data** | [**AppendixAppDataDayStatisticsRatesData**](AppendixAppDataDayStatisticsRatesData.md) |  | [optional] 
**total_app_data** | **float** |  | [optional] 
**content_analysis** | [**AppendixContentAnalysisDayStatisticsRatesData**](AppendixContentAnalysisDayStatisticsRatesData.md) |  | [optional] 
**total_content_analysis** | **float** |  | [optional] 
**content_generation** | [**AppendixContentGenerationDayStatisticsRatesData**](AppendixContentGenerationDayStatisticsRatesData.md) |  | [optional] 
**total_content_generation** | **float** |  | [optional] 
**value** | **str** | time period for grouping day in the yyyy-MM-dd format minute in the yyyy-MM-dd HH:mm format | [optional] 
**total_reviews** | **float** |  | [optional] 
**reviews** | [**AppendixInfo**](AppendixInfo.md) |  | [optional] 
**total_traffic_analytics** | **float** |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_day_statistics_rates_data import AppendixDayStatisticsRatesData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixDayStatisticsRatesData from a JSON string
appendix_day_statistics_rates_data_instance = AppendixDayStatisticsRatesData.from_json(json)
# print the JSON string representation of the object
print AppendixDayStatisticsRatesData.to_json()

# convert the object into a dict
appendix_day_statistics_rates_data_dict = appendix_day_statistics_rates_data_instance.to_dict()
# create an instance of AppendixDayStatisticsRatesData from a dict
appendix_day_statistics_rates_data_form_dict = appendix_day_statistics_rates_data.from_dict(appendix_day_statistics_rates_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


