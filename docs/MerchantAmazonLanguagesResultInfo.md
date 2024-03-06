[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# MerchantAmazonLanguagesResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional]
**language_code** | **str** | language code according to ISO 639-1 | [optional]

## Example

```python
from dataforseo_client.models.merchant_amazon_languages_result_info import MerchantAmazonLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAmazonLanguagesResultInfo from a JSON string
merchant_amazon_languages_result_info_instance = MerchantAmazonLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print MerchantAmazonLanguagesResultInfo.to_json()

# convert the object into a dict
merchant_amazon_languages_result_info_dict = merchant_amazon_languages_result_info_instance.to_dict()
# create an instance of MerchantAmazonLanguagesResultInfo from a dict
merchant_amazon_languages_result_info_form_dict = merchant_amazon_languages_result_info.from_dict(merchant_amazon_languages_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")