# PageContentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | [**PageSectionContentInfo**](PageSectionContentInfo.md) |  | [optional] 
**footer** | [**PageSectionContentInfo**](PageSectionContentInfo.md) |  | [optional] 
**main_topic** | [**List[TopicInfo]**](TopicInfo.md) | main topic on the page you can find more information about topic priority calculation in this help center article | [optional] 
**secondary_topic** | [**List[TopicInfo]**](TopicInfo.md) | secondary topic on the page you can find more information about topic priority calculation in this help center article | [optional] 
**ratings** | [**List[ContentRatingInfo]**](ContentRatingInfo.md) | contains objects with rating information for the products displayed on the page | [optional] 
**offers** | [**List[ContentOfferInfo]**](ContentOfferInfo.md) | array of products displayed on the page contains objects with information on products displayed on the page | [optional] 
**comments** | [**List[ContentCommentInfo]**](ContentCommentInfo.md) | array of comments displayed on the page contains objects with information on comments related to displayed products | [optional] 
**contacts** | [**Contacts**](Contacts.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.page_content_info import PageContentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PageContentInfo from a JSON string
page_content_info_instance = PageContentInfo.from_json(json)
# print the JSON string representation of the object
print(PageContentInfo.to_json())

# convert the object into a dict
page_content_info_dict = page_content_info_instance.to_dict()
# create an instance of PageContentInfo from a dict
page_content_info_from_dict = PageContentInfo.from_dict(page_content_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


