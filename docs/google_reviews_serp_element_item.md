# GoogleReviewsSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**reviews_count** | **StrictFloat** | the number of reviews |[optional]|
**rating** | **BusinessDataRatingInfo** | the element’s rating<br>the popularity rate based on reviews and displayed in SERP |[optional]|
**place_id** | **StrictStr** | the identifier of a place |[optional]|
**feature** | **StrictStr** | the additional feature of the review |[optional]|
**cid** | **StrictStr** | google-defined client id |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|