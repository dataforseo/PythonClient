[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# KeywordsDataBingKeywordsForSiteLiveRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain or URL required field the domain name or URL of the target website | [optional]
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations example: London,England,United Kingdom | [optional]
**location_code** | **int** | search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations example: 2840 | [optional]
**location_coordinate** | **str** | GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude” format the data will be provided for the country the specified coordinates belong to example: 52.6178549,-155.352142 | [optional]
**language_name** | **str** | full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code supported languages: English, French, German | [optional]
**language_code** | **str** | search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name supported languages: en, fr, de | [optional]
**keywords_negative** | **List[str]** | keywords negative array optional field These keywords will be ignored in the results array; You can specify a maximum of 200 terms that you want to exclude from the results; the specified keywords will be converted to lowercase format | [optional]
**device** | **str** | device type optional field specify this field if you want to get the data for a particular device typepossible values: all, mobile, desktop, tablet default value: all | [optional]
**date_from** | **str** | starting date of the time range optional field if you don’t specify this field, data will be provided for the last 12 months date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2020-01-01\&quot; | [optional]
**date_to** | **str** | ending date of the time range optional field if you don’t specify this field, data will be provided for the last 12 months; minimum value: two years back from today’s date; maximum value: one month from today’s date; note: we do not recommend using a custom time range for the past year’s dates; date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2020-03-15\&quot; | [optional]
**sort_by** | **str** | results sorting parameters optional field Use these parameters to sort the results by search_volume, cpc, competition or relevance in the descending order default value: relevance | [optional]
**search_partners** | **bool** | Bing search partners type optional field if you specify true, the results will be delivered for owned, operated, and syndicated networks across Bing, Yahoo, AOL and partner sites that host Bing, AOL, and Yahoo search. default value: false – results are returned for Bing, AOL, and Yahoo search networks | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.keywords_data_bing_keywords_for_site_live_request_info import KeywordsDataBingKeywordsForSiteLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataBingKeywordsForSiteLiveRequestInfo from a JSON string
keywords_data_bing_keywords_for_site_live_request_info_instance = KeywordsDataBingKeywordsForSiteLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataBingKeywordsForSiteLiveRequestInfo.to_json()

# convert the object into a dict
keywords_data_bing_keywords_for_site_live_request_info_dict = keywords_data_bing_keywords_for_site_live_request_info_instance.to_dict()
# create an instance of KeywordsDataBingKeywordsForSiteLiveRequestInfo from a dict
keywords_data_bing_keywords_for_site_live_request_info_form_dict = keywords_data_bing_keywords_for_site_live_request_info.from_dict(keywords_data_bing_keywords_for_site_live_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")