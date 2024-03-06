[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# KeywordsDataGoogleTrendsExploreLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **List[Optional[str]]** | keywords in a POST array | [optional]
**type** | **str** | type of element | [optional]
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional]
**language_code** | **str** | language code in a POST array if there is no data, then the value is null | [optional]
**check_url** | **str** | direct URL to the Google Trends results you can use it to make sure that we provided accurate results | [optional]
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**items_count** | **int** | the number of results returned in the items array | [optional]
**items** | [**List[BaseGoogleTrendsItem]**](BaseGoogleTrendsItem.md) | items on the Google Trends page | [optional]

## Example

```python
from dataforseo_client.models.keywords_data_google_trends_explore_live_result_info import KeywordsDataGoogleTrendsExploreLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordsDataGoogleTrendsExploreLiveResultInfo from a JSON string
keywords_data_google_trends_explore_live_result_info_instance = KeywordsDataGoogleTrendsExploreLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print KeywordsDataGoogleTrendsExploreLiveResultInfo.to_json()

# convert the object into a dict
keywords_data_google_trends_explore_live_result_info_dict = keywords_data_google_trends_explore_live_result_info_instance.to_dict()
# create an instance of KeywordsDataGoogleTrendsExploreLiveResultInfo from a dict
keywords_data_google_trends_explore_live_result_info_form_dict = keywords_data_google_trends_explore_live_result_info.from_dict(keywords_data_google_trends_explore_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")