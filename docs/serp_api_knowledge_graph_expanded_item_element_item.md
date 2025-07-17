# SerpApiKnowledgeGraphExpandedItemElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | title of the link |[optional]|
**data_attrid** | **StrictStr** | google defined data attribute ID<br>example:<br>kc:/local:place qa |[optional]|
**expanded_element** | **List[Optional[KnowledgeGraphExpandedElement]]** | link of the element |[optional]|