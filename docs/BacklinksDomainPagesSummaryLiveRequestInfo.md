# BacklinksDomainPagesSummaryLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain, subdomain or webpage to get summary data for required field a domain or a subdomain should be specified without https:// and www. a page should be specified with absolute URL (including http:// or https://) | [optional] 
**limit** | **int** | the maximum number of returned anchors optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned anchors optional field default value: 0 if you specify the 10 value, the first ten anchors in the results array will be omitted and the data will be provided for the successive anchors | [optional] 
**internal_list_limit** | **int** | maximum number of elements within internal arrays optional field you can use this field to limit the number of elements within the following arrays: referring_links_tld referring_links_types referring_links_attributes referring_links_platform_types referring_links_semantic_locations default value: 10 maximum value: 1000 | [optional] 
**backlinks_status_type** | **str** | set what backlinks to return and count optional field you can use this field to choose what backlinks will be returned and used for aggregated metrics for your target; possible values: all – all backlinks will be returned and counted; live – backlinks found during the last check will be returned and counted; lost – lost backlinks will be returned and counted; default value: live | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &#x3D;, &lt;&gt;, in, not_in, like, not_like, ilike, not_ilike, match, not_match you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;referring_links_types.anchors\&quot;,\&quot;&gt;\&quot;,\&quot;1\&quot;] [[\&quot;broken_pages\&quot;,\&quot;&gt;\&quot;,\&quot;2\&quot;], \&quot;and\&quot;, [\&quot;backlinks\&quot;,\&quot;&gt;\&quot;,\&quot;10\&quot;]] [[\&quot;first_seen\&quot;,\&quot;&gt;\&quot;,\&quot;2017-10-23 11:31:45 +00:00\&quot;], \&quot;and\&quot;, [[\&quot;anchor\&quot;,\&quot;like\&quot;,\&quot;%seo%\&quot;],\&quot;or\&quot;,[\&quot;referring_domains\&quot;,\&quot;&gt;\&quot;,\&quot;10\&quot;]]] The full list of possible filters is available here. | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;backlinks,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;backlinks,desc\&quot;,\&quot;rank,asc\&quot;] | [optional] 
**backlinks_filters** | **List[Optional[object]]** | filter the backlinks of your target optional field you can use this field to filter the initial backlinks that will be included in the dataset for aggregated metrics for your target you can filter the backlinks by all fields available in the response of this endpoint using this parameter, you can include only dofollow backlinks in the response and create a flexible backlinks dataset to calculate the metrics for example: \&quot;backlinks_filters\&quot;: [[\&quot;dofollow\&quot;, \&quot;&#x3D;\&quot;, true]] | [optional] 
**include_subdomains** | **bool** | indicates if the subdomains of the target domain will be included in the search optional field if set to false, the subdomains will be ignored default value: true | [optional] 
**include_indirect_links** | **bool** | indicates if indirect links to the target will be included in the results optional field if set to true, the results will include data on indirect links pointing to a page that either redirects to the target, or points to a canonical page if set to false, indirect links will be ignored default value: true | [optional] 
**exclude_internal_backlinks** | **bool** | indicates whether the backlinks from subdomains of the target are excluded optional field if set to false, backlinks from the subdomains of the target domain will be ommited and you won’t receive the same domain in the response; default value: true | [optional] 
**rank_scale** | **str** | defines the scale used for calculating and displaying the rank, domain_from_rank, and page_from_rank values optional field you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale possible values: one_hundred — rank values are displayed on a 0–100 scale one_thousand — rank values are displayed on a 0–1000 scale default value: one_thousand learn more about how this parameter works and how ranking metrics are calculated in this Help Center article | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_domain_pages_summary_live_request_info import BacklinksDomainPagesSummaryLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksDomainPagesSummaryLiveRequestInfo from a JSON string
backlinks_domain_pages_summary_live_request_info_instance = BacklinksDomainPagesSummaryLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksDomainPagesSummaryLiveRequestInfo.to_json())

# convert the object into a dict
backlinks_domain_pages_summary_live_request_info_dict = backlinks_domain_pages_summary_live_request_info_instance.to_dict()
# create an instance of BacklinksDomainPagesSummaryLiveRequestInfo from a dict
backlinks_domain_pages_summary_live_request_info_from_dict = BacklinksDomainPagesSummaryLiveRequestInfo.from_dict(backlinks_domain_pages_summary_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


