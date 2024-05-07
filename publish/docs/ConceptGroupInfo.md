# ConceptGroupInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the concept group name | [optional] 
**type** | **str** | type of element | [optional] 

## Example

```python
from dataforseo_client.models.concept_group_info import ConceptGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptGroupInfo from a JSON string
concept_group_info_instance = ConceptGroupInfo.from_json(json)
# print the JSON string representation of the object
print ConceptGroupInfo.to_json()

# convert the object into a dict
concept_group_info_dict = concept_group_info_instance.to_dict()
# create an instance of ConceptGroupInfo from a dict
concept_group_info_form_dict = concept_group_info.from_dict(concept_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


