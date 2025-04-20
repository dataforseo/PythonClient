# BacklinksHistoryLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**var_date** | **str** | date and time when the data for the target was stored in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**rank** | **int** | domain rank on the given date learn more about the metric and how it is calculated in this help center article | [optional] 
**backlinks** | **int** | number of backlinks | [optional] 
**new_backlinks** | **int** | number of new backlinks for the target data is provided based in a comparison with the previous period Note: this data is available from May 2021; if the date range specified in the POST request precedes May 2021, the field will equal 0 | [optional] 
**lost_backlinks** | **int** | number of lost backlinks for the target data is provided based in a comparison with the previous period Note: this data is available from May 2021; if the date range specified in the POST request precedes May 2021, the field will equal 0 | [optional] 
**new_referring_domains** | **int** | number of new referring domains for the target data is provided based in a comparison with the previous period Note: this data is available from May 2021; if the date range specified in the POST request precedes May 2021, the field will equal 0 | [optional] 
**lost_referring_domains** | **int** | number of lost referring domains for the target data is provided based in a comparison with the previous period Note: this data is available from May 2021; if the date range specified in the POST request precedes May 2021, the field will equal 0 | [optional] 
**crawled_pages** | **int** | number of crawled pages for the target | [optional] 
**info** | [**TargetInfo**](TargetInfo.md) |  | [optional] 
**internal_links_count** | **int** | number of internal links calculated as the sum of internal links on the pages of the specified target | [optional] 
**external_links_count** | **int** | number of external links on the page calculated as the sum of external links on the pages of the specified target | [optional] 
**broken_backlinks** | **int** | number of broken backlinks number of broken backlinks pointing to the target | [optional] 
**broken_pages** | **int** | number of broken pages number of pages that receive backlinks but respond with 4xx or 5xx status codes | [optional] 
**referring_domains** | **int** | number of referring domains referring domains include subdomains that are counted as separate domains for this metric | [optional] 
**referring_domains_nofollow** | **int** | number of domains pointing at least one nofollow link to the target | [optional] 
**referring_main_domains** | **int** | number of referring main domains | [optional] 
**referring_main_domains_nofollow** | **int** | number of main domains pointing at least one nofollow link to the target | [optional] 
**referring_ips** | **int** | number of referring IP addresses number of IP addresses pointing to this page | [optional] 
**referring_subnets** | **int** | number of referring subnetworks | [optional] 
**referring_pages** | **int** | number of pages pointing to the target | [optional] 
**referring_pages_nofollow** | **int** | number of referring pages pointing at least one nofollow link to the target | [optional] 
**referring_links_tld** | **Dict[str, Optional[int]]** | top-level domains of the referring links contains top-level domains and referring link count per each | [optional] 
**referring_links_types** | **Dict[str, Optional[int]]** | types of referring links indicates the types of the referring links and link count per each type possible values: anchor, image, link, meta, canonical, alternate, redirect | [optional] 
**referring_links_attributes** | **Dict[str, Optional[int]]** | link attributes of the referring links indicates link attributes of the referring links and link count per each attribute | [optional] 
**referring_links_platform_types** | **Dict[str, Optional[int]]** | types of referring platforms indicates referring platform types and and link count per each platform possible values: cms, blogs, ecommerce, message-boards, wikis, news, organization | [optional] 
**referring_links_semantic_locations** | **Dict[str, Optional[int]]** | semantic locations of the referring links indicates semantic elements in HTML where the referring links are located and link count per each semantic location you can get the full list of semantic elements here examples: article, section, summary | [optional] 
**referring_links_countries** | **Dict[str, Optional[int]]** | ISO country codes of the referring links indicates ISO country codes of the domains where the referring links are located and the link count per each country | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_history_live_item import BacklinksHistoryLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksHistoryLiveItem from a JSON string
backlinks_history_live_item_instance = BacklinksHistoryLiveItem.from_json(json)
# print the JSON string representation of the object
print(BacklinksHistoryLiveItem.to_json())

# convert the object into a dict
backlinks_history_live_item_dict = backlinks_history_live_item_instance.to_dict()
# create an instance of BacklinksHistoryLiveItem from a dict
backlinks_history_live_item_from_dict = BacklinksHistoryLiveItem.from_dict(backlinks_history_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


