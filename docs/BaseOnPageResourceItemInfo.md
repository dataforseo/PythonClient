# BaseOnPageResourceItemInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **str** | type of the returned resource | [optional] 
**status_code** | **int** | status code of the page | [optional] 
**location** | **str** | location header indicates the URL to redirect a page to | [optional] 
**url** | **str** | page URL | [optional] 
**resource_errors** | [**OnPageResourceIssueInfo**](OnPageResourceIssueInfo.md) |  | [optional] 
**size** | **int** | resource size indicates the size of a given page measured in bytes | [optional] 
**encoded_size** | **int** | page size after encoding indicates the size of the encoded page measured in bytes | [optional] 
**total_transfer_size** | **int** | compressed page size indicates the compressed size of a given page | [optional] 
**fetch_time** | **str** | date and time when a resource was fetched in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00 | [optional] 
**cache_control** | [**CacheControl**](CacheControl.md) |  | [optional] 
**checks** | **Dict[str, Optional[bool]]** | website checks on-page check-ups related to the page | [optional] 
**content_encoding** | **str** | type of encoding | [optional] 
**media_type** | **str** | types of media used to display a page | [optional] 
**server** | **str** | server version | [optional] 
**last_modified** | [**LastModified**](LastModified.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.base_on_page_resource_item_info import BaseOnPageResourceItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BaseOnPageResourceItemInfo from a JSON string
base_on_page_resource_item_info_instance = BaseOnPageResourceItemInfo.from_json(json)
# print the JSON string representation of the object
print(BaseOnPageResourceItemInfo.to_json())

# convert the object into a dict
base_on_page_resource_item_info_dict = base_on_page_resource_item_info_instance.to_dict()
# create an instance of BaseOnPageResourceItemInfo from a dict
base_on_page_resource_item_info_from_dict = BaseOnPageResourceItemInfo.from_dict(base_on_page_resource_item_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


