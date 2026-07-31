# BusinessDataGoogleReviewsTaskGetResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | <em>keyword received in a POST array</em><br><strong>keyword is returned with decoded %## (plus character '+' will be decoded to a space character)</strong> |[optional]|
**type** | **StrictStr** | type of element |[optional]|
**se_domain** | **StrictStr** | <em>search engine domain in a POST array</em> |[optional]|
**location_code** | **StrictInt** | <em>location code in a POST array</em> |[optional]|
**language_code** | **StrictStr** | <em>language code in a POST array</em> |[optional]|
**check_url** | **StrictStr** | <em>direct URL to search engine results</em><br>you can use it to make sure that we provided accurate results |[optional]|
**datetime** | **StrictStr** | <em>date and time when the result was received</em><br>in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”<br>example:<br><code class='long-string'>2019-11-15 12:57:46 +00:00</code> |[optional]|
**title** | **StrictStr** | <em>title of the 'reviews' element in SERP</em><br>the name of the local establishment for which the reviews are collected |[optional]|
**sub_title** | **StrictStr** | <em>subtitle of the 'reviews' element in SERP</em><br>additional information (e.g., address) on the 'reviews' element for which the reviews are collected |[optional]|
**rating** | **RatingInfo** | <em>rating of the corresponding local establishment</em><br>popularity rate based on reviews and displayed in SERP |[optional]|
**feature_id** | **StrictStr** | <em>the unique identifier of the 'reviews' element in SERP</em><br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**place_id** | **StrictStr** | <em>unique identifier of a business location assigned by Google</em><br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**cid** | **StrictStr** | <i>google-defined client id</i><br>unique id of a local establishment<br>learn more about the identifier in <a href='https://dataforseo.com/help-center/what-is-cid-place-id-feature-id' rel='noopener noreferrer' target='_blank'>this help center article</a> |[optional]|
**reviews_count** | **StrictInt** | <em>the total number of reviews</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of reviews items in the results array</em><br>you can get more results by using the <code>depth</code> parameter when setting a task |[optional]|
**items** | **List[Optional[GoogleReviewsSearch]]** | <em>found reviews</em><br>you can get more results by using the <code>depth</code> parameter when setting a task |[optional]|