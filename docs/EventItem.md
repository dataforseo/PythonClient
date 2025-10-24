# EventItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**position** | **string** | the alignment of the element in SERP<br>can take the following values:<br>left, right |[optional]|
**xpath** | **string** | the XPath of the element |[optional]|
**title** | **string** | title of the element |[optional]|
**description** | **string** | description of the results element in SERP |[optional]|
**url** | **string** | search URL with refinement parameters |[optional]|
**image_url** | **string** | URL of the image featured in the element |[optional]|
**event_dates** | **EventDates** | dates when the event takes place<br>if there are none, equals null |[optional]|
**location_info** | **LocationInfo** | information about the event’s venue |[optional]|
**information_and_tickets** | **AiModeLinkElementInfo[]** | additional information and ticket purchase options |[optional]|