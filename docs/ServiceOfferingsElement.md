# ServiceOfferingsElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**name** | **str** | name of the label example: Delivery | [optional] 
**is_available** | **bool** | availability of the offering if the value is false, the offering is not available | [optional] 

## Example

```python
from dataforseo_client.models.service_offerings_element import ServiceOfferingsElement

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceOfferingsElement from a JSON string
service_offerings_element_instance = ServiceOfferingsElement.from_json(json)
# print the JSON string representation of the object
print(ServiceOfferingsElement.to_json())

# convert the object into a dict
service_offerings_element_dict = service_offerings_element_instance.to_dict()
# create an instance of ServiceOfferingsElement from a dict
service_offerings_element_form_dict = service_offerings_element.from_dict(service_offerings_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


