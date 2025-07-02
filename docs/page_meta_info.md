# PageMetaInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**title** | **StrictStr** | page title |[optional]|
**charset** | **StrictInt** | code page<br>example: 65001 |[optional]|
**follow** | **StrictBool** | indicates whether a page’s ‘meta robots’ allows crawlers to follow the links on the page<br>if false, the page’s ‘meta robots’ tag contains “nofollow” parameter instructing crawlers not to follow the links on the page |[optional]|
**generator** | **StrictStr** | meta tag generator |[optional]|
**htags** | **Dict[str, Optional[List[Optional[StrictStr]]]]** | HTML header tags |[optional]|
**description** | **StrictStr** | content of the meta description tag |[optional]|
**favicon** | **StrictStr** | favicon of the page |[optional]|
**meta_keywords** | **StrictStr** | content of the keywords meta tag |[optional]|
**canonical** | **StrictStr** | canonical page |[optional]|
**internal_links_count** | **StrictInt** | number of internal links on the page |[optional]|
**external_links_count** | **StrictInt** | number of external links on the page |[optional]|
**inbound_links_count** | **StrictInt** | number of internal links pointing at the page |[optional]|
**images_count** | **StrictInt** | number of images on the page |[optional]|
**images_size** | **StrictInt** | total size of images on the page measured in bytes |[optional]|
**scripts_count** | **StrictInt** | number of scripts on the page |[optional]|
**scripts_size** | **StrictInt** | total size of scripts on the page measured in bytes |[optional]|
**stylesheets_count** | **StrictInt** | number of stylesheets on the page |[optional]|
**stylesheets_size** | **StrictInt** | total size of stylesheets on the page measured in bytes |[optional]|
**title_length** | **StrictInt** | length of the title tag in characters |[optional]|
**description_length** | **StrictInt** | length of the description tag in characters |[optional]|
**render_blocking_scripts_count** | **StrictInt** | number of scripts on the page that block page rendering |[optional]|
**render_blocking_stylesheets_count** | **StrictInt** | number of CSS styles on the page that block page rendering |[optional]|
**cumulative_layout_shift** | **StrictFloat** | Core Web Vitals metric measuring the layout stability of the page<br>measures the sum total of all individual layout shift scores for every unexpected layout shift that occurs during the entire lifespan of the page. Learn more. |[optional]|
**meta_title** | **StrictStr** | meta title of the page<br>meta tag in the head section of an HTML document that defines the title of a page |[optional]|
**content** | **HtmlContentInfo** | overall information about content of the page |[optional]|
**deprecated_tags** | **List[Optional[StrictStr]]** | deprecated tags on the page |[optional]|
**duplicate_meta_tags** | **List[Optional[StrictStr]]** | duplicate meta tags on the page |[optional]|
**spell** | **SpellInfo** | autocorrection of the search engine<br>if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection |[optional]|
**social_media_tags** | **Dict[str, Optional[StrictStr]]** | object of social media tags found on the page<br>contains social media tags and their content<br>supported tags include but are not limited to Open Graph and Twitter card |[optional]|
**broken_html** | **OnPageResourceIssueInfo** | resource errors and warnings |[optional]|