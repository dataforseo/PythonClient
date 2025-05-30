# GooglePostsSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**posts_id** | **StrictStr** | the identifier of the google_posts feature |[optional]|
**feature** | **StrictStr** | the additional feature of the review |[optional]|
**cid** | **StrictStr** | google-defined client id |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|