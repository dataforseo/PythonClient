# SerpGoogleAutocompleteAdvancedItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | group rank in SERP<br>position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank in SERP<br>absolute position among all the elements in SERP |[optional]|
**relevance** | **StrictInt** | relevance of suggested keyword<br>represents the relevant of the autocomplete suggestion to the target keyword<br>can take values from 500 to 2000<br>the higher the value, the more relevant is the suggestion<br>Note: only available for the following client:<br>chrome/chrome-omni |[optional]|
**suggestion** | **StrictStr** | google autocomplete keyword suggestion |[optional]|
**suggestion_type** | **StrictStr** | google autocomplete suggestion type<br>Note: only available for the following client:<br>chrome/chrome-omni |[optional]|
**search_query_url** | **StrictStr** | url to search results<br>url to search results relevant to the google autocomplete suggestion |[optional]|
**thumbnail_url** | **StrictStr** | url of the thumbnail image<br>url of the thumbnail image of the google autocomplete suggestion<br>Note: only available for the following client:<br>gws-wiz<br>gws-wiz-serp |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | keywords highlighted in autocomplete<br>contains a list of google autocomplete suggestions that are highlighted in the search bar;<br>Note: array is only available for the following client:<br>gws-wiz<br>psy-ab<br>gws-wiz-local |[optional]|