# AiOptimizationLlmMentionsTimeseriesDeltaLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**date** | **StrictStr** | <em>date timestamp</em><br> date format: <code>'yyyy-mm-dd'</code> |[optional]|
**delta_mentions** | **StrictInt** | <em>LLM mentions count delta</em><br>the difference in <code>mentions</code> between the current timestamp and the previous one |[optional]|
**delta_ai_search_volume** | **StrictInt** | <em>LLM mentions count delta</em><br>the difference in <code>ai_search_volume</code> values between the current timestamp and the previous one<br>learn more about this metric <a href='https://dataforseo.com/help-center/how-ai-search-volume-metrics-work-in-the-llm-mentions-timeseries-endpoints' rel='noopener noreferrer' target='_blank'>here</a> |[optional]|