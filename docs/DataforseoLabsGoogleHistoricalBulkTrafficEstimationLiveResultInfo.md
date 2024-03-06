[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional]
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional]
**total_count** | **int** | total amount of results in our database relevant to your request | [optional]
**items_count** | **int** | the number of results returned in the items array | [optional]
**items** | [**List[DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveItem]**](DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveItem.md) | array of items with relevant traffic estimation data | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_historical_bulk_traffic_estimation_live_result_info import DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveResultInfo from a JSON string
dataforseo_labs_google_historical_bulk_traffic_estimation_live_result_info_instance = DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveResultInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_historical_bulk_traffic_estimation_live_result_info_dict = dataforseo_labs_google_historical_bulk_traffic_estimation_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveResultInfo from a dict
dataforseo_labs_google_historical_bulk_traffic_estimation_live_result_info_form_dict = dataforseo_labs_google_historical_bulk_traffic_estimation_live_result_info.from_dict(dataforseo_labs_google_historical_bulk_traffic_estimation_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")