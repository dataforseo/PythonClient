# YoutubeComment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP for the target domain<br>absolute position among all the elements in SERP |[optional]|
**author_name** | **StrictStr** | name of the author of the comment |[optional]|
**author_thumbnail** | **StrictStr** | the URL of the page where the author’s channel logo is hosted |[optional]|
**author_url** | **StrictStr** | URL of the author’s channel |[optional]|
**text** | **StrictStr** | text of the comment |[optional]|
**publication_date** | **StrictStr** | displayed publication date |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2022-11-15 12:57:46 +00:00 |[optional]|
**likes_count** | **StrictInt** | number of likes on the comment |[optional]|
**reply_count** | **StrictInt** | number of replies on the comment |[optional]|