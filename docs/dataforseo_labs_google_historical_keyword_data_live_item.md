# DataforseoLabsGoogleHistoricalKeywordDataLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**keyword** | **StrictStr** | <em>keyword</em><br><strong>keyword is returned with decoded %## (plus character '+' will be decoded to a space character)</strong> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**history** | **List[Optional[History]]** | <em>array of objects with historical data for the keyword</em> |[optional]|