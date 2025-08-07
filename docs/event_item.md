# EventItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**position** | **StrictStr** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**xpath** | **StrictStr** | the XPath of the element |[optional]|
**title** | **StrictStr** | title of the element |[optional]|
**description** | **StrictStr** | description of the results element in SERP |[optional]|
**url** | **StrictStr** | search URL with refinement parameters |[optional]|
**image_url** | **StrictStr** | URL of the image featured in the element |[optional]|
**event_dates** | **EventDates** | dates when the event takes place<br>if there are none, equals null |[optional]|
**location_info** | **LocationInfo** | information about the event’s venue |[optional]|
**information_and_tickets** | **List[Optional[AiModeLinkElementInfo]]** | additional information and ticket purchase options |[optional]|