# FaqBox


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional] 
**items** | [**List[FaqBoxElement]**](FaqBoxElement.md) | contains results featured in the ‘hotels_pack’ element of SERP | [optional] 

## Example

```python
from dataforseo_client.models.faq_box import FaqBox

# TODO update the JSON string below
json = "{}"
# create an instance of FaqBox from a JSON string
faq_box_instance = FaqBox.from_json(json)
# print the JSON string representation of the object
print FaqBox.to_json()

# convert the object into a dict
faq_box_dict = faq_box_instance.to_dict()
# create an instance of FaqBox from a dict
faq_box_form_dict = faq_box.from_dict(faq_box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


