# LocalPackSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values;<br>positions of elements with different type values are omitted from rank_group;<br>always equals 0 for desktop |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP<br>always equals 0 for desktop |[optional]|
**title** | **StrictStr** | reference page title |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**domain** | **StrictStr** | domain in the URL |[optional]|
**phone** | **StrictStr** | phone number |[optional]|
**url** | **StrictStr** | URL |[optional]|
**is_paid** | **StrictBool** | indicates whether the element is an ad |[optional]|
**rating** | **RatingElement** | the element’s rating<br>the popularity rate based on reviews and displayed in SERP |[optional]|
**cid** | **StrictStr** | google-defined client id |[optional]|