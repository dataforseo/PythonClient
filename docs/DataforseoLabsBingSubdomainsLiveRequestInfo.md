# DataforseoLabsBingSubdomainsLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain required field the domain name of the target website the domain should be specified without https:// and www. | [optional] 
**location_name** | **str** | full name of the location optional field if you use this field, you don’t need to specify location_code you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available locations; Note: this endpoint currently supports the US location only; example: United States | [optional] 
**location_code** | **int** | location code optional field if you use this field, you don’t need to specify location_name you can receive the list of available locations with their location_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; ignore this field to get the results for all available locations; Note: this endpoint currently supports the US location only; example: 2840 | [optional] 
**language_name** | **str** | full name of the language optional field if you use this field, you don’t need to specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: English | [optional] 
**language_code** | **str** | language code optional field if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: en | [optional] 
**item_types** | **List[str]** | display results by item type optional field indicates the type of search results included in the response Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array; you will not be able to sort and filter results by the types of search results not included in the response; possible values: [\&quot;organic\&quot;, \&quot;paid\&quot;, \&quot;featured_snippet\&quot;, \&quot;local_pack\&quot;] default value: [\&quot;organic\&quot;, \&quot;paid\&quot;, \&quot;featured_snippet\&quot;, \&quot;local_pack\&quot;] | [optional] 
**historical_serp_mode** | **str** | data collection mode optional field you can use this field to filter the results; possible types of filtering: live — return metrics for SERPs in which the specified target currently has ranking results; lost — return metrics for SERPs in which the specified target had previously had ranking results, but didn’t have them during the last check; all — return metrics for both types of SERPs. default value: live | [optional] 
**ignore_synonyms** | **bool** | ignore highly similar keywords optional field if set to true, only core keywords will be returned, all highly similar keywords will be excluded; default value: false | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in example: [\&quot;metrics.paid.count\&quot;,\&quot;&gt;\&quot;,0] [[\&quot;metrics.paid.count\&quot;,\&quot;&gt;\&quot;,0],\&quot;and\&quot;,[\&quot;metrics.paid.etv\&quot;,\&quot;&gt;\&quot;,\&quot;50\&quot;]] [[\&quot;metrics.organic.count\&quot;,\&quot;&gt;\&quot;,\&quot;10\&quot;], \&quot;and\&quot;, [[\&quot;metrics.organic.pos_1\&quot;,\&quot;&lt;&gt;\&quot;,0],\&quot;or\&quot;,[\&quot;metrics.organic.pos_2_3\&quot;,\&quot;&lt;&gt;\&quot;,0]]] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to specify a sorting type example: [\&quot;metrics.paid.etv,asc\&quot;] Note: you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;metrics.organic.etv,desc\&quot;,\&quot;metrics.paid.count,asc\&quot;] default rule: [\&quot;metrics.organic.count,desc\&quot;] Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array | [optional] 
**limit** | **int** | the maximum number of returned keywords optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned keywords optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_bing_subdomains_live_request_info import DataforseoLabsBingSubdomainsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBingSubdomainsLiveRequestInfo from a JSON string
dataforseo_labs_bing_subdomains_live_request_info_instance = DataforseoLabsBingSubdomainsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsBingSubdomainsLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_bing_subdomains_live_request_info_dict = dataforseo_labs_bing_subdomains_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsBingSubdomainsLiveRequestInfo from a dict
dataforseo_labs_bing_subdomains_live_request_info_from_dict = DataforseoLabsBingSubdomainsLiveRequestInfo.from_dict(dataforseo_labs_bing_subdomains_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


