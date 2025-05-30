# LocalServicesSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the row |[optional]|
**url** | **StrictStr** | URL |[optional]|
**domain** | **StrictStr** | domain in the URL |[optional]|
**items** | **List[Optional[LocalServicesElement]]** | contains arrays of specific images |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|