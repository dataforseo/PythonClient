[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsGoogleSearchIntentLiveItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | target keyword in a POST array | [optional]
**keyword_intent** | [**KeywordIntentInfo**](KeywordIntentInfo.md) |  | [optional]
**secondary_keyword_intents** | [**List[KeywordIntentInfo]**](KeywordIntentInfo.md) | contains objects with other possible search intents for the specified keyword | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_search_intent_live_item import DataforseoLabsGoogleSearchIntentLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleSearchIntentLiveItem from a JSON string
dataforseo_labs_google_search_intent_live_item_instance = DataforseoLabsGoogleSearchIntentLiveItem.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleSearchIntentLiveItem.to_json()

# convert the object into a dict
dataforseo_labs_google_search_intent_live_item_dict = dataforseo_labs_google_search_intent_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleSearchIntentLiveItem from a dict
dataforseo_labs_google_search_intent_live_item_form_dict = dataforseo_labs_google_search_intent_live_item.from_dict(dataforseo_labs_google_search_intent_live_item_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")