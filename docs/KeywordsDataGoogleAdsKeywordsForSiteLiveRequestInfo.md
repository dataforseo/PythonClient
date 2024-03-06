[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain or page required field the domain name of the target website or the url of the target page; note: to obtain keywords for the target website, use the target_type parameter | [optional]
**target_type** | **str** | search keywords for site or for url optional field possible values: site, page; default value: page; if set to site, keywords will be provided for the entire site; if set to page, keywords will be provided for the specified webpage | [optional]
**location_name** | **str** | full name of search engine location optional field if you do not indicate the location, you will receive worldwide results, i.e., for all available locations; if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/locations example: London,England,United Kingdom | [optional]
**location_code** | **int** | search engine location code optional field if you do not indicate the location, you will receive worldwide results, i.e., for all available locations; if you use this field, you don’t need to specify location_name or location_coordinate; you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/locations example: 2840 | [optional]
**location_coordinate** | **str** | GPS coordinates of a location optional field if you do not indicate the location, you will receive worldwide results, i.e., for all available locations; if you use this field, you don’t need to specify location_name or location_code; location_coordinate parameter should be specified in the “latitude,longitude” format; the data will be provided for the country the specified coordinates belong to; example: 52.6178549,-155.352142 | [optional]
**language_name** | **str** | full name of search engine language optional field you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/languages example: English | [optional]
**language_code** | **str** | search engine language code optional field you can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/languages example: en | [optional]
**search_partners** | **bool** | include Google search partners optional field if you specify true, the results will be delivered for owned, operated, and syndicated networks across Google and partner sites that host Google search; default value: false – results are returned for Google search sites | [optional]
**date_from** | **str** | starting date of the time range optional field date format: \&quot;yyyy-mm-dd\&quot; minimal value: 4 years from the current date by default, data is returned for the past 12 months; Note: the indicated date cannot be greater than that specified in date_to and/or yesterday’s date;if Status endpoint returns false in the actual_data field, date_from can be set to the month before last and prior; if Status endpoint returns true in the actual_data field, date_from can be set to the last month and prior | [optional]
**date_to** | **str** | ending date of the time range optional field Note: the indicated date cannot be greater than yesterday’s date; if you don’t specify this field, yesterday’s date will be used by default date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2022-11-30\&quot; | [optional]
**include_adult_keywords** | **bool** | include keywords associated with adult content optional field if set to true, adult keywords will be included in the response default value: false note that the API may return no data for such keywords due to Google Ads restrictions | [optional]
**sort_by** | **str** | results sorting parameters optional field Use these parameters to sort the results by relevance, search_volume, competition_index, low_top_of_page_bid, or high_top_of_page_bid in descending order default value: relevance | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.keywords_data_google_ads_keywords_for_site_live_request_info import KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo from a JSON string
keywords_data_google_ads_keywords_for_site_live_request_info_instance = KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo.to_json()

# convert the object into a dict
keywords_data_google_ads_keywords_for_site_live_request_info_dict = keywords_data_google_ads_keywords_for_site_live_request_info_instance.to_dict()
# create an instance of KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo from a dict
keywords_data_google_ads_keywords_for_site_live_request_info_form_dict = keywords_data_google_ads_keywords_for_site_live_request_info.from_dict(keywords_data_google_ads_keywords_for_site_live_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")