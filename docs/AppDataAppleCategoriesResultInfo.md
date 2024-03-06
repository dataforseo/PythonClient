[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppDataAppleCategoriesResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[Optional[str]]** | contains full list of supported app categories | [optional]

## Example

```python
from dataforseo_client.models.app_data_apple_categories_result_info import AppDataAppleCategoriesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataAppleCategoriesResultInfo from a JSON string
app_data_apple_categories_result_info_instance = AppDataAppleCategoriesResultInfo.from_json(json)
# print the JSON string representation of the object
print AppDataAppleCategoriesResultInfo.to_json()

# convert the object into a dict
app_data_apple_categories_result_info_dict = app_data_apple_categories_result_info_instance.to_dict()
# create an instance of AppDataAppleCategoriesResultInfo from a dict
app_data_apple_categories_result_info_form_dict = app_data_apple_categories_result_info.from_dict(app_data_apple_categories_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")