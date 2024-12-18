from setuptools import setup, find_packages 

NAME = "dataforseo-client"
VERSION = "1.0.39"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, <= 2.2.3",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="DataForSEO API documentation",
    author="DataForSEO",
    author_email="info@dataforseo.com",
    url="",
    keywords=["DataForSEO API", "DataForSEO API documentation"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.
    """,  # noqa: E501
    package_data={"dataforseo_client": ["py.typed"]},
)
