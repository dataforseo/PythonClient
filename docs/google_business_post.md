# GoogleBusinessPost


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank among all the listed updates<br>absolute position among all present elements |[optional]|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values: right |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**author** | **StrictStr** | author of the post |[optional]|
**snippet** | **StrictStr** | additional content of a post |[optional]|
**post_text** | **StrictStr** | main content of a post |[optional]|
**url** | **StrictStr** | url of a post |[optional]|
**images_url** | **StrictStr** | url of an image included in the post |[optional]|
**post_date** | **StrictStr** | date when a post was published<br>in the following format:<br>'mm/dd/yyyy hh:mm:ss' |[optional]|
**timestamp** | **StrictStr** | time when a post was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**links** | **List[Optional[LinkElement]]** | links included in the post |[optional]|