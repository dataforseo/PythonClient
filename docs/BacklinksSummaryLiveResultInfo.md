# BacklinksSummaryLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | target in a POST array | [optional] 
**first_seen** | **str** | date and time when our crawler found the backlink for the target for the first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**lost_date** | **str** | date and time when the backlink was lost indicates the date and time when our crawler visited the target and it responded with a 4xx or 5xx status code or when its last backlink was removed in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**rank** | **int** | target rank learn more about the metric and how it is calculated in this help center article | [optional] 
**backlinks** | **int** | indicates the number of backlinks | [optional] 
**backlinks_spam_score** | **int** | spam score of the backlinks displays the total spam score of all backlinks pointing to the target domain, subdomain, or webpage; to learn more about how the metric is calculated, refer to this Help Center page | [optional] 
**crawled_pages** | **int** | number of crawled pages for the target | [optional] 
**info** | [**TargetInfo**](TargetInfo.md) |  | [optional] 
**internal_links_count** | **int** | number of internal links calculated as the sum of internal links on the pages of the specified target | [optional] 
**external_links_count** | **int** | number of external links on the page calculated as the sum of external links on the pages of the specified target | [optional] 
**broken_backlinks** | **int** | number of broken backlinks number of broken backlinks pointing to the target | [optional] 
**broken_pages** | **int** | number of broken pages number of pages on the target that respond with 4xx or 5xx status codes note that the number of broken pages includes pages on the target discovered by following external links, but it may also include pages discovered by following the target’s sitemap | [optional] 
**referring_domains** | **int** | indicates the number of referring domains referring domains include subdomains that are counted as separate domains for this metric | [optional] 
**referring_domains_nofollow** | **int** | number of domains pointing at least one nofollow link to the target | [optional] 
**referring_main_domains** | **int** | indicates the number of referring main domains | [optional] 
**referring_main_domains_nofollow** | **int** | number of main domains pointing at least one nofollow link to the target | [optional] 
**referring_ips** | **int** | number of referring IP addresses number of IP addresses pointing to this page | [optional] 
**referring_subnets** | **int** | number of referring subnetworks | [optional] 
**referring_pages** | **int** | indicates the number of pages pointing to the target | [optional] 
**referring_links_tld** | **Dict[str, Optional[int]]** | top-level domains of the referring links contains top level domains and referring link count per each | [optional] 
**referring_links_types** | **Dict[str, Optional[int]]** | types of referring links indicates the types of the referring links and link count per each type possible values: anchor, image, link, meta, canonical, alternate, redirect | [optional] 
**referring_links_attributes** | **Dict[str, Optional[int]]** | link attributes of the referring links indicates link attributes of the referring links and link count per each attribute example values: nofollow, noopener, noreferrer, external, ugc, sponsored | [optional] 
**referring_links_platform_types** | **Dict[str, Optional[int]]** | types of referring platforms indicates referring platform types and and link count per each platform example values: cms, blogs, unknown, ecommerce, message-boards | [optional] 
**referring_links_semantic_locations** | **Dict[str, Optional[int]]** | semantic locations of the referring links indicates semantic elements in HTML where the referring links are located and link count per each semantic location you can get the full list of semantic elements here example values: article, section, summary, \&quot;\&quot; | [optional] 
**referring_links_countries** | **Dict[str, Optional[int]]** | ISO country codes of the referring links indicates ISO country codes of the domains where the referring links are located and the link count per each country | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_summary_live_result_info import BacklinksSummaryLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksSummaryLiveResultInfo from a JSON string
backlinks_summary_live_result_info_instance = BacklinksSummaryLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksSummaryLiveResultInfo.to_json()

# convert the object into a dict
backlinks_summary_live_result_info_dict = backlinks_summary_live_result_info_instance.to_dict()
# create an instance of BacklinksSummaryLiveResultInfo from a dict
backlinks_summary_live_result_info_form_dict = backlinks_summary_live_result_info.from_dict(backlinks_summary_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


