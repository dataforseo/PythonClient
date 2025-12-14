# AiOptimizationLLmMentionsKeywordElement


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**keyword** | **StrictStr** | target keyword<br>required field if you don’t specify domain<br>you can specify up to 2000 characters in the keyword field<br>all %## will be decoded (plus character ‘+’ will be decoded to a space character)<br>if you need to use the “%” character for your keyword, please specify it as “%25”;<br>if you need to use the “+” character for your keyword, please specify it as “%2B”<br>learn more about rules and limitations of keyword and keywords fields in |[optional]|
**match_type** | **StrictStr** | target keyword match type<br>defines how the specified keyword is matched<br>optional field<br>possible values:<br>word_match – full-text search for terms that match the specified seed keyword with additional words included before, after, or within the key phrase (e.g., search for “light” will return results with “light bulb”, “light switch”);<br>partial_match – substring search that finds all instances containing the specified sequence of characters, even if it appears inside a longer word (e.g., search for “light” will return results with “lighting”, “highlight”);<br>default value: word_match |[optional]|
**search_scope** | **List[Optional[StrictStr]]** | target domain search scope<br>optional field<br>possible values:<br>any, sources, search_results<br>default value: any |[optional]|
**search_filter** | **StrictStr** | target domain search filter<br>optional field<br>possible values:<br>include, exclude<br>default value: include |[optional]|