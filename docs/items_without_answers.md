# ItemsWithoutAnswers


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | position within a group of elements with identical type values<br>positions of elements with different type values are omitted from rank_group |[optional]|
**rank_absolute** | **StrictInt** | absolute rank among all the elements |[optional]|
**question_id** | **StrictStr** | ID of the question |[optional]|
**url** | **StrictStr** | URL of the question |[optional]|
**profile_image_url** | **StrictStr** | URL of the user’s profile image |[optional]|
**profile_url** | **StrictStr** | URL of the user’s profile |[optional]|
**profile_name** | **StrictStr** | displayed name of the user |[optional]|
**question_text** | **StrictStr** | current text of the question |[optional]|
**original_question_text** | **StrictStr** | original text of the question |[optional]|
**time_ago** | **StrictStr** | estimated time when the question was posted |[optional]|
**timestamp** | **StrictStr** | exact time when the question was posted |[optional]|
**items** | **GoogleBusinessAnswerElement** | array of items<br>items within google_business_question_item |[optional]|