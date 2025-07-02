# AppDataGoogleAppListingsSearchLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | the total number of relevant results in the database |[optional]|
**count** | **StrictInt** | the number of items in the results array |[optional]|
**offset** | **StrictInt** | offset in the results array of returned apps |[optional]|
**offset_token** | **StrictStr** | token for subsequent requests<br>you can use this parameter in the POST request to avoid timeouts while trying to obtain over 100,000 results in a single request |[optional]|
**items** | **List[Optional[AppDataGoogleAppListingsSearchLiveItem]]** | array of apps and related data |[optional]|