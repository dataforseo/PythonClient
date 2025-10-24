# AiModeAiOverviewInfo

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**page** | **number** |  |[optional]|
**position** | **string** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**xpath** | **string** | the XPath of the element |[optional]|
**markdown** | **string** | content of the element in markdown format<br>the text of the ai_overview formatted in the markdown markup language |[optional]|
**items** | **BaseSerpApiAiModeAiOverviewElementItem[]** | elements of search results found in SERP |[optional]|
**references** | **AiModeAiOverviewReferenceInfo[]** | additional references relevant to the item<br>includes references to webpages that may have been used to generate the ai_overview |[optional]|
**rectangle** | **AiModeRectangleInfo** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|