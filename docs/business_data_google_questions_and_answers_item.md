# BusinessDataGoogleQuestionsAndAnswersItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictFloat** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictFloat** | absolute rank among all the elements |[optional]|
**question_id** | **StrictStr** | ID of the question |[optional]|
**url** | **StrictStr** | URL of the question |[optional]|
**profile_image_url** | **StrictStr** | URL of the user’s profile image |[optional]|
**profile_url** | **StrictStr** | URL of the user’s profile |[optional]|
**profile_name** | **StrictStr** | displayed name of the user |[optional]|
**question_text** | **StrictStr** | current text of the question |[optional]|
**original_question_text** | **StrictStr** | original text of the question |[optional]|
**time_ago** | **StrictStr** | estimated time when the question was posted |[optional]|
**timestamp** | **StrictStr** | exact time when the question was posted |[optional]|
**items** | **List[Optional[GoogleBusinessAnswerElement]]** | array of google business question items with answers<br>possible item types: google_business_question_item |[optional]|