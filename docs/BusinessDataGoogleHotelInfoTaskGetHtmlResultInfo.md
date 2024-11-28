# BusinessDataGoogleHotelInfoTaskGetHtmlResultInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | identifier received in a POST array this field will contain the hotel_identifier parameter specified when setting a task; example: CgoI-KWyzenM_MV3EAE | [optional] 
**location_code** | **int** | location code in a POST array | [optional] 
**language_code** | **str** | language code in a POST array | [optional] 
**datetime** | **str** | date and time when the result was received in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**items_count** | **int** | the number of results returned in the items array | [optional] 
**items** | [**List[HtmlItem]**](HtmlItem.md) | HTML pages | [optional] 
**type** | **str** |  | [optional] 
**se_domain** | **str** |  | [optional] 

## Example

```python
from dataforseo_client.models.business_data_google_hotel_info_task_get_html_result_info import BusinessDataGoogleHotelInfoTaskGetHtmlResultInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDataGoogleHotelInfoTaskGetHtmlResultInfo from a JSON string
business_data_google_hotel_info_task_get_html_result_info_instance = BusinessDataGoogleHotelInfoTaskGetHtmlResultInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDataGoogleHotelInfoTaskGetHtmlResultInfo.to_json())

# convert the object into a dict
business_data_google_hotel_info_task_get_html_result_info_dict = business_data_google_hotel_info_task_get_html_result_info_instance.to_dict()
# create an instance of BusinessDataGoogleHotelInfoTaskGetHtmlResultInfo from a dict
business_data_google_hotel_info_task_get_html_result_info_from_dict = BusinessDataGoogleHotelInfoTaskGetHtmlResultInfo.from_dict(business_data_google_hotel_info_task_get_html_result_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


