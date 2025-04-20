# DataforseoLabsGoogleSearchIntentLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | target keywords required field UTF-8 encoding maximum number of keywords you can specify in this array: 1000; the keywords will be converted to lowercase format learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**language_name** | **str** | full name of the language required field if don’t specify language_code you can receive the list of available languages with their language_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages  Note: this endpoint currently supports the following languages only: Arabic, ar, Chinese(Traditional), zh-TW, Czech, cs, Danish, da, Dutch, nl, English, en, Finnish, fi, French, fr, German, de, Hebrew, he, Hindi, hi, Italian, it, Japanese, ja, Korean, ko, Malay, ms, Norwegian(Bokmål), nb, Polish, pl, Portuguese, pt, Romanian, ro, Russian, ru, Spanish, es, Swedish, sv, Thai, th, Ukrainian, uk, Vietnamese, vi, Bulgarian, bg, Croatian, hr, Serbian, sr, Slovenian, sl, Bosnian, bs example: English | [optional] 
**language_code** | **str** | language code required field if don’t specify language_name you can receive the list of available languages with their language_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages Note: this endpoint currently supports these languages only; example: en | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_search_intent_live_request_info import DataforseoLabsGoogleSearchIntentLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleSearchIntentLiveRequestInfo from a JSON string
dataforseo_labs_google_search_intent_live_request_info_instance = DataforseoLabsGoogleSearchIntentLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleSearchIntentLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_search_intent_live_request_info_dict = dataforseo_labs_google_search_intent_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleSearchIntentLiveRequestInfo from a dict
dataforseo_labs_google_search_intent_live_request_info_from_dict = DataforseoLabsGoogleSearchIntentLiveRequestInfo.from_dict(dataforseo_labs_google_search_intent_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


