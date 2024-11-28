# OnPageLighthouseLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional] 
**language_code** | **str** | language code according to ISO 639-1 | [optional] 

## Example

```python
from dataforseo_client.models.on_page_lighthouse_languages_result_info import OnPageLighthouseLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OnPageLighthouseLanguagesResultInfo from a JSON string
on_page_lighthouse_languages_result_info_instance = OnPageLighthouseLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print(OnPageLighthouseLanguagesResultInfo.to_json())

# convert the object into a dict
on_page_lighthouse_languages_result_info_dict = on_page_lighthouse_languages_result_info_instance.to_dict()
# create an instance of OnPageLighthouseLanguagesResultInfo from a dict
on_page_lighthouse_languages_result_info_from_dict = OnPageLighthouseLanguagesResultInfo.from_dict(on_page_lighthouse_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


