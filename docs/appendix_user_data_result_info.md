# AppendixUserDataResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**login** | **StrictStr** | <em>your login</em> |[optional]|
**timezone** | **StrictStr** | <em>your time zone</em><br><strong>can be set in your profile settings</strong> |[optional]|
**rates** | **AppendixRatesData** | <em>your API rates</em> |[optional]|
**money** | **AppendixMoneyData** | <em>section of your spending, USD</em> |[optional]|
**price** | **AppendixPriceData** | <em>pricing</em> |[optional]|
**backlinks_subscription_expiry_date** | **StrictStr** | <em>expiry date of the backlinks api subscription</em><br>date and time when the current subscription to Backlinks API expires;<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2025-06-15 12:57:46 +00:00</code><br><strong>Note:</strong> if there is no active subscription to Backlinks API, the value equals <code>null</code> |[optional]|
**llm_mentions_subscription_expiry_date** | **StrictStr** | <em>expiry date of the llm mentions api subscription</em><br>date and time when the current subscription to LLM Mentions API expires;<br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2026-02-28 14:01:38 +00:00</code><br><strong>Note:</strong> if there is no active subscription to LLM Mentions API, the value equals <code>null</code> |[optional]|