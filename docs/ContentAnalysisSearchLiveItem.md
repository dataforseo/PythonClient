[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ContentAnalysisSearchLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**url** | **str** | URL where the citation was found | [optional]
**domain** | **str** | domain name | [optional]
**main_domain** | **str** | main domain | [optional]
**url_rank** | **int** | rank of the url this value is based on backlink data for the given URL from DataForSEO Backlink Index; url_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional]
**spam_score** | **str** | backlink spam score of the url this value is based on backlink data for the given URL from DataForSEO Backlink Index; learn more about how the metric is calculated on this help center page | [optional]
**domain_rank** | **str** | rank of the domain this value is based on backlink data for the given domain from DataForSEO Backlink Index; domain_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional]
**fetch_time** | **str** | date and time when our crawler visited the page in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59 +00:00 | [optional]
**country** | **str** | country code of the domain registration to obtain a full list of available countries, refer to the Locations endpoint | [optional]
**language** | **str** | main language of the domain to obtain a full list of available languages, refer to the Languages endpoint | [optional]
**score** | **str** | citation prominence score this value is based on url_rank, domain_rank, keyword presence in title, main_title, url, snippet the higher the score, the more value the related citation has | [optional]
**page_category** | **List[int]** | contains all relevant page categories product and service categories relevant for the page to obtain a full list of available categories, refer to the Categories endpoint | [optional]
**page_types** | **List[str]** | page types | [optional]
**ratings** | **object** | ratings found on the page all ratings found on the page based on microdata | [optional]
**social_metrics** | [**List[SocialMetricsInfo]**](SocialMetricsInfo.md) | social media engagement metrics data on social media interactions associated with the content based on website embeds developed and supported by social media platforms | [optional]
**content_info** | [**AnalysisContentInfo**](AnalysisContentInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.content_analysis_search_live_item import ContentAnalysisSearchLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisSearchLiveItem from a JSON string
content_analysis_search_live_item_instance = ContentAnalysisSearchLiveItem.from_json(json)
# print the JSON string representation of the object
print ContentAnalysisSearchLiveItem.to_json()

# convert the object into a dict
content_analysis_search_live_item_dict = content_analysis_search_live_item_instance.to_dict()
# create an instance of ContentAnalysisSearchLiveItem from a dict
content_analysis_search_live_item_form_dict = content_analysis_search_live_item.from_dict(content_analysis_search_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")