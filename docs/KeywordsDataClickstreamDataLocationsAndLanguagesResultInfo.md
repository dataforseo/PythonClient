# KeywordsDataClickstreamDataLocationsAndLanguagesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_code** | **int** | location code | [optional] 
**location_name** | **str** | full name of the location | [optional] 
**location_code_parent** | **int** | the code of the superordinate location the value will be null as Country is the only supported location_type for this API | [optional] 
**country_iso_code** | **str** | ISO country code of the location | [optional] 
**location_type** | **str** | location type possible values: Country | [optional] 
**available_languages** | [**List[AvailableLanguages]**](AvailableLanguages.md) | supported languages contains the languages which are supported for a specific location | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_clickstream_data_locations_and_languages_result_info import KeywordsDataClickstreamDataLocationsAndLanguagesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataClickstreamDataLocationsAndLanguagesResultInfo from a JSON string
keywords_data_clickstream_data_locations_and_languages_result_info_instance = KeywordsDataClickstreamDataLocationsAndLanguagesResultInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataClickstreamDataLocationsAndLanguagesResultInfo.to_json()

# convert the object into a dict
keywords_data_clickstream_data_locations_and_languages_result_info_dict = keywords_data_clickstream_data_locations_and_languages_result_info_instance.to_dict()
# create an instance of KeywordsDataClickstreamDataLocationsAndLanguagesResultInfo from a dict
keywords_data_clickstream_data_locations_and_languages_result_info_form_dict = keywords_data_clickstream_data_locations_and_languages_result_info.from_dict(keywords_data_clickstream_data_locations_and_languages_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


