[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixMerchantPriceData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google** | [**AppendixGoogleMerchantPriceData**](AppendixGoogleMerchantPriceData.md) |  | [optional]
**amazon** | [**AppendixAmazonMerchantPriceData**](AppendixAmazonMerchantPriceData.md) |  | [optional]
**errors** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**languages** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**locations** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**reviews** | [**AppendixProductGoogleMerchantPriceDataInfo**](AppendixProductGoogleMerchantPriceDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_merchant_price_data import AppendixMerchantPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixMerchantPriceData from a JSON string
appendix_merchant_price_data_instance = AppendixMerchantPriceData.from_json(json)
# print the JSON string representation of the object
print AppendixMerchantPriceData.to_json()

# convert the object into a dict
appendix_merchant_price_data_dict = appendix_merchant_price_data_instance.to_dict()
# create an instance of AppendixMerchantPriceData from a dict
appendix_merchant_price_data_form_dict = appendix_merchant_price_data.from_dict(appendix_merchant_price_data_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")