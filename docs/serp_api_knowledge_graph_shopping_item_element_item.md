# SerpApiKnowledgeGraphShoppingItemElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | title of the place |[optional]|
**data_attrid** | **StrictStr** | google defined data attribute ID<br>example:<br>kc:/shopping/gpc:organic-offers |[optional]|
**items** | **List[Optional[KnowledgeGraphShoppingElement]]** | additional items present in the element<br>if there are none, equals null |[optional]|