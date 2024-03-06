[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# HotelInfoPriceOffer

featured price offers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the hotel | [optional]
**price** | **int** | price per night | [optional]
**currency** | **str** | price currency USD is applied by default, unless specified in the POST array | [optional]
**url** | **str** | url of the price offer URL to the page of the website where price offer appears | [optional]
**max_visitors** | **int** | the maximal number of visitors the maximum number of visitors for which the price offer is valid | [optional]
**offer_images** | **List[Optional[str]]** | price offer images URLs of the images featured in the price offer | [optional]
**free_cancellation_until** | **str** | date until free cancellation is available in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” equals null if free cancellation is not available for the selected dates | [optional]

## Example

```python
from dataforseo_client.models.hotel_info_price_offer import HotelInfoPriceOffer

# TODO update the JSON string below
json = "{}"
# create an instance of HotelInfoPriceOffer from a JSON string
hotel_info_price_offer_instance = HotelInfoPriceOffer.from_json(json)
# print the JSON string representation of the object
print HotelInfoPriceOffer.to_json()

# convert the object into a dict
hotel_info_price_offer_dict = hotel_info_price_offer_instance.to_dict()
# create an instance of HotelInfoPriceOffer from a dict
hotel_info_price_offer_form_dict = hotel_info_price_offer.from_dict(hotel_info_price_offer_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")