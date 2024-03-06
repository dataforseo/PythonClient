[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixGoogleBusinessDataPriceData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hotel_info** | [**AppendixHotelInfoGoogleBusinessDataPriceData**](AppendixHotelInfoGoogleBusinessDataPriceData.md) |  | [optional]
**hotel_searches** | [**AppendixGoogleBusinessDataPriceDataInfo**](AppendixGoogleBusinessDataPriceDataInfo.md) |  | [optional]
**my_business_info** | [**AppendixGoogleBusinessDataPriceDataInfo**](AppendixGoogleBusinessDataPriceDataInfo.md) |  | [optional]
**my_business_updates** | [**AppendixGoogleBusinessDataPriceDataInfo**](AppendixGoogleBusinessDataPriceDataInfo.md) |  | [optional]
**reviews** | [**AppendixGoogleBusinessDataPriceDataInfo**](AppendixGoogleBusinessDataPriceDataInfo.md) |  | [optional]

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

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")