# BaseSerpApiGoogleMapsElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**domain** | **StrictStr** | domain in SERP |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**url** | **StrictStr** | search URL with refinement parameters |[optional]|
**rating** | **RatingElement** | the element’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**rating_distribution** | **Dict[str, Optional[StrictInt]]** | the distribution of ratings of the business entity<br>the object displays the number of 1-star to 5-star ratings, as reviewed by users |[optional]|