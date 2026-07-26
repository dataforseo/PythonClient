# DomainAnalyticsWhoisOverviewLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | <em>total amount of results in our database relevant to your request</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**offset** | **StrictInt** | <em> results offset value specified in POST request</em> |[optional]|
**offset_token** | **StrictStr** |  |[optional]|
**items** | **List[Optional[DomainAnalyticsWhoisOverviewLiveItem]]** | <em>contains ranking and traffic data</em> |[optional]|