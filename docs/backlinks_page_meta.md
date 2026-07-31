# BacklinksPageMeta


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | <em>page title</em> |[optional]|
**canonical** | **StrictStr** | <em>canonical page</em> |[optional]|
**internal_links_count** | **StrictInt** | <em>number of internal links on the page</em> |[optional]|
**external_links_count** | **StrictInt** | <em>number of external links on the page</em> |[optional]|
**images_count** | **StrictInt** | <em>number of images on the page</em> |[optional]|
**words_count** | **StrictInt** | <em>number of words on the page</em> |[optional]|
**page_spam_score** | **StrictInt** | <em>spam score of the page</em><br>learn more about how the metric is calculated on <a href='https://dataforseo.com/help-center/what-is-spam-score-and-how-is-it-calculated' rel='noopener noreferrer' target='_blank'>this help center page</a> |[optional]|
**social_media_tags** | **Dict[str, Optional[StrictStr]]** | <em>array of social media tags found on the page</em><br>contains social media tags and their content<br>supported tags include but are not limited to <a href='https://ogp.me/'>Open Graph</a> and <a href='https://developer.twitter.com/en/docs/twitter-for-websites/cards/guides/getting-started'>Twitter card</a> |[optional]|
**h_1** | **List[Optional[StrictStr]]** | <em>h1 tag</em><br>content of <code>h1</code> tags |[optional]|
**h_2** | **List[Optional[StrictStr]]** | <em>h2 tag</em><br>content of <code>h2</code> tags |[optional]|
**h_3** | **List[Optional[StrictStr]]** | <em>h3 tag</em><br>content of <code>h3</code> tags |[optional]|
**images_alt** | **List[Optional[StrictStr]]** | <em>content of <code>alt</code> tags</em> |[optional]|
**powered_by** | **List[Optional[StrictStr]]** | <em>CMS details</em> |[optional]|
**language** | **StrictStr** | <em>page content language</em><br>example:<br><code>en</code> |[optional]|
**charset** | **StrictStr** | <em>character encoding</em><br>examples:<br><code>utf-8</code> |[optional]|
**platform_type** | **List[Optional[StrictStr]]** | <em>type of a platform</em> |[optional]|
**technologies** | **Dict[str, Optional[StrictStr]]** | <em>website technologies</em> |[optional]|