# HotelPriceItemInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | title of the hotel |[optional]|
**price** | **StrictInt** | price per night |[optional]|
**currency** | **StrictStr** | price currency<br>USD is applied by default, unless specified in the POST array |[optional]|
**url** | **StrictStr** | third-party page url<br>URL to the third-party website page with pricing information |[optional]|
**domain** | **StrictStr** | third-party domain<br>domain of the third-party website page with pricing information |[optional]|
**is_paid** | **StrictBool** | indicates a paid hotel listing<br>if true, related hotel_search_item is a paid ad<br>if false, related hotel_search_item is an organic hotel listing |[optional]|
**free_cancellation_until** | **StrictStr** | date until which free cancellation is available<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>equals null if free cancellation is not available for the selected dates |[optional]|
**offers** | **List[Optional[HotelInfoPriceOffer]]** | featured price offers |[optional]|