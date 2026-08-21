# SerpApiGoogleFinanceQuoteElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**quote** | **BaseSerpApiGoogleFinanceElementItem** | <em>quoted market indexes</em> |[optional]|
**graph_items** | **List[Optional[GraphItems]]** | <em>values on graph</em> |[optional]|