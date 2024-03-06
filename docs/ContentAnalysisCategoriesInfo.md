[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# ContentAnalysisCategoriesInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **List[Optional[int]]** |  | [optional]
**count** | **int** |  | [optional]

## Example

```python
from dataforseo_client.models.content_analysis_categories_info import ContentAnalysisCategoriesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentAnalysisCategoriesInfo from a JSON string
content_analysis_categories_info_instance = ContentAnalysisCategoriesInfo.from_json(json)
# print the JSON string representation of the object
print ContentAnalysisCategoriesInfo.to_json()

# convert the object into a dict
content_analysis_categories_info_dict = content_analysis_categories_info_instance.to_dict()
# create an instance of ContentAnalysisCategoriesInfo from a dict
content_analysis_categories_info_form_dict = content_analysis_categories_info.from_dict(content_analysis_categories_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")