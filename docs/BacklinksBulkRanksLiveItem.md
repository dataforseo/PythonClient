[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksBulkRanksLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | domain, subdomain or webpage from a POST array | [optional]
**rank** | **int** | rank of the target rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm learn more about the metric and how it is calculated in this help center article | [optional]

## Example

```python
from dataforseo_client.models.backlinks_bulk_ranks_live_item import BacklinksBulkRanksLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkRanksLiveItem from a JSON string
backlinks_bulk_ranks_live_item_instance = BacklinksBulkRanksLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksBulkRanksLiveItem.to_json()

# convert the object into a dict
backlinks_bulk_ranks_live_item_dict = backlinks_bulk_ranks_live_item_instance.to_dict()
# create an instance of BacklinksBulkRanksLiveItem from a dict
backlinks_bulk_ranks_live_item_form_dict = backlinks_bulk_ranks_live_item.from_dict(backlinks_bulk_ranks_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")