# pythonPlayPlay
My first python scripts

### Notes:

- Keywords:
  `True`, `False`, and `None` are capitalized, the rest of the

### Boolean behavior examples:
- True == 1 => True  
- False == 0 => True  
- True + True == 2 => True  

### `None`:
  None is a special constant in Python that represents the absence of a value
  or a null value. It is an object of its own datatype, the NoneType. We cannot
  create multiple None objects but can assign it to variables.
  We must take special care thet `None` does not imply `False`, `0` or an empty
  list, dictionary, string etc.  

  Void functions that do not return anything will return a None object
  automatically. None is also returned by functions in which the program flow
  does not encounter a return statement.    

- example:
  ```
    def a_void_function():
      a = 1
      b = 2
      c = a + b

    x = a_void_function()
    print(x)

    Output: None
  ```
  and one where only some return cases are handled:  
  ```
    def improper_return_function(a):
        if (a % 2) == 0:
            return True

    x = improper_return_function(2)
    y = improper_return_function(3)

    print(x) => True
    print(y) => None
  ```
### `not` operator:  
- similar to JavaScript `!`

### `as` operator:  
- used to create alias while importing a module.  
  - example:  
    `import math as myAlias`  

### `break` and `continue`:  
- used in `for` and `while` loops to alter default behavior  
  -  `break` ends the current iteration AND the loop  
  -  `continue` end the current iteration but continues the loops  
