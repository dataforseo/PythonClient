# SerpApiGoogleFinanceFinancialElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**quarterly_metrics** | **List[Optional[GoogleFinanceMetricsBundleInfo]]** | <em>quarterly google finance metrics</em> |[optional]|
**annual_metrics** | **List[Optional[GoogleFinanceMetricsBundleInfo]]** | <em>annual google finance metrics</em> |[optional]|