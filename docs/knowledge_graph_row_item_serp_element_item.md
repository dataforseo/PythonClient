# KnowledgeGraphRowItemSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the item |[optional]|
**data_attrid** | **StrictStr** | google defined data attribute ID<br>example:<br>kc:/common/topic:social media presence |[optional]|
**text** | **StrictStr** | reference text<br>text snippet from the page that was used to generate the ai_overview_element |[optional]|
**links** | **List[Optional[LinkElement]]** | links featured in the faq_box_element |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|