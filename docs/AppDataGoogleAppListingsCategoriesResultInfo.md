# AppDataGoogleAppListingsCategoriesResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | name of the supported app category | [optional] 
**count** | **int** | number of app listings that make up the supported app category | [optional] 

## Example

```python
from dataforseo_client.models.app_data_google_app_listings_categories_result_info import AppDataGoogleAppListingsCategoriesResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataGoogleAppListingsCategoriesResultInfo from a JSON string
app_data_google_app_listings_categories_result_info_instance = AppDataGoogleAppListingsCategoriesResultInfo.from_json(json)
# print the JSON string representation of the object
print(AppDataGoogleAppListingsCategoriesResultInfo.to_json())

# convert the object into a dict
app_data_google_app_listings_categories_result_info_dict = app_data_google_app_listings_categories_result_info_instance.to_dict()
# create an instance of AppDataGoogleAppListingsCategoriesResultInfo from a dict
app_data_google_app_listings_categories_result_info_from_dict = AppDataGoogleAppListingsCategoriesResultInfo.from_dict(app_data_google_app_listings_categories_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


