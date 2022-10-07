# Basic Calculator(calculatorfirstversion)
## pip install calculatorfirstversion
***
This calculator is a basic version of a calculation that can perform simple arithmetic operations including Addition, Subtraction, Multiplication, Division, Modulus, Exponentiation, and Floor division. The name of functions are as below


> **Addition : add_numbers**

> **Subtraction : sub_numbers**

> **Multiplication : mult_numbers**

> **Division : div_numbers**

> **Modulus : mod_numbers**

> **Exponentiation : squ_number**

> **Floor division : fdiv_numbers**

---
---

## To build your first pypi package 

1. Create a package
    - Prepare your code to share
    - Create the **__init__.py** file

2. Create the **License** and **README** files
    - License.txt will tell users the terms and conditions under which they can use your package. 
    Go to   and copy and past into your file the [MIT license](https://opensource.org/licenses/MIT)

    - README.md will simply tell users what your package is

3. Create **setup.py** file 
	
4. Install the required packages with _pip_ or _pip3_

    - **Setuptools**  
    - **Twine**
    


5. Run the command to generate your source distribution : 

> python setup.py sdist bdist_wheel


6. Register yourself
> https://pypi.org/account/register

7. Run the command to upload package :

> twine upload --repository-url https://upload.pypi.org/legacy/ dist/*


8. Test the package  
> pip install   _packagename_
