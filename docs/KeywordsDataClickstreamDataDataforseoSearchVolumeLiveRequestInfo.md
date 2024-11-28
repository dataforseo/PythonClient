# KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | target keywords required field UTF-8 encoding maximum number of keywords you can specify in this array: 1000 the keywords will be converted to lowercase format Note: certain symbols and characters (e.g., UTF symbols, emojis) are not allowed to learn more about which symbols and characters can be used, please refer to this article learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **str** | full name of search engine location required field if you don’t specify location_code  you can receive the list of available locations with location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages example: London,England,United Kingdom | [optional] 
**location_code** | **int** | search engine location code required field if you don’t specify location_name if you use this field, you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages example: 2840 | [optional] 
**language_name** | **str** | full name of search engine language required field if don’t specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages example: English | [optional] 
**language_code** | **str** | search engine language code required field if don’t specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages example: en | [optional] 
**use_clickstream** | **bool** | use clickstream data to provide results optional field if set to true, you will get DataForSEO search volume values based on clickstream data; if set to false, Bing search volume data will be used to calculate DataForSEO search volume; default value: true; Note: some locations may not be available for calculating Bing search volume, in this case search volume will be calculated based on clickstream data even if you set this parameter to false | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_clickstream_data_dataforseo_search_volume_live_request_info import KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo from a JSON string
keywords_data_clickstream_data_dataforseo_search_volume_live_request_info_instance = KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo.to_json())

# convert the object into a dict
keywords_data_clickstream_data_dataforseo_search_volume_live_request_info_dict = keywords_data_clickstream_data_dataforseo_search_volume_live_request_info_instance.to_dict()
# create an instance of KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo from a dict
keywords_data_clickstream_data_dataforseo_search_volume_live_request_info_from_dict = KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo.from_dict(keywords_data_clickstream_data_dataforseo_search_volume_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


