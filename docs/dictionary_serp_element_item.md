# DictionarySerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | title of the result in SERP |[optional]|
**url** | **StrictStr** | relevant URL of the Ad element in SERP |[optional]|
**domain** | **StrictStr** | domain in SERP |[optional]|
**breadcrumb** | **StrictStr** | breadcrumb of the Ad element in SERP |[optional]|
**keyword** | **StrictStr** | keyword highlighted in the result |[optional]|
**snippet** | **StrictStr** | snippet of the element |[optional]|
**text** | **StrictStr** | description of the results element in SERP |[optional]|
**links** | **List[Optional[LinkElement]]** | sitelinks<br>the links shown below some of search results<br>if there are none, equals null |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>note: calculate_rectangles parameter is not yet available when setting tasks for Baidu search engine, that’s why rectangle always equals null |[optional]|