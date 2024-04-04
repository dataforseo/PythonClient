# MerchantGoogleLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional] 
**language_code** | **str** | language code according to ISO 639-1 | [optional] 

## Example

```python
from dataforseo_client.models.merchant_google_languages_result_info import MerchantGoogleLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantGoogleLanguagesResultInfo from a JSON string
merchant_google_languages_result_info_instance = MerchantGoogleLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print MerchantGoogleLanguagesResultInfo.to_json()

# convert the object into a dict
merchant_google_languages_result_info_dict = merchant_google_languages_result_info_instance.to_dict()
# create an instance of MerchantGoogleLanguagesResultInfo from a dict
merchant_google_languages_result_info_form_dict = merchant_google_languages_result_info.from_dict(merchant_google_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


