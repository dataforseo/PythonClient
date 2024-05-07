# BacklinksBulkPagesSummaryLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**url** | **str** | page URL | [optional] 
**rank** | **int** | page rank rank of the page on the target website rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional] 
**main_domain_rank** | **int** | rank of the main domain rank of the main domain is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional] 
**backlinks** | **int** | number of backlinks | [optional] 
**first_seen** | **str** | date and time when our crawler found a backlink to this page for the first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**lost_date** | **str** | date and time when the last backlink to this page was lost indicates the date and time when our crawler visited the page and it responded with 4xx or 5xx status code or the last backlink was removed in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59 +00:00 | [optional] 
**backlinks_spam_score** | **int** | average spam score of the backlinks pointing to the page learn more about how the metric is calculated on this help center page | [optional] 
**broken_backlinks** | **int** | number of broken backlinks number of broken backlinks pointing to the page | [optional] 
**broken_pages** | **int** | number of broken pages number of pages that respond with 4xx or 5xx status codes where backlinks are pointing to | [optional] 
**referring_domains** | **int** | indicates the number domains referring to the page | [optional] 
**referring_domains_nofollow** | **int** | number of domains pointing at least one nofollow link to the target | [optional] 
**referring_main_domains** | **int** | indicates the number of referring main domains | [optional] 
**referring_main_domains_nofollow** | **int** | number of main domains pointing at least one nofollow link to the target | [optional] 
**referring_ips** | **int** | number of referring IP addresses number of IP addresses pointing to this page | [optional] 
**referring_subnets** | **int** | number of referring subnetworks | [optional] 
**referring_pages** | **int** | indicates the number of pages pointing to the relevant url | [optional] 
**referring_pages_nofollow** | **int** | number of referring pages pointing at least one nofollow link to the target | [optional] 
**referring_links_tld** | **Dict[str, Optional[int]]** |  | [optional] 
**referring_links_types** | **Dict[str, Optional[int]]** |  | [optional] 
**referring_links_attributes** | **Dict[str, Optional[int]]** |  | [optional] 
**referring_links_platform_types** | **Dict[str, Optional[int]]** |  | [optional] 
**referring_links_semantic_locations** | **Dict[str, Optional[int]]** |  | [optional] 
**referring_links_countries** | **Dict[str, Optional[int]]** |  | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_bulk_pages_summary_live_item import BacklinksBulkPagesSummaryLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkPagesSummaryLiveItem from a JSON string
backlinks_bulk_pages_summary_live_item_instance = BacklinksBulkPagesSummaryLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksBulkPagesSummaryLiveItem.to_json()

# convert the object into a dict
backlinks_bulk_pages_summary_live_item_dict = backlinks_bulk_pages_summary_live_item_instance.to_dict()
# create an instance of BacklinksBulkPagesSummaryLiveItem from a dict
backlinks_bulk_pages_summary_live_item_form_dict = backlinks_bulk_pages_summary_live_item.from_dict(backlinks_bulk_pages_summary_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


