# DictionarySerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**url** | **StrictStr** | relevant URL of the Ad element in SERP |[optional]|
**domain** | **StrictStr** | domain in SERP |[optional]|
**breadcrumb** | **StrictStr** | breadcrumb of the Ad element in SERP |[optional]|
**keyword** | **StrictStr** | keyword highlighted in the result |[optional]|
**snippet** | **StrictStr** | snippet of the element |[optional]|
**text** | **StrictStr** | description of the results element in SERP |[optional]|
**links** | **List[Optional[LinkElement]]** | sitelinks<br>the links shown below some of search results<br>if there are none, equals null |[optional]|