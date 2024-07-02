# DataforseoLabsSubdomainsLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**subdomain** | **str** | returned subdomain | [optional] 
**metrics** | [**Dict[str, DataforseoLabsMetricsInfo]**](DataforseoLabsMetricsInfo.md) | ranking data relevant to subdomain | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_subdomains_live_item import DataforseoLabsSubdomainsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsSubdomainsLiveItem from a JSON string
dataforseo_labs_subdomains_live_item_instance = DataforseoLabsSubdomainsLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsSubdomainsLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_subdomains_live_item_dict = dataforseo_labs_subdomains_live_item_instance.to_dict()
# create an instance of DataforseoLabsSubdomainsLiveItem from a dict
dataforseo_labs_subdomains_live_item_form_dict = dataforseo_labs_subdomains_live_item.from_dict(dataforseo_labs_subdomains_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


