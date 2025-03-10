# ScholarlyArticlesSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**url** | **str** | source URL | [optional] 
**items** | [**List[ScholarlyArticlesElement]**](ScholarlyArticlesElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.scholarly_articles_serp_element_item import ScholarlyArticlesSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ScholarlyArticlesSerpElementItem from a JSON string
scholarly_articles_serp_element_item_instance = ScholarlyArticlesSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(ScholarlyArticlesSerpElementItem.to_json())

# convert the object into a dict
scholarly_articles_serp_element_item_dict = scholarly_articles_serp_element_item_instance.to_dict()
# create an instance of ScholarlyArticlesSerpElementItem from a dict
scholarly_articles_serp_element_item_from_dict = ScholarlyArticlesSerpElementItem.from_dict(scholarly_articles_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


