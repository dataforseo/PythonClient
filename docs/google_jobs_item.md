# GoogleJobsItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**job_id** | **StrictStr** | ID of the job on Google Jobs |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**employer_name** | **StrictStr** | name of the employer |[optional]|
**employer_url** | **StrictStr** | URL to the employer’s website |[optional]|
**employer_image_url** | **StrictStr** | URL to the image used in the job posting |[optional]|
**location** | **StrictStr** | location for which the job vacancy is posted |[optional]|
**source_name** | **StrictStr** | original source of the job vacancy |[optional]|
**source_url** | **StrictStr** | URL to the original source of the job vacancy |[optional]|
**salary** | **StrictStr** | the salary indicated in the job vacancy<br>if the salary isn’t indicated, this field will equal null |[optional]|
**contract_type** | **StrictStr** | employment contract type |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**time_ago** | **StrictStr** | indicates how long ago the job vacancy was posted |[optional]|
**rectangle** | **RectangleInfo** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP;<br>in this case, will equal null |[optional]|