# SerpAiSummaryRequestInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**task_id** | **StrictStr** | <em>task identifier</em><br><strong>required field</strong><br>unique identifier of the associated task in the <a href='https://en.wikipedia.org/wiki/Universally_unique_identifier'>UUID</a> format<br>you will be able to use it within <strong>30 days</strong> to request the results of the task at any time |[optional]|
**prompt** | **StrictStr** | <em>AI prompt</em><br>optional field<br>additional task for AI summariser;<br>any form of text, question or information that communicates to AI what response you're looking for;<br>max number of symbols or characters you can specify: <code>2000</code>;<br><strong>note:</strong> your prompt has to be relevant to the keyword specified in the POST request to SERP API |[optional]|
**support_extra** | **StrictBool** | <em>support extra SERP features</em><br>optional field<br>if set to <code>true</code>, the AI model will consider the following extra SERP features, in addition to <code>organic</code> results: <code>answer_box</code>, <code>knowledge_graph</code>, <code>featured_snippet</code>;<br>default value: <code>true</code> |[optional]|
**fetch_content** | **StrictBool** | <em>fetch content from pages in SERPs</em><br>optional field<br>if set to <code>true</code>, the API will fetch the content from pages featured in SERP results, and the AI model will consider this content when generating the summary in the result;<br>default value: <code>false</code> |[optional]|
**include_links** | **StrictBool** | <em>include source links in the summary</em><br>optional field<br>if set to <code>true</code>, the <code>summary</code> field in the API response will contain links to sources of the generated summary;<br>default value: <code>false</code> |[optional]|