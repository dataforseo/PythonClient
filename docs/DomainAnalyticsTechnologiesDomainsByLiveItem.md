[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DomainAnalyticsTechnologiesDomainsByLiveItem

items array

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**domain** | **str** | specified domain name | [optional]
**title** | **str** | domain meta title | [optional]
**description** | **str** | domain meta description | [optional]
**meta_keywords** | **List[Optional[str]]** | domain meta keywords | [optional]
**domain_rank** | **str** | backlink rank of the target domain learn more about the metric and how it is calculated in this help center article | [optional]
**last_visited** | **str** | most recent date when our crawler visited the domain in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2022-10-10 12:57:46 +00:00 | [optional]
**country_iso_code** | **str** | domain ISO code ISO code of the country that target domain is determined to belong to | [optional]
**language_code** | **str** | domain language code of the language that target domain is determined to be associated with | [optional]
**content_language_code** | **str** | content language code of the language that content on the target domain is written with | [optional]
**phone_numbers** | **List[Optional[str]]** | phone numbers of the target contact phone numbers indicated on the target website | [optional]
**emails** | **List[Optional[str]]** | emails of the target emails indicated on the target website | [optional]
**social_graph_urls** | **List[Optional[str]]** | social media links and handles social media URLs detected in the social graphs of the target website | [optional]
**technologies** | [**TechnologiesInfo**](TechnologiesInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_domains_by_live_item import DomainAnalyticsTechnologiesDomainsByLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesDomainsByLiveItem from a JSON string
domain_analytics_technologies_domains_by_live_item_instance = DomainAnalyticsTechnologiesDomainsByLiveItem.from_json(json)
# print the JSON string representation of the object
print DomainAnalyticsTechnologiesDomainsByLiveItem.to_json()

# convert the object into a dict
domain_analytics_technologies_domains_by_live_item_dict = domain_analytics_technologies_domains_by_live_item_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesDomainsByLiveItem from a dict
domain_analytics_technologies_domains_by_live_item_form_dict = domain_analytics_technologies_domains_by_live_item.from_dict(domain_analytics_technologies_domains_by_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")