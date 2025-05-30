# KnowledgeGraphExpandedItemSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the link |[optional]|
**data_attrid** | **StrictStr** | google defined data attribute ID<br>example:<br>kc:/local:place qa |[optional]|
**expanded_element** | **List[Optional[KnowledgeGraphExpandedElement]]** | link of the element |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|