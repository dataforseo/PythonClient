# YoutubeSubtitles


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP for the target domain<br>absolute position among all the elements in SERP |[optional]|
**text** | **StrictStr** | text translated in subtitles |[optional]|
**start_time** | **StrictFloat** | the second subtitled text starts |[optional]|
**end_time** | **StrictFloat** | the second subtitled text ends |[optional]|
**duration_time** | **StrictFloat** | duration of subtitles in seconds |[optional]|