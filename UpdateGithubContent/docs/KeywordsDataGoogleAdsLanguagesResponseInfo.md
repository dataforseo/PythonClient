# KeywordsDataGoogleAdsLanguagesResponseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | the current version of the API | [optional] 
**status_code** | **int** | general status code you can find the full list of the response codes here | [optional] 
**status_message** | **str** | general informational message you can find the full list of general informational messages here | [optional] 
**time** | **str** | total execution time, seconds | [optional] 
**cost** | **float** | total tasks cost, USD | [optional] 
**tasks_count** | **int** | the number of tasks in the tasks array | [optional] 
**tasks_error** | **int** | the number of tasks in the tasks array returned with an error | [optional] 
**tasks** | [**List[KeywordsDataGoogleAdsLanguagesTaskInfo]**](KeywordsDataGoogleAdsLanguagesTaskInfo.md) | array of tasks | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_google_ads_languages_response_info import KeywordsDataGoogleAdsLanguagesResponseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataGoogleAdsLanguagesResponseInfo from a JSON string
keywords_data_google_ads_languages_response_info_instance = KeywordsDataGoogleAdsLanguagesResponseInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataGoogleAdsLanguagesResponseInfo.to_json()

# convert the object into a dict
keywords_data_google_ads_languages_response_info_dict = keywords_data_google_ads_languages_response_info_instance.to_dict()
# create an instance of KeywordsDataGoogleAdsLanguagesResponseInfo from a dict
keywords_data_google_ads_languages_response_info_form_dict = keywords_data_google_ads_languages_response_info.from_dict(keywords_data_google_ads_languages_response_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

