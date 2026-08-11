# YoutubeSubtitles


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em> absolute rank in SERP for the target domain</em><br>absolute position among all the elements in SERP |[optional]|
**text** | **StrictStr** | <em>text translated in subtitles</em> |[optional]|
**start_time** | **StrictFloat** | <em>the second subtitled text starts</em> |[optional]|
**end_time** | **StrictFloat** | <em>the second subtitled text ends</em> |[optional]|
**duration_time** | **StrictFloat** | <em>duration of subtitles in seconds</em> |[optional]|