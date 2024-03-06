[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BacklinksTimeseriesNewLostSummaryLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**var_date** | **str** | date and time when the data for the target was stored in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**new_backlinks** | **int** | number of new backlinks number of new backlinks pointing to the target | [optional]
**lost_backlinks** | **int** | number of lost backlinks number of lost backlinks of the target | [optional]
**new_referring_domains** | **int** | number of new referring domains number of new referring domains pointing to the target | [optional]
**lost_referring_domains** | **int** | number of lost referring domains number of lost referring domains of the target | [optional]
**new_referring_main_domains** | **int** | number of new referring main domains number of new referring main domains pointing to the target | [optional]
**lost_referring_main_domains** | **int** | number of lost referring main domains number of lost referring main domains of the target | [optional]

## Example

```python
from dataforseo_client.models.backlinks_timeseries_new_lost_summary_live_item import BacklinksTimeseriesNewLostSummaryLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of BacklinksTimeseriesNewLostSummaryLiveItem from a JSON string
backlinks_timeseries_new_lost_summary_live_item_instance = BacklinksTimeseriesNewLostSummaryLiveItem.from_json(json)
# print the JSON string representation of the object
print BacklinksTimeseriesNewLostSummaryLiveItem.to_json()

# convert the object into a dict
backlinks_timeseries_new_lost_summary_live_item_dict = backlinks_timeseries_new_lost_summary_live_item_instance.to_dict()
# create an instance of BacklinksTimeseriesNewLostSummaryLiveItem from a dict
backlinks_timeseries_new_lost_summary_live_item_form_dict = backlinks_timeseries_new_lost_summary_live_item.from_dict(backlinks_timeseries_new_lost_summary_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")