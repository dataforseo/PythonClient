[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixSellersGoogleMerchantPriceData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ad_url** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**task_get** | [**AppendixTaskGetProductGoogleMerchantPriceDataInfo**](AppendixTaskGetProductGoogleMerchantPriceDataInfo.md) |  | [optional]
**task_post** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**tasks_ready** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_sellers_google_merchant_price_data import AppendixSellersGoogleMerchantPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixSellersGoogleMerchantPriceData from a JSON string
appendix_sellers_google_merchant_price_data_instance = AppendixSellersGoogleMerchantPriceData.from_json(json)
# print the JSON string representation of the object
print AppendixSellersGoogleMerchantPriceData.to_json()

# convert the object into a dict
appendix_sellers_google_merchant_price_data_dict = appendix_sellers_google_merchant_price_data_instance.to_dict()
# create an instance of AppendixSellersGoogleMerchantPriceData from a dict
appendix_sellers_google_merchant_price_data_form_dict = appendix_sellers_google_merchant_price_data.from_dict(appendix_sellers_google_merchant_price_data_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")