[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsGoogleRankedKeywordsLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional]
**keyword_data** | [**KeywordData**](KeywordData.md) |  | [optional]
**ranked_serp_element** | [**RankedSerpElement**](RankedSerpElement.md) |  | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_ranked_keywords_live_item import DataforseoLabsGoogleRankedKeywordsLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleRankedKeywordsLiveItem from a JSON string
dataforseo_labs_google_ranked_keywords_live_item_instance = DataforseoLabsGoogleRankedKeywordsLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleRankedKeywordsLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_google_ranked_keywords_live_item_dict = dataforseo_labs_google_ranked_keywords_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleRankedKeywordsLiveItem from a dict
dataforseo_labs_google_ranked_keywords_live_item_form_dict = dataforseo_labs_google_ranked_keywords_live_item.from_dict(dataforseo_labs_google_ranked_keywords_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")