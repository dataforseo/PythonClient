# AiOptimizationLlmMentionsTimeseriesNewLostLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**date** | **StrictStr** | date timestamp<br> date format: 'yyyy-mm-dd' |[optional]|
**new_mentions** | **StrictInt** | new LLM mentions<br>indicates the LLM responses that contain the target at the date_to timestamp, did not contain it at the date_from timestamp |[optional]|
**lost_mentions** | **StrictInt** | lost LLM mentions<br>indicates the LLM responses that contained the specified target at the date_from timestamp, do not contain it at the date_to timestamp |[optional]|
**new_ai_search_volume** | **StrictInt** | ai_search_volume increment<br>indicates the increase of ai_search_volume values between the current timestamp and the previous one<br>learn more about this metric here |[optional]|
**lost_ai_search_volume** | **StrictInt** | ai_search_volume decrement<br>indicates the decrease of ai_search_volume values between the current timestamp and the previous one<br>learn more about this metric here |[optional]|