from setuptools import setup


with open("README.md", "r") as fp:
    long_description = fp.read()

setup(
    name='hellocdk',
    version='0.0.2',

    descritption="A test CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    py_modules=["hellocdk"],
    package_dir={'': 'src'},

    install_requires=[
        "aws-cdk.core",
        "aws-cdk.aws-s3"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: GNU General Public License v3.0",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)