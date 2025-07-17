# LocalPack


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**domain** | **StrictStr** | domain in SERP |[optional]|
**phone** | **StrictStr** | phone number |[optional]|
**url** | **StrictStr** | search URL with refinement parameters |[optional]|
**is_paid** | **StrictBool** | indicates whether the element is an ad |[optional]|
**rating** | **RatingElement** | the item’s rating <br>the popularity rate based on reviews and displayed in SERP |[optional]|
**cid** | **StrictStr** | google-defined client id<br>unique id of a local establishment;<br>can be used with Google Reviews API to get a full list of reviews |[optional]|
**rectangle** | **Any** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>in this case, will equal null |[optional]|