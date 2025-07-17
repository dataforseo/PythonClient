# SerpApiKnowledgeGraphPartItemElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**data_attrid** | **StrictStr** | google defined data attribute ID<br>example:<br>kc:/local:place qa |[optional]|
**text** | **StrictStr** | reference text<br>text snippet from the page that was used to generate the ai_overview_element |[optional]|
**links** | **List[Optional[LinkElement]]** | sitelinks<br>the links shown below some of Google’s search results<br>if there are none, equals null |[optional]|