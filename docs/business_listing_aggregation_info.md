# BusinessListingAggregationInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**top_categories** | **Dict[str, Optional[StrictInt]]** | the most mentioned related categories<br>top categories displayed with the number of businesses in each category |[optional]|
**top_countries** | **Dict[str, Optional[StrictInt]]** | the most mentioned counties<br>country codes with the biggest number of businesses in the category |[optional]|
**websites_count** | **StrictInt** | number of unique websites |[optional]|
**count** | **StrictInt** | number of unique entities |[optional]|
**top_attributes** | **Dict[str, Optional[StrictInt]]** | the most mentioned service details<br>service details of a business entity displayed in a form of checks and the number of entities mentioning each attribute |[optional]|
**top_place_topics** | **Dict[str, Optional[StrictInt]]** | top keywords mentioned in customer reviews<br>contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword |[optional]|