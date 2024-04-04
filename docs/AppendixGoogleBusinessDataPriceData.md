# AppendixGoogleBusinessDataPriceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_info** | [**AppendixHotelInfoGoogleBusinessDataPriceData**](AppendixHotelInfoGoogleBusinessDataPriceData.md) |  | [optional] 
**hotel_searches** | [**AppendixHotelSearchesGoogleBusinessDataPriceData**](AppendixHotelSearchesGoogleBusinessDataPriceData.md) |  | [optional] 
**my_business_info** | [**AppendixHotelSearchesGoogleBusinessDataPriceData**](AppendixHotelSearchesGoogleBusinessDataPriceData.md) |  | [optional] 
**my_business_updates** | [**AppendixHotelSearchesGoogleBusinessDataPriceData**](AppendixHotelSearchesGoogleBusinessDataPriceData.md) |  | [optional] 
**reviews** | [**AppendixHotelSearchesGoogleBusinessDataPriceData**](AppendixHotelSearchesGoogleBusinessDataPriceData.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.appendix_google_business_data_price_data import AppendixGoogleBusinessDataPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixGoogleBusinessDataPriceData from a JSON string
appendix_google_business_data_price_data_instance = AppendixGoogleBusinessDataPriceData.from_json(json)
# print the JSON string representation of the object
print AppendixGoogleBusinessDataPriceData.to_json()

# convert the object into a dict
appendix_google_business_data_price_data_dict = appendix_google_business_data_price_data_instance.to_dict()
# create an instance of AppendixGoogleBusinessDataPriceData from a dict
appendix_google_business_data_price_data_form_dict = appendix_google_business_data_price_data.from_dict(appendix_google_business_data_price_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


