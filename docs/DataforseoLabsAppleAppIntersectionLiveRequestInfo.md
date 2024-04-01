# DataforseoLabsAppleAppIntersectionLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_ids** | **Dict[str, Optional[str]]** | ids of the target apps required field IDs of the target mobile applications on App Store; you can find the ID in the URL of every app listed on App Store; example: in the URL https://apps.apple.com/us/app/id835599320 the id is 835599320; the ids should be specified the following way: \&quot;app_ids\&quot;: { \&quot;1\&quot;: \&quot;686449807\&quot;, \&quot;2\&quot;: \&quot;382617920\&quot; } if you specify a single ID here, the API will return results only for one application; the maximum number of app IDs you can specify in this object is 20 | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US location only; example: United States | [optional] 
**location_code** | **int** | location code required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US location only; example: 2840 | [optional] 
**language_name** | **str** | full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the English language only; example: English | [optional] 
**language_code** | **str** | language code required field if you don’t specify language_name Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the English language only example: en | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in example: [\&quot;keyword_data.keyword_info.search_volume\&quot;,\&quot;&gt;\&quot;,500] [[\&quot;keyword_data.keyword_info.search_volume\&quot;,\&quot;&lt;&gt;\&quot;,500],\&quot;and\&quot;,[intersection_result.382617920.rank_group\&quot;,\&quot;&gt;&#x3D;\&quot;,\&quot;10\&quot;]] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results; possible sorting types: asc – results will be sorted in the ascending order; desc – results will be sorted in the descending order; you should use a comma to specify a sorting type; example: [\&quot;intersection_result.382617920.rank_absolute,asc\&quot;] Note: you can set no more than three sorting rules in a single request; you should use a comma to separate several sorting rules; example: [\&quot;intersection_result.382617920.rank_absolute,desc\&quot;,\&quot;keyword_data.keyword_info.search_volume,asc\&quot;] default rule: [\&quot;keyword_data.keyword_info.search_volume,desc\&quot;] Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array | [optional] 
**limit** | **int** | the maximum number of returned keywords optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned keywords optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_apple_app_intersection_live_request_info import DataforseoLabsAppleAppIntersectionLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAppleAppIntersectionLiveRequestInfo from a JSON string
dataforseo_labs_apple_app_intersection_live_request_info_instance = DataforseoLabsAppleAppIntersectionLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsAppleAppIntersectionLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_apple_app_intersection_live_request_info_dict = dataforseo_labs_apple_app_intersection_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsAppleAppIntersectionLiveRequestInfo from a dict
dataforseo_labs_apple_app_intersection_live_request_info_form_dict = dataforseo_labs_apple_app_intersection_live_request_info.from_dict(dataforseo_labs_apple_app_intersection_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


