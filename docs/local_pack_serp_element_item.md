# LocalPackSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values;<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code>;<br>always equals <code>0</code> for <code>desktop</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP<br>always equals <code>0</code> for <code>desktop</code> |[optional]|
**title** | **StrictStr** | <em>title of the row</em> |[optional]|
**description** | **StrictStr** | <em>description of the link</em> |[optional]|
**domain** | **StrictStr** | <em>domain of the website hosting the video</em> |[optional]|
**phone** | **StrictStr** | <em>phone number</em> |[optional]|
**booking_url** | **StrictStr** | <em>URL of the booking page</em> |[optional]|
**url** | **StrictStr** | <i>URL of the third-party review source</i> |[optional]|
**is_paid** | **StrictBool** | <em>indicates whether the element is an ad</em> |[optional]|
**rating** | **RatingInfo** | <em>the element's rating</em><br>the popularity rate based on reviews and displayed in SERP;<br>if there is none, equals <code>null</code> |[optional]|
**cid** | **StrictStr** | <em>google-defined client id</em> |[optional]|