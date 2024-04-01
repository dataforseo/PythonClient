# KeywordsDataDataforseoTrendsMergedDataLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[str]** | keywords required field the maximum number of keywords you can specify: 5 avoid symbols and special characters (e.g., UTF symbols, emojis); specifying non-Latin characters, you’ll get data for the countries where they are used | [optional] 
**location_name** | **str** | full name of search engine location optional field if you don’t use this field, you will recieve global results if you use this field, you don’t need to specify location_code you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations note that the data will be provided for the country the specified location_name belongs to; example: United Kingdom | [optional] 
**location_code** | **int** | search engine location code optional field if you don’t use this field, you will recieve global results if you use this field, you don’t need to specify location_name you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations note that the data will be provided for the country the specified location_code belongs to; example: 2840 | [optional] 
**type** | **str** | type of element | [optional] 
**date_from** | **str** | starting date of the time range optional field if you don’t specify this field, the current day and month of the preceding year will be used by default minimal value for the web type: 2004-01-01 minimal value for other types: 2008-01-01 date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**date_to** | **str** | ending date of the time range optional field if you don’t specify this field, the today’s date will be used by default date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2019-01-15\&quot; | [optional] 
**time_range** | **str** | preset time ranges optional field if you specify date_from or date_to parameters, this field will be ignored when setting a task possible values for all type parameters: past_4_hours, past_day, past_7_days, past_30_days, past_90_days, past_12_months, past_5_years | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.keywords_data_dataforseo_trends_merged_data_live_request_info import KeywordsDataDataforseoTrendsMergedDataLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataDataforseoTrendsMergedDataLiveRequestInfo from a JSON string
keywords_data_dataforseo_trends_merged_data_live_request_info_instance = KeywordsDataDataforseoTrendsMergedDataLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordsDataDataforseoTrendsMergedDataLiveRequestInfo.to_json())

# convert the object into a dict
keywords_data_dataforseo_trends_merged_data_live_request_info_dict = keywords_data_dataforseo_trends_merged_data_live_request_info_instance.to_dict()
# create an instance of KeywordsDataDataforseoTrendsMergedDataLiveRequestInfo from a dict
keywords_data_dataforseo_trends_merged_data_live_request_info_form_dict = keywords_data_dataforseo_trends_merged_data_live_request_info.from_dict(keywords_data_dataforseo_trends_merged_data_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


