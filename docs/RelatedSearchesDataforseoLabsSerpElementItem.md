# RelatedSearchesDataforseoLabsSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**se_type** | **str** | search engine type | [optional] 
**rank_group** | **int** | position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group | [optional] 
**rank_absolute** | **int** | absolute rank in SERP absolute position among all the elements in SERP | [optional] 
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**items** | **List[Optional[str]]** | additional items present in the element if there are none, equals null | [optional] 

## Example

```python
from dataforseo_client.models.related_searches_dataforseo_labs_serp_element_item import RelatedSearchesDataforseoLabsSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedSearchesDataforseoLabsSerpElementItem from a JSON string
related_searches_dataforseo_labs_serp_element_item_instance = RelatedSearchesDataforseoLabsSerpElementItem.from_json(json)
# print the JSON string representation of the object
print RelatedSearchesDataforseoLabsSerpElementItem.to_json()

# convert the object into a dict
related_searches_dataforseo_labs_serp_element_item_dict = related_searches_dataforseo_labs_serp_element_item_instance.to_dict()
# create an instance of RelatedSearchesDataforseoLabsSerpElementItem from a dict
related_searches_dataforseo_labs_serp_element_item_form_dict = related_searches_dataforseo_labs_serp_element_item.from_dict(related_searches_dataforseo_labs_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


