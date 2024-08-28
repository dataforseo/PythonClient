# DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain required field the domain name of the target website the domain should be specified without https:// and www. | [optional] 
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: United Kingdom | [optional] 
**location_code** | **int** | location code required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: 2840 | [optional] 
**language_name** | **str** | full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English | [optional] 
**language_code** | **str** | language code required field if you don’t specify language_name Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en | [optional] 
**item_types** | **List[str]** | display results by item type optional field indicates the type of search results included in the response Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array; you will not be able to sort and filter results by the types of search results not included in the response; possible values: [\&quot;organic\&quot;, \&quot;paid\&quot;, \&quot;featured_snippet\&quot;, \&quot;local_pack\&quot;] default value: [\&quot;organic\&quot;, \&quot;paid\&quot;] | [optional] 
**include_clickstream_data** | **bool** | include or exclude data from clickstream-based metrics in the result optional field if the parameter is set to true, you will receive clickstream_etv, clickstream_gender_distribution, and clickstream_age_distribution fields with clickstream data in the response default value: false with this parameter enabled, you will be charged double the price for the request learn more about how clickstream-based metrics are calculated in this help center article | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in example: [\&quot;metrics.organic.count\&quot;,\&quot;&gt;\&quot;,50] [[\&quot;metrics.organic.pos_1\&quot;,\&quot;&lt;&gt;\&quot;,0],\&quot;and\&quot;,[\&quot;metrics.organic.impressions_etv\&quot;,\&quot;&gt;&#x3D;\&quot;,\&quot;10\&quot;]] [[[\&quot;metrics.organic.count\&quot;,\&quot;&gt;&#x3D;\&quot;,50],\&quot;and\&quot;,[\&quot;metrics.organic.pos_1\&quot;,\&quot;in\&quot;,[1,5]]], \&quot;or\&quot;, [\&quot;metrics.organic.etv\&quot;,\&quot;&gt;&#x3D;\&quot;,\&quot;100\&quot;]] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to specify a sorting type example: [\&quot;metrics.paid.etv,asc\&quot;] Note: you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;metrics.organic.etv,desc\&quot;,\&quot;metrics.paid.count,asc\&quot;] default rule: [\&quot;metrics.organic.count,desc\&quot;] Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array | [optional] 
**limit** | **int** | the maximum number of returned domains optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned domains optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords | [optional] 
**max_rank_group** | **int** | maximum rank up to which competitors will be considered optional field default value: 100 if you specify 10 here, we will extract competitors from the top 10 Google search results only | [optional] 
**exclude_top_domains** | **bool** | indicates whether to exclude world’s largest websites optional field default value: false set to true if you want to get highly-relevant competitors excluding the websites listed below: wikipedia.org pinterest.com amazon.com google.com facebook.com wordpress.com medium.com quora.com reddit.com youtube.com ebay.com uol.com.br instagram.com olx.com twitter.com linkedin.com slideshare.net | [optional] 
**intersecting_domains** | **List[str]** | additional domains for improving results accuracy optional field to improve the accuracy of the result, you can specify domains that are known to intersect with the target in SERPs; if you use this array, metrics in the result will be based on SERPs where both target website and intersecting_domains appear; Note: you can specify up to 20 domains in this array | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_competitors_domain_live_request_info import DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo from a JSON string
dataforseo_labs_google_competitors_domain_live_request_info_instance = DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_competitors_domain_live_request_info_dict = dataforseo_labs_google_competitors_domain_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo from a dict
dataforseo_labs_google_competitors_domain_live_request_info_form_dict = dataforseo_labs_google_competitors_domain_live_request_info.from_dict(dataforseo_labs_google_competitors_domain_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


