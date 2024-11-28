# ScholarlyArticlesElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**title** | **str** | title of a given link element | [optional] 
**url** | **str** | URL | [optional] 
**author** | **str** | author | [optional] 
**description** | **str** | description | [optional] 

## Example

```python
from dataforseo_client.models.scholarly_articles_element import ScholarlyArticlesElement

# TODO update the JSON string below
json = "{}"
# create an instance of ScholarlyArticlesElement from a JSON string
scholarly_articles_element_instance = ScholarlyArticlesElement.from_json(json)
# print the JSON string representation of the object
print(ScholarlyArticlesElement.to_json())

# convert the object into a dict
scholarly_articles_element_dict = scholarly_articles_element_instance.to_dict()
# create an instance of ScholarlyArticlesElement from a dict
scholarly_articles_element_from_dict = ScholarlyArticlesElement.from_dict(scholarly_articles_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


