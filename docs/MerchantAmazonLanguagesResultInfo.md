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
print(MerchantAmazonLanguagesResultInfo.to_json())

# convert the object into a dict
merchant_amazon_languages_result_info_dict = merchant_amazon_languages_result_info_instance.to_dict()
# create an instance of MerchantAmazonLanguagesResultInfo from a dict
merchant_amazon_languages_result_info_from_dict = MerchantAmazonLanguagesResultInfo.from_dict(merchant_amazon_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


