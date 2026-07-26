# AiModeAiOverviewInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**page** | **StrictInt** | <em>SERP page</em><br>SERP page on which the element ranks |[optional]|
**position** | **StrictStr** | <em>the alignment of the element in SERP</em><br>can take the following values:<br><code>left</code>, <code>right</code> |[optional]|
**xpath** | **StrictStr** | <em>the <a href='https://en.wikipedia.org/wiki/XPath' rel='noopener noreferrer' target='_blank'>XPath</a> of the element</em> |[optional]|
**markdown** | **StrictStr** | <em>content of the element in markdown format</em><br>the text of the <code>ai_overview</code> formatted in the <a href='https://en.wikipedia.org/wiki/Markdown' target='_blank'>markdown markup language</a> |[optional]|
**items** | **List[Optional[BaseSerpApiAiModeAiOverviewElementItem]]** | <em>items present in the element</em> |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | <em>additional references relevant to the item</em><br>includes references to webpages that may have been used to generate the <code>ai_overview</code> |[optional]|
**rectangle** | **AiModeRectangleInfo** | <em>rectangle parameters</em><br>contains cartesian coordinates and pixel dimensions of the result's snippet in SERP<br>equals <code>null</code> if <code>calculate_rectangles</code> in the POST request is not set to <code>true</code> |[optional]|