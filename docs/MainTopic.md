# MainTopic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**h_title** | **str** | meta title | [optional] 
**main_title** | **str** | main title of the block | [optional] 
**author** | **str** | content author name | [optional] 
**language** | **str** | content language | [optional] 
**level** | **int** | HTML level | [optional] 
**primary_content** | [**List[ContentItemInfo]**](ContentItemInfo.md) | primary content on the page you can find more information about content priority calculation in this help center article | [optional] 
**secondary_content** | [**List[ContentItemInfo]**](ContentItemInfo.md) | secondary content on the page you can find more information about content priority calculation in this help center article | [optional] 
**table_content** | [**List[TableContent]**](TableContent.md) | content of the table on the page | [optional] 

## Example

```python
from dataforseo_client.models.main_topic import MainTopic

# TODO update the JSON string below
json = "{}"
# create an instance of MainTopic from a JSON string
main_topic_instance = MainTopic.from_json(json)
# print the JSON string representation of the object
print MainTopic.to_json()

# convert the object into a dict
main_topic_dict = main_topic_instance.to_dict()
# create an instance of MainTopic from a dict
main_topic_form_dict = main_topic.from_dict(main_topic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


