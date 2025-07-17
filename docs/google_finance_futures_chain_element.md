# GoogleFinanceFuturesChainElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**expiration_timestamp** | **StrictStr** | futures’ date and time of expiration<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2025-02-10 09:40:00 +00:00 |[optional]|
**symbol** | **StrictStr** | futures’ symbol |[optional]|
**price** | **StrictFloat** | price of the market instrument<br>price of the market instrument at a given timestamp |[optional]|
**price_currency** | **StrictStr** | currency of the price value |[optional]|
**price_delta** | **StrictFloat** | change in price of the market instrument<br>change in price at a given timestamp |[optional]|
**percentage_delta** | **StrictFloat** | percentage of change in value of the market index |[optional]|
**trend** | **StrictStr** | growth trend of the market index<br>possible values: up, down, stable |[optional]|