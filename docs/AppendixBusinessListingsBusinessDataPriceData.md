[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppendixBusinessListingsBusinessDataPriceData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**categories_aggregation** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]
**locations** | [**AppendixTaskKeywordsDataPriceDataInfo**](AppendixTaskKeywordsDataPriceDataInfo.md) |  | [optional]
**search** | [**AppendixKeywordBingKeywordsDataPriceDataInfo**](AppendixKeywordBingKeywordsDataPriceDataInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.appendix_business_listings_business_data_price_data import AppendixBusinessListingsBusinessDataPriceData

# TODO update the JSON string below
json = "{}"
# create an instance of AppendixBusinessListingsBusinessDataPriceData from a JSON string
appendix_business_listings_business_data_price_data_instance = AppendixBusinessListingsBusinessDataPriceData.from_json(json)
# print the JSON string representation of the object
print AppendixBusinessListingsBusinessDataPriceData.to_json()

# convert the object into a dict
appendix_business_listings_business_data_price_data_dict = appendix_business_listings_business_data_price_data_instance.to_dict()
# create an instance of AppendixBusinessListingsBusinessDataPriceData from a dict
appendix_business_listings_business_data_price_data_form_dict = appendix_business_listings_business_data_price_data.from_dict(appendix_business_listings_business_data_price_data_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")