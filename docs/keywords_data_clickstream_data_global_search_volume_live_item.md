# KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | keyword<br>keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character) |[optional]|
**search_volume** | **StrictInt** | clickstream-based average monthly search volume rate<br>represents the (approximate) number of searches for the given keyword idea based on clickstream<br>you can learn more about clickstream search volume in this Help Center article |[optional]|
**country_distribution** | **List[Optional[CountryDistribution]]** | distribution of clickstream by countries<br>represents clickstream-based search volume in available countries, as well as its respective percentage of global search volume |[optional]|