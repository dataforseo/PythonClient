# SerpApiGoogleFinanceDetailsElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**badges** | **List[Optional[StrictStr]]** | <em>google finance badges relevant to the element</em><br>example: <code>Futures Contract</code> |[optional]|
**previous_close** | **StrictFloat** | <em>value of the previous close</em> |[optional]|
**start_day_range** | **StrictFloat** | <em>value of the start day range</em> |[optional]|
**end_day_range** | **StrictFloat** | <em>value of the end day range</em> |[optional]|
**start_year_range** | **StrictFloat** | <em>value of the start year range</em> |[optional]|
**end_year_range** | **StrictFloat** | <em>value of the end year range</em> |[optional]|
**market_cap** | **StrictFloat** | <em>market cap value</em> |[optional]|
**volume** | **StrictFloat** | <em>total volume value</em> |[optional]|
**avg_volume** | **StrictFloat** | <em>average volume value</em> |[optional]|
**pe_ratio** | **StrictFloat** | <em>price-earnings ratio</em> |[optional]|
**dividend_yield** | **StrictFloat** | <em>dividend yield value</em> |[optional]|
**primary_exchange** | **StrictStr** | <em>primary exchange value</em> |[optional]|
**ytd_return** | **StrictFloat** | <em>year-to-date return value</em> |[optional]|
**expense_ratio** | **StrictFloat** | <em>expense ratio value</em> |[optional]|
**category** | **StrictStr** | <em>category name</em> |[optional]|
**net_assets** | **StrictFloat** |  |[optional]|
**yield_** | **StrictFloat** | <em>yield value</em> |[optional]|
**front_load** | **StrictFloat** | <em>front load value</em> |[optional]|
**market_segment** | **StrictStr** | <em>name of the relevant market segment</em> |[optional]|
**open_interest** | **StrictFloat** | <em>open interest value</em> |[optional]|
**settlement_price** | **StrictFloat** | <em>settlement price value</em> |[optional]|
**cdp_climate_change_score** | **StrictStr** | <em>climate change score by carbon disclosure project methodology</em> |[optional]|
**metrics_currency** | **StrictStr** | <em>currency of the metrics</em> |[optional]|