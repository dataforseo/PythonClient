# AppDataGoogleLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional] 
**language_code** | **str** | language code according to ISO 639-1 | [optional] 

## Example

```python
from dataforseo_client.models.app_data_google_languages_result_info import AppDataGoogleLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataGoogleLanguagesResultInfo from a JSON string
app_data_google_languages_result_info_instance = AppDataGoogleLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print(AppDataGoogleLanguagesResultInfo.to_json())

# convert the object into a dict
app_data_google_languages_result_info_dict = app_data_google_languages_result_info_instance.to_dict()
# create an instance of AppDataGoogleLanguagesResultInfo from a dict
app_data_google_languages_result_info_from_dict = AppDataGoogleLanguagesResultInfo.from_dict(app_data_google_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


