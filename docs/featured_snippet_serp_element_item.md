# FeaturedSnippetSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em> absolute rank in SERP</em><br>absolute position among all the elements found in SERP<strong>note</strong> values are returned in the ascending order, with values corresponding to advanced SERP features omitted from the results;<br>to get all items (including SERP features and rich snippets) with their positions, please refer to the <a href='https://docs.dataforseo.com/v3/serp/google/organic/live/advanced/?php'>Google Organiс Advanced SERP</a> endpoint |[optional]|
**domain** | **StrictStr** | <em>domain of the ad element in SERP</em> |[optional]|
**title** | **StrictStr** | <em>title of the ad element in SERP</em> |[optional]|
**description** | **StrictStr** | <em>description of the ad element in SERP</em> |[optional]|
**url** | **StrictStr** | <em>relevant URL of the ad element in SERP</em> |[optional]|
**breadcrumb** | **StrictStr** | <em>breadcrumb of the ad element in SERP</em> |[optional]|
**featured_title** | **StrictStr** | title |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**images** | **List[Optional[AiModeImagesElementInfo]]** | images of the element<br>if there are none, equals null |[optional]|
**table** | **Table** | table present in the element<br>the header and content of the table present in the element |[optional]|