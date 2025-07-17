# KnowledgeGraphHotelsBookingItemSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values;<br>positions of elements with different type values are omitted from rank_group;<br>always equals 0 for desktop |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP<br>always equals 0 for desktop |[optional]|
**title** | **StrictStr** | reference page title |[optional]|
**date_from** | **StrictStr** | starting date of stay<br>in the format “year-month-date”<br>example:<br>2019-11-15 |[optional]|
**date_to** | **StrictStr** | ending date of stay<br>in the format “year-month-date”<br>example:<br>2019-11-17 |[optional]|
**data_attrid** | **StrictStr** | google defined data attribute ID<br>example:<br>action:listen_artist |[optional]|
**items** | **List[Optional[KnowledgeGraphHotelsBookingElement]]** | contains arrays of specific images |[optional]|