# SerpApiKnowledgeGraphCarouselItemElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **number** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**title** | **string** | title of the result in SERP |[optional]|
**data_attrid** | **string** | google defined data attribute ID<br>example:<br>action:listen_artist |[optional]|
**link** | **LinkElement** | link of the element |[optional]|
**items** | **KnowledgeGraphListElement[]** | elements of search results found in SERP |[optional]|