# DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**top_categories** | **List[Optional[StrictInt]]** | <em>categories for which domains are collected</em> |[optional]|
**organic_etv** | **StrictFloat** | <em>current organic ETV of the domain</em> |[optional]|
**organic_count** | **StrictInt** | <em>current total count of organic SERPs that contain the domain</em> |[optional]|
**organic_is_lost** | **StrictInt** | <em>current number of lost ranked elements</em><br>indicates how many ranked elements of the domain were previously presented in SERPs, but weren’t found during the last check |[optional]|
**organic_is_new** | **StrictInt** | <em>current number of new ranked elements</em><br>indicates how many new ranked elements were found for the domain |[optional]|
**domain** | **StrictStr** | <em>domain found for the specified category</em> |[optional]|
**main_domain** | **StrictStr** | <em>primary domain</em> |[optional]|
**metrics_history** | **Dict[str, Optional[Dict[str, Optional[DataforseoLabsMetricsInfo]]]]** | <em>historical ranking and traffic data of the domain</em> |[optional]|
**metrics_difference** | **Dict[str, Optional[DataforseoLabsMetricsInfo]]** | <em>metrics difference between <code>first_date</code> and <code>second_date</code></em><br>calculated by subtracting domain metrics as of the greater date from domain metrics as of the smaller date |[optional]|