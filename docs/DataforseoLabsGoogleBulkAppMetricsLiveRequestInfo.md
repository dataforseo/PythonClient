[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# DataforseoLabsGoogleBulkAppMetricsLiveRequestInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_ids** | **List[str]** | ids of the app required field IDs of the mobile applications on Google Play; you can find the ID in the URL of every app listed on Google Play; example: in the URL https://play.google.com/store/apps/details?id&#x3D;org.telegram.messenger the id is org.telegram.messenger; the maximum number of IDs you can specify in this field is 1000 | [optional]
**location_name** | **str** | full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_name by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US location only; example: United States | [optional]
**location_code** | **int** | location code required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code by making a separate request to https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the US location only; example: 2840 | [optional]
**language_name** | **str** | full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the English language only; example: English | [optional]
**language_code** | **str** | language code required field if you don’t specify language_name Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages; Note: this endpoint currently supports the English language only example: en | [optional]
**tag** | **str** | user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response | [optional]

## Example

```python
from dataforseo_client.models.dataforseo_labs_google_bulk_app_metrics_live_request_info import DataforseoLabsGoogleBulkAppMetricsLiveRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DataforseoLabsGoogleBulkAppMetricsLiveRequestInfo from a JSON string
dataforseo_labs_google_bulk_app_metrics_live_request_info_instance = DataforseoLabsGoogleBulkAppMetricsLiveRequestInfo.from_json(json)
# print the JSON string representation of the object
print DataforseoLabsGoogleBulkAppMetricsLiveRequestInfo.to_json()

# convert the object into a dict
dataforseo_labs_google_bulk_app_metrics_live_request_info_dict = dataforseo_labs_google_bulk_app_metrics_live_request_info_instance.to_dict()
# create an instance of DataforseoLabsGoogleBulkAppMetricsLiveRequestInfo from a dict
dataforseo_labs_google_bulk_app_metrics_live_request_info_form_dict = dataforseo_labs_google_bulk_app_metrics_live_request_info.from_dict(dataforseo_labs_google_bulk_app_metrics_live_request_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")