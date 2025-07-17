# CurrencyBoxSerpElementItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values;<br>positions of elements with different type values are omitted from rank_group;<br>always equals 0 for desktop |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP<br>always equals 0 for desktop |[optional]|
**value** | **StrictFloat** | the value of the rating |[optional]|
**converted_value** | **StrictFloat** | value converted to a requested currency<br>indicates the exact value based on Google Fincance data at the time when our API pulled the results<br>note that exchange rates displayed in the currency_box element may be delayed according to the Google Finance disclaimer |[optional]|
**currency** | **StrictStr** | currency of the listed price<br>ISO code of the currency applied to the price |[optional]|
**converted_currency** | **StrictStr** | converted currency |[optional]|
**timestamp** | **StrictStr** | date and time when the result was published<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2019-11-15 12:57:46 +00:00 |[optional]|
**table** | **Table** | results table<br>if there are none, equals null |[optional]|
**graph** | **Graph** | contains data provided in the graph of the element |[optional]|