# AppDataAppleLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional] 
**language_code** | **str** | language code according to ISO 639-1 | [optional] 

## Example

```python
from dataforseo_client.models.app_data_apple_languages_result_info import AppDataAppleLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataAppleLanguagesResultInfo from a JSON string
app_data_apple_languages_result_info_instance = AppDataAppleLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print(AppDataAppleLanguagesResultInfo.to_json())

# convert the object into a dict
app_data_apple_languages_result_info_dict = app_data_apple_languages_result_info_instance.to_dict()
# create an instance of AppDataAppleLanguagesResultInfo from a dict
app_data_apple_languages_result_info_from_dict = AppDataAppleLanguagesResultInfo.from_dict(app_data_apple_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


