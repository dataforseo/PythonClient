# DataforseoLabsGoogleHistoricalSearchVolumeLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | keywords required field The maximum number of keywords you can specify: 700 The maximum number of characters for each keyword: 80 The maximum number of words for each keyword phrase: 10 the specified keywords will be converted to lowercase format, data will be provided in a separate array note that if some of the keywords specified in this array are omitted in the results you receive, then our database doesn’t contain such keywords and cannot return data on them you will not be charged for the keywords omitted in the results learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: United Kingdom | [optional] 
**location_code** | **int** | location code required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: 2840 | [optional] 
**language_name** | **str** | full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code you can receive the list of available locations with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English | [optional] 
**language_code** | **str** | language code required field if you don’t specify language_name Note: it is required to specify either language_name or language_code you can receive the list of available locations with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en | [optional] 
**include_serp_info** | **bool** | include data from SERP for each keyword optional field if set to true, we will return a serp_info array containing SERP data (number of search results, relevant URL, and SERP features) for every keyword in the response default value: false | [optional] 
**include_clickstream_data** | **bool** | include or exclude data from clickstream-based metrics in the result optional field if the parameter is set to true, you will receive clickstream_keyword_info, keyword_info_normalized_with_clickstream, and keyword_info_normalized_with_bing fields in the response default value: false with this parameter enabled, you will be charged double the price for the request learn more about how clickstream-based metrics are calculated in this help center article | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_historical_search_volume_live_request_info import DataforseoLabsGoogleHistoricalSearchVolumeLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleHistoricalSearchVolumeLiveRequestInfo from a JSON string
dataforseo_labs_google_historical_search_volume_live_request_info_instance = DataforseoLabsGoogleHistoricalSearchVolumeLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleHistoricalSearchVolumeLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_historical_search_volume_live_request_info_dict = dataforseo_labs_google_historical_search_volume_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleHistoricalSearchVolumeLiveRequestInfo from a dict
dataforseo_labs_google_historical_search_volume_live_request_info_from_dict = DataforseoLabsGoogleHistoricalSearchVolumeLiveRequestInfo.from_dict(dataforseo_labs_google_historical_search_volume_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


