# SerpApiGoogleFinanceDetailsElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**badges** | **List[Optional[StrictStr]]** | google finance badges relevant to the element<br>example: Futures Contract |[optional]|
**previous_close** | **StrictFloat** | value of the previous close |[optional]|
**start_day_range** | **StrictFloat** | value of the start day range |[optional]|
**end_day_range** | **StrictFloat** | value of the end day range |[optional]|
**start_year_range** | **StrictFloat** | value of the start year range |[optional]|
**end_year_range** | **StrictFloat** | value of the end year range |[optional]|
**market_cap** | **StrictFloat** | market cap value |[optional]|
**volume** | **StrictFloat** | total volume value |[optional]|
**avg_volume** | **StrictFloat** | average volume value |[optional]|
**pe_ratio** | **StrictFloat** | price-earnings ratio |[optional]|
**dividend_yield** | **StrictFloat** | dividend yield value |[optional]|
**primary_exchange** | **StrictStr** | primary exchange value |[optional]|
**ytd_return** | **StrictFloat** | year-to-date return value |[optional]|
**expense_ratio** | **StrictFloat** | expense ratio value |[optional]|
**category** | **StrictStr** | category name |[optional]|
**net_assets** | **StrictFloat** |  |[optional]|
**yield_** | **StrictFloat** | yield value |[optional]|
**front_load** | **StrictFloat** | front load value |[optional]|
**market_segment** | **StrictStr** | name of the relevant market segment |[optional]|
**open_interest** | **StrictFloat** | open interest value |[optional]|
**settlement_price** | **StrictFloat** | settlement price value |[optional]|
**cdp_climate_change_score** | **StrictStr** | climate change score by carbon disclosure project methodology |[optional]|
**metrics_currency** | **StrictStr** | currency of the metrics |[optional]|