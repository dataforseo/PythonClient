# SerpGoogleDatasetAdvancedItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictFloat** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictFloat** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**dataset_id** | **StrictStr** | ID of the dataset |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**image_url** | **StrictStr** | URL of the image<br>the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available) |[optional]|
**scholarly_citations_count** | **StrictFloat** | count of articles that refer to the dataset |[optional]|
**scholarly_articles_url** | **StrictStr** | url of scholarly articles<br>link to the list of scholarly articles on Google Scholar<br>example: https://scholar.google.com/scholar?q=%2210.6084%20m9%20figshare%207427933%20v1%22 |[optional]|
**unique_identifier** | **StrictStr** | digital identifier of an object<br>unique digital identifier of the dataset<br>example: https://doi.org/10.5061/dryad.hmgqnk9m3 |[optional]|
**related_article** | **StrictStr** | link to related article<br>link to the published article that is related to the dataset |[optional]|
**links** | **List[Optional[LinkElement]]** | sitelinks<br>the links shown below some of Google Dataset’s search results<br>if there are none, equals null |[optional]|
**dataset_providers** | **List[Optional[LicensesElement]]** | the list of institutions that provided the dataset |[optional]|
**formats** | **List[Optional[FormatsElement]]** | the list of file formats of the dataset |[optional]|
**authors** | **List[Optional[AuthorsElement]]** | the list of authors of the dataset |[optional]|
**licenses** | **List[Optional[LicensesElement]]** | the list of licenses issued to the dataset |[optional]|
**updated_date** | **StrictStr** | date and time when the result was last updated<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2022-11-27 02:00:00 +00:00 |[optional]|
**area_covered** | **List[Optional[StrictStr]]** | the list of areas covered in the dataset<br>for example: Africa, Global |[optional]|
**period_covered** | **PeriodCovered** | period covered in the dataset |[optional]|
**dataset_description** | **DatasetDescription** | description of the dataset |[optional]|