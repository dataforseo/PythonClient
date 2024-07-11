# BacklinksPageIntersectionLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | **Dict[str, Optional[str]]** | domains, subdomains or webpages to get links for required field you can set up to 20 domains, subdomains or webpages a domain or a subdomain should be specified without https:// and www. a page should be specified with absolute URL (including http:// or https://) example: \&quot;targets\&quot;: { \&quot;1\&quot;: \&quot;http://planet.postgresql.org/\&quot;, \&quot;2\&quot;: \&quot;http://gborg.postgresql.org/\&quot; } | [optional] 
**exclude_targets** | **List[str]** | domains, subdomains or webpages you want to exclude optional field you can set up to 10 domains, subdomains or webpages if you use this array, results will contain the referring pages that link to targets but don’t link to exclude_targets example: \&quot;exclude_targets\&quot;: [ \&quot;bbc.com\&quot;, \&quot;https://www.apple.com/iphone/*\&quot;, \&quot;https://dataforseo.com/apis/*\&quot;] | [optional] 
**backlinks_status_type** | **str** | set what backlinks to return and count optional field you can use this field to choose what backlinks will be returned and used for aggregated metrics for your targets; possible values: all – all backlinks will be returned and counted; live – backlinks found during the last check will be returned and counted; lost – lost backlinks will be returned and counted; default value: live | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, &#x3D;, &lt;&gt;, in, not_in, like, not_like, ilike, not_ilike you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;1.rank\&quot;,\&quot;&gt;\&quot;,\&quot;80\&quot;] [[\&quot;2.page_from_rank\&quot;,\&quot;&gt;\&quot;,\&quot;55\&quot;], \&quot;and\&quot;, [\&quot;1.original\&quot;,\&quot;&#x3D;\&quot;,\&quot;true\&quot;]] [[\&quot;1.first_seen\&quot;,\&quot;&gt;\&quot;,\&quot;2017-10-23 11:31:45 +00:00\&quot;], \&quot;and\&quot;, [[\&quot;1.acnhor\&quot;,\&quot;like\&quot;,\&quot;%seo%\&quot;],\&quot;or\&quot;,[\&quot;1.text_pre\&quot;,\&quot;not_like\&quot;,\&quot;%seo%\&quot;]]] The full list of possible filters is available here. | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;rank,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;domain_from_rank,desc\&quot;,\&quot;page_from_rank,asc\&quot;] | [optional] 
**offset** | **int** | offset in the results array of the returned backlinks optional field default value: 0 if you specify the 10 value, the first ten backlinks in the results array will be omitted and the data will be provided for the successive backlinks | [optional] 
**limit** | **int** | the maximum number of returned backlinks optional field default value: 100 maximum value: 1000 | [optional] 
**internal_list_limit** | **int** | maximum number of elements within internal arrays optional field you can use this field to limit the number of elements within the following arrays: attributes domain_from_platform_type default value: 10 maximum value: 1000 | [optional] 
**include_subdomains** | **bool** | indicates if the subdomains of the targets will be included in the search optional field if set to false, the subdomains will be ignored default value: true | [optional] 
**include_indirect_links** | **bool** | indicates if indirect links to the targets will be included in the results optional field if set to true, the results will include data on indirect links pointing to a page that either redirects to a target, or points to a canonical page if set to false, indirect links will be ignored default value: true | [optional] 
**exclude_internal_backlinks** | **bool** | indicates if internal backlinks from subdomains to the target will be excluded from the results optional field if set to true, the results will not include data on internal backlinks from subdomains of the same domain as target if set to false, internal links will be included in the result default value: true | [optional] 
**intersection_mode** | **str** | indicates whether to intersect backlinks optional field use this field to intersect or merge results for the specified URLs possible values: all, partial all – results are based on all backlinks; partial – results are based on the intersecting backlinks only; default value: all | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_page_intersection_live_request_info import BacklinksPageIntersectionLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksPageIntersectionLiveRequestInfo from a JSON string
backlinks_page_intersection_live_request_info_instance = BacklinksPageIntersectionLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksPageIntersectionLiveRequestInfo.to_json()

# convert the object into a dict
backlinks_page_intersection_live_request_info_dict = backlinks_page_intersection_live_request_info_instance.to_dict()
# create an instance of BacklinksPageIntersectionLiveRequestInfo from a dict
backlinks_page_intersection_live_request_info_form_dict = backlinks_page_intersection_live_request_info.from_dict(backlinks_page_intersection_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


