# CompareSitesSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | title of the row | [optional] 
**items** | [**List[CompareSitesElement]**](CompareSitesElement.md) | contains arrays of specific images | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.compare_sites_serp_element_item import CompareSitesSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of CompareSitesSerpElementItem from a JSON string
compare_sites_serp_element_item_instance = CompareSitesSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(CompareSitesSerpElementItem.to_json())

# convert the object into a dict
compare_sites_serp_element_item_dict = compare_sites_serp_element_item_instance.to_dict()
# create an instance of CompareSitesSerpElementItem from a dict
compare_sites_serp_element_item_from_dict = CompareSitesSerpElementItem.from_dict(compare_sites_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


