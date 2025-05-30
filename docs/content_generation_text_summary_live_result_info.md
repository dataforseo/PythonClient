# ContentGenerationTextSummaryLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**sentences** | **StrictFloat** | number of sentences found in the target text |[optional]|
**paragraphs** | **StrictFloat** | number of paragraphs found in the target text |[optional]|
**words** | **StrictFloat** | number of words found in the target text |[optional]|
**characters_without_spaces** | **StrictFloat** | number of characters without spaces found in the target text |[optional]|
**characters_with_spaces** | **StrictFloat** | number of characters with spaces found in the target text |[optional]|
**words_per_sentence** | **StrictFloat** | average number of words per sentence in the target text |[optional]|
**characters_per_word** | **StrictFloat** | average number of characters per word in the target text |[optional]|
**vocabulary_density** | **StrictFloat** | vocabulary density of the target text |[optional]|
**keyword_density** | **Dict[str, Optional[StrictInt]]** | keyword density of the target text<br>contains most common words and their count |[optional]|
**automated_readability_index** | **StrictFloat** | Automated Readability Index |[optional]|
**coleman_liau_index** | **StrictFloat** | Coleman–Liau Index |[optional]|
**flesch_kincaid_grade_level** | **StrictFloat** | Flesch–Kincaid Readability Index |[optional]|
**smog_readability_index** | **StrictFloat** | SMOG Readability Index |[optional]|
**spelling_errors** | **StrictFloat** | number of spelling errors found in the target text |[optional]|
**grammar_errors** | **StrictFloat** | number of grammar errors found in the target text |[optional]|