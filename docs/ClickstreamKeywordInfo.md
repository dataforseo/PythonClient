# ClickstreamKeywordInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_volume** | **int** | monthly average clickstream search volume rate | [optional] 
**last_updated_time** | **str** | date and time when the clickstream dataset was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” | [optional] 
**gender_distribution** | **Dict[str, Optional[int]]** | distribution of estimated clickstream-based metrics by gender learn more about how the metric is calculated in this help center article | [optional] 
**age_distribution** | **Dict[str, Optional[int]]** | distribution of clickstream-based metrics by age learn more about how the metric is calculated in this help center article | [optional] 
**monthly_searches** | [**List[MonthlySearches]**](MonthlySearches.md) | monthly clickstream search volume rates array of objects with clickstream search volume rates in a certain month of a year | [optional] 

## Example

```python
from dataforseo_client.models.clickstream_keyword_info import ClickstreamKeywordInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClickstreamKeywordInfo from a JSON string
clickstream_keyword_info_instance = ClickstreamKeywordInfo.from_json(json)
# print the JSON string representation of the object
print ClickstreamKeywordInfo.to_json()

# convert the object into a dict
clickstream_keyword_info_dict = clickstream_keyword_info_instance.to_dict()
# create an instance of ClickstreamKeywordInfo from a dict
clickstream_keyword_info_form_dict = clickstream_keyword_info.from_dict(clickstream_keyword_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


