# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.on_page_task_request_info import OnPageTaskRequestInfo

class TestOnPageTaskRequestInfo(unittest.TestCase):
    """OnPageTaskRequestInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OnPageTaskRequestInfo:
        """Test OnPageTaskRequestInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OnPageTaskRequestInfo`
        """
        model = OnPageTaskRequestInfo()
        if include_optional:
            return OnPageTaskRequestInfo(
                target = '',
                max_crawl_pages = 56,
                start_url = '',
                force_sitewide_checks = True,
                priority_urls = [
                    ''
                    ],
                max_crawl_depth = 56,
                crawl_delay = 56,
                store_raw_html = True,
                enable_content_parsing = True,
                support_cookies = True,
                accept_language = '',
                custom_robots_txt = '',
                robots_txt_merge_mode = '',
                custom_user_agent = '',
                browser_preset = '',
                browser_screen_width = 56,
                browser_screen_height = 56,
                browser_screen_scale_factor = 1.337,
                respect_sitemap = True,
                custom_sitemap = '',
                crawl_sitemap_only = True,
                load_resources = True,
                enable_www_redirect_check = True,
                enable_javascript = True,
                enable_xhr = True,
                enable_browser_rendering = True,
                disable_cookie_popup = True,
                custom_js = '',
                validate_micromarkup = True,
                allow_subdomains = True,
                allowed_subdomains = [
                    ''
                    ],
                disallowed_subdomains = [
                    ''
                    ],
                check_spell = True,
                check_spell_language = '',
                check_spell_exceptions = [
                    ''
                    ],
                calculate_keyword_density = True,
                checks_threshold = {
                    'key' : 56
                    },
                disable_sitewide_checks = [
                    ''
                    ],
                disable_page_checks = [
                    ''
                    ],
                switch_pool = True,
                return_despite_timeout = True,
                tag = '',
                pingback_url = ''
            )
        else:
            return OnPageTaskRequestInfo(
        )
        """

    def testOnPageTaskRequestInfo(self):
        """Test OnPageTaskRequestInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
