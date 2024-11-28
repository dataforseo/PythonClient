# MerchantErrorsRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | the maximum number of returned tasks that responded with an error optional field default value: 1000 maximum value: 1000 | [optional] 
**offset** | **int** | offset in the results array of returned tasks optional field default value: 0 if you specify the 10 value, the first ten tasks in the results array will be omitted and the data will be provided for the successive tasks | [optional] 
**filtered_function** | **str** | return tasks with a certain function use this field to obtain a list of tasks that returned an error filtered by a certain function you can filter the results by the values you receive in the function fields of the API response i.e., once you receive unfiltered results, you can call this API again to filter them by function example: sellers/ad_url, postback_url, pingback_url | [optional] 
**datetime_from** | **str** | start time for filtering results optional field allows filtering results by the datetime parameter within the range of the last 7 days; must be specified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2021-11-15 12:57:46 +00:00 | [optional] 
**datetime_to** | **str** | finish time for filtering results optional field allows filtering results by the datetime parameter within the range of the last 7 days; must be specified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2021-11-15 13:57:46 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.merchant_errors_request_info import MerchantErrorsRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantErrorsRequestInfo from a JSON string
merchant_errors_request_info_instance = MerchantErrorsRequestInfo.from_json(json)
# print the JSON string representation of the object
print(MerchantErrorsRequestInfo.to_json())

# convert the object into a dict
merchant_errors_request_info_dict = merchant_errors_request_info_instance.to_dict()
# create an instance of MerchantErrorsRequestInfo from a dict
merchant_errors_request_info_from_dict = MerchantErrorsRequestInfo.from_dict(merchant_errors_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


