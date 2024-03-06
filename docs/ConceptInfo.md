[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ConceptInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the concept name for the keyword in the concept_group | [optional]
**concept_group** | [**ConceptGroupInfo**](ConceptGroupInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.concept_info import ConceptInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConceptInfo from a JSON string
concept_info_instance = ConceptInfo.from_json(json)
# print the JSON string representation of the object
print ConceptInfo.to_json()

# convert the object into a dict
concept_info_dict = concept_info_instance.to_dict()
# create an instance of ConceptInfo from a dict
concept_info_form_dict = concept_info.from_dict(concept_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")