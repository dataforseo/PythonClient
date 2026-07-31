# BacklinksTimeseriesSummaryLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**target** | **StrictStr** | <em><code>target</code> from a POST array</em> |[optional]|
**date_from** | **StrictStr** | <em>starting date of the time range</em><br>in the UTC format: “yyyy-mm-dd”<br>example:<br><code>2019-01-01</code> |[optional]|
**date_to** | **StrictStr** | <em>ending date of the time range</em><br>in the UTC format: <code>'yyyy-mm-dd'</code><br>example:<br><code>'2019-01-15'</code> |[optional]|
**group_range** | **StrictStr** | group_range from a POST array |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[BacklinksTimeseriesSummaryLiveItem]]** | <em>contains relevant summary data</em> |[optional]|