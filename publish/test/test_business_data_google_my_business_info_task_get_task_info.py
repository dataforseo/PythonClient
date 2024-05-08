# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.business_data_google_my_business_info_task_get_task_info import BusinessDataGoogleMyBusinessInfoTaskGetTaskInfo

class TestBusinessDataGoogleMyBusinessInfoTaskGetTaskInfo(unittest.TestCase):
    """BusinessDataGoogleMyBusinessInfoTaskGetTaskInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BusinessDataGoogleMyBusinessInfoTaskGetTaskInfo:
        """Test BusinessDataGoogleMyBusinessInfoTaskGetTaskInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BusinessDataGoogleMyBusinessInfoTaskGetTaskInfo`
        """
        model = BusinessDataGoogleMyBusinessInfoTaskGetTaskInfo()
        if include_optional:
            return BusinessDataGoogleMyBusinessInfoTaskGetTaskInfo(
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
                    dataforseo_client.models.business_data_google_my_business_info_task_get_result_info.BusinessDataGoogleMyBusinessInfoTaskGetResultInfo(
                        keyword = '', 
                        se_domain = '', 
                        location_code = 56, 
                        language_code = '', 
                        check_url = '', 
                        datetime = '', 
                        item_types = [
                            ''
                            ], 
                        items_count = 56, 
                        items = [
                            dataforseo_client.models.base_business_data_serp_element_item.BaseBusinessDataSerpElementItem()
                            ], )
                    ]
            )
        else:
            return BusinessDataGoogleMyBusinessInfoTaskGetTaskInfo(
        )
        """

    def testBusinessDataGoogleMyBusinessInfoTaskGetTaskInfo(self):
        """Test BusinessDataGoogleMyBusinessInfoTaskGetTaskInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()