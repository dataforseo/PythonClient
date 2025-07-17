# SerpApiGoogleFinanceQuoteElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**quote** | **BaseSerpApiGoogleFinanceElementItem** | quoted market indexes |[optional]|
**graph_items** | **List[Optional[GraphItems]]** | values on graph |[optional]|