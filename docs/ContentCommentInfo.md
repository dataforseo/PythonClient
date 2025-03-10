# ContentCommentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | [**ContentRatingInfo**](ContentRatingInfo.md) |  | [optional] 
**title** | **float** | title of the customer’s comment | [optional] 
**publish_date** | **str** | date when the comment was published | [optional] 
**author** | **str** | author of the comment | [optional] 
**have_form** | **bool** |  | [optional] 
**primary_content** | [**List[SectionContentItemInfo]**](SectionContentItemInfo.md) | primary content on the page you can find more information about content priority calculation in this help center article | [optional] 

## Example

```python
from dataforseo_client.models.content_comment_info import ContentCommentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentCommentInfo from a JSON string
content_comment_info_instance = ContentCommentInfo.from_json(json)
# print the JSON string representation of the object
print(ContentCommentInfo.to_json())

# convert the object into a dict
content_comment_info_dict = content_comment_info_instance.to_dict()
# create an instance of ContentCommentInfo from a dict
content_comment_info_from_dict = ContentCommentInfo.from_dict(content_comment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


