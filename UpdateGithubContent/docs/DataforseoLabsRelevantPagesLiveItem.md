# DataforseoLabsRelevantPagesLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**page_address** | **str** | absolute URL of the relevant page | [optional] 
**metrics** | [**Dict[str, MetricsInfo]**](MetricsInfo.md) | rankings and traffic metrics for the relevant page | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_relevant_pages_live_item import DataforseoLabsRelevantPagesLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsRelevantPagesLiveItem from a JSON string
dataforseo_labs_relevant_pages_live_item_instance = DataforseoLabsRelevantPagesLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsRelevantPagesLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_relevant_pages_live_item_dict = dataforseo_labs_relevant_pages_live_item_instance.to_dict()
# create an instance of DataforseoLabsRelevantPagesLiveItem from a dict
dataforseo_labs_relevant_pages_live_item_form_dict = dataforseo_labs_relevant_pages_live_item.from_dict(dataforseo_labs_relevant_pages_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


