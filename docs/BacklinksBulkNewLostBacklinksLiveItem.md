# BacklinksBulkNewLostBacklinksLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain, subdomain or webpage from a POST array | [optional] 
**new_backlinks** | **int** | number of new backlinks number of new backlinks pointing to the target | [optional] 
**lost_backlinks** | **int** | number of lost backlinks number of lost backlinks of the target | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_bulk_new_lost_backlinks_live_item import BacklinksBulkNewLostBacklinksLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkNewLostBacklinksLiveItem from a JSON string
backlinks_bulk_new_lost_backlinks_live_item_instance = BacklinksBulkNewLostBacklinksLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksBulkNewLostBacklinksLiveItem.to_json()

# convert the object into a dict
backlinks_bulk_new_lost_backlinks_live_item_dict = backlinks_bulk_new_lost_backlinks_live_item_instance.to_dict()
# create an instance of BacklinksBulkNewLostBacklinksLiveItem from a dict
backlinks_bulk_new_lost_backlinks_live_item_form_dict = backlinks_bulk_new_lost_backlinks_live_item.from_dict(backlinks_bulk_new_lost_backlinks_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


