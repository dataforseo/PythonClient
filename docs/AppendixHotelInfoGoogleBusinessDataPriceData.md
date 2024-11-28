# AppendixHotelInfoGoogleBusinessDataPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live** | [**AppendixTaskGetProductGoogleMerchantPriceDataInfo**](AppendixTaskGetProductGoogleMerchantPriceDataInfo.md) |  | [optional] 
**task_get** | [**AppendixTaskGetProductGoogleMerchantPriceDataInfo**](AppendixTaskGetProductGoogleMerchantPriceDataInfo.md) |  | [optional] 
**task_post** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 
**tasks_ready** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_hotel_info_google_business_data_price_data import AppendixHotelInfoGoogleBusinessDataPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixHotelInfoGoogleBusinessDataPriceData from a JSON string
appendix_hotel_info_google_business_data_price_data_instance = AppendixHotelInfoGoogleBusinessDataPriceData.from_json(json)
# print the JSON string representation of the object
print(AppendixHotelInfoGoogleBusinessDataPriceData.to_json())

# convert the object into a dict
appendix_hotel_info_google_business_data_price_data_dict = appendix_hotel_info_google_business_data_price_data_instance.to_dict()
# create an instance of AppendixHotelInfoGoogleBusinessDataPriceData from a dict
appendix_hotel_info_google_business_data_price_data_from_dict = AppendixHotelInfoGoogleBusinessDataPriceData.from_dict(appendix_hotel_info_google_business_data_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


