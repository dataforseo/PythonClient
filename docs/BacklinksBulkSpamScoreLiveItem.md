[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksBulkSpamScoreLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**target** | **str** | domain, subdomain or webpage from a POST array | [optional]
**spam_score** | **int** | average spam score the target learn more about how the metric is calculated | [optional]

## Example

```python
from dataforseo_client.models.backlinks_bulk_spam_score_live_item import BacklinksBulkSpamScoreLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksBulkSpamScoreLiveItem from a JSON string
backlinks_bulk_spam_score_live_item_instance = BacklinksBulkSpamScoreLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksBulkSpamScoreLiveItem.to_json()

# convert the object into a dict
backlinks_bulk_spam_score_live_item_dict = backlinks_bulk_spam_score_live_item_instance.to_dict()
# create an instance of BacklinksBulkSpamScoreLiveItem from a dict
backlinks_bulk_spam_score_live_item_form_dict = backlinks_bulk_spam_score_live_item.from_dict(backlinks_bulk_spam_score_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")