# GoogleReviewsSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values;<br>positions of elements with different type values are omitted from rank_group;<br>always equals 0 for desktop |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP<br>always equals 0 for desktop |[optional]|
**reviews_count** | **StrictInt** | the number of reviews |[optional]|
**rating** | **RatingElement** | the element’s rating<br>the popularity rate based on reviews and displayed in SERP |[optional]|
**place_id** | **StrictStr** | the identifier of a place |[optional]|
**feature** | **StrictStr** | the additional feature of the review |[optional]|
**cid** | **StrictStr** | google-defined client id |[optional]|