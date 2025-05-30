# BacklinksTimeseriesNewLostSummaryLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**target** | **StrictStr** | target from a POST array |[optional]|
**date_from** | **StrictStr** | starting date of the time range<br>in the UTC format: “yyyy-mm-dd”<br>example:<br>2019-01-01 |[optional]|
**date_to** | **StrictStr** | ending date of the time range<br>in the UTC format: 'yyyy-mm-dd'<br>example:<br>'2019-01-15' |[optional]|
**group_range** | **StrictStr** | group_range from the POST array |[optional]|
**items_count** | **StrictFloat** | the number of results returned in the items array |[optional]|
**items** | **List[Optional[BacklinksTimeseriesNewLostSummaryLiveItem]]** | contains relevant backlinks and referring domains data |[optional]|