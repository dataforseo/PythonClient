from setuptools import setup, find_packages  
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
NAME = "dataforseo-client"
VERSION = "2.0.6"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.2.3",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="DataForSEO API documentation",
    author="DataForSeo",
    author_email="info@dataforseo.com",
    url="https://github.com/dataforseo/PythonClient",
    keywords=["OpenAPI", "DataForSEO", "DataForSEO API documentation"],
    install_requires=REQUIRES,
    homepage="https://github.com/dataforseo/PythonClient",
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={"dataforseo_client": ["py.typed"]},
)