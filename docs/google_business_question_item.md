# GoogleBusinessQuestionItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**rank_group** | **StrictInt** | <em>position within a group of elements with identical <code>type</code> values</em><br>positions of elements with different <code>type</code> values are omitted from <code>rank_group</code> |[optional]|
**rank_absolute** | **StrictInt** | <em>absolute rank among all the elements</em> |[optional]|
**question_id** | **StrictStr** | <em>ID of the question</em> |[optional]|
**url** | **StrictStr** | <em>URL of the question</em> |[optional]|
**profile_image_url** | **StrictStr** | <em>URL of the user's profile image</em> |[optional]|
**profile_url** | **StrictStr** | <em>URL of the user's profile</em> |[optional]|
**profile_name** | **StrictStr** | <em>displayed name of the user</em> |[optional]|
**question_text** | **StrictStr** | <em>current text of the question</em> |[optional]|
**original_question_text** | **StrictStr** | <em>original text of the question</em> |[optional]|
**time_ago** | **StrictStr** | <em>estimated time when the question was posted</em> |[optional]|
**timestamp** | **StrictStr** | <em>exact time when the question was posted</em> |[optional]|
**items** | **List[Optional[GoogleBusinessAnswerElement]]** | <em>array of items</em><br>items within <code>google_business_question_item</code> |[optional]|