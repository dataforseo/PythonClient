# DataforseoLabsGoogleCategoriesForKeywordsLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | target keywords required field UTF-8 encoding maximum number of keywords you can specify in this array: 1000 each keyword should be at least 3 characters long; the keywords will be converted to lowercase format | [optional] 
**language_name** | **str** | full name of the language required field if don’t specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/google/categories_for_keywords/languages example: English | [optional] 
**language_code** | **str** | language code required field if don’t specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/google/categories_for_keywords/languages example: en | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_categories_for_keywords_live_request_info import DataforseoLabsGoogleCategoriesForKeywordsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleCategoriesForKeywordsLiveRequestInfo from a JSON string
dataforseo_labs_google_categories_for_keywords_live_request_info_instance = DataforseoLabsGoogleCategoriesForKeywordsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleCategoriesForKeywordsLiveRequestInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_categories_for_keywords_live_request_info_dict = dataforseo_labs_google_categories_for_keywords_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleCategoriesForKeywordsLiveRequestInfo from a dict
dataforseo_labs_google_categories_for_keywords_live_request_info_form_dict = dataforseo_labs_google_categories_for_keywords_live_request_info.from_dict(dataforseo_labs_google_categories_for_keywords_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


