# DatasetDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | text of the description | [optional] 
**links** | [**List[LinkElement]**](LinkElement.md) | links featured in the ‘dataset_description’ | [optional] 

## Example

```python
from dataforseo_client.models.dataset_description import DatasetDescription

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetDescription from a JSON string
dataset_description_instance = DatasetDescription.from_json(json)
# print the JSON string representation of the object
print DatasetDescription.to_json()

# convert the object into a dict
dataset_description_dict = dataset_description_instance.to_dict()
# create an instance of DatasetDescription from a dict
dataset_description_form_dict = dataset_description.from_dict(dataset_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


