# EventItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**position** | **StrictStr** | <em>the alignment of the element in SERP</em><br>can take the following values:<br><code>left</code>, <code>right</code> |[optional]|
**xpath** | **StrictStr** | <em>the <a href='https://en.wikipedia.org/wiki/XPath' rel='noopener noreferrer' target='_blank'>XPath</a> of the element</em> |[optional]|
**title** | **StrictStr** | <em>title of the element</em> |[optional]|
**description** | **StrictStr** | <em>description of the results element in SERP</em> |[optional]|
**url** | **StrictStr** | <em>search URL with refinement parameters</em> |[optional]|
**image_url** | **StrictStr** | <em>URL of the image featured in the element</em> |[optional]|
**event_dates** | **EventDates** | <em>dates when the event takes place</em><br>if there are none, equals <code>null</code> |[optional]|
**location_info** | **LocationInfo** | <em>information about the event's venue</em> |[optional]|
**information_and_tickets** | **List[Optional[AiModeLinkElementInfo]]** | <em>additional information and ticket purchase options</em> |[optional]|