# HotelAboutInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**description** | **StrictStr** | <em>description of the hotel</em><br>the description of the hotel entity for which the results are collected |[optional]|
**sub_descriptions** | **List[Optional[StrictStr]]** | <em>additional description of the hotel</em><br>details about the hotel provided in addition to the description |[optional]|
**check_in_time** | **TimeInfo** | <em>hotel check-in time</em><br>check-in time indicated in the hotel listing |[optional]|
**check_out_time** | **TimeInfo** | <em>hotel check-out time</em><br>check-out time indicated in the hotel listing |[optional]|
**full_address** | **StrictStr** | <em>full address of the hotel</em><br>address of the hotel indicated in the standardised format |[optional]|
**domain** | **StrictStr** | <em>hotel domain</em><br>domain of the hotel's website |[optional]|
**url** | **StrictStr** | <em>hotel url</em><br>URL to the hotel's website indicated in the listing |[optional]|
**amenities** | **List[Optional[HotelAmenityInfo]]** | <em>hotel amenities</em><br>information about hotel amenities |[optional]|
**popular_amenities** | **List[Optional[HotelAmenityItemInfo]]** | <em>hotel amenities</em><br>information about hotel amenities labelled as 'popular' |[optional]|