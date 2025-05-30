# KnowledgeGraphDescriptionItemSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**text** | **StrictStr** | text or description of the element in SERP |[optional]|
**links** | **List[Optional[LinkElement]]** | sitelinks<br>the links shown below some of Google’s search results<br>if there are none, equals null |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|