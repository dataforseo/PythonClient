# BacklinksBulkRanksLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain, subdomain or webpage from a POST array | [optional] 
**rank** | **int** | rank of the target values represent real-time data for the date of the request rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional] 

## Example

```python
from dataforseo_client.models.backlinks_bulk_ranks_live_item import BacklinksBulkRanksLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkRanksLiveItem from a JSON string
backlinks_bulk_ranks_live_item_instance = BacklinksBulkRanksLiveItem.from_json(json)
# print the JSON string representation of the object
print(BacklinksBulkRanksLiveItem.to_json())

# convert the object into a dict
backlinks_bulk_ranks_live_item_dict = backlinks_bulk_ranks_live_item_instance.to_dict()
# create an instance of BacklinksBulkRanksLiveItem from a dict
backlinks_bulk_ranks_live_item_from_dict = BacklinksBulkRanksLiveItem.from_dict(backlinks_bulk_ranks_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


