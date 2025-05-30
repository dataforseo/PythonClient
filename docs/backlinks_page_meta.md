# BacklinksPageMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | page title |[optional]|
**canonical** | **StrictStr** | canonical page |[optional]|
**internal_links_count** | **StrictFloat** | number of internal links on the page |[optional]|
**external_links_count** | **StrictFloat** | number of external links on the page |[optional]|
**images_count** | **StrictFloat** | number of images on the page |[optional]|
**words_count** | **StrictFloat** | number of words on the page |[optional]|
**page_spam_score** | **StrictFloat** | spam score of the page<br>learn more about how the metric is calculated on this help center page |[optional]|
**social_media_tags** | **Dict[str, Optional[StrictStr]]** | array of social media tags found on the page<br>contains social media tags and their content<br>supported tags include but are not limited to Open Graph and Twitter card |[optional]|
**h_1** | **List[Optional[StrictStr]]** | h1 tag<br>content of h1 tags |[optional]|
**h_2** | **List[Optional[StrictStr]]** | h2 tag<br>content of h2 tags |[optional]|
**h_3** | **List[Optional[StrictStr]]** | h3 tag<br>content of h3 tags |[optional]|
**images_alt** | **List[Optional[StrictStr]]** | content of alt tags |[optional]|
**powered_by** | **List[Optional[StrictStr]]** | CMS details |[optional]|
**language** | **StrictStr** | page content language<br>example:<br>en |[optional]|
**charset** | **StrictStr** | character encoding<br>examples:<br>utf-8 |[optional]|
**platform_type** | **List[Optional[StrictStr]]** | type of a platform |[optional]|
**technologies** | **Dict[str, Optional[StrictStr]]** | website technologies |[optional]|