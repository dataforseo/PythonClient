# KnowledgeGraphShoppingItemSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the place |[optional]|
**data_attrid** | **StrictStr** | google defined data attribute ID<br>example:<br>kc:/shopping/gpc:organic-offers |[optional]|
**items** | **List[Optional[KnowledgeGraphShoppingElement]]** | additional items present in the element<br>if there are none, equals null |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|