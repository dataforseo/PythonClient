# DataforseoLabsCompetitorsDomainLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**domain** | **str** | domain name | [optional] 
**avg_position** | **float** | average position of the domain in SERP Note: average position is calculated for intersected keywords only; the value for a given domain may differ when combined with different target websites | [optional] 
**sum_position** | **int** | sum of all domain positions in SERP Note: average position is calculated for intersected keywords only; the value for a given domain may differ when combined with different target websites | [optional] 
**intersections** | **int** | number of intersecting keywords | [optional] 
**full_domain_metrics** | [**Dict[str, MetricsInfo]**](MetricsInfo.md) | metrics for all keywords of the domain full overview of ranking and traffic data relevant to all keywords that the provided domain is ranking for | [optional] 
**metrics** | [**Dict[str, MetricsInfo]**](MetricsInfo.md) | metrics for intersecting keywords ranking and traffic data relevant to the keywords that the provided domain shares with the target domain note: in this array ranking and traffic data is provided for the target considering the keywords target shares in search with the competitor’s domain | [optional] 
**competitor_metrics** | [**Dict[str, MetricsInfo]**](MetricsInfo.md) | metrics for intersecting keywords ranking and traffic data relevant to the keywords that the provided domain shares with the target domain note: in this array ranking and traffic data is provided for the returned competitor’s domain | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_competitors_domain_live_item import DataforseoLabsCompetitorsDomainLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsCompetitorsDomainLiveItem from a JSON string
dataforseo_labs_competitors_domain_live_item_instance = DataforseoLabsCompetitorsDomainLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsCompetitorsDomainLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_competitors_domain_live_item_dict = dataforseo_labs_competitors_domain_live_item_instance.to_dict()
# create an instance of DataforseoLabsCompetitorsDomainLiveItem from a dict
dataforseo_labs_competitors_domain_live_item_form_dict = dataforseo_labs_competitors_domain_live_item.from_dict(dataforseo_labs_competitors_domain_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


