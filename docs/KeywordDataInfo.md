# KeywordDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**keyword** | **str** | returned keyword idea | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**keyword_info** | [**KeywordInfo**](KeywordInfo.md) |  | [optional] 
**clickstream_keyword_info** | [**ClickstreamKeywordInfo**](ClickstreamKeywordInfo.md) |  | [optional] 
**keyword_properties** | [**KeywordProperties**](KeywordProperties.md) |  | [optional] 
**impressions_info** | [**ImpressionsInfo**](ImpressionsInfo.md) |  | [optional] 
**serp_info** | [**SerpInfo**](SerpInfo.md) |  | [optional] 
**avg_backlinks_info** | [**AvgBacklinksInfo**](AvgBacklinksInfo.md) |  | [optional] 
**search_intent_info** | [**SearchIntentInfo**](SearchIntentInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.keyword_data_info import KeywordDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordDataInfo from a JSON string
keyword_data_info_instance = KeywordDataInfo.from_json(json)
# print the JSON string representation of the object
print KeywordDataInfo.to_json()

# convert the object into a dict
keyword_data_info_dict = keyword_data_info_instance.to_dict()
# create an instance of KeywordDataInfo from a dict
keyword_data_info_form_dict = keyword_data_info.from_dict(keyword_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


