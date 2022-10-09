import email
import setuptools

# create folder for code library
# create __init__.py file inside folder
# create setup.py file outside code library
# code files can be added to the quantlib folder and used like a regular package


setuptools.setup(
    name="quantlib",
    version="0.1",
    description="code lib by zfla",
    url="#",
    author="zfla",
    requires=["opencv-python"],
    author_email="",
    packages=setuptools.find_packages(),
    zip_safe=False
)