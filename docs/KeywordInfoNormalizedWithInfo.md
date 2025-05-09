# KeywordInfoNormalizedWithInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_updated_time** | **str** | date and time when the dataset was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**search_volume** | **str** | current search volume rate of a keyword | [optional] 
**is_normalized** | **str** | keyword info is normalized if true, values are normalized with Bing data | [optional] 
**monthly_searches** | [**List[MonthlySearches]**](MonthlySearches.md) | monthly search volume rates array of objects with search volume rates in a certain month of a year | [optional] 

## Example

```python
from dataforseo_client.models.keyword_info_normalized_with_info import KeywordInfoNormalizedWithInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KeywordInfoNormalizedWithInfo from a JSON string
keyword_info_normalized_with_info_instance = KeywordInfoNormalizedWithInfo.from_json(json)
# print the JSON string representation of the object
print(KeywordInfoNormalizedWithInfo.to_json())

# convert the object into a dict
keyword_info_normalized_with_info_dict = keyword_info_normalized_with_info_instance.to_dict()
# create an instance of KeywordInfoNormalizedWithInfo from a dict
keyword_info_normalized_with_info_from_dict = KeywordInfoNormalizedWithInfo.from_dict(keyword_info_normalized_with_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


