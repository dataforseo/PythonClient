# HotelsPackSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the row |[optional]|
**date_from** | **StrictStr** | starting date of stay<br>in the format “year-month-date”<br>example:<br>2019-11-15 |[optional]|
**date_to** | **StrictStr** | ending date of stay<br>in the format “year-month-date”<br>example:<br>2019-11-17 |[optional]|
**items** | **List[Optional[HotelsPackElement]]** | contains arrays of specific images |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|