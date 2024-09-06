# AiOverviewSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asynchronous_ai_overview** | **bool** | indicates whether the element is loaded asynchronically if true, the ai_overview element is loaded asynchronically; if false, the ai_overview element is loaded from cache; | [optional] 
**items** | [**List[AiOverviewElement]**](AiOverviewElement.md) | contains arrays of specific images | [optional] 
**references** | [**List[AiOverviewReference]**](AiOverviewReference.md) | additional references relevant to the item includes references to webpages that may have been used to generate the ai_overview | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.ai_overview_serp_element_item import AiOverviewSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of AiOverviewSerpElementItem from a JSON string
ai_overview_serp_element_item_instance = AiOverviewSerpElementItem.from_json(json)
# print the JSON string representation of the object
print AiOverviewSerpElementItem.to_json()

# convert the object into a dict
ai_overview_serp_element_item_dict = ai_overview_serp_element_item_instance.to_dict()
# create an instance of AiOverviewSerpElementItem from a dict
ai_overview_serp_element_item_form_dict = ai_overview_serp_element_item.from_dict(ai_overview_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


