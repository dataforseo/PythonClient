[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsGoogleKeywordIdeasLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**seed_keywords** | **List[Optional[str]]** | keywords in a POST array keywords are returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) | [optional]
**location_code** | **int** | location code in a POST array | [optional]
**language_code** | **str** | language code in a POST array | [optional]
**total_count** | **int** | total number of results relevant to your request in our database | [optional]
**items_count** | **int** | number of results returned in the items array | [optional]
**offset** | **int** | current offset value | [optional]
**offset_token** | **str** | offset token for subsequent requests you can use the string provided in this field to get the subsequent results of the initial task; note: offset_token values are unique for each subsequent task | [optional]
**items** | [**List[KeywordDataInfo]**](KeywordDataInfo.md) | contains keyword ideas and related data | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_keyword_ideas_live_result_info import DataforseoLabsGoogleKeywordIdeasLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleKeywordIdeasLiveResultInfo from a JSON string
dataforseo_labs_google_keyword_ideas_live_result_info_instance = DataforseoLabsGoogleKeywordIdeasLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleKeywordIdeasLiveResultInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_keyword_ideas_live_result_info_dict = dataforseo_labs_google_keyword_ideas_live_result_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleKeywordIdeasLiveResultInfo from a dict
dataforseo_labs_google_keyword_ideas_live_result_info_form_dict = dataforseo_labs_google_keyword_ideas_live_result_info.from_dict(dataforseo_labs_google_keyword_ideas_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")