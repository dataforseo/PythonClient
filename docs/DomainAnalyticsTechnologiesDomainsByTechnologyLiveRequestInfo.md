# DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**technology_paths** | **List[str]** | target technology paths required field if you don’t specify groups, technologies, keywords or categories at least one field (technology_paths, groups, technologies, keywords or categories) must be set; each technology path should be specified as a separate object containing “path” and “name”, where “path” is specified as “$group_id.$category_id” and “name” – as the name of the target technology; each object with a technology path should be separated with a comma you can find the full list of technology group ids, category ids and technology names on this page note: you can specify up to 10 technology paths in this array example: [{\&quot;path\&quot;: \&quot;content.cms\&quot;,\&quot;name\&quot;: \&quot;wordpress\&quot;}, {\&quot;path\&quot;: \&quot;marketing.crm\&quot;,\&quot;name\&quot;: \&quot;salesforce\&quot;}] | [optional] 
**groups** | **List[str]** | ids of the target technology groups required field if you don’t specify technologies, technology_paths, keywords or categories you can find the full list of technology group ids on this page note: you can specify up to 10 technology groups in this array example: [\&quot;sales\&quot;, \&quot;marketing\&quot;] | [optional] 
**categories** | **List[str]** | ids of the target technology categories required field if you don’t specify groups, technology_paths, keywords or technologies you can find the full list of technology category ids on this page note: you can specify up to 10 technology categories in this array example: [\&quot;payment_processors\&quot;,\&quot;crm\&quot;] | [optional] 
**technologies** | **List[str]** | target technologies required field if you don’t specify groups, technology_paths, keywords or categories you can find the full list of technologies you can specify here on this page note: you can specify up to 10 technologies in this array example: [\&quot;Google Pay\&quot;,\&quot;Salesforce\&quot;] | [optional] 
**keywords** | **List[str]** | target keywords in the domain’s title, description or meta keywords required field if you don’t specify groups, technology_paths, technologies or categories optional field UTF-8 encoding example: [\&quot;seo\&quot;,\&quot;software\&quot;] | [optional] 
**mode** | **str** | search mode optional field possible search mode types: as_is – search for results exactly matching the specified group ids, category ids, or technology names entry – search for results matching a part of the specified group ids, category ids, or technology names default value: as_is | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\&quot;country_iso_code\&quot;,\&quot;&#x3D;\&quot;,\&quot;US\&quot;] [[\&quot;country_iso_code\&quot;,\&quot;&#x3D;\&quot;,\&quot;US\&quot;], \&quot;and\&quot;, [\&quot;domain_rank\&quot;,\&quot;&gt;\&quot;,100]] [[\&quot;domain_rank\&quot;,\&quot;&gt;\&quot;,100], \&quot;and\&quot;, [[\&quot;country_iso_code\&quot;,\&quot;&#x3D;\&quot;,\&quot;US\&quot;],\&quot;or\&quot;,[\&quot;country_iso_code\&quot;,\&quot;&#x3D;\&quot;,\&quot;CA\&quot;]]] for more information about filters, please refer to Domain Analytics Technologies API – Filters | [optional] 
**order_by** | **List[str]** | results sorting rules optional field available fields: domain_rank, domain, last_visited, country_iso_code, language_code, content_language_code possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;last_visited,desc\&quot;] default rule: [\&quot;domain_rank,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;last_visited,desc\&quot;,\&quot;domain_rank,desc\&quot;] | [optional] 
**limit** | **int** | the maximum number of returned domains optional field default value: 100 maximum value: 10000 | [optional] 
**offset** | **int** | offset in the results array of returned domains optional field default value: 0 if you specify the 10 value, the first ten domains in the results array will be omitted and the data will be provided for the successive domains; Note: the maximum value is 9999, the sum of limit and offset must not exceed 10000; use the offset_token if you would like to offset more results | [optional] 
**offset_token** | **str** | token for subsequent requests optional field provided in the identical filed of the response to each request; use this parameter to avoid timeouts while trying to obtain over 100,000 results in a single request; by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task; offset_token values are unique for each subsequent task Note: if the offset_token is specified in the request, all other parameters should be identical to the previous request | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_domains_by_technology_live_request_info import DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo from a JSON string
domain_analytics_technologies_domains_by_technology_live_request_info_instance = DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo.to_json()

# convert the object into a dict
domain_analytics_technologies_domains_by_technology_live_request_info_dict = domain_analytics_technologies_domains_by_technology_live_request_info_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo from a dict
domain_analytics_technologies_domains_by_technology_live_request_info_form_dict = domain_analytics_technologies_domains_by_technology_live_request_info.from_dict(domain_analytics_technologies_domains_by_technology_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


