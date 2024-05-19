# SecondaryTopic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**h_title** | **str** | meta title | [optional] 
**main_title** | **str** | main title of the block | [optional] 
**author** | **str** | content author name | [optional] 
**language** | **str** | content language | [optional] 
**level** | **int** | HTML level | [optional] 
**primary_content** | **str** | primary content on the page you can find more information about content priority calculation in this help center article | [optional] 
**secondary_content** | [**List[ContentItemInfo]**](ContentItemInfo.md) | secondary content on the page you can find more information about content priority calculation in this help center article | [optional] 
**table_content** | [**List[TableContent]**](TableContent.md) | content of the table on the page | [optional] 

## Example

```python
from dataforseo_client.models.secondary_topic import SecondaryTopic

# TODO update the JSON string below
json = "{}"
# create an instance of SecondaryTopic from a JSON string
secondary_topic_instance = SecondaryTopic.from_json(json)
# print the JSON string representation of the object
print SecondaryTopic.to_json()

# convert the object into a dict
secondary_topic_dict = secondary_topic_instance.to_dict()
# create an instance of SecondaryTopic from a dict
secondary_topic_form_dict = secondary_topic.from_dict(secondary_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


