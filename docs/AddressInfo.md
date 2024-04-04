# AddressInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borough** | **str** | administrative unit or district the local establishment belongs to | [optional] 
**address** | **str** | street address of the local establishment | [optional] 
**city** | **str** | name of the city where the local establishment is located | [optional] 
**zip** | **str** | ZIP code of the local establishment | [optional] 
**region** | **str** | DMA region the local establishment belongs to | [optional] 
**country_code** | **str** | ISO country code of the local establishment | [optional] 

## Example

```python
from dataforseo_client.models.address_info import AddressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AddressInfo from a JSON string
address_info_instance = AddressInfo.from_json(json)
# print the JSON string representation of the object
print AddressInfo.to_json()

# convert the object into a dict
address_info_dict = address_info_instance.to_dict()
# create an instance of AddressInfo from a dict
address_info_form_dict = address_info.from_dict(address_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


