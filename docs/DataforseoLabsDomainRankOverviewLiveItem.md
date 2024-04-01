# DataforseoLabsDomainRankOverviewLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**metrics** | [**Dict[str, MetricsInfo]**](MetricsInfo.md) | ranking data relevant to the specified domain | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_domain_rank_overview_live_item import DataforseoLabsDomainRankOverviewLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsDomainRankOverviewLiveItem from a JSON string
dataforseo_labs_domain_rank_overview_live_item_instance = DataforseoLabsDomainRankOverviewLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsDomainRankOverviewLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_domain_rank_overview_live_item_dict = dataforseo_labs_domain_rank_overview_live_item_instance.to_dict()
# create an instance of DataforseoLabsDomainRankOverviewLiveItem from a dict
dataforseo_labs_domain_rank_overview_live_item_form_dict = dataforseo_labs_domain_rank_overview_live_item.from_dict(dataforseo_labs_domain_rank_overview_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


