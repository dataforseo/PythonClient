# LocalPackSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the row |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**domain** | **StrictStr** | domain in the URL |[optional]|
**phone** | **StrictStr** | phone number |[optional]|
**url** | **StrictStr** | URL |[optional]|
**is_paid** | **StrictBool** | indicates whether the element is an ad |[optional]|
**rating** | **BusinessDataRatingInfo** | the element’s rating<br>the popularity rate based on reviews and displayed in SERP |[optional]|
**cid** | **StrictStr** | google-defined client id |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|