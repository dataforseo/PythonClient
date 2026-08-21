# KeywordProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | <em>search engine type</em> |[optional]|
**core_keyword** | **StrictStr** | <em>main keyword in a group</em><br>contains the main keyword in a group determined by the synonym clustering algorithm<br>if the value is <code>null</code>, our database does not contain any keywords the corresponding algorithm could identify as synonymous with <code>keyword</code> |[optional]|
**synonym_clustering_algorithm** | **StrictStr** | <em>the algorithm used to identify synonyms</em><br>possible values:<br><code>keyword_metrics</code> - indicates the algorithm based on <code>keyword_info</code> parameters<br><code>text_processing</code> - indicates the text-based algorithm<br>if the value is <code>null</code>, our database does not contain any keywords the corresponding algorithm could identify as synonymous with <code>keyword</code> |[optional]|
**keyword_difficulty** | **StrictInt** | <em>difficulty of ranking in the first top-10 organic results for a keyword</em><br>indicates the chance of getting in top-10 organic results for a keyword on a logarithmic scale from 0 to 100;<br>calculated by analysing, among other parameters, link profiles of the first 10 pages in SERP;<br>learn more about the metric in <a href='https://dataforseo.com/help-center/what-is-keyword-difficulty-and-how-is-it-calculated' target='_blank' rel='noopener noreferrer'>this help center guide</a> |[optional]|
**detected_language** | **StrictStr** | <em>detected language of the keyword</em><br>indicates the language of the keyword as identified by our system |[optional]|
**is_another_language** | **StrictBool** | <em>detected language of the keyword is different from the set language</em><br>if <code>true</code>, the language set in the request does not match the language determined by our system for a given keyword |[optional]|
**words_count** | **StrictInt** | <em>number of words in the keyword</em><br>indicates how many words the keyword consists of |[optional]|