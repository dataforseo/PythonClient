# BusinessDataGoogleHotelSearchesItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**hotel_identifier** | **StrictStr** | <em>unique identifier of a hotel entity in Google search</em><br>example:<br><code>CgoI-KWyzenM_MV3EAE</code> |[optional]|
**title** | **StrictStr** | <em>title of the hotel</em> |[optional]|
**stars** | **StrictInt** | <em>hotel class rating</em><br>class rating that ranges between 1-5 stars |[optional]|
**is_paid** | **StrictBool** | <em>indicates a paid hotel listing</strong></em><br>if <code>true</code>, related <code>hotel_search_item</code> is a paid ad<br>if <code>false</code>, related <code>hotel_search_item</code> is an organic hotel listing |[optional]|
**location** | **GpsCoordinatesLocationInfo** | <em>GPS coordinates of the hotel's location</em> |[optional]|
**reviews** | **HotelReviewInfo** | <em>hotel reviews and rating information</em> |[optional]|
**overview_images** | **List[Optional[StrictStr]]** | <em>featured images for a hotel</em> |[optional]|
**prices** | **HotelPriceInfo** | <em>hotel price</em> |[optional]|