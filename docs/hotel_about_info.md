# HotelAboutInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**description** | **StrictStr** | description of the hotel<br>the description of the hotel entity for which the results are collected |[optional]|
**sub_descriptions** | **List[Optional[StrictStr]]** | additional description of the hotel<br>details about the hotel provided in addition to the description |[optional]|
**check_in_time** | **Info** | hotel check-in time<br>check-in time indicated in the hotel listing |[optional]|
**check_out_time** | **Info** | hotel check-out time<br>check-out time indicated in the hotel listing |[optional]|
**full_address** | **StrictStr** | full address of the hotel<br>address of the hotel indicated in the standardised format |[optional]|
**domain** | **StrictStr** | hotel domain<br>domain of the hotel’s website |[optional]|
**url** | **StrictStr** | hotel url<br>URL to the hotel’s website indicated in the listing |[optional]|
**amenities** | **List[Optional[HotelAmenityInfo]]** | hotel amenities<br>information about hotel amenities |[optional]|
**popular_amenities** | **List[Optional[HotelAmenityItemInfo]]** | hotel amenities<br>information about hotel amenities labelled as “popular” |[optional]|