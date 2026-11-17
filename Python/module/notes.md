# MOdules and packages

**module** is a collection of functions/file
-  built in - time, pickle, csv, math, keyword, abc - must be imported and functions are used with module name
- user-defined - normal.py file with some functions in it

**packages** collection of modules/ folder with files inside it; not available directly, we need to install it
- built in - pandas, sklearn, numpy, matplotlib,   
- user defined - created by user; folder which contains python .py files

to check if installed - try import packagename
ModuelNotFoundError
pip install pacakge

### install packages 
```
pip install package_name
import package_name
```

go to root location of the python is installed -> cmd -> pip install

## SAME PACKAGE

### how to access ALL functions from one module to another within the same package

NOTE- create a package in python root location so its accessible by other packages

```
import modulename #-> to access ALL the functions
module.func() 
```

output we are getting from both current and module file 
cos importing functions also get executed 
avoid it by writing conditions:

execution in done in one moduel also executes in it sparent modeul so the ocndition we specify in n

if __name__=='__main__':
name - take the current file being executed
and it is written in the main file/module

__main__ - the one calling it
__name __ - the current file name

### to access a particular function onyl present in a module

```
from module import func1, func2,... #func1() 
from module import *  #access all
func()
```


## DIFFERENT PACKAGES

packages are all in the same folder/location

## how to access ALL functions from one module to another in DIFFERNT package


```
from package import module
module.func()
```

### to access a particular function onyl present in a module in a different package

```
from package.module import func1, func2
func1()
```
