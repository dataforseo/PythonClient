# EstCInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**high** | **float** | indicates the upper bound of the range result | [optional] 
**low** | **float** | indicates the lower bound of the range result | [optional] 

## Example

```python
from dataforseo_client.models.est_c_info import EstCInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EstCInfo from a JSON string
est_c_info_instance = EstCInfo.from_json(json)
# print the JSON string representation of the object
print(EstCInfo.to_json())

# convert the object into a dict
est_c_info_dict = est_c_info_instance.to_dict()
# create an instance of EstCInfo from a dict
est_c_info_from_dict = EstCInfo.from_dict(est_c_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


