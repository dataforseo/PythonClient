# BaseSerpApiGoogleMapsElementItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**domain** | **string** | domain in SERP |[optional]|
**title** | **string** | title of the element |[optional]|
**url** | **string** | search URL with refinement parameters |[optional]|
**rating** | **RatingInfo** | the element’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**rating_distribution** | **{ [key: string]: number; }** | the distribution of ratings of the business entity<br>the object displays the number of 1-star to 5-star ratings, as reviewed by users |[optional]|