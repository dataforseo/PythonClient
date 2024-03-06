[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsBingRankedKeywordsLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**target** | **str** | target domain in a POST array | [optional]
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional]
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional]
**total_count** | **int** | total number of results in our database relevant to your request | [optional]
**items_count** | **int** | the number of results returned in the items array | [optional]
**metrics** | [**Dict[str, MetricsInfo]**](MetricsInfo.md) | ranking data relevant to the specified domain ranking data is provided by the rank_group parameters that show the result’s rank considering only equivalent SERP elements | [optional]
**metrics_absolute** | [**Dict[str, MetricsInfo]**](MetricsInfo.md) | ranking data relevant to the specified domain ranking data is provided by the rank_absolute parameters that indicate the result’s position among all SERP elements | [optional]
**items** | [**List[DataforseoLabsBingRankedKeywordsLiveItem]**](DataforseoLabsBingRankedKeywordsLiveItem.md) | contains ranked keywords and related data | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_bing_ranked_keywords_live_result_info import DataforseoLabsBingRankedKeywordsLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsBingRankedKeywordsLiveResultInfo from a JSON string
dataforseo_labs_bing_ranked_keywords_live_result_info_instance = DataforseoLabsBingRankedKeywordsLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsBingRankedKeywordsLiveResultInfo.to_json()

# convert the object into a dict
dataforseo_labs_bing_ranked_keywords_live_result_info_dict = dataforseo_labs_bing_ranked_keywords_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsBingRankedKeywordsLiveResultInfo from a dict
dataforseo_labs_bing_ranked_keywords_live_result_info_form_dict = dataforseo_labs_bing_ranked_keywords_live_result_info.from_dict(dataforseo_labs_bing_ranked_keywords_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")