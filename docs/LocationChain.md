# LocationChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | card identifier | [optional] 
**feature_id** | **str** | feature identifier learn more about the identifier in this help center article | [optional] 
**cid** | **str** | client id learn more about the identifier in this help center article | [optional] 
**title** | **str** | title of the element in the location chain | [optional] 

## Example

```python
from dataforseo_client.models.location_chain import LocationChain

# TODO update the JSON string below
json = "{}"
# create an instance of LocationChain from a JSON string
location_chain_instance = LocationChain.from_json(json)
# print the JSON string representation of the object
print(LocationChain.to_json())

# convert the object into a dict
location_chain_dict = location_chain_instance.to_dict()
# create an instance of LocationChain from a dict
location_chain_form_dict = location_chain.from_dict(location_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


