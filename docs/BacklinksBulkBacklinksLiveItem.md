[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

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
print BacklinksBulkBacklinksLiveItem.to_json()

# convert the object into a dict
backlinks_bulk_backlinks_live_item_dict = backlinks_bulk_backlinks_live_item_instance.to_dict()
# create an instance of BacklinksBulkBacklinksLiveItem from a dict
backlinks_bulk_backlinks_live_item_form_dict = backlinks_bulk_backlinks_live_item.from_dict(backlinks_bulk_backlinks_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")