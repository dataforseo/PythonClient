# DataforseoLabsBingDomainRankOverviewLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain required field the domain name of the target website the domain should be specified without https:// and www. | [optional] 
**location_name** | **str** | full name of the location optional field if you use this field, you don’t need to specify location_code you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; ignore this field to get the results for all available locations; Note: this endpoint currently supports the US location only; example: United States | [optional] 
**location_code** | **int** | location code optional field if you use this field, you don’t need to specify location_name you can receive the list of available locations with their location_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available locations; Note: this endpoint currently supports the US location only; example: 2840 | [optional] 
**language_name** | **str** | full name of the language optional field if you use this field, you don’t need to specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: English | [optional] 
**language_code** | **str** | language code optional field if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: en | [optional] 
**limit** | **int** | the maximum number of returned results for domain optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned items optional field default value: 0 if you specify the 10 value, the first ten items in the results array will be omitted and the data will be provided for the successive items | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_bing_domain_rank_overview_live_request_info import DataforseoLabsBingDomainRankOverviewLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBingDomainRankOverviewLiveRequestInfo from a JSON string
dataforseo_labs_bing_domain_rank_overview_live_request_info_instance = DataforseoLabsBingDomainRankOverviewLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsBingDomainRankOverviewLiveRequestInfo.to_json()

# convert the object into a dict
dataforseo_labs_bing_domain_rank_overview_live_request_info_dict = dataforseo_labs_bing_domain_rank_overview_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsBingDomainRankOverviewLiveRequestInfo from a dict
dataforseo_labs_bing_domain_rank_overview_live_request_info_form_dict = dataforseo_labs_bing_domain_rank_overview_live_request_info.from_dict(dataforseo_labs_bing_domain_rank_overview_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


