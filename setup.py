from setuptools import setup, find_packages

setup(
    name="friend-number",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["friend_number"],  # main module file, e.g., friend_number.py
    license="MIT",
    description="A Python package to find and check Pythagoras friend numbers",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Md. Ariful Islam",
    author_email="iamx.ariful.islam@gmail.com",
    url="https://github.com/iamx-ariful-islam/friend-number",
    project_urls={
        "Bug Tracker": "https://github.com/iamx-ariful-islam/friend-number/issues",
        "Documentation": "https://github.com/iamx-ariful-islam/friend-number#readme",
        "Source Code": "https://github.com/iamx-ariful-islam/friend-number",
    },
    install_requires=[
        # no external dependencies — keep empty if pure python
        # example if needed: "numpy >= 1.25.0"
    ],
    keywords=[
        "numbers",
        "friend-number",
        "pythagoras-number",
        "math",
        "number-theory",
        "python-package",
        "python",
        "utility",
        "library",
        "opensource",
        "iamx-ariful-islam",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)