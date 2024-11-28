# AppendixBusinessDataPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_listings** | [**AppendixBusinessListingsBusinessDataPriceData**](AppendixBusinessListingsBusinessDataPriceData.md) |  | [optional] 
**errors** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**google** | [**AppendixGoogleBusinessDataPriceData**](AppendixGoogleBusinessDataPriceData.md) |  | [optional] 
**social_media** | [**AppendixSocialMediaBusinessDataPriceData**](AppendixSocialMediaBusinessDataPriceData.md) |  | [optional] 
**languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**locations** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**tripadvisor** | [**AppendixTrBusinessDataPriceDataInfo**](AppendixTrBusinessDataPriceDataInfo.md) |  | [optional] 
**trustpilot** | [**AppendixTrBusinessDataPriceDataInfo**](AppendixTrBusinessDataPriceDataInfo.md) |  | [optional] 
**yelp** | [**AppendixTrBusinessDataPriceDataInfo**](AppendixTrBusinessDataPriceDataInfo.md) |  | [optional] 
**tasks_ready** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_business_data_price_data import AppendixBusinessDataPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixBusinessDataPriceData from a JSON string
appendix_business_data_price_data_instance = AppendixBusinessDataPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixBusinessDataPriceData.to_json())

# convert the object into a dict
appendix_business_data_price_data_dict = appendix_business_data_price_data_instance.to_dict()
# create an instance of AppendixBusinessDataPriceData from a dict
appendix_business_data_price_data_from_dict = AppendixBusinessDataPriceData.from_dict(appendix_business_data_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


