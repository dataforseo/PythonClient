# BacklinksTimeseriesSummaryLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**var_date** | **str** | date and time when the data for the target was stored in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**rank** | **int** | target rank for the given date learn more about the metric and how it is calculated in this help center article | [optional] 
**backlinks** | **int** | number of backlinks for the given date | [optional] 
**backlinks_nofollow** | **int** | number of nofollow backlinks for the given date | [optional] 
**referring_pages** | **int** | number of pages pointing to target for the given date | [optional] 
**referring_pages_nofollow** | **int** | number of referring pages pointing at least one nofollow link to the target for the given date | [optional] 
**referring_domains** | **int** | number of referring domains for the given date referring domains include subdomains that are counted as separate domains for this metric | [optional] 
**referring_domains_nofollow** | **int** | number of domains pointing at least one nofollow link to the target for the given date | [optional] 
**referring_main_domains** | **int** | number of referring main domains for the given date | [optional] 
**referring_main_domains_nofollow** | **int** | number of main domains pointing at least one nofollow link to the target for the given date | [optional] 
**referring_ips** | **int** | number of referring IP addresses for the given date number of IP addresses pointing to this page | [optional] 
**referring_subnets** | **int** | number of referring subnetworks for the given date | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_timeseries_summary_live_item import BacklinksTimeseriesSummaryLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksTimeseriesSummaryLiveItem from a JSON string
backlinks_timeseries_summary_live_item_instance = BacklinksTimeseriesSummaryLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksTimeseriesSummaryLiveItem.to_json()

# convert the object into a dict
backlinks_timeseries_summary_live_item_dict = backlinks_timeseries_summary_live_item_instance.to_dict()
# create an instance of BacklinksTimeseriesSummaryLiveItem from a dict
backlinks_timeseries_summary_live_item_form_dict = backlinks_timeseries_summary_live_item.from_dict(backlinks_timeseries_summary_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


