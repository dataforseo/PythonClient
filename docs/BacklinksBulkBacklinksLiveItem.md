# BacklinksBulkBacklinksLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain, subdomain or webpage from a POST array | [optional] 
**backlinks** | **int** | number of backlinks pointing to the target | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_bulk_backlinks_live_item import BacklinksBulkBacklinksLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkBacklinksLiveItem from a JSON string
backlinks_bulk_backlinks_live_item_instance = BacklinksBulkBacklinksLiveItem.from_json(json)
# print the JSON string representation of the object
print(BacklinksBulkBacklinksLiveItem.to_json())

# convert the object into a dict
backlinks_bulk_backlinks_live_item_dict = backlinks_bulk_backlinks_live_item_instance.to_dict()
# create an instance of BacklinksBulkBacklinksLiveItem from a dict
backlinks_bulk_backlinks_live_item_from_dict = BacklinksBulkBacklinksLiveItem.from_dict(backlinks_bulk_backlinks_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


