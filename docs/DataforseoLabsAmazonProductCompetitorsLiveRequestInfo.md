# DataforseoLabsAmazonProductCompetitorsLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asin** | **str** | product ID required field unique product identifier (ASIN) on Amazon; you can receive the asin parameter by making a separate request to the Amazon Products endpoint | [optional] 
**location_name** | **str** | full name of the location required field if don’t specify location_code you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only; example: United States | [optional] 
**location_code** | **int** | location code required field if don’t specify location_name you can receive the list of available locations with their location_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only; example: 2840 | [optional] 
**language_name** | **str** | full name of the language required field if don’t specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English | [optional] 
**language_code** | **str** | language code required field if don’t specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en | [optional] 
**limit** | **int** | the maximum number of products in the results array optional field default value: 100; maximum value: 1000 | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;full_metrics.amazon_serp.pos_1\&quot;,\&quot;&gt;\&quot;, 20] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting parameter example: [\&quot;full_metrics.amazon_serp.pos_1,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;full_metrics.amazon_serp.pos_1,desc\&quot;,\&quot;avg_position,desc\&quot;] default rule: [\&quot;ranked_serp_element.serp_item.rank_group,asc\&quot;] | [optional] 
**offset** | **int** | offset in the results array of returned product competitors optional field default value: 0 if you specify the 10 value, the first ten product competitors in the results array will be omitted and the data will be provided for the successive product competitors | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_amazon_product_competitors_live_request_info import DataforseoLabsAmazonProductCompetitorsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsAmazonProductCompetitorsLiveRequestInfo from a JSON string
dataforseo_labs_amazon_product_competitors_live_request_info_instance = DataforseoLabsAmazonProductCompetitorsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsAmazonProductCompetitorsLiveRequestInfo.to_json()

# convert the object into a dict
dataforseo_labs_amazon_product_competitors_live_request_info_dict = dataforseo_labs_amazon_product_competitors_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsAmazonProductCompetitorsLiveRequestInfo from a dict
dataforseo_labs_amazon_product_competitors_live_request_info_form_dict = dataforseo_labs_amazon_product_competitors_live_request_info.from_dict(dataforseo_labs_amazon_product_competitors_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


