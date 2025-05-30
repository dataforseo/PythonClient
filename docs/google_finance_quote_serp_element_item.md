# GoogleFinanceQuoteSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictFloat** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictFloat** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**quote** | **BaseGoogleFinanceSerpElementItem** | quoted market indexes |[optional]|
**graph_items** | **List[Optional[GraphItems]]** | values on graph |[optional]|