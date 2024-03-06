[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksBulkBacklinksLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items_count** | **int** | the number of results returned in the items array | [optional]
**items** | [**List[BacklinksBulkBacklinksLiveItem]**](BacklinksBulkBacklinksLiveItem.md) | contains relevant backlink data | [optional]

## Example

```python
from dataforseo_client.models.backlinks_bulk_backlinks_live_result_info import BacklinksBulkBacklinksLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkBacklinksLiveResultInfo from a JSON string
backlinks_bulk_backlinks_live_result_info_instance = BacklinksBulkBacklinksLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print BacklinksBulkBacklinksLiveResultInfo.to_json()

# convert the object into a dict
backlinks_bulk_backlinks_live_result_info_dict = backlinks_bulk_backlinks_live_result_info_instance.to_dict()
# create an instance of BacklinksBulkBacklinksLiveResultInfo from a dict
backlinks_bulk_backlinks_live_result_info_form_dict = backlinks_bulk_backlinks_live_result_info.from_dict(backlinks_bulk_backlinks_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")