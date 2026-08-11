# HtmlContentInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**plain_text_size** | **StrictInt** | <em>total size of the text on the page measured in bytes</em> |[optional]|
**plain_text_rate** | **StrictFloat** | plaintext rate value<br>plain_text_size to size ratio |[optional]|
**plain_text_word_count** | **StrictInt** | <em>number of words on the page</em> |[optional]|
**automated_readability_index** | **StrictFloat** | <em><a href='https://en.wikipedia.org/wiki/Automated_readability_index' target='_blank' rel='noopener noreferrer'>Automated Readability Index</a></em> |[optional]|
**coleman_liau_readability_index** | **StrictFloat** | <em><a href='https://en.wikipedia.org/wiki/Coleman%E2%80%93Liau_index' target='_blank' rel='noopener noreferrer'>Coleman–Liau Index</a></em> |[optional]|
**dale_chall_readability_index** | **StrictFloat** | <em><a href='https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula' target='_blank' rel='noopener noreferrer'>Dale–Chall Readability Index</a></em> |[optional]|
**flesch_kincaid_readability_index** | **StrictFloat** | <em><a href='https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests' target='_blank' rel='noopener noreferrer'>Flesch–Kincaid Readability Index</a></em> |[optional]|
**smog_readability_index** | **StrictFloat** | <em><a href='https://en.wikipedia.org/wiki/SMOG' target='_blank' rel='noopener noreferrer'>SMOG Readability Index</a></em> |[optional]|
**description_to_content_consistency** | **StrictFloat** | <em>consistency of the meta <code>description</code> tag with the page content</em><br>measured from 0 to 1 |[optional]|
**title_to_content_consistency** | **StrictFloat** | <em>consistency of the meta <code>title</code> tag with the page content</em><br>measured from 0 to 1 |[optional]|
**meta_keywords_to_content_consistency** | **StrictFloat** | <em>consistency of meta <code>keywords</code>tag with the page content</em><br>measured from 0 to 1 |[optional]|