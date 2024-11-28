# KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language_name** | **str** | language name | [optional] 
**language_code** | **str** | language code according to ISO 639-1 | [optional] 
**available_locations** | [**List[AvailableLocations]**](AvailableLocations.md) | array of available locations for a certain language | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_bing_search_volume_history_locations_and_languages_result_info import KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResultInfo from a JSON string
keywords_data_bing_search_volume_history_locations_and_languages_result_info_instance = KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResultInfo.to_json())

# convert the object into a dict
keywords_data_bing_search_volume_history_locations_and_languages_result_info_dict = keywords_data_bing_search_volume_history_locations_and_languages_result_info_instance.to_dict()
# create an instance of KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResultInfo from a dict
keywords_data_bing_search_volume_history_locations_and_languages_result_info_from_dict = KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResultInfo.from_dict(keywords_data_bing_search_volume_history_locations_and_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


