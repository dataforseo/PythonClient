# PageSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_seen** | **str** | date and time when our crawler found the backlink for the first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**lost_date** | **str** | date and time when the last backlink for this page was lost indicates the date and time when our crawler visited the page and it responded with 4xx or 5xx status code or the last backlink was removed in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59 +00:00 | [optional] 
**rank** | **int** | page rank rank of the page rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional] 
**backlinks** | **int** | indicates the number of backlinks | [optional] 
**backlinks_spam_score** | **int** | average spam score of the backlinks pointing to the page learn more about how the metric is calculated on this help center page | [optional] 
**broken_backlinks** | **int** | number of broken backlinks number of broken backlinks pointing to the page | [optional] 
**broken_pages** | **int** | number of broken pages number of pages that respond with 4xx or 5xx status codes where backlinks are pointing to | [optional] 
**referring_domains** | **int** | indicates the number of referring domains | [optional] 
**referring_domains_nofollow** | **int** | number of domains pointing at least one nofollow link to the page | [optional] 
**referring_main_domains** | **int** | indicates the number of referring main domains | [optional] 
**referring_main_domains_nofollow** | **int** | number of main domains pointing at least one nofollow link to the page | [optional] 
**referring_ips** | **int** | number of referring IP addresses number of IP addresses pointing to this page | [optional] 
**referring_subnets** | **int** | number of referring subnetworks | [optional] 
**referring_pages** | **int** | indicates the number of pages pointing to the page | [optional] 
**referring_pages_nofollow** | **int** | number of referring pages pointing at least one nofollow link to the page | [optional] 
**referring_links_tld** | **Dict[str, Optional[int]]** | top-level domains of the referring links contains top level domains and referring link count per each | [optional] 
**referring_links_types** | **Dict[str, Optional[int]]** | types of referring links indicates the types of the referring links and link count per each type possible values: anchor, image, link, meta, canonical, alternate, redirect | [optional] 
**referring_links_attributes** | **Dict[str, Optional[int]]** | link attributes of the referring links indicates link attributes of the referring links and link count per each attribute | [optional] 
**referring_links_platform_types** | **Dict[str, Optional[int]]** | types of referring platforms indicates referring platform types and and link count per each platform possible values: cms, blogs, ecommerce, message-boards, wikis, news, organization | [optional] 
**referring_links_semantic_locations** | **Dict[str, Optional[int]]** | semantic locations of the referring links indicates semantic elements in HTML where the referring links are located and link count per each semantic location you can get the full list of semantic elements here examples: article, section, summary | [optional] 
**referring_links_countries** | **Dict[str, Optional[int]]** | ISO country codes of the referring links indicates ISO country codes of the domains where the referring links are located and the link count per each country | [optional] 

## Example

```python
from dataforseo_client.models.page_summary import PageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PageSummary from a JSON string
page_summary_instance = PageSummary.from_json(json)
# print the JSON string representation of the object
print(PageSummary.to_json())

# convert the object into a dict
page_summary_dict = page_summary_instance.to_dict()
# create an instance of PageSummary from a dict
page_summary_from_dict = PageSummary.from_dict(page_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


