# AnswerBoxSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**text** | **List[Optional[StrictStr]]** | text<br>if there is none, equals null |[optional]|
**links** | **List[Optional[LinkElement]]** | link of the element |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|