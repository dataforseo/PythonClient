# GoogleHotelsSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**hotel_identifier** | **StrictStr** | unique hotel identifier<br>unique hotel identifier assigned by Google;<br>example: 'CgoIjaeSlI6CnNpVEAE' |[optional]|
**url** | **StrictStr** | URL |[optional]|
**cid** | **StrictStr** | google-defined client id |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|