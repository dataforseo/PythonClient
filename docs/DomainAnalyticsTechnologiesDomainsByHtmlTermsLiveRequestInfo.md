# DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_terms** | **List[str]** | target search terms required field specify target HTML elements, tags, attributes, their content or all of the above if you specify more than one search term, you will receive only the domains containing all of the specified terms in the HTML code of their homepage maximum number of search terms you can specify: 10 example: [\&quot;data-attrid\&quot;] | [optional] 
**keywords** | **List[str]** | target keywords in the domain’s title, description or meta keywords optional field UTF-8 encoding each keyword should be at least 3 characters long maximum number of keywords you can specify: 10 example: [\&quot;seo\&quot;,\&quot;software\&quot;] | [optional] 
**mode** | **str** | search mode optional field possible search mode types: strict_entry – search for results exactly matching the order, intervals and separators in the specified search terms entry – search for results ignoring the order, intervals and separators in the specified search terms default value: entry | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;domain\&quot;,\&quot;like\&quot;,\&quot;%seo%\&quot;] [[\&quot;country_iso_code\&quot;,\&quot;&#x3D;\&quot;,\&quot;US\&quot;], \&quot;and\&quot;, [\&quot;domain_rank\&quot;,\&quot;&gt;\&quot;,100]] [[\&quot;domain_rank\&quot;,\&quot;&gt;\&quot;,100], \&quot;and\&quot;, [[\&quot;country_iso_code\&quot;,\&quot;&#x3D;\&quot;,\&quot;US\&quot;],\&quot;or\&quot;,[\&quot;country_iso_code\&quot;,\&quot;&#x3D;\&quot;,\&quot;CA\&quot;]]] for more information about filters, please refer to Domain Analytics Technologies API – Filters | [optional] 
**order_by** | **List[str]** | results sorting rules optional field available fields: domain_rank, domain, last_visited, country_iso_code, language_code, content_language_code possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;last_visited,desc\&quot;] default rule: [\&quot;domain_rank,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;last_visited,desc\&quot;,\&quot;domain_rank,desc\&quot;] | [optional] 
**limit** | **int** | the maximum number of returned domains optional field default value: 100 maximum value: 10000 | [optional] 
**offset** | **int** | offset in the results array of returned domains optional field default value: 0 if you specify the 10 value, the first ten domains in the results array will be omitted and the data will be provided for the successive domains; Note: the maximum value is 9999, the sum of limit and offset must not exceed 10000; use the offset_token if you would like to offset more results | [optional] 
**offset_token** | **str** | token for subsequent requests optional field provided in the identical filed of the response to each request; use this parameter to avoid timeouts while trying to obtain over 100,000 results in a single request; by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task; offset_token values are unique for each subsequent task Note: if the offset_token is specified in the request, all other parameters should be identical to the previous request | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_domains_by_html_terms_live_request_info import DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo from a JSON string
domain_analytics_technologies_domains_by_html_terms_live_request_info_instance = DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo.to_json())

# convert the object into a dict
domain_analytics_technologies_domains_by_html_terms_live_request_info_dict = domain_analytics_technologies_domains_by_html_terms_live_request_info_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo from a dict
domain_analytics_technologies_domains_by_html_terms_live_request_info_form_dict = domain_analytics_technologies_domains_by_html_terms_live_request_info.from_dict(domain_analytics_technologies_domains_by_html_terms_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


