from setuptools import setup, find_packages
import pathlib

README = (pathlib.Path(__file__).parent / "README.md").read_text()

setup(
    name="hanapin",
    version="0.1.3",
    description="Simple web search library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/TheBoringDude/hanapin",
    author="Real Python",
    author_email="info@realpython.com",
    license="MIT",
    project_urls={"Bug Tracker": "https://github.com/TheBoringDude/hanapin/issues"},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude="tests"),
    include_package_data=True,
    install_requires=["requests", "bs4", "lxml"],
)