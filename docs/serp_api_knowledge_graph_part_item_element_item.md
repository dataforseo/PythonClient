# SerpApiKnowledgeGraphPartItemElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | <em>title of the place</em> |[optional]|
**data_attrid** | **StrictStr** | <em>google defined data attribute ID</em><br>example:<br><code>kc:/local:place qa</code> |[optional]|
**text** | **StrictStr** | <em>reference text</em><br>text snippet from the page that was used to generate the <code>ai_overview_element</code> |[optional]|
**links** | **List[Optional[LinkElement]]** | <em>sitelinks</em><br>the links shown below some of Google's search results<br>if there are none, equals <code>null</code> |[optional]|