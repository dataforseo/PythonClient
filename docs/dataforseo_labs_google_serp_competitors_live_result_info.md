# DataforseoLabsGoogleSerpCompetitorsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**seed_keywords** | **List[Optional[StrictStr]]** | <em>keywords specified in the request</em><br><strong>keyword is returned with decoded %## (plus character '+' will be decoded to a space character)</strong> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em><br>if there is no data, then the value is_<code>null</code>n |[optional]|
**total_count** | **StrictInt** | <em>the total amount of results in our database relevant to your request</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[DataforseoLabsGoogleSerpCompetitorsLiveItem]]** | <em>contains detected SERP competitors and related data</em> |[optional]|