import setuptools

# HERE = pathlib.Path(__file__).parent
   
setuptools.setup(
    name='calculatorfirstversion',
    version='0.0.1',
    author="Fatemeh Honarvar",
    author_email="el.honarvar@gmail.com",
    description="This is a very basic calculator",
    # long_description=(HERE / "README.md").read_text(),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)