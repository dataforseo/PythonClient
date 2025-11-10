# AiOverviewSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values;<br>positions of elements with different type values are omitted from rank_group;<br>always equals 0 for desktop |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP<br>always equals 0 for desktop |[optional]|
**asynchronous_ai_overview** | **StrictBool** | indicates whether the element is loaded asynchronously<br>if true, the ai_overview element is loaded asynchronously;<br>if false, the ai_overview element is loaded from cache; |[optional]|
**markdown** | **StrictStr** | content of the element in markdown format<br>the text of the ai_overview formatted in the markdown markup language |[optional]|
**items** | **List[Optional[BaseSerpApiAiOverviewElementItem]]** | contains arrays of elements available in the list |[optional]|
**references** | **List[Optional[AiModeAiOverviewReferenceInfo]]** | references relevant to the element<br>includes references to webpages that were used to generate the ai_overview_element |[optional]|