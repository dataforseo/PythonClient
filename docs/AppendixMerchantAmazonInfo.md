[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixMerchantAmazonInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional]
**products** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional]
**sellers** | [**AppendixSerpLimitsRatesDataInfo**](AppendixSerpLimitsRatesDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_merchant_amazon_info import AppendixMerchantAmazonInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixMerchantAmazonInfo from a JSON string
appendix_merchant_amazon_info_instance = AppendixMerchantAmazonInfo.from_json(json)
# print the JSON string representation of the object
print AppendixMerchantAmazonInfo.to_json()

# convert the object into a dict
appendix_merchant_amazon_info_dict = appendix_merchant_amazon_info_instance.to_dict()
# create an instance of AppendixMerchantAmazonInfo from a dict
appendix_merchant_amazon_info_form_dict = appendix_merchant_amazon_info.from_dict(appendix_merchant_amazon_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")