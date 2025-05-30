# FeaturedSnippetSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**domain** | **StrictStr** | domain of the ad element in SERP |[optional]|
**title** | **StrictStr** | title of the ad element in SERP |[optional]|
**description** | **StrictStr** | description of the ad element in SERP |[optional]|
**url** | **StrictStr** | relevant URL of the ad element in SERP |[optional]|
**breadcrumb** | **StrictStr** | breadcrumb of the ad element in SERP |[optional]|
**featured_title** | **StrictStr** | title |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**images** | **List[Optional[ImagesElement]]** | images of the element |[optional]|
**table** | **Table** | results table<br>if there are none, equals null |[optional]|
**rectangle** | **Rectangle** | rectangle parameters<br>contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP<br>equals null if calculate_rectangles in the POST request is not set to true |[optional]|