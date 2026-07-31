# GoogleBusinessPost


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank among all the listed updates</em><br>absolute position among all present elements |[optional]|
**position** | **StrictStr** | <em>the alignment of the element in SERP</em><br>can take the following values: <code>right</code> |[optional]|
**xpath** | **StrictStr** | <em>the <a href='https://en.wikipedia.org/wiki/XPath'>XPath</a> of the element</em> |[optional]|
**author** | **StrictStr** | <em>author of the post</em> |[optional]|
**snippet** | **StrictStr** | <em>additional content of a post</em> |[optional]|
**post_text** | **StrictStr** | <em>main content of a post</em> |[optional]|
**url** | **StrictStr** | <em>url of a post</em> |[optional]|
**images_url** | **StrictStr** | <em>url of an image included in the post</em> |[optional]|
**post_date** | **StrictStr** | <em>date when a post was published</em><br>in the following format:<br><code>'mm/dd/yyyy hh:mm:ss'</code> |[optional]|
**timestamp** | **StrictStr** | <em>time when a post was published</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**links** | **List[Optional[LinkElement]]** | <em>links included in the post</em> |[optional]|