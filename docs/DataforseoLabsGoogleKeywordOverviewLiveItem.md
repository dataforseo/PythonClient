# DataforseoLabsGoogleKeywordOverviewLiveItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword** | **str** | keyword keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character) | [optional] 
**location_code** | **int** | location code in a POST array if there is no data, then the value is null | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**search_partners** | **bool** | indicates data for Google and partner sites if true, the results are returned for owned, operated, and syndicated networks across Google and partner sites that host Google search; if false, the results are returned for Google search sites only | [optional] 
**keyword_info** | [**KeywordInfo**](KeywordInfo.md) |  | [optional] 
**keyword_info_normalized_with_bing** | [**KeywordInfoNormalizedWithInfo**](KeywordInfoNormalizedWithInfo.md) |  | [optional] 
**keyword_info_normalized_with_clickstream** | [**KeywordInfoNormalizedWithInfo**](KeywordInfoNormalizedWithInfo.md) |  | [optional] 
**clickstream_keyword_info** | **object** |  | [optional] 
**keyword_properties** | [**KeywordProperties**](KeywordProperties.md) |  | [optional] 
**serp_info** | [**SerpInfo**](SerpInfo.md) |  | [optional] 
**avg_backlinks_info** | [**AvgBacklinksInfo**](AvgBacklinksInfo.md) |  | [optional] 
**search_intent_info** | [**SearchIntentInfo**](SearchIntentInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_keyword_overview_live_item import DataforseoLabsGoogleKeywordOverviewLiveItem

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleKeywordOverviewLiveItem from a JSON string
dataforseo_labs_google_keyword_overview_live_item_instance = DataforseoLabsGoogleKeywordOverviewLiveItem.from_json(json)
# print the JSON string representation of the object
print(DataforseoLabsGoogleKeywordOverviewLiveItem.to_json())

# convert the object into a dict
dataforseo_labs_google_keyword_overview_live_item_dict = dataforseo_labs_google_keyword_overview_live_item_instance.to_dict()
# create an instance of DataforseoLabsGoogleKeywordOverviewLiveItem from a dict
dataforseo_labs_google_keyword_overview_live_item_from_dict = DataforseoLabsGoogleKeywordOverviewLiveItem.from_dict(dataforseo_labs_google_keyword_overview_live_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


