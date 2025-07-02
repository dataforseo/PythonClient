# GoogleFinanceAssetPairElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**base_symbol** | **StrictStr** | identifier of the base asset in a pair<br>example: EUR |[optional]|
**quote_symbol** | **StrictStr** | identifier of the quote asset in a pair<br>example: USD |[optional]|
**base_display_name** | **StrictStr** | full name of the base asset in a pair<br>example: Euro |[optional]|
**quote_display_name** | **StrictStr** | full name of the base asset in a pair<br>example: Euro |[optional]|
**price** | **StrictFloat** | value of the base asset compared to the quote asset |[optional]|
**price_delta** | **StrictFloat** | change in price<br>change in price at a given timestamp |[optional]|
**identifier** | **StrictStr** | identifier of the element<br>full identifier of the element that consists from ticker and market_identifier<br>example: PX1:INDEXDB |[optional]|
**displayed_name** | **StrictStr** | name of the market index as displayed on Google Finance<br>example: CAC 40 |[optional]|
**url** | **StrictStr** | URL to the page of the market index on Google Finance |[optional]|
**location** | **StrictStr** | location of the market index<br>example: Europe/Paris |[optional]|
**trend** | **StrictStr** | growth trend of the market index<br>possible values: up, down, stable |[optional]|
**timestamp** | **StrictStr** | date and time of the value readout<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2025-02-10 09:40:00 +00:00 |[optional]|
**percentage_delta** | **StrictFloat** | percentage of change in value of the market index |[optional]|