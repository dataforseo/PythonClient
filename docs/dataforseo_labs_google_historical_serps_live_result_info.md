# DataforseoLabsGoogleHistoricalSerpsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type in a POST array</em> |[optional]|
**keyword** | **StrictStr** | <em>keyword received in a POST array</em><br>            <strong>the keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character)</strong> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**total_count** | **StrictInt** | <em>the total amount of results in our database relevant to your request</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[DataforseoLabsGoogleHistoricalSerpsLiveItem]]** | <em>historical SERPs and related data found in the database</em> |[optional]|