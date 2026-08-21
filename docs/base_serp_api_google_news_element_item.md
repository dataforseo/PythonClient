# BaseSerpApiGoogleNewsElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em> absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**xpath** | **StrictStr** | <em>the <a href='https://en.wikipedia.org/wiki/XPath' rel='noopener noreferrer' target='_blank'>XPath</a> of the element</em> |[optional]|
**title** | **StrictStr** | <em>title of the element</em> |[optional]|
**rectangle** | **AiModeRectangleInfo** | <em>rectangle parameters</em><br>contains cartesian coordinates and pixel dimensions of the result's snippet in SERP<br>equals <code>null</code> if <code>calculate_rectangles</code> in the POST request is not set to <code>true</code> |[optional]|