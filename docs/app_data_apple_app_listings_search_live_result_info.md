# AppDataAppleAppListingsSearchLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | <em>the total number of relevant results in the database</em> |[optional]|
**count** | **StrictInt** | <em>the number of items in the results array</em> |[optional]|
**offset** | **StrictInt** | <em>offset in the results array of returned apps</em> |[optional]|
**offset_token** | **StrictStr** | <em>token for subsequent requests</em><br>you can use this parameter in the POST request to avoid timeouts while trying to obtain over 100,000 results in a single request |[optional]|
**items** | **List[Optional[AppDataAppleAppListingsSearchLiveItem]]** | <em>array of apps and related data</em> |[optional]|