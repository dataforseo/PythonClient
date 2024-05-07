# InterestsComparison


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AbsoluteItems]**](AbsoluteItems.md) | contains keyword popularity and related data | [optional] 
**absolute_items** | [**List[AbsoluteItems]**](AbsoluteItems.md) | keyword popularity rates across all locations values in this array represent percentages relative to the maximum value across all locations | [optional] 

## Example

```python
from dataforseo_client.models.interests_comparison import InterestsComparison

# TODO update the JSON string below
json = "{}"
# create an instance of InterestsComparison from a JSON string
interests_comparison_instance = InterestsComparison.from_json(json)
# print the JSON string representation of the object
print InterestsComparison.to_json()

# convert the object into a dict
interests_comparison_dict = interests_comparison_instance.to_dict()
# create an instance of InterestsComparison from a dict
interests_comparison_form_dict = interests_comparison.from_dict(interests_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


