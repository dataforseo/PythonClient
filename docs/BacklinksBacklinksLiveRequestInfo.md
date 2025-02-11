# BacklinksBacklinksLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain, subdomain or webpage to get backlinks for required field a domain or a subdomain should be specified without https:// and www. a page should be specified with absolute URL (including http:// or https://) | [optional] 
**mode** | **str** | results grouping type optional field possible grouping types: as_is – returns all backlinks one_per_domain – returns one backlink per domain one_per_anchor – returns one backlink per anchor default value: as_is | [optional] 
**custom_mode** | **Dict[str, Optional[object]]** | detailed results grouping type optional field use this object to get a specific number of backlinks per field if you use custom_mode, then mode will be ignored example: \&quot;custom_mode\&quot;: {\&quot;field\&quot;: \&quot;domain\&quot;, \&quot;value\&quot;: 100} | [optional] 
**var_field** | **str** | response field required field if you choose to specify custom_mode possible values: anchor domain_from domain_from_country tld_from page_from_encoding page_from_language item_type page_from_status_code semantic_location | [optional] 
**value** | **int** | number of backlinks to return per field required field if you choose to specify custom_mode can be set from 1 to 1000 | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: &#x3D;, &lt;&gt;, in, not_in, like, not_like, ilike, not_ilike, regex, not_regex, match, not_match you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;rank\&quot;,\&quot;&gt;\&quot;,\&quot;80\&quot;] [[\&quot;page_from_rank\&quot;,\&quot;&gt;\&quot;,\&quot;55\&quot;], \&quot;and\&quot;, [\&quot;dofollow\&quot;,\&quot;&#x3D;\&quot;,true]] [[\&quot;first_seen\&quot;,\&quot;&gt;\&quot;,\&quot;2017-10-23 11:31:45 +00:00\&quot;], \&quot;and\&quot;, [[\&quot;anchor\&quot;,\&quot;like\&quot;,\&quot;%seo%\&quot;],\&quot;or\&quot;,[\&quot;text_pre\&quot;,\&quot;like\&quot;,\&quot;%seo%\&quot;]]] The full list of possible filters is available here. | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;rank,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;domain_from_rank,desc\&quot;,\&quot;page_from_rank,asc\&quot;] | [optional] 
**offset** | **int** | offset in the results array of the returned backlinks optional field default value: 0 if you specify the 10 value, the first ten backlinks in the results array will be omitted and the data will be provided for the successive backlinks; Note: the maximum value is 20,000, use the search_after_token if you would like to offset more results | [optional] 
**search_after_token** | **str** | token for subsequent requests optional field provided in the identical filed of the response to each request; use this parameter to avoid timeouts while trying to obtain over 20,000 results in a single request; by specifying the unique search_after_token value from the response array, you will get the subsequent results of the initial task; search_after_token values are unique for each subsequent task ; Note: if the search_after_token is specified in the request, all other parameters should be identical to the previous request | [optional] 
**limit** | **int** | the maximum number of returned backlinks optional field default value: 100 maximum value: 1000 | [optional] 
**backlinks_status_type** | **str** | set what backlinks to return and count optional field you can use this field to choose what backlinks will be returned and used for aggregated metrics for your target; possible values: all – all backlinks will be returned and counted; live – backlinks found during the last check will be returned and counted; lost – lost backlinks will be returned and counted; default value: live | [optional] 
**include_subdomains** | **bool** | indicates if the subdomains of the target will be included in the search optional field if set to false, the subdomains will be ignored default value: true | [optional] 
**include_indirect_links** | **bool** | indicates if indirect links to the target will be included in the results optional field if set to true, the results will include data on indirect links pointing to a page that either redirects to the target, or points to a canonical page if set to false, indirect links will be ignored default value: true | [optional] 
**exclude_internal_backlinks** | **bool** | indicates if internal backlinks from subdomains to the target will be excluded from the results optional field if set to true, the results will not include data on internal backlinks from subdomains of the same domain as target if set to false, internal links will be included in the results default value: true | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_backlinks_live_request_info import BacklinksBacklinksLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBacklinksLiveRequestInfo from a JSON string
backlinks_backlinks_live_request_info_instance = BacklinksBacklinksLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(BacklinksBacklinksLiveRequestInfo.to_json())

# convert the object into a dict
backlinks_backlinks_live_request_info_dict = backlinks_backlinks_live_request_info_instance.to_dict()
# create an instance of BacklinksBacklinksLiveRequestInfo from a dict
backlinks_backlinks_live_request_info_from_dict = BacklinksBacklinksLiveRequestInfo.from_dict(backlinks_backlinks_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


