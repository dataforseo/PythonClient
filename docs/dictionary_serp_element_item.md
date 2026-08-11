# DictionarySerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br><br>            position within a group of elements with identical <code>type</code> values<br><br>            positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br><br>            absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | <em>title of the result in SERP</em> |[optional]|
**url** | **StrictStr** | <em> relevant URL of the Ad element in SERP</em> |[optional]|
**domain** | **StrictStr** | <em>domain in SERP</em> |[optional]|
**breadcrumb** | **StrictStr** | <em>breadcrumb of the Ad element in SERP</em> |[optional]|
**keyword** | **StrictStr** | <em>keyword highlighted in the result</em> |[optional]|
**snippet** | **StrictStr** | <em>snippet of the element</em> |[optional]|
**text** | **StrictStr** | <em>description of the results element in SERP</em> |[optional]|
**links** | **List[Optional[LinkElement]]** | <em>sitelinks</em><br><br>            the links shown below some of search results<br><br>            if there are none, equals <code>null</code> |[optional]|