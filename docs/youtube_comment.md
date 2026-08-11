# YoutubeComment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em> absolute rank in SERP for the target domain</em><br>absolute position among all the elements in SERP |[optional]|
**author_name** | **StrictStr** | <em>name of the author of the comment</em> |[optional]|
**author_thumbnail** | **StrictStr** | <em>the URL of the page where the author's channel logo is hosted</em> |[optional]|
**author_url** | **StrictStr** | <em>URL of the author's channel</em> |[optional]|
**text** | **StrictStr** | <em>text of the comment</em> |[optional]|
**publication_date** | **StrictStr** | <em>displayed publication date</em> |[optional]|
**timestamp** | **StrictStr** | <em>date and time when the result was published</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code>2022-11-15 12:57:46 +00:00</code> |[optional]|
**likes_count** | **StrictInt** | <em>number of likes on the comment</em> |[optional]|
**reply_count** | **StrictInt** | <em>number of replies on the comment</em> |[optional]|