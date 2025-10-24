# GoogleBusinessQuestionItem

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **string** | type of element |[optional]|
**rank_group** | **number** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **number** | absolute rank among all the elements |[optional]|
**question_id** | **string** | ID of the question |[optional]|
**url** | **string** | URL of the question |[optional]|
**profile_image_url** | **string** | URL of the user’s profile image |[optional]|
**profile_url** | **string** | URL of the user’s profile |[optional]|
**profile_name** | **string** | displayed name of the user |[optional]|
**question_text** | **string** | current text of the question |[optional]|
**original_question_text** | **string** | original text of the question |[optional]|
**time_ago** | **string** | estimated time when the question was posted |[optional]|
**timestamp** | **string** | exact time when the question was posted |[optional]|
**items** | **GoogleBusinessAnswerElement[]** | array of items<br>items within google_business_question_item |[optional]|