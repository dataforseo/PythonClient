# SerpApiKnowledgeGraphHotelsBookingItemElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | title of a given link element |[optional]|
**date_from** | **StrictStr** | starting date of stay<br>in the format “year-month-date”<br>example:<br>2019-11-15 |[optional]|
**date_to** | **StrictStr** | ending date of stay<br>in the format “year-month-date”<br>example:<br>2019-11-17 |[optional]|
**data_attrid** | **StrictStr** | google defined data attribute ID<br>example:<br>kc:/local:hotel booking |[optional]|
**items** | **List[Optional[KnowledgeGraphHotelsBookingElement]]** | additional items present in the element<br>if there are none, equals null |[optional]|