# DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**top_categories** | **List[Optional[StrictInt]]** | categories for which domains are collected |[optional]|
**organic_etv** | **StrictFloat** | current organic ETV of the domain |[optional]|
**organic_count** | **StrictInt** | current total count of organic SERPs that contain the domain |[optional]|
**organic_is_lost** | **StrictInt** | current number of lost ranked elements<br>indicates how many ranked elements of the domain were previously presented in SERPs, but weren’t found during the last check |[optional]|
**organic_is_new** | **StrictInt** | current number of new ranked elements<br>indicates how many new ranked elements were found for the domain |[optional]|
**domain** | **StrictStr** | domain found for the specified category |[optional]|
**main_domain** | **StrictStr** | primary domain |[optional]|
**metrics_history** | **Dict[str, Optional[Dict[str, Optional[DataforseoLabsMetricsInfo]]]]** | historical ranking and traffic data of the domain |[optional]|
**metrics_difference** | **Dict[str, Optional[DataforseoLabsMetricsInfo]]** | metrics difference between first_date and second_date<br>calculated by subtracting domain metrics as of the greater date from domain metrics as of the smaller date |[optional]|