# ProductConsiderationsExpandedElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | title of the carousel item |[optional]|
**featured_title** | **StrictStr** | the title of the featured snippets source page |[optional]|
**breadcrumb** | **StrictStr** | breadcrumb of the Ad element in SERP |[optional]|
**snippet** | **StrictStr** | text alongside the link title |[optional]|
**domain** | **StrictStr** | domain where a link points |[optional]|
**url** | **StrictStr** | URL of element |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**related_searches** | **List[Optional[StrictStr]]** | search queries related to the elment |[optional]|
**about_this_result** | **AboutThisResultElement** | contains information from the ‘About this result’ panel<br>‘About this result’ panel provides additional context about why Google returned this result for the given query;<br>this feature appears after clicking on the three dots next to most results |[optional]|