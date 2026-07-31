# HotelPriceInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**price** | **StrictFloat** | <em>price per night</em> |[optional]|
**price_without_discount** | **StrictFloat** | <em>full price per night without a discount applied</em> |[optional]|
**currency** | **StrictStr** | <em>price currency</em><br><code>USD</code> is applied by default, unless specified in the POST array |[optional]|
**discount_text** | **StrictStr** | <em>text about a discount applied</em> |[optional]|
**check_in** | **StrictStr** | <em>check-in date and time</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**check_out** | **StrictStr** | <em>check-out date and time</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2019-11-15 12:57:46 +00:00</code> |[optional]|
**visitors** | **StrictInt** | <em>number of hotel visitors for this price</em> |[optional]|
**items** | **List[Optional[HotelPriceItemInfo]]** | <em>encountered item types</em><br>types of search engine results encountered in the <code>items</code> array;<br>possible item types: <code>hotel_search_item</code> |[optional]|
**prices_by_dates** | **List[Optional[PricesByDates]]** |  |[optional]|