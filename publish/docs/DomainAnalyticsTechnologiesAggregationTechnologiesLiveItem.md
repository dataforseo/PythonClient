# DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem

items array

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**group** | **str** | technology group id | [optional] 
**category** | **str** | technology category id | [optional] 
**technology** | **str** | technology name | [optional] 
**groups_count** | **int** | technology groups count number of domains that match the parameters you specified and are using technologies from the indicated group | [optional] 
**categories_count** | **int** | technology categories count number of domains that match the parameters you specified and are using technologies from the indicated category | [optional] 
**technologies_count** | **int** | technologies count number of domains that match the parameters you specified and are using the indicated technology | [optional] 

## Example

```python
from dataforseo_client.models.domain_analytics_technologies_aggregation_technologies_live_item import DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem from a JSON string
domain_analytics_technologies_aggregation_technologies_live_item_instance = DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem.from_json(json)
# print the JSON string representation of the object
print DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem.to_json()

# convert the object into a dict
domain_analytics_technologies_aggregation_technologies_live_item_dict = domain_analytics_technologies_aggregation_technologies_live_item_instance.to_dict()
# create an instance of DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem from a dict
domain_analytics_technologies_aggregation_technologies_live_item_form_dict = domain_analytics_technologies_aggregation_technologies_live_item.from_dict(domain_analytics_technologies_aggregation_technologies_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


