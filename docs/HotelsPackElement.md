[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# HotelsPackElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**price** | [**PriceInfo**](PriceInfo.md) |  | [optional]
**title** | **str** | title of the row | [optional]
**description** | **str** | description of the results element in SERP | [optional]
**hotel_identifier** | **str** | unique hotel identifier unique hotel identifier assigned by Google; example: \&quot;CgoIjaeSlI6CnNpVEAE\&quot; | [optional]
**domain** | **str** | domain where a link points | [optional]
**url** | **str** | URL | [optional]
**is_paid** | **bool** | indicates whether the element is an ad | [optional]
**rating** | [**RatingInfo**](RatingInfo.md) |  | [optional]

## Example

```python
from dataforseo_client.models.hotels_pack_element import HotelsPackElement

# TODO update the JSON string below
json = "{}"
# create an instance of HotelsPackElement from a JSON string
hotels_pack_element_instance = HotelsPackElement.from_json(json)
# print the JSON string representation of the object
print HotelsPackElement.to_json()

# convert the object into a dict
hotels_pack_element_dict = hotels_pack_element_instance.to_dict()
# create an instance of HotelsPackElement from a dict
hotels_pack_element_form_dict = hotels_pack_element.from_dict(hotels_pack_element_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")