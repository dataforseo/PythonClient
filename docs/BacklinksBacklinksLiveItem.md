# BacklinksBacklinksLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**domain_from** | **str** | domain referring to the target domain or webpage | [optional] 
**url_from** | **str** | URL of the page where the backlink is found | [optional] 
**url_from_https** | **bool** | indicates whether the referring URL is secured with HTTPS if true, the referring URL is secured with HTTPS | [optional] 
**domain_to** | **str** | domain the backlink is pointing to | [optional] 
**url_to** | **str** | URL the backlink is pointing to | [optional] 
**url_to_https** | **bool** | indicates if the URL the backlink is pointing to is secured with HTTPS if true, the URL is secured with HTTPS | [optional] 
**tld_from** | **str** | top-level domain of the referring URL | [optional] 
**is_new** | **bool** | indicates whether the backlink is new if true, the backlink was found on the page last time our crawler visited it | [optional] 
**is_lost** | **bool** | indicates whether the backlink was removed if true, the backlink or the entire page was removed | [optional] 
**backlink_spam_score** | **int** | spam score of the backlink learn more about how the metric is calculated on this help center page | [optional] 
**rank** | **int** | backlink rank rank that the given backlink passes to the target rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional] 
**page_from_rank** | **int** | page rank of the referring page page_from_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional] 
**domain_from_rank** | **int** | domain rank of the referring domain domain_from_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional] 
**domain_from_platform_type** | **List[Optional[str]]** | platform types of the referring domain example: \&quot;cms\&quot;, \&quot;blogs\&quot; | [optional] 
**domain_from_is_ip** | **bool** | indicates if the domain is IP if true, the domain functions as an IP address and does not have a domain name | [optional] 
**domain_from_ip** | **str** | IP address of the referring domain | [optional] 
**domain_from_country** | **str** | ISO country code of the referring domain | [optional] 
**page_from_external_links** | **int** | number of external links found on the referring page | [optional] 
**page_from_internal_links** | **int** | number of internal links found on the referring page | [optional] 
**page_from_size** | **int** | size of the referring page, in bytes example: 63357 | [optional] 
**page_from_encoding** | **str** | character encoding of the referring page example: utf-8 | [optional] 
**page_from_language** | **str** | language of the referring page in ISO 639-1 format example: en | [optional] 
**page_from_title** | **str** | title of the referring page | [optional] 
**page_from_status_code** | **int** | HTTP status code returned by the referring page example: 200 | [optional] 
**first_seen** | **str** | date and time when our crawler found the backlink for the first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**prev_seen** | **str** | previous to the most recent date when our crawler visited the backlink in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**last_seen** | **str** | most recent date when our crawler visited the backlink in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**item_type** | **str** | link type possible values: anchor, image, meta, canonical, alternate, redirect | [optional] 
**attributes** | **List[Optional[str]]** | link attributes of the referring links example: nofollow | [optional] 
**dofollow** | **bool** | indicates whether the backlink is dofollow if false, the backlink is nofollow | [optional] 
**original** | **bool** | indicates whether the backlink was present on the referring page when our crawler first visited it | [optional] 
**alt** | **str** | alternative text of the image this field will be null if backlink type is not image | [optional] 
**image_url** | **str** | URL of the image the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) | [optional] 
**anchor** | **str** | anchor text of the backlink | [optional] 
**text_pre** | **str** | snippet before the anchor text | [optional] 
**text_post** | **str** | snippet after the anchor text | [optional] 
**semantic_location** | **str** | indicates semantic element in HTML where the backlink is found you can get the full list of semantic elements here examples: article, section, summary | [optional] 
**links_count** | **int** | number of identical backlinks found on the referring page | [optional] 
**group_count** | **int** | indicates total number of backlinks from this domain for example, if mode is set to one_per_domain, this field will indicate the total number of backlinks coming from this domain | [optional] 
**is_broken** | **bool** | indicates whether the backlink is broken if true, the backlink is pointing to a page responding with a 4xx or 5xx status code | [optional] 
**url_to_status_code** | **int** | status code of the referenced page if the value is null, our crawler hasn’t yet visited the webpage the link is pointing to example: 200 | [optional] 
**url_to_spam_score** | **int** | spam score of the referenced page if the value is null, our crawler hasn’t yet visited the webpage the link is pointing to; learn more about how the metric is calculated on this help center page | [optional] 
**url_to_redirect_target** | **str** | target url of the redirect target page the redirect is pointing to | [optional] 
**ranked_keywords_info** | [**RankedKeywordsInfo**](RankedKeywordsInfo.md) |  | [optional] 
**is_indirect_link** | **bool** | indicates whether the backlink is an indirect link if true, the backlink is an indirect link pointing to a page that either redirects to url_to, or points to a canonical page | [optional] 
**indirect_link_path** | [**List[Redirect]**](Redirect.md) | indirect link path indicates a URL or a sequence of URLs that lead to url_to | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_backlinks_live_item import BacklinksBacklinksLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBacklinksLiveItem from a JSON string
backlinks_backlinks_live_item_instance = BacklinksBacklinksLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksBacklinksLiveItem.to_json()

# convert the object into a dict
backlinks_backlinks_live_item_dict = backlinks_backlinks_live_item_instance.to_dict()
# create an instance of BacklinksBacklinksLiveItem from a dict
backlinks_backlinks_live_item_form_dict = backlinks_backlinks_live_item.from_dict(backlinks_backlinks_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


