# Autocomplete


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>group rank in SERP</em><br>position within a group of elements with identical <code>type</code> values<br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank in SERP</em><br>absolute position among all the elements in SERP |[optional]|
**relevance** | **StrictInt** | <em>relevance of suggested keyword</em><br>represents the relevant of the autocomplete suggestion to the target keyword<br>can take values from <code>500</code> to <code>2000</code><br>the higher the value, the more relevant is the suggestion<br><strong>Note:</strong> only available for the following <code>client</code>:<br><code>chrome/chrome-omni</code> |[optional]|
**suggestion** | **StrictStr** | <em>google autocomplete keyword suggestion</em> |[optional]|
**suggestion_type** | **StrictStr** | <em>google autocomplete suggestion type</em><br><strong>Note:</strong> only available for the following <code>client</code>:<br><code>chrome/chrome-omni</code> |[optional]|
**search_query_url** | **StrictStr** | <em>url to search results</em><br>url to search results relevant to the google autocomplete suggestion |[optional]|
**thumbnail_url** | **StrictStr** | <em>url of the thumbnail image</em><br>url of the thumbnail image of the google autocomplete suggestion<br><strong>Note:</strong> only available for the following <code>client</code>:<br><code>gws-wiz</code><br><code>gws-wiz-serp</code> |[optional]|
**highlighted** | **List[Optional[StrictStr]]** | <em>keywords highlighted in autocomplete</em><br>contains a list of google autocomplete suggestions that are highlighted in the search bar;<br><strong>Note:</strong> array is only available for the following <code>client</code>:<br><code>gws-wiz</code><br><code>psy-ab</code><br><code>gws-wiz-local</code> |[optional]|