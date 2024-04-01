# SerpYoutubeLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional] 
**language_code** | **str** | language code according to ISO 639-1 | [optional] 

## Example

```python
from dataforseo_client.models.serp_youtube_languages_result_info import SerpYoutubeLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SerpYoutubeLanguagesResultInfo from a JSON string
serp_youtube_languages_result_info_instance = SerpYoutubeLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print(SerpYoutubeLanguagesResultInfo.to_json())

# convert the object into a dict
serp_youtube_languages_result_info_dict = serp_youtube_languages_result_info_instance.to_dict()
# create an instance of SerpYoutubeLanguagesResultInfo from a dict
serp_youtube_languages_result_info_form_dict = serp_youtube_languages_result_info.from_dict(serp_youtube_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


