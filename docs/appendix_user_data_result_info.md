# AppendixUserDataResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**login** | **StrictStr** | your login |[optional]|
**timezone** | **StrictStr** | your time zone<br>can be set in your profile settings |[optional]|
**rates** | **AppendixRatesData** | your API rates |[optional]|
**money** | **AppendixMoneyData** | section of your spending, USD |[optional]|
**price** | **AppendixPriceData** | pricing |[optional]|
**backlinks_subscription_expiry_date** | **StrictStr** | expiry date of the backlinks api subscription<br>date and time when the current subscription to Backlinks API expires;<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br>2025-06-15 12:57:46 +00:00<br>Note: if there is no active subscription to Backlinks API, the value equals null |[optional]|