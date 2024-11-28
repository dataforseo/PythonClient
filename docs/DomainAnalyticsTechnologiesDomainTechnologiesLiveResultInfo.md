# DomainAnalyticsTechnologiesDomainTechnologiesLiveResultInfo


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
**country_iso_code** | **str** | domain ISO code ISO code of the country that the target domain is determined to belong to | [optional] 
**language_code** | **str** | domain language code of the language that the target domain is determined to be associated with | [optional] 
**content_language_code** | **str** | content language code of the language that content on the target domain is written in | [optional] 
**phone_numbers** | **List[Optional[str]]** | phone numbers of the target contact phone numbers indicated on the target website | [optional] 
**emails** | **List[Optional[str]]** | emails of the target emails indicated on the target website | [optional] 
**social_graph_urls** | **List[Optional[str]]** | social media links and handles social media URLs detected in the social graphs of the target website | [optional] 
**technologies** | [**TechnologiesInfo**](TechnologiesInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_domain_technologies_live_result_info import DomainAnalyticsTechnologiesDomainTechnologiesLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesDomainTechnologiesLiveResultInfo from a JSON string
domain_analytics_technologies_domain_technologies_live_result_info_instance = DomainAnalyticsTechnologiesDomainTechnologiesLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print(DomainAnalyticsTechnologiesDomainTechnologiesLiveResultInfo.to_json())

# convert the object into a dict
domain_analytics_technologies_domain_technologies_live_result_info_dict = domain_analytics_technologies_domain_technologies_live_result_info_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesDomainTechnologiesLiveResultInfo from a dict
domain_analytics_technologies_domain_technologies_live_result_info_from_dict = DomainAnalyticsTechnologiesDomainTechnologiesLiveResultInfo.from_dict(domain_analytics_technologies_domain_technologies_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


