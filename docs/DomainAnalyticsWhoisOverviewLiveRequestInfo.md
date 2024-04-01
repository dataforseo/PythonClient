# DomainAnalyticsWhoisOverviewLiveRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | the maximum number of returned domains optional field default value: 100 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned items optional field default value: 0 if you specify the 10 value, the first ten items in the results array will be omitted and the data will be provided for the successive items | [optional] 
**filters** | **List[Optional[object]]** | array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;, &#x3D;, &lt;&gt;, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters examples: [\&quot;expiration_datetime\&quot;, \&quot;&lt;\&quot;, \&quot;2021-02-15 01:00:00 +00:00\&quot;] [[\&quot;expiration_datetime\&quot;, \&quot;&lt;\&quot;, \&quot;2021-02-15 01:00:00 +00:00\&quot;],  \&quot;and\&quot;,  [\&quot;domain\&quot;, \&quot;like\&quot;, \&quot;%seo%\&quot;]]  for more information about filters, please refer to Filters Page or this help center guide | [optional] 
**order_by** | **List[str]** | results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc - results will be sorted in the ascending order desc - results will be sorted in the descending order the comma is used as a separator example: [\&quot;metrics.organic.pos_1,desc\&quot;] default rule: [\&quot;metrics.organic.count,desc\&quot;] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\&quot;expiration_datetime,asc\&quot;,\&quot;metrics.organic.etv,desc\&quot;,\&quot;metrics.organic.pos_1,desc\&quot;] | [optional] 
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_whois_overview_live_request_info import DomainAnalyticsWhoisOverviewLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsWhoisOverviewLiveRequestInfo from a JSON string
domain_analytics_whois_overview_live_request_info_instance = DomainAnalyticsWhoisOverviewLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print(DomainAnalyticsWhoisOverviewLiveRequestInfo.to_json())

# convert the object into a dict
domain_analytics_whois_overview_live_request_info_dict = domain_analytics_whois_overview_live_request_info_instance.to_dict()
# create an instance of DomainAnalyticsWhoisOverviewLiveRequestInfo from a dict
domain_analytics_whois_overview_live_request_info_form_dict = domain_analytics_whois_overview_live_request_info.from_dict(domain_analytics_whois_overview_live_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


