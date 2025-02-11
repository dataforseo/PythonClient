# DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asins** | **Dict[str, Optional[str]]** | asins of target products required field product IDs of the products for which you need to find keyword intersections; specify the ASINs as in the following example: \&quot;asins\&quot;: { \&quot;1\&quot;: \&quot;019005476X\&quot;, \&quot;2\&quot;: \&quot;0190074442\&quot; } the maximum number of ASINs you can specify in this object is 20; learn more about the parameter on this help center page | [optional] 
**location_name** | **str** | full name of the location required field if don’t specify location_code you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only; example: United Kingdom | [optional] 
**location_code** | **int** | location code required field if don’t specify location_name you can receive the list of available locations with their location_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only; example: 2840 | [optional] 
**language_name** | **str** | full name of the language required field if don’t specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English | [optional] 
**language_code** | **str** | language code required field if don’t specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en | [optional] 
**limit** | **int** | the maximum number of products in the results array optional field default value: 100; maximum value: 1000 | [optional] 
**intersection_mode** | **str** | mode for finding asin intersections optional field possible values: union, intersect; default value: intersect; learn more about the parameter in this help center guide | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, ilike, not_ilike, like, not_like, match, not_match you can use the % operator with like and not_like, as well as ilike and not_ilike to match any string of zero or more characters example: [\&quot;avg_position\&quot;,\&quot;&lt;\&quot;, 10] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting parameter example: [\&quot;sum_position,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;intersections,desc\&quot;,\&quot;avg_position,asc\&quot;] default rule: [\&quot;intersections,desc\&quot;] | [optional] 
**offset** | **int** | offset in the results array of returned keywords optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_amazon_product_keyword_intersections_live_request_info import DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo from a JSON string
dataforseo_labs_amazon_product_keyword_intersections_live_request_info_instance = DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_amazon_product_keyword_intersections_live_request_info_dict = dataforseo_labs_amazon_product_keyword_intersections_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo from a dict
dataforseo_labs_amazon_product_keyword_intersections_live_request_info_from_dict = DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo.from_dict(dataforseo_labs_amazon_product_keyword_intersections_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


