# AnalysisContentInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**content_type** | **StrictStr** | type of content<br>example:<br>page_content, comment |[optional]|
**title** | **StrictStr** | title of the result |[optional]|
**main_title** | **StrictStr** | page title |[optional]|
**previous_title** | **StrictStr** | title of the previous content block |[optional]|
**level** | **StrictFloat** | title heading level<br>indicates h-tag level from 1 (top) to 6 (bottom) |[optional]|
**author** | **StrictStr** | author of the content |[optional]|
**snippet** | **StrictStr** | content snippet |[optional]|
**snippet_length** | **StrictFloat** | character length of the snippet |[optional]|
**social_metrics** | **List[Optional[Facebook]]** | social media engagement metrics<br>data on social media interactions associated with the content based on website embeds developed and supported by social media platforms |[optional]|
**highlighted_text** | **StrictStr** | highlighted text from the snippet |[optional]|
**language** | **StrictStr** | content language<br>to obtain a full list of available languages, refer to the Languages endpoint |[optional]|
**sentiment_connotations** | **Dict[str, Optional[StrictInt]]** | sentiment connotations<br>contains sentiments (emotional reactions) related to the given citation and probability index per each sentiment<br>possible sentiment connotations: anger, happiness, love, sadness, share, fun |[optional]|
**connotation_types** | **Dict[str, Optional[StrictInt]]** | connotation types<br>contains types of sentiments (sentiment polarity) related to the given citation and probability index per each sentiment type<br>possible sentiment connotation types: positive, negative, neutral |[optional]|
**text_category** | **List[Optional[StrictFloat]]** | text category<br>to obtain a full list of available categories, refer to the Categories endpoint |[optional]|
**date_published** | **StrictStr** | date and time when the content was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2017-01-24 13:20:59 +00:00 |[optional]|
**content_quality_score** | **StrictFloat** | content quality score<br>this value is calculated based on the number of words, sentences and characters the content contains |[optional]|
**semantic_location** | **StrictStr** | semantic location<br>indicates semantic element in HTML where the target keyword citation is located<br>example:<br>article, header |[optional]|
**rating** | **ContentRatingInfo** | content rating<br>rating related to content_info |[optional]|
**group_date** | **StrictStr** | citation group date and time<br>indicates content publication date or date and time when our crawler visited the page for the first time;<br>this field can be used to group citations by date and display citation trends;<br>date and time are provided in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2017-01-24 13:20:59 +00:00 |[optional]|