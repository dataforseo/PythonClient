# YoutubeCommentSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_name** | **str** | name of the author of the comment | [optional] 
**author_thumbnail** | **str** | the URL of the page where the author’s channel logo is hosted | [optional] 
**author_url** | **str** | URL of the author’s channel | [optional] 
**text** | **str** | text of the comment | [optional] 
**publication_date** | **str** | displayed publication date | [optional] 
**timestamp** | **str** | date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2022-11-15 12:57:46 +00:00 | [optional] 
**likes_count** | **int** | number of likes on the comment | [optional] 
**reply_count** | **int** | number of replies on the comment | [optional] 

## Example

```python
from dataforseo_client.models.youtube_comment_serp_element_item import YoutubeCommentSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of YoutubeCommentSerpElementItem from a JSON string
youtube_comment_serp_element_item_instance = YoutubeCommentSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(YoutubeCommentSerpElementItem.to_json())

# convert the object into a dict
youtube_comment_serp_element_item_dict = youtube_comment_serp_element_item_instance.to_dict()
# create an instance of YoutubeCommentSerpElementItem from a dict
youtube_comment_serp_element_item_from_dict = YoutubeCommentSerpElementItem.from_dict(youtube_comment_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


