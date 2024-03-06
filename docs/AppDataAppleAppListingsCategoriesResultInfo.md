[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppDataAppleAppListingsCategoriesResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | name of the supported app category | [optional]
**count** | **int** | number of app listings that make up the supported app category | [optional]

## Example

```python
from dataforseo_client.models.app_data_apple_app_listings_categories_result_info import AppDataAppleAppListingsCategoriesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataAppleAppListingsCategoriesResultInfo from a JSON string
app_data_apple_app_listings_categories_result_info_instance = AppDataAppleAppListingsCategoriesResultInfo.from_json(json)
# print the JSON string representation of the object
print AppDataAppleAppListingsCategoriesResultInfo.to_json()

# convert the object into a dict
app_data_apple_app_listings_categories_result_info_dict = app_data_apple_app_listings_categories_result_info_instance.to_dict()
# create an instance of AppDataAppleAppListingsCategoriesResultInfo from a dict
app_data_apple_app_listings_categories_result_info_form_dict = app_data_apple_app_listings_categories_result_info.from_dict(app_data_apple_app_listings_categories_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")