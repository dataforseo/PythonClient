# HotelPriceInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**price** | **StrictFloat** | price per night |[optional]|
**price_without_discount** | **StrictFloat** | full price per night without a discount applied |[optional]|
**currency** | **StrictStr** | price currency<br>USD is applied by default, unless specified in the POST array |[optional]|
**discount_text** | **StrictStr** | text about a discount applied |[optional]|
**check_in** | **StrictStr** | check-in date and time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**check_out** | **StrictStr** | check-out date and time<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**visitors** | **StrictInt** | number of hotel visitors for this price |[optional]|
**items** | **List[Optional[HotelPriceItemInfo]]** | encountered item types<br>types of search engine results encountered in the items array;<br>possible item types: hotel_search_item |[optional]|
**prices_by_dates** | **List[Optional[PricesByDates]]** |  |[optional]|