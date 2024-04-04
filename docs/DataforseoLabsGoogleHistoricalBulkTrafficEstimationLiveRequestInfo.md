# DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | **List[str]** | target domains and subdomains required field you can specify domains and subdomains in this field; domains and subdomains should be specified without https:// and www.; you can set up to 1000 domains or subdomains | [optional] 
**location_name** | **str** | full name of the location if you use this field, you don’t have to specify location_code you can receive the list of available locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available locations example: United Kingdom | [optional] 
**location_code** | **int** | location code if you use this field, you don’t have to specify location_name you can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available locations example: 2840 | [optional] 
**language_name** | **str** | full name of the language if you use this field, you don’t need to specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: English | [optional] 
**language_code** | **str** | language code if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: en | [optional] 
**date_from** | **str** | starting date of the time range optional field if you don’t specify this field, the data will be provided for the previous 12 months minimal possible value: 2020-10-01 date format: \&quot;yyyy-mm-dd\&quot; | [optional] 
**date_to** | **str** | ending date of the time range optional field if you don’t specify this field, the today’s date will be used by default; date format: \&quot;yyyy-mm-dd\&quot; example: \&quot;2021-04-01\&quot; | [optional] 
**item_types** | **List[str]** | display results by item type optional field indicates the type of search results included in the response; Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array; possible values: [\&quot;organic\&quot;, \&quot;paid\&quot;, \&quot;featured_snippet\&quot;, \&quot;local_pack\&quot;] default value: [\&quot;organic\&quot;, \&quot;paid\&quot;] | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_historical_bulk_traffic_estimation_live_request_info import DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo from a JSON string
dataforseo_labs_google_historical_bulk_traffic_estimation_live_request_info_instance = DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_historical_bulk_traffic_estimation_live_request_info_dict = dataforseo_labs_google_historical_bulk_traffic_estimation_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo from a dict
dataforseo_labs_google_historical_bulk_traffic_estimation_live_request_info_form_dict = dataforseo_labs_google_historical_bulk_traffic_estimation_live_request_info.from_dict(dataforseo_labs_google_historical_bulk_traffic_estimation_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


