# ScholarlyArticlesDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the result in SERP | [optional] 
**url** | **str** | relevant URL | [optional] 
**items** | [**List[ScholarlyArticlesElement]**](ScholarlyArticlesElement.md) | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.scholarly_articles_dataforseo_labs_serp_element_item import ScholarlyArticlesDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of ScholarlyArticlesDataforseoLabsSerpElementItem from a JSON string
scholarly_articles_dataforseo_labs_serp_element_item_instance = ScholarlyArticlesDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(ScholarlyArticlesDataforseoLabsSerpElementItem.to_json())

# convert the object into a dict
scholarly_articles_dataforseo_labs_serp_element_item_dict = scholarly_articles_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of ScholarlyArticlesDataforseoLabsSerpElementItem from a dict
scholarly_articles_dataforseo_labs_serp_element_item_from_dict = ScholarlyArticlesDataforseoLabsSerpElementItem.from_dict(scholarly_articles_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


