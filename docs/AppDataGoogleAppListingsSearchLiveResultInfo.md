[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# AppDataGoogleAppListingsSearchLiveResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | the total number of relevant results in the database | [optional]
**count** | **int** | the number of items in the results array | [optional]
**offset** | **int** | offset in the results array of returned apps | [optional]
**offset_token** | **str** | token for subsequent requests you can use this parameter in the POST request to avoid timeouts while trying to obtain over 100,000 results in a single request | [optional]
**items** | [**List[AppDataleAppListingsSearchLiveItem]**](AppDataleAppListingsSearchLiveItem.md) | array of apps and related data | [optional]

## Example

```python
from dataforseo_client.models.app_data_google_app_listings_search_live_result_info import AppDataGoogleAppListingsSearchLiveResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AppDataGoogleAppListingsSearchLiveResultInfo from a JSON string
app_data_google_app_listings_search_live_result_info_instance = AppDataGoogleAppListingsSearchLiveResultInfo.from_json(json)
# print the JSON string representation of the object
print AppDataGoogleAppListingsSearchLiveResultInfo.to_json()

# convert the object into a dict
app_data_google_app_listings_search_live_result_info_dict = app_data_google_app_listings_search_live_result_info_instance.to_dict()
# create an instance of AppDataGoogleAppListingsSearchLiveResultInfo from a dict
app_data_google_app_listings_search_live_result_info_form_dict = app_data_google_app_listings_search_live_result_info.from_dict(app_data_google_app_listings_search_live_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")