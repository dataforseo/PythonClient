# BusinessDirectoryInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the element domain of the online menu system | [optional] 
**items** | [**List[BaseBusinessDataSerpElementItem]**](BaseBusinessDataSerpElementItem.md) | encountered item types types of search engine results encountered in the items array; possible item types: google_business_info | [optional] 

## Example

```python
from dataforseo_client.models.business_directory_info import BusinessDirectoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessDirectoryInfo from a JSON string
business_directory_info_instance = BusinessDirectoryInfo.from_json(json)
# print the JSON string representation of the object
print(BusinessDirectoryInfo.to_json())

# convert the object into a dict
business_directory_info_dict = business_directory_info_instance.to_dict()
# create an instance of BusinessDirectoryInfo from a dict
business_directory_info_from_dict = BusinessDirectoryInfo.from_dict(business_directory_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


