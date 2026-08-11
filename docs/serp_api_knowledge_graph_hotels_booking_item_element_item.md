# SerpApiKnowledgeGraphHotelsBookingItemElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | <em>title of a given link element</em> |[optional]|
**date_from** | **StrictStr** | <em>starting date of stay</em><br>in the format “year-month-date”<br>example:<br>2019-11-15 |[optional]|
**date_to** | **StrictStr** | <em>ending date of stay</em><br>in the format “year-month-date”<br>example:<br>2019-11-17 |[optional]|
**data_attrid** | **StrictStr** | <em>google defined data attribute ID</em><br>example:<br><code>kc:/local:hotel booking</code> |[optional]|
**items** | **List[Optional[KnowledgeGraphHotelsBookingElement]]** | <em>popular keywords relevant to the initial search query</em><br>if there are none, equals <code>null</code> |[optional]|