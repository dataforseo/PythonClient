[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# BusinessDataGoogleHotelInfoLiveHtmlResultInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | unique hotel identifier specified as \&quot;hotel_id:$\&quot; | [optional]
**type** | **str** | type of element | [optional]
**se_domain** | **str** | search engine domain in a POST array | [optional]
**location_code** | **int** | location code in a POST array | [optional]
**language_code** | **str** | language code in a POST array | [optional]
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional]
**items_count** | **int** | the number of results returned in the items array | [optional]
**items** | [**List[HtmlItem]**](HtmlItem.md) | HTML pages | [optional]

## Example

```python
from dataforseo_client.models.business_data_google_hotel_info_live_html_result_info import BusinessDataGoogleHotelInfoLiveHtmlResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleHotelInfoLiveHtmlResultInfo from a JSON string
business_data_google_hotel_info_live_html_result_info_instance = BusinessDataGoogleHotelInfoLiveHtmlResultInfo.from_json(json)
# print the JSON string representation of the object
print BusinessDataGoogleHotelInfoLiveHtmlResultInfo.to_json()

# convert the object into a dict
business_data_google_hotel_info_live_html_result_info_dict = business_data_google_hotel_info_live_html_result_info_instance.to_dict()
# create an instance of BusinessDataGoogleHotelInfoLiveHtmlResultInfo from a dict
business_data_google_hotel_info_live_html_result_info_form_dict = business_data_google_hotel_info_live_html_result_info.from_dict(business_data_google_hotel_info_live_html_result_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")