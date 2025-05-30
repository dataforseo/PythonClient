# ThirdPartyReviewsSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**reviews_count** | **StrictFloat** | the number of reviews |[optional]|
**title** | **StrictStr** | title of the row |[optional]|
**url** | **StrictStr** | URL |[optional]|
**rating** | **BusinessDataRatingInfo** | the element’s rating<br>the popularity rate based on reviews and displayed in SERP |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|