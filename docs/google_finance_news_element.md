# GoogleFinanceNewsElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | <em>title of the news article</em> |[optional]|
**url** | **StrictStr** | <em>URL to the page of the market index on Google Finance</em> |[optional]|
**source** | **StrictStr** | <em>name of the news source</em><br>name of the website where the news article is published |[optional]|
**image_url** | **StrictStr** | <em>featured image URL</em><br>URL of the news article's featured image |[optional]|
**timestamp** | **StrictStr** | <em>date and time of the value readout</em><br>in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code class='long-string'>2025-02-10 09:40:00 +00:00</code> |[optional]|
**quotes** | **List[Optional[BaseSerpApiGoogleFinanceElementItem]]** | <em>market indexes quoted in the news article</em><br>information about market indexes quoted in the <code>google_finance_news_element</code> |[optional]|