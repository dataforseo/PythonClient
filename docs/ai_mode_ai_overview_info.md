# AiModeAiOverviewInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**page** | **StrictInt** |  |[optional]|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format<br>the text of the ai_overview formatted in the markdown markup language |[optional]|
**items** | **List[Optional[BaseSerpApiAiModeAiOverviewElementItem]]** | items of the element |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | additional references relevant to the item<br>includes references to webpages that may have been used to generate the ai_overview |[optional]|
**rectangle** | **AiModeRectangleInfo** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|