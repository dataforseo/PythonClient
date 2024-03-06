[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ConnotationTypeInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positive** | **float** | positive connotation | [optional]
**negative** | **float** | negative connotation | [optional]
**neutral** | **float** | neutral connotation | [optional]

## Example

```python
from dataforseo_client.models.connotation_type_info import ConnotationTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ConnotationTypeInfo from a JSON string
connotation_type_info_instance = ConnotationTypeInfo.from_json(json)
# print the JSON string representation of the object
print ConnotationTypeInfo.to_json()

# convert the object into a dict
connotation_type_info_dict = connotation_type_info_instance.to_dict()
# create an instance of ConnotationTypeInfo from a dict
connotation_type_info_form_dict = connotation_type_info.from_dict(connotation_type_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")