# Interests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyword** | **str** | relevant keyword the data included in the values element is based on this keyword | [optional] 
**values** | [**List[Values]**](Values.md) | contains data on relative keyword popularity by country or region | [optional] 

## Example

```python
from dataforseo_client.models.interests import Interests

# TODO update the JSON string below
json = "{}"
# create an instance of Interests from a JSON string
interests_instance = Interests.from_json(json)
# print the JSON string representation of the object
print(Interests.to_json())

# convert the object into a dict
interests_dict = interests_instance.to_dict()
# create an instance of Interests from a dict
interests_form_dict = interests.from_dict(interests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


