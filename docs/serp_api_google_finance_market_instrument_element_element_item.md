# SerpApiGoogleFinanceMarketInstrumentElementElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**ticker** | **StrictStr** | <em>ticker of the market index</em><br>example: <code>DAX</code> |[optional]|
**price** | **StrictFloat** | <em>value of the base asset compared to the quote asset</em> |[optional]|
**price_delta** | **StrictFloat** | <em>change in price</em><br>change in <code>price</code> at a given <code>timestamp</code> |[optional]|
**price_currency** | **StrictStr** | <em>price currency</em><br>example: <code>USD</code> |[optional]|
**identifier** | **StrictStr** | <em>identifier of the element</em><br>full identifier of the element that consists from <code>ticker</code> and <code>market_identifier</code><br>example: <code>PX1:INDEXDB</code> |[optional]|
**displayed_name** | **StrictStr** | <em>name of the market index as displayed on Google Finance</em><br>example: <code>CAC 40</code> |[optional]|
**url** | **StrictStr** | <em>URL to the page of the market index on Google Finance</em> |[optional]|
**location** | **StrictStr** | <em>location of the market index</em><br>example: <code>Europe/Paris</code> |[optional]|
**trend** | **StrictStr** | <em>growth trend of the market index</em><br>possible values: <code>up</code>, <code>down</code>, <code>stable</code> |[optional]|
**timestamp** | **StrictStr** | <em>date and time of the value readout</em><br>in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'<br>example:<br><code class='long-string'>2025-02-10 09:40:00 +00:00</code> |[optional]|
**percentage_delta** | **StrictFloat** | <em>percentage of change in value of the market index</em> |[optional]|