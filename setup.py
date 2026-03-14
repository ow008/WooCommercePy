from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="WooCommercePy",
    version="1.0.0",
    author="ow008",
    author_email="joeballer194@gmail.com",
    description="A modern Python wrapper for the WooCommerce REST API with model classes and intuitive methods",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ow008/WooCommercePy",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.31.0",
    ],
    keywords="woocommerce api wrapper ecommerce",
)
