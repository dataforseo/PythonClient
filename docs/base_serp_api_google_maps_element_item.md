# BaseSerpApiGoogleMapsElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em> absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**domain** | **StrictStr** | <em>domain in SERP</em> |[optional]|
**title** | **StrictStr** | <em>title of the element</em> |[optional]|
**url** | **StrictStr** | <em>search URL with refinement parameters</em> |[optional]|
**rating** | **RatingInfo** | <em>the element's rating </em><br>the popularity rate based on reviews and displayed in SERP |[optional]|
**rating_distribution** | **Dict[str, Optional[StrictInt]]** | <em>the distribution of ratings of the business entity</em><br>the object displays the number of 1-star to 5-star ratings, as reviewed by users |[optional]|