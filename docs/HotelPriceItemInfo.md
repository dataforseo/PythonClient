[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")

# HotelPriceItemInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type of element | [optional]
**title** | **str** | title of the hotel | [optional]
**price** | **int** | price per night | [optional]
**currency** | **str** | price currency USD is applied by default, unless specified in the POST array | [optional]
**url** | **str** | third-party page url URL to the third-party website page with pricing information | [optional]
**domain** | **str** | third-party domain domain of the third-party website page with pricing information | [optional]
**is_paid** | **bool** | indicates a paid hotel listing if true, related hotel_search_item is a paid ad if false, related hotel_search_item is an organic hotel listing | [optional]
**free_cancellation_until** | **str** | date until which free cancellation is available in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” equals null if free cancellation is not available for the selected dates | [optional]
**offers** | [**List[HotelInfoPriceOffer]**](HotelInfoPriceOffer.md) | featured price offers | [optional]

## Example

```python
from dataforseo_client.models.hotel_price_item_info import HotelPriceItemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HotelPriceItemInfo from a JSON string
hotel_price_item_info_instance = HotelPriceItemInfo.from_json(json)
# print the JSON string representation of the object
print HotelPriceItemInfo.to_json()

# convert the object into a dict
hotel_price_item_info_dict = hotel_price_item_info_instance.to_dict()
# create an instance of HotelPriceItemInfo from a dict
hotel_price_item_info_form_dict = hotel_price_item_info.from_dict(hotel_price_item_info_dict)
```

  

[root](./../ "root") / [docs](./ "docs")

[[Back to README.md]](./../README.md "[Back to README.md]")