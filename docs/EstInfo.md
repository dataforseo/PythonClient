# EstInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**high** | **int** | indicates the upper bound of the range result | [optional] 
**low** | **int** | indicates the lower bound of the range result | [optional] 

## Example

```python
from dataforseo_client.models.est_info import EstInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EstInfo from a JSON string
est_info_instance = EstInfo.from_json(json)
# print the JSON string representation of the object
print(EstInfo.to_json())

# convert the object into a dict
est_info_dict = est_info_instance.to_dict()
# create an instance of EstInfo from a dict
est_info_from_dict = EstInfo.from_dict(est_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


