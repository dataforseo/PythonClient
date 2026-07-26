# BusinessListingAggregationInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**top_categories** | **Dict[str, Optional[StrictInt]]** | <em>the most mentioned related categories</em><br>top categories displayed with the number of businesses in each category |[optional]|
**top_countries** | **Dict[str, Optional[StrictInt]]** | <em>the most mentioned counties</em><br>country codes with the biggest number of businesses in the category |[optional]|
**websites_count** | **StrictInt** | <em>number of unique websites</em> |[optional]|
**count** | **StrictInt** | <em>item types</em><br>the number of items in the <code>items</code> array |[optional]|
**top_attributes** | **Dict[str, Optional[StrictInt]]** | <em>the most mentioned service details</em><br>service details of a business entity displayed in a form of checks and the number of entities mentioning each attribute |[optional]|
**top_place_topics** | **Dict[str, Optional[StrictInt]]** | <em>top keywords mentioned in customer reviews</em><br>contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword |[optional]|