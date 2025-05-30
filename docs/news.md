# News


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**title** | **StrictStr** | title of the news article |[optional]|
**url** | **StrictStr** | URL to the page of the market index on Google Finance |[optional]|
**source** | **StrictStr** | name of the news source<br>name of the website where the news article is published |[optional]|
**image_url** | **StrictStr** | featured image URL<br>URL of the news article’s featured image |[optional]|
**timestamp** | **StrictStr** | date and time of the value readout<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2025-02-10 09:40:00 +00:00 |[optional]|
**quotes** | **List[Optional[BaseGoogleFinanceSerpElementItem]]** | market indexes quoted in the news article<br>information about market indexes quoted in the google_finance_news_element |[optional]|