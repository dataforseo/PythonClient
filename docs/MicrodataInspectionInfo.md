[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# MicrodataInspectionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | **List[Optional[str]]** | parent microdata types for a full list of available types, please visit schema.org | [optional]
**fields** | [**List[MicrodataFieldsInfo]**](MicrodataFieldsInfo.md) | microdata fields an array of objects containing data fields related to the certain microdata type | [optional]

## Example

```python
from dataforseo_client.models.microdata_inspection_info import MicrodataInspectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodataInspectionInfo from a JSON string
microdata_inspection_info_instance = MicrodataInspectionInfo.from_json(json)
# print the JSON string representation of the object
print MicrodataInspectionInfo.to_json()

# convert the object into a dict
microdata_inspection_info_dict = microdata_inspection_info_instance.to_dict()
# create an instance of MicrodataInspectionInfo from a dict
microdata_inspection_info_form_dict = microdata_inspection_info.from_dict(microdata_inspection_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")