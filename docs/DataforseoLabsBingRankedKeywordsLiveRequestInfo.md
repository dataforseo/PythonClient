# DataforseoLabsBingRankedKeywordsLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain required field the domain name of the target website the domain should be specified without https:// or www. if you want to get the keywords a particular webpage ranks for, specify the filter by the ranked_serp_element.serp_item.relative_url parameter example: \&quot;filters\&quot;:[ \&quot;ranked_serp_element.serp_item.relative_url\&quot;, \&quot;&#x3D;\&quot;, \&quot;/apis/rank-tracker-api\&quot;] | [optional] 
**location_name** | **str** | full name of the location optional field if you use this field, you don’t need to specify location_code you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; ignore this field to get the results for all available locations; Note: this endpoint currently supports the US location only; example: United States | [optional] 
**location_code** | **int** | location code optional field if you use this field, you don’t need to specify location_name you can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available locations; Note: this endpoint currently supports the US location only; example: 2840 | [optional] 
**language_name** | **str** | full name of the language optional field if you use this field, you don’t need to specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: English | [optional] 
**language_code** | **str** | language code optional field if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available languages example: en | [optional] 
**item_types** | **List[str]** | display results by item type optional field indicates the type of search results included in the response Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array; you will not be able to sort and filter results by the types of search results not included in the response; possible values: [\&quot;organic\&quot;, \&quot;paid\&quot;, \&quot;featured_snippet\&quot;, \&quot;local_pack\&quot;] default value: [\&quot;organic\&quot;, \&quot;paid\&quot;, \&quot;featured_snippet\&quot;, \&quot;local_pack\&quot;] | [optional] 
**ignore_synonyms** | **bool** | ignore highly similar keywords optional field if set to true only core keywords will be returned, all highly similar keywords will be excluded; default value: false | [optional] 
**limit** | **int** | the maximum number of returned keywords optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned keywords optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords | [optional] 
**load_rank_absolute** | **bool** | return rankings distribution by rank_absolute optional field default value: false if set to true, we will return the field metrics_absolute containing rankings distribution by the rank_absolute parameter that indicates the result’s position among all SERP elements | [optional] 
**historical_serp_mode** | **str** | data collection mode optional field you can use this field to filter the results; possible types of filtering: live — return keywords for which the specified target currently has ranking results in SERP; lost — return keywords for which the specified target had previously had ranking results in SERP, but didn’t have them during the last check; all — return both types of keywords. default value: live | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;ranked_serp_element.serp_item.rank_group\&quot;,\&quot;&lt;&#x3D;\&quot;,10] [[\&quot;ranked_serp_element.serp_item.rank_group\&quot;,\&quot;&lt;&#x3D;\&quot;,10], \&quot;and\&quot;, [\&quot;ranked_serp_element.serp_item.type\&quot;,\&quot;&lt;&gt;\&quot;,\&quot;paid\&quot;]] [[\&quot;keyword_data.keyword_info.search_volume\&quot;,\&quot;&lt;&gt;\&quot;,0], \&quot;and\&quot;, [[\&quot;ranked_serp_element.serp_item.type\&quot;,\&quot;&lt;&gt;\&quot;,\&quot;paid\&quot;],\&quot;or\&quot;,[\&quot;ranked_serp_element.serp_item.is_malicious\&quot;,\&quot;&#x3D;\&quot;,false]]] if you want to get the keywords a particular webpage ranks for, specify the filter by the ranked_serp_element.serp_item.relative_url parameter example: [\&quot;ranked_serp_element.serp_item.relative_url\&quot;, \&quot;&#x3D;\&quot;, \&quot;/apis/rank-tracker-api\&quot;] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;keyword_data.keyword_info.competition,desc\&quot;] default rule: [\&quot;ranked_serp_element.serp_item.rank_group,asc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;keyword_data.keyword_info.search_volume,desc\&quot;,\&quot;keyword_data.keyword_info.cpc,desc\&quot;] | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_bing_ranked_keywords_live_request_info import DataforseoLabsBingRankedKeywordsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBingRankedKeywordsLiveRequestInfo from a JSON string
dataforseo_labs_bing_ranked_keywords_live_request_info_instance = DataforseoLabsBingRankedKeywordsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsBingRankedKeywordsLiveRequestInfo.to_json())

# convert the object into a dict
dataforseo_labs_bing_ranked_keywords_live_request_info_dict = dataforseo_labs_bing_ranked_keywords_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsBingRankedKeywordsLiveRequestInfo from a dict
dataforseo_labs_bing_ranked_keywords_live_request_info_form_dict = dataforseo_labs_bing_ranked_keywords_live_request_info.from_dict(dataforseo_labs_bing_ranked_keywords_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


