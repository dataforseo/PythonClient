# AiOverviewSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**asynchronous_ai_overview** | **StrictBool** | indicates whether the element is loaded asynchronically<br>if true, the ai_overview element is loaded asynchronically;<br>if false, the ai_overview element is loaded from cache; |[optional]|
**items** | **List[Optional[AiOverviewElement]]** | contains arrays of specific images |[optional]|
**references** | **List[Optional[AiOverviewReference]]** | additional references relevant to the item<br>includes references to webpages that may have been used to generate the ai_overview |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|