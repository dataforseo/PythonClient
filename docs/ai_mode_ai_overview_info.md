# AiModeAiOverviewInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | group rank in SERPposition within a group of elements with identical type valuespositions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERPabsolute position among all the elements in SERP |[optional]|
**page** | **StrictInt** | SERP pageSERP page on which the element ranks |[optional]|
**position** | **StrictStr** | the alignment of the element in SERPcan take the following values:left, right |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**markdown** | **StrictStr** | content of the element in markdown formatthe text of the ai_overview formatted in the markdown markup language |[optional]|
**items** | **List[Optional[BaseSerpApiAiModeAiOverviewElementItem]]** | elements of search results found in SERP |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | additional references relevant to the itemincludes references to webpages that may have been used to generate the ai_overview |[optional]|
**rectangle** | **AiModeRectangleInfo** | rectangle parameterscontains cartesian coordinates and pixel dimensions of the result's snippet in SERPequals null if calculate_rectangles in the POST request is not set to true |[optional]|