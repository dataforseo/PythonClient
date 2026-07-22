# LocalPackSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values;<br>positions of elements with different type values are omitted from rank_group;<br>always equals 0 for desktop |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP<br>always equals 0 for desktop |[optional]|
**title** | **StrictStr** | title of the row |[optional]|
**description** | **StrictStr** | description of the link |[optional]|
**domain** | **StrictStr** | domain of the website hosting the video |[optional]|
**phone** | **StrictStr** | phone number |[optional]|
**booking_url** | **StrictStr** | URL of the booking page |[optional]|
**url** | **StrictStr** | URL of the third-party review source |[optional]|
**is_paid** | **StrictBool** | indicates whether the element is an ad |[optional]|
**rating** | **RatingInfo** | the element’s rating<br>the popularity rate based on reviews and displayed in SERP;<br>if there is none, equals null |[optional]|
**cid** | **StrictStr** | google-defined client id |[optional]|