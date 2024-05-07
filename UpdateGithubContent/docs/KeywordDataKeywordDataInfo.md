# KeywordDataKeywordDataInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type search engine type specified in a POST request; for this endpoint, the field equals bing | [optional] 
**keyword** | **str** | returned keyword | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**keyword_info** | [**KeywordInfo**](KeywordInfo.md) |  | [optional] 
**keyword_properties** | [**KeywordProperties**](KeywordProperties.md) |  | [optional] 
**serp_info** | [**SerpInfo**](SerpInfo.md) |  | [optional] 
**avg_backlinks_info** | [**AvgBacklinksInfo**](AvgBacklinksInfo.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.keyword_data_keyword_data_info import KeywordDataKeywordDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordDataKeywordDataInfo from a JSON string
keyword_data_keyword_data_info_instance = KeywordDataKeywordDataInfo.from_json(json)
# print the JSON string representation of the object
print KeywordDataKeywordDataInfo.to_json()

# convert the object into a dict
keyword_data_keyword_data_info_dict = keyword_data_keyword_data_info_instance.to_dict()
# create an instance of KeywordDataKeywordDataInfo from a dict
keyword_data_keyword_data_info_form_dict = keyword_data_keyword_data_info.from_dict(keyword_data_keyword_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


