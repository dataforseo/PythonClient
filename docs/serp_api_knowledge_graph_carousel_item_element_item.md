# SerpApiKnowledgeGraphCarouselItemElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**data_attrid** | **StrictStr** | google defined data attribute ID<br>example:<br>action:listen_artist |[optional]|
**link** | **LinkElement** | link of the element |[optional]|
**items** | **List[Optional[KnowledgeGraphListElement]]** | elements of search results found in SERP |[optional]|