[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsBingRelevantPagesLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**target** | **str** | target domain in a POST array | [optional]
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional]
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional]
**total_count** | **int** | total amount of results in our database relevant to your request | [optional]
**items_count** | **int** | the number of results returned in the items array | [optional]
**items** | [**List[DataforseoLabsRelevantPagesLiveItem]**](DataforseoLabsRelevantPagesLiveItem.md) | relevant pages and related data | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_bing_relevant_pages_live_result_info import DataforseoLabsBingRelevantPagesLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBingRelevantPagesLiveResultInfo from a JSON string
dataforseo_labs_bing_relevant_pages_live_result_info_instance = DataforseoLabsBingRelevantPagesLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsBingRelevantPagesLiveResultInfo.to_json()

# convert the object into a dict
dataforseo_labs_bing_relevant_pages_live_result_info_dict = dataforseo_labs_bing_relevant_pages_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsBingRelevantPagesLiveResultInfo from a dict
dataforseo_labs_bing_relevant_pages_live_result_info_form_dict = dataforseo_labs_bing_relevant_pages_live_result_info.from_dict(dataforseo_labs_bing_relevant_pages_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")