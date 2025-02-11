# AppendixGoogleBusinessDataPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extended_reviews** | [**AppendixAKeywordsDataPriceDataInfo**](AppendixAKeywordsDataPriceDataInfo.md) |  | [optional] 
**hotel_info** | [**AppendixHotelInfoGoogleBusinessDataPriceData**](AppendixHotelInfoGoogleBusinessDataPriceData.md) |  | [optional] 
**hotel_searches** | [**AppendixGoogleBusinessDataPriceDataInfo**](AppendixGoogleBusinessDataPriceDataInfo.md) |  | [optional] 
**my_business_info** | [**AppendixGoogleBusinessDataPriceDataInfo**](AppendixGoogleBusinessDataPriceDataInfo.md) |  | [optional] 
**my_business_updates** | [**AppendixGoogleBusinessDataPriceDataInfo**](AppendixGoogleBusinessDataPriceDataInfo.md) |  | [optional] 
**questions_and_answers** | [**AppendixGoogleBusinessDataPriceDataInfo**](AppendixGoogleBusinessDataPriceDataInfo.md) |  | [optional] 
**reviews** | [**AppendixGoogleBusinessDataPriceDataInfo**](AppendixGoogleBusinessDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_google_business_data_price_data import AppendixGoogleBusinessDataPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixGoogleBusinessDataPriceData from a JSON string
appendix_google_business_data_price_data_instance = AppendixGoogleBusinessDataPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixGoogleBusinessDataPriceData.to_json())

# convert the object into a dict
appendix_google_business_data_price_data_dict = appendix_google_business_data_price_data_instance.to_dict()
# create an instance of AppendixGoogleBusinessDataPriceData from a dict
appendix_google_business_data_price_data_from_dict = AppendixGoogleBusinessDataPriceData.from_dict(appendix_google_business_data_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


