# KeywordProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**se_type** | **StrictStr** | search engine type |[optional]|
**core_keyword** | **StrictStr** | main keyword in a groupcontains the main keyword in a group determined by the synonym clustering algorithmif the value is null, our database does not contain any keywords the corresponding algorithm could identify as synonymous with keyword |[optional]|
**synonym_clustering_algorithm** | **StrictStr** | the algorithm used to identify synonymspossible values:keyword_metrics - indicates the algorithm based on keyword_info parameterstext_processing - indicates the text-based algorithmif the value is null, our database does not contain any keywords the corresponding algorithm could identify as synonymous with keyword |[optional]|
**keyword_difficulty** | **StrictInt** | difficulty of ranking in the first top-10 organic results for a keywordindicates the chance of getting in top-10 organic results for a keyword on a logarithmic scale from 0 to 100;calculated by analysing, among other parameters, link profiles of the first 10 pages in SERP;learn more about the metric in this help center guide |[optional]|
**detected_language** | **StrictStr** | detected language of the keywordindicates the language of the keyword as identified by our system |[optional]|
**is_another_language** | **StrictBool** | detected language of the keyword is different from the set languageif true, the language set in the request does not match the language determined by our system for a given keyword |[optional]|
**words_count** | **StrictInt** | number of words in the keywordindicates how many words the keyword consists of |[optional]|