# AiModePriceInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**current** | **StrictInt** | <em>current price</em><br>indicates the current price of the shopping element |[optional]|
**regular** | **StrictFloat** | <i>regular price</i><br>indicates the regular price of the shopping element |[optional]|
**max_value** | **StrictFloat** | <i>the maximum price</i><br>indicates the maximum price of the shopping element |[optional]|
**currency** | **StrictStr** | <i>currency of the listed price</i><br>ISO code of the currency applied to the price |[optional]|
**is_price_range** | **StrictBool** | <i>price is provided as a range</i><br>indicates whether a price is provided in a range |[optional]|
**displayed_price** | **StrictStr** | <i>price string in the result</i><br>raw price string as provided in the result |[optional]|