# AnalysisContentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | type of content example: page_content, comment | [optional] 
**title** | **str** | title of the result | [optional] 
**main_title** | **str** | page title | [optional] 
**previous_title** | **str** | title of the previous content block | [optional] 
**level** | **int** | title heading level indicates h-tag level from 1 (top) to 6 (bottom) | [optional] 
**author** | **str** | author of the content | [optional] 
**snippet** | **str** | content snippet | [optional] 
**snippet_length** | **int** | character length of the snippet | [optional] 
**social_metrics** | [**List[SocialMetricsInfo]**](SocialMetricsInfo.md) | social media engagement metrics data on social media interactions associated with the content based on website embeds developed and supported by social media platforms | [optional] 
**highlighted_text** | **str** | highlighted text from the snippet | [optional] 
**language** | **str** | content language to obtain a full list of available languages, refer to the Languages endpoint | [optional] 
**sentiment_connotations** | [**SentimentConnotationInfo**](SentimentConnotationInfo.md) |  | [optional] 
**connotation_types** | [**ConnotationTypeInfo**](ConnotationTypeInfo.md) |  | [optional] 
**text_category** | **List[int]** | text category to obtain a full list of available categories, refer to the Categories endpoint | [optional] 
**date_published** | **str** | date and time when the content was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59 +00:00 | [optional] 
**content_quality_score** | **int** | content quality score this value is calculated based on the number of words, sentences and characters the content contains | [optional] 
**semantic_location** | **str** | semantic location indicates semantic element in HTML where the target keyword citation is located example: article, header | [optional] 
**rating** | [**ContentAnalysisRatingInfo**](ContentAnalysisRatingInfo.md) |  | [optional] 
**group_date** | **str** | citation group date and time indicates content publication date or date and time when our crawler visited the page for the first time; this field can be used to group citations by date and display citation trends; date and time are provided in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2017-01-24 13:20:59 +00:00 | [optional] 

## Example

```python
from dataforseo_client.models.analysis_content_info import AnalysisContentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisContentInfo from a JSON string
analysis_content_info_instance = AnalysisContentInfo.from_json(json)
# print the JSON string representation of the object
print AnalysisContentInfo.to_json()

# convert the object into a dict
analysis_content_info_dict = analysis_content_info_instance.to_dict()
# create an instance of AnalysisContentInfo from a dict
analysis_content_info_form_dict = analysis_content_info.from_dict(analysis_content_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


