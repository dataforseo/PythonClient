# ContentGenerationTextSummaryLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**sentences** | **StrictInt** | number of sentences found in the target text |[optional]|
**paragraphs** | **StrictInt** | number of paragraphs found in the target text |[optional]|
**words** | **StrictInt** | number of words found in the target text |[optional]|
**characters_without_spaces** | **StrictInt** | number of characters without spaces found in the target text |[optional]|
**characters_with_spaces** | **StrictInt** | number of characters with spaces found in the target text |[optional]|
**words_per_sentence** | **StrictFloat** | average number of words per sentence in the target text |[optional]|
**characters_per_word** | **StrictFloat** | average number of characters per word in the target text |[optional]|
**vocabulary_density** | **StrictFloat** | vocabulary density of the target text |[optional]|
**keyword_density** | **Dict[str, Optional[StrictInt]]** | keyword density of the target text<br>contains most common words and their count |[optional]|
**automated_readability_index** | **StrictFloat** | Automated Readability Index |[optional]|
**coleman_liau_index** | **StrictFloat** | Coleman–Liau Index |[optional]|
**flesch_kincaid_grade_level** | **StrictFloat** | Flesch–Kincaid Readability Index |[optional]|
**smog_readability_index** | **StrictFloat** | SMOG Readability Index |[optional]|
**spelling_errors** | **StrictInt** | number of spelling errors found in the target text |[optional]|
**grammar_errors** | **StrictInt** | number of grammar errors found in the target text |[optional]|