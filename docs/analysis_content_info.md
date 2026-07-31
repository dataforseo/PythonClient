# AnalysisContentInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**content_type** | **StrictStr** | <em>type of content</em><br>example:<br><code>page_content</code>, <code>comment</code> |[optional]|
**title** | **StrictStr** | <em>title of the result</em> |[optional]|
**main_title** | **StrictStr** | <em>page title</em> |[optional]|
**previous_title** | **StrictStr** | <em>title of the previous content block</em> |[optional]|
**level** | **StrictInt** | <em><code>title</code> heading level</em><br>indicates h-tag level from <code>1</code> (top) to <code>6</code> (bottom) |[optional]|
**author** | **StrictStr** | <em>author of the content</em> |[optional]|
**snippet** | **StrictStr** | <em>content snippet</em> |[optional]|
**snippet_length** | **StrictInt** | <em>character length of the snippet</em> |[optional]|
**social_metrics** | **List[Optional[SocialMetricsInfo]]** | <em>social media engagement metrics</em><br>data on social media interactions associated with the content based on website embeds developed and supported by social media platforms |[optional]|
**highlighted_text** | **StrictStr** | <em>highlighted text from the <code>snippet</code></em> |[optional]|
**language** | **StrictStr** | <em>main language of the domain</em><br>to obtain a full list of available languages, refer to the <a href='/v3/content_analysis/languages/' rel='noopener noreferrer' target='_blank'>Languages</a> endpoint |[optional]|
**sentiment_connotations** | **Dict[str, Optional[StrictInt]]** | <em>sentiment connotations</em><br>contains sentiments (emotional reactions) related to the given citation and probability index per each sentiment<br>possible sentiment connotations: <code>anger</code>, <code>happiness</code>, <code>love</code>, <code>sadness</code>, <code>share</code>, <code>fun</code> |[optional]|
**connotation_types** | **Dict[str, Optional[StrictInt]]** | <em>connotation types</em><br>contains types of sentiments (sentiment polarity) related to the given citation and probability index per each sentiment type<br>possible sentiment connotation types: <code>positive</code>, <code>negative</code>, <code>neutral</code> |[optional]|
**text_category** | **List[Optional[StrictInt]]** | <em>text category</em><br>to obtain a full list of available categories, refer to the <a href='/v3/content_analysis/categories/' rel='noopener noreferrer' target='_blank'>Categories</a> endpoint |[optional]|
**date_published** | **StrictStr** | <em>date and time when the content was published</em><br>in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code>2017-01-24 13:20:59 +00:00</code> |[optional]|
**content_quality_score** | **StrictInt** | <em>content quality score</em><br>this value is calculated based on the number of words, sentences and characters the content contains |[optional]|
**semantic_location** | **StrictStr** | <em>semantic location</em><br>indicates semantic element in HTML where the target keyword citation is located<br>example:<br><code>article</code>, <code>header</code> |[optional]|
**rating** | **ContentRatingInfo** | <em>content rating</em><br>rating related to <code>content_info</code> |[optional]|
**group_date** | **StrictStr** | <em>citation group date and time</em><br>indicates content publication date or date and time when our crawler visited the page for the first time;<br>this field can be used to group citations by date and display citation trends;<br>date and time are provided in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code>2017-01-24 13:20:59 +00:00</code> |[optional]|