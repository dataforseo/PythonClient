# SpellInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword obtained as a result of search engine autocorrection  the results will be provided for the corrected keyword | [optional] 
**type** | **str** | type of autocorrection  possible values:  did_you_mean, showing_results_for, no_results_found_for, including_results_for  note: Yahoo and Yandex support only the following autocorrection type:  including_results_for | [optional] 

## Example

```python
from dataforseo_client.models.spell_info import SpellInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SpellInfo from a JSON string
spell_info_instance = SpellInfo.from_json(json)
# print the JSON string representation of the object
print SpellInfo.to_json()

# convert the object into a dict
spell_info_dict = spell_info_instance.to_dict()
# create an instance of SpellInfo from a dict
spell_info_form_dict = spell_info.from_dict(spell_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


