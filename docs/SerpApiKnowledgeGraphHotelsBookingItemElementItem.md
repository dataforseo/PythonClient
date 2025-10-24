# SerpApiKnowledgeGraphHotelsBookingItemElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **number** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**title** | **string** | title of a given link element |[optional]|
**date_from** | **string** | starting date of stay<br>in the format “year-month-date”<br>example:<br>2019-11-15 |[optional]|
**date_to** | **string** | ending date of stay<br>in the format “year-month-date”<br>example:<br>2019-11-17 |[optional]|
**data_attrid** | **string** | google defined data attribute ID<br>example:<br>kc:/local:hotel booking |[optional]|
**items** | **KnowledgeGraphHotelsBookingElement[]** | additional items present in the element<br>if there are none, equals null |[optional]|