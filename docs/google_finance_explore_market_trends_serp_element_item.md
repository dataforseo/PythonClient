# GoogleFinanceExploreMarketTrendsSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictFloat** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictFloat** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**title** | **StrictStr** | title of the market trends element<br>example: Europe, Middle East, and Africa |[optional]|
**sub_title** | **StrictStr** | sub-title of the market trends element |[optional]|
**url** | **StrictStr** | URL to finance pair on Google Finance |[optional]|
**items** | **List[Optional[BaseGoogleFinanceSerpElementItem]]** | market indexes data<br>array of items containing market indexes data;<br>possible type of items: google_finance_asset_pair_element, google_finance_market_instrument_element, google_finance_market_index_element |[optional]|