# SerpApiProductConsiderationsExpandedElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | <em>title of the carousel item</em> |[optional]|
**featured_title** | **StrictStr** | <em>the title of the featured snippets source page</em> |[optional]|
**breadcrumb** | **StrictStr** | <em>breadcrumb of the Ad element in SERP</em> |[optional]|
**snippet** | **StrictStr** | <em>text alongside the link title</em> |[optional]|
**domain** | **StrictStr** | <em>source domain</em> |[optional]|
**url** | **StrictStr** | <em>relevant URL</em> |[optional]|
**timestamp** | **StrictStr** | <em>date and time when the result was published</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**related_searches** | **List[Optional[StrictStr]]** |  |[optional]|
**about_this_result** | **AboutThisResultElement** | <em>contains information from the 'About this result' panel</em><br><strong>Note:</strong> element no longer appears in SERP and has been deprecated in SERP API |[optional]|