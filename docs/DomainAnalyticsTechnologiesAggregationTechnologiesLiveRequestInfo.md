# DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | id of the target technology group required field if you don’t specify technology or category you can find the full list of technology group ids on this page example: \&quot;marketing\&quot; | [optional] 
**category** | **str** | id of the target technology category required field if you don’t specify group or technology you can find the full list of technology category ids on this page example: \&quot;crm\&quot; | [optional] 
**technology** | **str** | target technology required field if you don’t specify group or category you can find the full list of technologies on this page example: \&quot;Salesforce\&quot; | [optional] 
**keyword** | **str** | target keyword in the domain’s meta keywords optional field UTF-8 encoding each keyword should be at least 3 characters long example: \&quot;seo\&quot; | [optional] 
**mode** | **str** | search mode optional field possible search mode types: as_is – search for results exactly matching the specified group ids, category ids, or technology names entry – search for results matching a part of the specified group ids, category ids, or technology names default value: as_is | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like,not_like you can use the % operator with like and not_like to match any string of zero or more characters you can use the following parameters to filter the results: domain_rank, last_visited, country_iso_code, language_code, content_language_code example: [[\&quot;country_iso_code\&quot;,\&quot;&#x3D;\&quot;,\&quot;US\&quot;], \&quot;and\&quot;, [\&quot;domain_rank\&quot;,\&quot;&gt;\&quot;,800]]for more information about filters, please refer to Domain Analytics Technologies API – Filters | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the following values to sort the results: groups_count, categories_count, technologies_count possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\&quot;groups_count,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;groups_count,desc\&quot;,\&quot;technologies_count,desc\&quot;] default value: [\&quot;groups_count,desc\&quot;,\&quot;categories_count,desc\&quot;,\&quot;technologies_count,desc\&quot;] | [optional] 
**internal_groups_list_limit** | **int** | maximum number of returned technology groups optional field you can use this field to limit the number of items with identical \&quot;group\&quot; in the results default value: 5 maximum value: 10000 | [optional] 
**internal_categories_list_limit** | **int** | maximum number of returned technology categories within the same group optional field you can use this field to limit the number of items with identical \&quot;category\&quot; in the results default value: 5 maximum value: 10000 | [optional] 
**internal_technologies_list_limit** | **int** | maximum number of returned technologies within the same category optional field you can use this field to limit the number of items with identical \&quot;technology\&quot; in the results default value: 10 maximum value: 10000 | [optional] 
**internal_list_limit** | **int** | maximum number of items with identical \&quot;category\&quot;, \&quot;group\&quot;, and \&quot;technology\&quot; optional field if you use this field, the values specified in internal_groups_list_limit, internal_categories_list_limit and internal_technologies_list_limit will be ignored; you can use this field to limit the number of items with identical \&quot;category\&quot;, \&quot;group\&quot;, or \&quot;technology\&quot; default value: 10 maximum value: 10000 | [optional] 
**limit** | **int** | the maximum number of returned technologies optional field default value: 100 maximum value: 10000 | [optional] 
**offset** | **int** | offset in the results array of returned domains optional field default value: 0 maximum value: 9999 if you specify the 10 value, the first ten technologies in the results array will be omitted and the data will be provided for the successive technologies | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_aggregation_technologies_live_request_info import DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo from a JSON string
domain_analytics_technologies_aggregation_technologies_live_request_info_instance = DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo.to_json())

# convert the object into a dict
domain_analytics_technologies_aggregation_technologies_live_request_info_dict = domain_analytics_technologies_aggregation_technologies_live_request_info_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo from a dict
domain_analytics_technologies_aggregation_technologies_live_request_info_form_dict = domain_analytics_technologies_aggregation_technologies_live_request_info.from_dict(domain_analytics_technologies_aggregation_technologies_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


