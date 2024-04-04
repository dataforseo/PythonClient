# DomainAnalyticsTechnologiesTechnologyStatsLiveItem

items array

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**var_date** | **str** | date for which the data is provided | [optional] 
**domains_count** | **int** | number of domains that use the specified technology | [optional] 
**countries** | **Dict[str, Optional[int]]** | distribution of websites by country contains country codes and number of websites per country | [optional] 
**languages** | **Dict[str, Optional[int]]** | distribution of websites by language contains language codes and number of websites per language | [optional] 
**domains_rank** | **Dict[str, Optional[int]]** | distribution of websites by backlink rank contains domain rank ranges and number of websites per range learn more about rank and how it is calculated in this help center article | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_technology_stats_live_item import DomainAnalyticsTechnologiesTechnologyStatsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesTechnologyStatsLiveItem from a JSON string
domain_analytics_technologies_technology_stats_live_item_instance = DomainAnalyticsTechnologiesTechnologyStatsLiveItem.from_json(json)
# print the JSON string representation of the object
print DomainAnalyticsTechnologiesTechnologyStatsLiveItem.to_json()

# convert the object into a dict
domain_analytics_technologies_technology_stats_live_item_dict = domain_analytics_technologies_technology_stats_live_item_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesTechnologyStatsLiveItem from a dict
domain_analytics_technologies_technology_stats_live_item_form_dict = domain_analytics_technologies_technology_stats_live_item.from_dict(domain_analytics_technologies_technology_stats_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


