# LocalPackSerpElementItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | the alignment of the element in SERP can take the following values: left, right | [optional] 
**xpath** | **str** | the XPath of the element | [optional] 
**title** | **str** | title of the row | [optional] 
**description** | **str** | description of the results element in SERP | [optional] 
**domain** | **str** | source domain | [optional] 
**phone** | **str** | phone number | [optional] 
**url** | **str** | source URL | [optional] 
**is_paid** | **bool** | indicates whether the element is an ad | [optional] 
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional] 
**cid** | **str** | google-defined client id | [optional] 
**rectangle** | [**Rectangle**](Rectangle.md) |  | [optional] 

## Example

```python
from dataforseo_client.models.local_pack_serp_element_item import LocalPackSerpElementItem

# TODO update the JSON string below
json = "{}"
# create an instance of LocalPackSerpElementItem from a JSON string
local_pack_serp_element_item_instance = LocalPackSerpElementItem.from_json(json)
# print the JSON string representation of the object
print(LocalPackSerpElementItem.to_json())

# convert the object into a dict
local_pack_serp_element_item_dict = local_pack_serp_element_item_instance.to_dict()
# create an instance of LocalPackSerpElementItem from a dict
local_pack_serp_element_item_from_dict = LocalPackSerpElementItem.from_dict(local_pack_serp_element_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


