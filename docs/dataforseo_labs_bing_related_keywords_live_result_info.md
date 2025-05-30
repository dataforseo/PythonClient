# DataforseoLabsBingRelatedKeywordsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**seed_keyword** | **StrictStr** | keyword in a POST array |[optional]|
**seed_keyword_data** | **KeywordDataInfo** | keyword data for the seed keyword<br>fields in the array are identical to that of keyword_data |[optional]|
**location_code** | **StrictFloat** | location code in a POST array |[optional]|
**language_code** | **StrictStr** | language code in a POST array |[optional]|
**total_count** | **StrictFloat** | total amount of results in our database relevant to your request |[optional]|
**items_count** | **StrictFloat** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[DataforseoLabsRelatedKeywordsLiveItem]]** | contains keywords and related data |[optional]|