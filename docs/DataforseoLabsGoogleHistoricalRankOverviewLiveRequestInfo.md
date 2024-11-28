# DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain required field the domain name of the target website the domain should be specified without https:// and www. | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: United Kingdom | [optional] 
**location_code** | **int** | location code required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: 2840 | [optional] 
**language_name** | **str** | full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code you can receive the list of available locations with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English | [optional] 
**language_code** | **str** | language code required field if you don’t specify language_name Note: it is required to specify either language_name or language_code you can receive the list of available locations with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en | [optional] 
**date_from** | **str** | starting date of the time range optional field if you don’t specify this field, the data will be provided for the previous 6 months minimal possible value: 2020-10-01 date format: \&quot;yyyy-mm-dd\&quot; | [optional] 
**date_to** | **str** | ending date of the time range optional field if you don’t specify this field, the today’s date will be used by default date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2021-04-01\&quot; | [optional] 
**correlate** | **bool** | correlate data with previously obtained datasets optional field default value: true if you use this parameter, our system will correlate data you obtain now with previously obtained datasets this parameter is intended to mitigate any inconsistencies that may result from changes to our database we recommend always setting correlate to true | [optional] 
**ignore_synonyms** | **bool** | ignore highly similar keywords optional field if set to true, only data based on core keywords will be returned, data for all highly similar keywords will be excluded; default value: false | [optional] 
**include_clickstream_data** | **bool** | include or exclude data from clickstream-based metrics in the result optional field if the parameter is set to true, you will receive clickstream_etv, clickstream_gender_distribution, and clickstream_age_distribution fields with clickstream data in the response; default value: false; Note: historical clickstream data is available from 2024/05 (May, 2024); with this parameter enabled, you will be charged double the price for the request; learn more about how clickstream-based metrics are calculated in this help center article | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_historical_rank_overview_live_request_info import DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo from a JSON string
dataforseo_labs_google_historical_rank_overview_live_request_info_instance = DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_google_historical_rank_overview_live_request_info_dict = dataforseo_labs_google_historical_rank_overview_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo from a dict
dataforseo_labs_google_historical_rank_overview_live_request_info_from_dict = DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo.from_dict(dataforseo_labs_google_historical_rank_overview_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


