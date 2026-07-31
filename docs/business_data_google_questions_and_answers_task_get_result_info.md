# BusinessDataGoogleQuestionsAndAnswersTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword received in a POST array</em><br><strong>keyword is returned with decoded %## (plus character '+' will be decoded to a space character)</strong><br>this field will contain the <code>cid</code> parameter if you specified it in the <code>keyword</code> field when setting a task;<br>example:<br><code>cid:2946633002421908862</code><br>learn more about the parameter in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain as specified in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**cid** | **StrictStr** | <em>google-defined client id</em><br>unique id of a local establishment;<br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' target='_blank' rel='noopener noreferrer'>this help center article</a> |[optional]|
**feature_id** | **StrictStr** | <em> unique identifier of the SERP feature</em> |[optional]|
**item_types** | **List[Optional[StrictStr]]** | <em>item types</em><br>types of search engine results encountered in the <code>items</code> array;<br>possible item types: <code>google_business_question_item</code> |[optional]|
**items_without_answers** | **List[Optional[GoogleBusinessQuestionItem]]** | <em>array of google business question items without answers</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of items in the <code>items</code> array</em> |[optional]|
**items** | **List[Optional[GoogleBusinessQuestionItem]]** | <em> array of items within <code>google_business_question_item</code></em><br>contains answers to the google business questions;<br>the maximum number of answers returned for each question: <code>5</code> <br>possible item types <code>google_business_answer_element</code> |[optional]|