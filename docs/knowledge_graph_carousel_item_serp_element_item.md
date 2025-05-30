# KnowledgeGraphCarouselItemSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**data_attrid** | **StrictStr** | google defined data attribute ID<br>example:<br>action:listen_artist |[optional]|
**link** | **LinkElement** | link of the element |[optional]|
**items** | **List[Optional[KnowledgeGraphListElement]]** | elements of search results found in SERP |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|