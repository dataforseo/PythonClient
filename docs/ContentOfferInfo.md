# ContentOfferInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the product | [optional] 
**price** | **float** | price of the product | [optional] 
**price_currency** | **str** | price currency | [optional] 
**price_valid_until** | **str** | displays the date and time until which the price is valid in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: \&quot;2022-11-01 10:02:52 +00:00\&quot; | [optional] 

## Example

```python
from dataforseo_client.models.content_offer_info import ContentOfferInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContentOfferInfo from a JSON string
content_offer_info_instance = ContentOfferInfo.from_json(json)
# print the JSON string representation of the object
print(ContentOfferInfo.to_json())

# convert the object into a dict
content_offer_info_dict = content_offer_info_instance.to_dict()
# create an instance of ContentOfferInfo from a dict
content_offer_info_from_dict = ContentOfferInfo.from_dict(content_offer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


