[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsBulkTrafficEstimationLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**target** | **str** | target domain in a POST array | [optional]
**metrics** | [**Dict[str, BulkMetricsInfo]**](BulkMetricsInfo.md) | traffic data relevant to the specified domain | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_bulk_traffic_estimation_live_item import DataforseoLabsBulkTrafficEstimationLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBulkTrafficEstimationLiveItem from a JSON string
dataforseo_labs_bulk_traffic_estimation_live_item_instance = DataforseoLabsBulkTrafficEstimationLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsBulkTrafficEstimationLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_bulk_traffic_estimation_live_item_dict = dataforseo_labs_bulk_traffic_estimation_live_item_instance.to_dict()
# create an instance of DataforseoLabsBulkTrafficEstimationLiveItem from a dict
dataforseo_labs_bulk_traffic_estimation_live_item_form_dict = dataforseo_labs_bulk_traffic_estimation_live_item.from_dict(dataforseo_labs_bulk_traffic_estimation_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")