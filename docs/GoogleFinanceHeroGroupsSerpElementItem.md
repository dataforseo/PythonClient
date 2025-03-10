# GoogleFinanceHeroGroupsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**markets** | [**List[GoogleFinanceMarketsInfo]**](GoogleFinanceMarketsInfo.md) | financial markets data array of items containing market indexes and other financial information related to these indexes | [optional] 

## Example

```python
from dataforseo_client.models.google_finance_hero_groups_serp_element_item import GoogleFinanceHeroGroupsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleFinanceHeroGroupsSerpElementItem from a JSON string
google_finance_hero_groups_serp_element_item_instance = GoogleFinanceHeroGroupsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(GoogleFinanceHeroGroupsSerpElementItem.to_json())

# convert the object into a dict
google_finance_hero_groups_serp_element_item_dict = google_finance_hero_groups_serp_element_item_instance.to_dict()
# create an instance of GoogleFinanceHeroGroupsSerpElementItem from a dict
google_finance_hero_groups_serp_element_item_from_dict = GoogleFinanceHeroGroupsSerpElementItem.from_dict(google_finance_hero_groups_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


