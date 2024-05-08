# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.app_data_google_app_reviews_task_get_advanced_task_info import AppDataGoogleAppReviewsTaskGetAdvancedTaskInfo

class TestAppDataGoogleAppReviewsTaskGetAdvancedTaskInfo(unittest.TestCase):
    """AppDataGoogleAppReviewsTaskGetAdvancedTaskInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppDataGoogleAppReviewsTaskGetAdvancedTaskInfo:
        """Test AppDataGoogleAppReviewsTaskGetAdvancedTaskInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppDataGoogleAppReviewsTaskGetAdvancedTaskInfo`
        """
        model = AppDataGoogleAppReviewsTaskGetAdvancedTaskInfo()
        if include_optional:
            return AppDataGoogleAppReviewsTaskGetAdvancedTaskInfo(
                id = '',
                status_code = 56,
                status_message = '',
                time = '',
                cost = 1.337,
                result_count = 56,
                path = [
                    ''
                    ],
                data = dataforseo_client.models.data.data(),
                result = [
                    dataforseo_client.models.app_data_google_app_reviews_task_get_advanced_result_info.AppDataGoogleAppReviewsTaskGetAdvancedResultInfo(
                        app_id = '', 
                        type = '', 
                        se_domain = '', 
                        location_code = 56, 
                        language_code = '', 
                        check_url = '', 
                        datetime = '', 
                        title = '', 
                        rating = dataforseo_client.models.rating_info.RatingInfo(
                            rating_type = '', 
                            value = 1.337, 
                            votes_count = 56, 
                            rating_max = 56, ), 
                        reviews_count = 56, 
                        items_count = 56, 
                        items = [
                            dataforseo_client.models.base_app_data_serp_element_item.BaseAppDataSerpElementItem()
                            ], )
                    ]
            )
        else:
            return AppDataGoogleAppReviewsTaskGetAdvancedTaskInfo(
        )
        """

    def testAppDataGoogleAppReviewsTaskGetAdvancedTaskInfo(self):
        """Test AppDataGoogleAppReviewsTaskGetAdvancedTaskInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()