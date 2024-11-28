# KeywordsDataClickstreamDataBulkSearchVolumeLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | target keywords required field UTF-8 encoding maximum number of keywords you can specify in this array: 1000; each keyword should be at least 3 characters long; the keywords will be converted to lowercase format; Note: certain symbols and characters (e.g., UTF symbols, emojis) are not allowed to learn more about which symbols and characters can be used, please refer to this article learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages example: United Kingdom | [optional] 
**location_code** | **int** | location code required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages example: 2840 | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_clickstream_data_bulk_search_volume_live_request_info import KeywordsDataClickstreamDataBulkSearchVolumeLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataClickstreamDataBulkSearchVolumeLiveRequestInfo from a JSON string
keywords_data_clickstream_data_bulk_search_volume_live_request_info_instance = KeywordsDataClickstreamDataBulkSearchVolumeLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataClickstreamDataBulkSearchVolumeLiveRequestInfo.to_json())

# convert the object into a dict
keywords_data_clickstream_data_bulk_search_volume_live_request_info_dict = keywords_data_clickstream_data_bulk_search_volume_live_request_info_instance.to_dict()
# create an instance of KeywordsDataClickstreamDataBulkSearchVolumeLiveRequestInfo from a dict
keywords_data_clickstream_data_bulk_search_volume_live_request_info_from_dict = KeywordsDataClickstreamDataBulkSearchVolumeLiveRequestInfo.from_dict(keywords_data_clickstream_data_bulk_search_volume_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


