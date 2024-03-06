[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixAmazonMerchantPriceData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | [**AppendixProductGoogleMerchantPriceDataInfo**](AppendixProductGoogleMerchantPriceDataInfo.md) |  | [optional]
**products** | [**AppendixProductGoogleMerchantPriceDataInfo**](AppendixProductGoogleMerchantPriceDataInfo.md) |  | [optional]
**sellers** | [**AppendixProductGoogleMerchantPriceDataInfo**](AppendixProductGoogleMerchantPriceDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_amazon_merchant_price_data import AppendixAmazonMerchantPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixAmazonMerchantPriceData from a JSON string
appendix_amazon_merchant_price_data_instance = AppendixAmazonMerchantPriceData.from_json(json)
# print the JSON string representation of the object
print AppendixAmazonMerchantPriceData.to_json()

# convert the object into a dict
appendix_amazon_merchant_price_data_dict = appendix_amazon_merchant_price_data_instance.to_dict()
# create an instance of AppendixAmazonMerchantPriceData from a dict
appendix_amazon_merchant_price_data_form_dict = appendix_amazon_merchant_price_data.from_dict(appendix_amazon_merchant_price_data_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")