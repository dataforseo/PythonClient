# KnowledgeGraphHotelsBookingItemSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of a given link element |[optional]|
**date_from** | **StrictStr** | starting date of stay<br>in the format “year-month-date”<br>example:<br>2019-11-15 |[optional]|
**date_to** | **StrictStr** | ending date of stay<br>in the format “year-month-date”<br>example:<br>2019-11-17 |[optional]|
**data_attrid** | **StrictStr** | google defined data attribute ID<br>example:<br>kc:/local:hotel booking |[optional]|
**items** | **List[Optional[KnowledgeGraphHotelsBookingElement]]** | additional items present in the element<br>if there are none, equals null |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|