# Loan Qualifier Application

---

## Technologies

This project leverages python 3.9 with the following packages:
* [sys](https://docs.python.org/3/library/sys.html) - Allow for operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter. 

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entry-point.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [pathlib](https://docs.python.org/3/library/pathlib.html#module-pathlib) - Pathlib is a module which provides an object API for working with files and directories. 

* [csv](https://docs.python.org/3/library/csv.html) - For reading and writing csv files. 

---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
    
```
All other imports are part of the standard library of python 3.9

---

## Usage

To use the Loan Qualifier Application simply clone the repository and run the **app.py**:

```python
python app.py
```

Upon launching the Loan Qualifying Application you will be greeted with the following prompts (please also see CLI input screenshot below).

The Appliation will first ask for the location of the Bank rate sheet input file location and name

* input file name and location

The Application will ask you to Input your
* credit_score
* debt
* income
* loan_amount
* home_value

If there are no qualifying loans, application will exit

if there are qualifying loans, application will prompt you to save file with the qualifying loans (Y/n). 
* Save file

if Y, application will prompt for
* File Output Path
* File Name 

![Loan Qualifying Application CLI](images/loan_qualifying_app.png)

---

## Contributors

This project was created by Niels de Haan (nlsdhn@gmail.com)

---

## License

MIT
