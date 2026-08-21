# SerpApiGoogleFinanceExploreMarketTrendsElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | <em>title of the market trends element</em><br>example: <code>Europe, Middle East, and Africa</code> |[optional]|
**sub_title** | **StrictStr** | <em>sub-title of the market trends element</em> |[optional]|
**url** | **StrictStr** | <em>URL to finance pair on Google Finance</em> |[optional]|
**items** | **List[Optional[BaseSerpApiGoogleFinanceElementItem]]** | <em>market indexes data</em><br>array of items containing market indexes data;<br>possible <code>type</code> of items: <code>google_finance_asset_pair_element</code>, <code>google_finance_market_instrument_element</code>, <code>google_finance_market_index_element</code> |[optional]|