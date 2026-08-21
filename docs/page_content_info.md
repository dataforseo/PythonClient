# PageContentInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**header** | **PageSectionContentInfo** | <em>parsed content of the header</em><br> |[optional]|
**footer** | **PageSectionContentInfo** | <em>content of the footer of the table</em><br> |[optional]|
**main_topic** | **List[Optional[TopicInfo]]** | <em>main topic on the page</em><br>            you can find more information about topic priority calculation in this <a href='https://dataforseo.com/help-center/difference-between-primary-and-secondary-content#topics' rel='noopener noreferrer' target='_blank'>help center article</a><br> |[optional]|
**secondary_topic** | **List[Optional[TopicInfo]]** | <em>secondary topic on the page</em><br>            you can find more information about topic priority calculation in this <a href='https://dataforseo.com/help-center/difference-between-primary-and-secondary-content#topics' rel='noopener noreferrer' target='_blank'>help center article</a><br> |[optional]|
**ratings** | **List[Optional[ContentRatingInfo]]** | <em>contains objects with rating information for the products displayed on the page</em><br> |[optional]|
**offers** | **List[Optional[ContentOfferInfo]]** | <em>array of products displayed on the page</em><br>            contains objects with information on products displayed on the page |[optional]|
**comments** | **List[Optional[ContentCommentInfo]]** | <em>array of comments displayed on the page</em><br>            contains objects with information on comments related to displayed products |[optional]|
**contacts** | **Contacts** | <em>contact information</em><br>            contains contact information displayed on the page |[optional]|