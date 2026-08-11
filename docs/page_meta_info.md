# PageMetaInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | <em>page title</em> |[optional]|
**charset** | **StrictInt** | <em><a href='https://en.wikipedia.org/wiki/Code_page' target='_blank' rel='noopener noreferrer'>code page</a></em><br>example: <code>65001</code> |[optional]|
**follow** | **StrictBool** | <em>indicates whether a page's 'meta robots' allows crawlers to follow the links on the page</em><br>if <code>false</code>, the page's 'meta robots' tag contains 'nofollow' parameter instructing crawlers not to follow the links on the page |[optional]|
**generator** | **StrictStr** | <em>meta tag generator</em> |[optional]|
**htags** | **Dict[str, Optional[List[Optional[StrictStr]]]]** | <em>HTML header tags</em> |[optional]|
**description** | **StrictStr** | <em>content of the meta description tag</em> |[optional]|
**favicon** | **StrictStr** | <em>favicon of the page</em> |[optional]|
**meta_keywords** | **StrictStr** | <em>content of the <code>keywords</code> meta tag</em> |[optional]|
**canonical** | **StrictStr** | <em>canonical page</em> |[optional]|
**internal_links_count** | **StrictInt** | <em>number of internal links on the page</em> |[optional]|
**external_links_count** | **StrictInt** | <em>number of external links on the page</em> |[optional]|
**inbound_links_count** | **StrictInt** | <em>number of internal links pointing at the page</em> |[optional]|
**images_count** | **StrictInt** | <em>number of images on the page</em> |[optional]|
**images_size** | **StrictInt** | <em>total size of images on the page measured in bytes</em> |[optional]|
**scripts_count** | **StrictInt** | <em>number of scripts on the page</em> |[optional]|
**scripts_size** | **StrictInt** | <em>total size of scripts on the page measured in bytes</em> |[optional]|
**stylesheets_count** | **StrictInt** | <em>number of stylesheets on the page</em> |[optional]|
**stylesheets_size** | **StrictInt** | <em>total size of stylesheets on the page measured in bytes</em> |[optional]|
**title_length** | **StrictInt** | <em>length of the <code>title</code> tag in characters</em> |[optional]|
**description_length** | **StrictInt** | <em>length of the <code>description</code> tag in characters</em> |[optional]|
**render_blocking_scripts_count** | **StrictInt** | <em>number of scripts on the page that block page rendering</em> |[optional]|
**render_blocking_stylesheets_count** | **StrictInt** | <em>number of CSS styles on the page that block page rendering</em> |[optional]|
**cumulative_layout_shift** | **StrictFloat** | <em>Core Web Vitals metric measuring the layout stability of the page</em><br>measures the sum total of all individual layout shift scores for every unexpected layout shift that occurs during the entire lifespan of the page. <a href='https://web.dev/cls/'>Learn more.</a> |[optional]|
**meta_title** | **StrictStr** | <em>meta title of the page</em><br>meta tag in the head section of an HTML document that defines the title of a page |[optional]|
**content** | **HtmlContentInfo** | <em>overall information about content of the page</em> |[optional]|
**deprecated_tags** | **List[Optional[StrictStr]]** | <em>deprecated tags on the page</em> |[optional]|
**duplicate_meta_tags** | **List[Optional[StrictStr]]** | <em>duplicate meta tags on the page</em> |[optional]|
**spell** | **HunspellInfo** | <em>spellcheck</em><br><a href='http://hunspell.github.io/' target='_blank' rel='noopener noreferrer'>hunspell</a> spellcheck errors |[optional]|
**social_media_tags** | **Dict[str, Optional[StrictStr]]** | <em>object of social media tags found on the page</em><br>contains social media tags and their content<br>supported tags include but are not limited to <a href='https://ogp.me/'>Open Graph</a> and <a href='https://developer.twitter.com/en/docs/twitter-for-websites/cards/guides/getting-started'>Twitter card</a> |[optional]|
**broken_html** | **OnPageResourceIssueInfo** | resource errors and warnings |[optional]|