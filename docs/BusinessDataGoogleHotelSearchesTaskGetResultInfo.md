[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BusinessDataGoogleHotelSearchesTaskGetResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | keyword received in a POST array keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character); in order to obtain accurate search results, the location name is appended to the keyword automatically | [optional]
**location_code** | **int** | location code in a POST array | [optional]
**language_code** | **str** | language code in a POST array | [optional]
**check_url** | **str** | direct URL to search engine results you can use it to make sure that we provided accurate results | [optional]
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**items_count** | **int** | item types the number of items in the items array | [optional]
**items** | [**List[BusinessDataGoogleHotelSearchesItem]**](BusinessDataGoogleHotelSearchesItem.md) | array of items note: this field always equals null; use it to facilitate integration and ensure interoperability with the Hotel Info endpoint | [optional]

## Example

```python
from dataforseo_client.models.business_data_google_hotel_searches_task_get_result_info import BusinessDataGoogleHotelSearchesTaskGetResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleHotelSearchesTaskGetResultInfo from a JSON string
business_data_google_hotel_searches_task_get_result_info_instance = BusinessDataGoogleHotelSearchesTaskGetResultInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataGoogleHotelSearchesTaskGetResultInfo.to_json()

# convert the object into a dict
business_data_google_hotel_searches_task_get_result_info_dict = business_data_google_hotel_searches_task_get_result_info_instance.to_dict()
# create an instance of BusinessDataGoogleHotelSearchesTaskGetResultInfo from a dict
business_data_google_hotel_searches_task_get_result_info_form_dict = business_data_google_hotel_searches_task_get_result_info.from_dict(business_data_google_hotel_searches_task_get_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")