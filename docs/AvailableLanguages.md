# AvailableLanguages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_sources** | **List[Optional[str]]** | supported sources contains the sources of data supported for a specific location and language combination only google and bing are currently available | [optional] 
**language_name** | **str** | language name | [optional] 
**language_code** | **str** | language code according to ISO 639-1 | [optional] 
**keywords** | **int** | the number of keywords available for the given location and language | [optional] 
**serps** | **int** | the number of SERP pages available for the given location and language | [optional] 

## Example

```python
from dataforseo_client.models.available_languages import AvailableLanguages

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableLanguages from a JSON string
available_languages_instance = AvailableLanguages.from_json(json)
# print the JSON string representation of the object
print(AvailableLanguages.to_json())

# convert the object into a dict
available_languages_dict = available_languages_instance.to_dict()
# create an instance of AvailableLanguages from a dict
available_languages_from_dict = AvailableLanguages.from_dict(available_languages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


