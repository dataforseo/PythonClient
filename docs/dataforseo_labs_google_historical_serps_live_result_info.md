# DataforseoLabsGoogleHistoricalSerpsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**keyword** | **StrictStr** | keyword received in a POST array<br>the keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character) |[optional]|
**location_code** | **StrictFloat** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**total_count** | **StrictFloat** | the number of results returned in the items array |[optional]|
**items_count** | **StrictFloat** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[DataforseoLabsGoogleHistoricalSerpsLiveItem]]** | additional items present in the element<br>if there are none, equals null |[optional]|