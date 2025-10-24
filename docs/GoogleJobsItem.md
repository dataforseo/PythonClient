# GoogleJobsItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**position** | **string** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**xpath** | **string** | the XPath of the element |[optional]|
**job_id** | **string** | ID of the job on Google Jobs |[optional]|
**title** | **string** | title of the element |[optional]|
**employer_name** | **string** | name of the employer |[optional]|
**employer_url** | **string** | URL to the employer’s website |[optional]|
**employer_image_url** | **string** | URL to the image used in the job posting |[optional]|
**location** | **string** | location for which the job vacancy is posted |[optional]|
**source_name** | **string** | original source of the job vacancy |[optional]|
**source_url** | **string** | URL to the original source of the job vacancy |[optional]|
**salary** | **string** | the salary indicated in the job vacancy<br>if the salary isn’t indicated, this field will equal null |[optional]|
**contract_type** | **string** | employment contract type |[optional]|
**timestamp** | **string** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**time_ago** | **string** | indicates how long ago the job vacancy was posted |[optional]|
**rectangle** | **AiModeRectangleInfo** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP;<br>in this case, will equal null |[optional]|