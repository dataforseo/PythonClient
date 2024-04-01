# DomainAnalyticsWhoisOverviewLiveItem

items array

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | domain name | [optional] 
**created_datetime** | **str** | date and time of registration date and time (in the ISO 8601 format) when the domain was first registered example: \&quot;1997-03-29 03:00:00 +00:00\&quot; | [optional] 
**changed_datetime** | **str** | date and time when the domain entry was changed date and time (in the ISO 8601 format) when the domain entry was last modified example: \&quot;2021-01-14 08:36:28 +00:00\&quot; | [optional] 
**expiration_datetime** | **str** | date and time when the domain will expire date and time (in the ISO 8601 format) when the domain is due to expire example: \&quot;2022-11-26 17:21:23 +00:00\&quot; | [optional] 
**updated_datetime** | **str** | date and time when the domain was updated date and time (in the ISO 8601 format) when the domain was last updated example: \&quot;2021-01-29 13:59:38 +00:00\&quot; | [optional] 
**first_seen** | **str** | date and time when our crawler found the domain for the first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: \&quot;2019-11-15 12:57:46 +00:00\&quot; | [optional] 
**epp_status_codes** | **List[Optional[str]]** | extensive provisioning protocol status codes the status of a domain name registration as defined by ICANN | [optional] 
**tld** | **str** | top-level domain top-level domain in the DNS root zone | [optional] 
**registered** | **bool** | domain registration status if false, the domain name registration has expired Note: expired domains will remain in the database for only a short period of time | [optional] 
**registrar** | **str** | domain registrar if null, the domain registrar is unknown example: NameCheap, Inc. | [optional] 
**metrics** | [**MetricsBundleInfo**](MetricsBundleInfo.md) |  | [optional] 
**backlinks_info** | [**BacklinksInfo**](BacklinksInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_whois_overview_live_item import DomainAnalyticsWhoisOverviewLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsWhoisOverviewLiveItem from a JSON string
domain_analytics_whois_overview_live_item_instance = DomainAnalyticsWhoisOverviewLiveItem.from_json(json)
# print the JSON string representation of the object
print(DomainAnalyticsWhoisOverviewLiveItem.to_json())

# convert the object into a dict
domain_analytics_whois_overview_live_item_dict = domain_analytics_whois_overview_live_item_instance.to_dict()
# create an instance of DomainAnalyticsWhoisOverviewLiveItem from a dict
domain_analytics_whois_overview_live_item_form_dict = domain_analytics_whois_overview_live_item.from_dict(domain_analytics_whois_overview_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


