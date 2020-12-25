import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="welcomesample", # Replace with your own username
    version="0.0.1",
    author="Kota Sai Durga Kamesh",
    author_email="ksdkamesh99@gmail.com",
    description="A Sample Welcome message Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ksdkamesh99/Medium-Blogs/tree/master/Publish%20a%20Python%20package%20like%20a%C2%A0Pro/WelcomeSample",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["welcomesample"],
    package_dir={'':'WelcomeSample/src'},
    install_requires=[]
    
)