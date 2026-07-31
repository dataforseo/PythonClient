# DataforseoLabsleAppIntersectionLiveItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**keyword_data** | **KeywordDataInfo** | <em>keyword data for the returned keyword</em> |[optional]|
**intersection_result** | **Dict[str, Optional[GooglePlaySearchOrganic]]** | <em>contains SERP data for the returned <code>keyword</code></em><br>data will be provided in separate arrays for each app ID you specified in the <code>app_ids</code> object when setting a task;<br>depending on the number of specified app IDs, it can contain from 1 to 20 arrays named respectively |[optional]|