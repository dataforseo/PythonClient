# ContentAnalysisSentimentAnalysisLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**type** | **StrictStr** | type of element |[optional]|
**positive_connotation_distribution** | **PositiveConnotationDistribution** | citation distribution by sentiment connotation types<br>contains objects with citation counts and relevant data distributed by types of sentiments (sentiment polarity);<br>possible sentiment connotation types: positive, negative, neutral |[optional]|
**sentiment_connotation_distribution** | **SentimentConnotationDistribution** | citation distribution by sentiment connotations<br>contains objects with citation counts and relevant data distributed by sentiments (emotional reactions);<br>possible sentiment connotation types: anger, happiness, love, sadness, share, fun |[optional]|