# Modules and Testing Lab

This lab focuses on practicing modules and testing in Python by implementing factorial functions using iteration and recursion, as well as a "clumsy" factorial function. Tests are also provided for each of these functions.

---

## Factorial Functions

### `factorial_iterative(n)`

Calculates the factorial of a positive integer `n` using iteration.

### `factorial_recursion(n)`

Calculates the factorial of a positive integer `n` using recursion.

### `clumsy(n)`

Calculates the "clumsy" factorial of a positive integer `n`.

---

## Testing

Tests are provided for each function in their respective test files:

- **Test for `factorial_iterative` Function:**
  - Located in `test_factorial_iterative.py`.
- **Test for `factorial_recursion` Function:**
  - Located in `test_factorial_recursion.py`.
- **Test for `clumsy` Function:**
  - Located in `test_clumsy.py`.

---

## How to Run Tests

1. **Create a Virtual Environment:**

   Before running the tests, it's recommended to create and activate a virtual environment to isolate the project's dependencies. You can create a virtual environment named `venv` in the root directory of your project with the following command: ```python -m venv venv```


2. **Activate the Virtual Environment:**

To activate the virtual environment, use the appropriate command based on your operating system:

- **Windows:**

  ```
  venv\Scripts\activate
  ```

- **Unix or MacOS:**

  ```
  source venv/bin/activate
  ```

Once activated, you should see the name of the virtual environment in your command prompt, indicating that it's active.

3. **Navigate to the Root Directory of the Project:**

Make sure you are in the root directory of your project before proceeding further.

4. **Install the Required Dependencies:**

Run the following command to install the required dependencies: ```pip install -r requirements.txt```


5. **Execute All Tests:**

Once the dependencies are installed, execute all tests using the following command: ```pytest```. This will run all the tests in the project.

 
