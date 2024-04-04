# MonthlySearches


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** | year | [optional] 
**month** | **int** | month | [optional] 
**search_volume** | **int** | monthly average search volume rate | [optional] 

## Example

```python
from dataforseo_client.models.monthly_searches import MonthlySearches

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlySearches from a JSON string
monthly_searches_instance = MonthlySearches.from_json(json)
# print the JSON string representation of the object
print MonthlySearches.to_json()

# convert the object into a dict
monthly_searches_dict = monthly_searches_instance.to_dict()
# create an instance of MonthlySearches from a dict
monthly_searches_form_dict = monthly_searches.from_dict(monthly_searches_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


