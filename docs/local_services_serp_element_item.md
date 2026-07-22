# LocalServicesSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values;<br>positions of elements with different type values are omitted from rank_group;<br>always equals 0 for desktop |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP<br>always equals 0 for desktop |[optional]|
**title** | **StrictStr** | title of the row |[optional]|
**url** | **StrictStr** | URL of the third-party review source |[optional]|
**domain** | **StrictStr** | domain of the website hosting the video |[optional]|
**items** | **List[Optional[LocalServicesElement]]** | contains arrays of elements available in the list |[optional]|