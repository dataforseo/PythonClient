# RankChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**previous_rank_absolute** | **int** | previous absolute rank in SERP indicates previous rank of the element in Google SERP; if this element is new, the value will be null | [optional] 
**is_new** | **bool** | element was previously present in SERP if the value is true, previously collected SERP didn’t contain this element | [optional] 
**is_up** | **bool** | rank of this element went up if the value is true, position of the element in SERP is higher compared to the previous check | [optional] 
**is_down** | **bool** | rank of this element went down if the value is true, position of the element in SERP is lower compared to the previous check | [optional] 

## Example

```python
from dataforseo_client.models.rank_changes import RankChanges

# TODO update the JSON string below
json = "{}"
# create an instance of RankChanges from a JSON string
rank_changes_instance = RankChanges.from_json(json)
# print the JSON string representation of the object
print(RankChanges.to_json())

# convert the object into a dict
rank_changes_dict = rank_changes_instance.to_dict()
# create an instance of RankChanges from a dict
rank_changes_form_dict = rank_changes.from_dict(rank_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


