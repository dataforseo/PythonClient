# DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | total number of relevant items in the database | [optional] 
**items_count** | **int** | number of items in the results array | [optional] 
**offset** | **int** | specified offset value | [optional] 
**offset_token** | **str** | token for subsequent requests by specifying the unique offset_token when setting a new task, you will get the subsequent results of the initial task; offset_token values are unique for each subsequent task | [optional] 
**items** | [**List[DomainAnalyticsTechnologiesDomainsByLiveItem]**](DomainAnalyticsTechnologiesDomainsByLiveItem.md) | items array | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_domains_by_html_terms_live_result_info import DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveResultInfo from a JSON string
domain_analytics_technologies_domains_by_html_terms_live_result_info_instance = DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveResultInfo.to_json()

# convert the object into a dict
domain_analytics_technologies_domains_by_html_terms_live_result_info_dict = domain_analytics_technologies_domains_by_html_terms_live_result_info_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveResultInfo from a dict
domain_analytics_technologies_domains_by_html_terms_live_result_info_form_dict = domain_analytics_technologies_domains_by_html_terms_live_result_info.from_dict(domain_analytics_technologies_domains_by_html_terms_live_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


