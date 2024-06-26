# [DS-02] Introduction to Python

## What is Python?

**Python** is a programming language, born in 1991. The latest stable version (when this is being written) is Python 3.11. As a programming language, Python can be used by a programmer to write a program that performs a task. Since this course is data-oriented, let us mention a few examples in that line:

* A **web scraping** program that captures data on the current prices published in an e-commerce web site, storing them in a database.

* A **machine learning** program that trains an algorithm that assigns credit scores to borrowers in a lending platform.

* A **pricing algorithm** that estimates the market price of a real estate asset.

These programs are later executed many times without being modified. But you can use Python in other ways. For instance, to examine the variation of the stock price of a specific company, or the structure of the vacation rental market in a specific region. Either for developing a program, which always involves a bit of trial and error, or in a data analysis, we use a basic tool, the **Python interactive interpreter**. We can have several instances of the interpreter, called **kernels**, running independently in our computer. To deal with the Python interpreter, Pythonistas use an app that provides an as interface to the Python interpreter, chosen among the many available choices (see below). 

## Python modules and packages

Many additional resources have been added to Python in the form of **modules**. A module is just a text file containing Python code. Modules are grouped in **libraries**. The **Python Standard Library**, distributed with Python, contains **built-in modules** providing standardized solutions for many problems that occur in everyday programming. For instance, the module `math` provides mathematical functions, while the module `datetime` provides functions for manipulating dates and times.

Other libraries are typically called **packages**, because their elements are packed according to some specific rules which allow you to install and call them together. Python can be extended by more than 300,000 packages. Some big packages like scikit-learn (a machine learning toolkit) have **subpackages**.

Since the basic Python toolkit (without any module) is quite limited, you will need to **import** additional resources for practically everything. Once a module has been imported, all its functions are available. Alternatively, you can import a single function from a module. Resources are imported just for the current kernel. You can only import from packages which are already **installed** in your computer. 

Almost everything in the Python world is open-source. In particular, Python packages are contributed by various agents, such as university professors, freelance programmers, or industry behemoths like Google. This leads to a dynamic ecosystem, where you may find overlapping, dependencies and multiple versions. 

## Python distributions

A **Python distribution** is a software bundle, containing, at least, a Python interpreter and the corresponding version of the standard library. It also includes a collection of packages and one or more package managers for installing, uninstalling or updating packages. All distributions have a **package manager** called `pip`, and some distributions have a specific package manager.

One option for working with Python is to start a Python kernel directly in a **shell** application associated to the operating system of your computer. Shell apps are typically called **Terminal** in Mac/Linux computers and **Prompt** in Windows computers. For this approach to work, the shell app has to find the Python files. This is automatic when the folder where the Python distribution is in the **path** of that shell. In the contrary, you have to know where to find it. 

If you are just starting with Python, you will prefer a friendlier approach. Python distributions provide various interfaces to the Python interpreter. All include a **command line interface** (CLI), which may be a shell-like application or an **integrated development environment** (IDE). A Python IDE provides a Python-aware code editor integrated with the ability to run code from that editor. Details about one of the top popular Python distributions follow.

## The Anaconda distribution

In the data science community, **Anaconda** (`anaconda.com`) is the favorite distribution. The current Anaconda distribution comes with Python 3.10. Anaconda provides all the packages used in this course, so no extra installation is needed. Anyway, Anaconda has a specific package manager, called `conda`. You may need `conda` for more advanced work, because it reviews the packages that are already installed in our computer, keeping track of the dependencies, and solving version conflicts between packages. On the downside, `conda` is much slower than `pip`.

After downloading and installing Anaconda, you can start your Python experience with the **Anaconda Navigator**, which opens in the browser and allows you to choose among different interfaces to the Python interpreter. First, you have **Jupyter Qt Console**, which is a shell-like app with some extra features. Jupyter (Julia/Python/R) is a new name for an older project called **IPython** (Interactive Python). IPython's contribution was the IPython shell, which added some features to the mere Python language. Qt Console is the result of adding a **graphical user interface** (GUI), with drop-down menus, mouse-clicking, etc, to the IPython shell, by means of a toolkit called Qt.

Part of the popularity of the IPython shell was due to the **magic commands**, which were extra commands written as `%cmd`. For instance, `%cd` allows you to change the **working directory**. These commands *are not part of Python*. Though some textbooks and tutorials are still very keen on magic commands, these commands appear very briefly in this course. To get more information about them, enter `%quickref` in the console. Although, in practice, you can omit the percentage sign (so `%cd` works exactly the same as `cd`), it is always safer to keep using it to distinguish the magic commands from the Python code.

Jupyter provides an alternative approach, based on the **notebook** concept. A notebook is kind of document where you can combine input, output and ordinary text. A notebook is stored in a file with extension `ipynb` (IPython notebook). In the notebook arena, **Jupyter Notebook** is the leading choice. Notebooks are multilingual, that is, they can be used, not only with Python, but also with other languages like R. Most data scientists prefer the console for developing their code, but use notebooks for diffusion, specially for posting their work on platforms like **GitHub**.

Besides the Jupyter apps, Anaconda also provides a Python IDE called **Spyder**, where you can manage together a console and a text editor for your code. If you have previous experience with IDE's, for instance from working with R in RStudio, you may prefer Spyder to Qt Console.

Once Anaconda is installed, you can bypass the navigator by calling your preferred interface from a shell. To start Qt Console, enter `jupyter qtconsole`. To get access to the notebooks in the default browser (*e.g*. Google Chrome), enter `jupyter notebook`. To start Spyder, enter `spyder`.

*Note*. Use *Anaconda Prompt* in Windows, instead of the standard Windows prompt, whose path does not contain the Anaconda apps.

## The main packages

This course does not look at Python as a programming language, but from a very specific perspective, assuming a data science context. From this perspective, the main Python packages are:

* **NumPy** adds support for large vectors and matrices, called there **arrays**.

* **Matplotlib**, based on NumPy, provides a plotting toolkit.

* **Pandas** is a popular library for data management, used in the examples of this course. Pandas is built on top of NumPy and Matplotlib.

## Colab notebooks

**Google Colaboratory** is a Google app which allows you to write and executing Python code in a browser, with some advantages: (a) it does not require installation nor configuration, (b) it gives you access to GPU's (meaning more computing power) for free, and (c) it allows you an easy way to share content. In Google Colaboratory, you work with documents called **Colab notebooks**. Though they are not exactly the same, Colab notebooks are pretty similar to Jupyter notebooks, and they stored in Google Drive as files with extension `ipynb`. 

You may be interested in using Colab, since you can access it from any deviced connected to Internet, such as an IPAD. The only thing you need to start working with Colab notebooks is a Google account, meaning a `gmail.com` address and its password. Colab work happens in **Google Drive** (enter through `https://www.google.com/drive`). In your debout, you have to install the Google Colaboratory app in your drive. To do this, click on the *Settings* button, select *Settings >> Manage apps* button and click on *Connect more apps*. `ipynb` files can be uploaded to and downloaded from Google Drive.

## Typing Python code

Let us assume that you are working on Jupyter Qt Console. The console produces **input prompts** (such as `In[1]:`), where you can type a command and press *Return*. The console responds with either the corresponding **output** (preceded by `Out[1]:`), an **error message** or no answer at all. Error messages are typically long and unfriendly. 

A simple example follows. Note the white space in the input, around the *plus* sign (`+`), which is ignored by the Python interpreter, but improves the **readability** of our code.

```
In [1]: 2 + 2
Out[1]: 4
```

So, if you enter `2 + 2`, the output will be the result of this calculation. But, if you want to store this result for later use (in the same session), you will enter it with a name, as follows:

```
In [2]: a = 2 + 2
```

This creates the **variable** `a`. Note that the value of `2 + 2` is not outputted now. But you can call it:

```
In [3]: a
Out[3]: 4
```

In Pyhton, when you assign a value to a variable which has already been created, the previous assignment is forgotten:

```
In [4]: a = 7 - 2

In [5]: a
Out[5]: 5
```

Suppose that you copypaste in the console code chunks from a text editor. This is what you would do if you were working in the console, so you could readily save your code. You can so input several code lines at once. In that case, the console only shows the output for the last line of the input. An example follows.

```
In [6]: b = 2 * 3
   ...: b - 1
   ...: b**2
Out[6]: 36
```

*Note*. You would probably have written `b^2` for the square of 2, but the caret symbol (`^`) plays a different role in Python.

If you are typing the code in the console, you can open a new line within the same input with *Ctrl+Return*. You can then finish the input, calling for the output, by pressing *Return*. If the cursor is not at the end of the last line, you have to press *Shift+Return* to finish the input. 

Typing in a notebook is just a bit different. The notebook is a sequence of **cells**. There two type of cells, the Markdown cells and the code cells. In the **Markdown cells**, you write comments, while in the **code cells** you write the Python commands. Every code cell of the notebook corresponds to an input of the console. When you are typing in a cell, pressing *Return* starts a new line *within the same cell*, without ending the input. With *Shift+Return*, you finish the the input, so you get the ouput, opening a new cell. To finish the input without opening a new cell, use *Cmd+Return* in Mac or *Ctrl+Return* in Windows.   


## Python packages

Additional Python resources come in **packages**. For instance, suppose that you want to do some math, calculating the square root of 2. You will then **import** the package `math`, whose resources include the square root and many other mathematical functions. Once the package has been imported, all its functions are available, so you can call the function as `math.sqrt()`. This notation indicates that `sqrt()` is a function of the module `math`.

In the console, the square root calculation shows up as:

```
In [7]: import math
   ...: math.sqrt(2)
Out[7]: 1.4142135623730951
```

Alternatively, you can import only the functions that you plan to use:

```
In [8]: from math import sqrt
   ...: sqrt(2)
Out[8]: 1.4142135623730951
```

Packages are imported just for the current kernel. You can only import a package only if it is already **installed** in your computer. With the Anaconda distribution, all the packages used in this course are already available and can be directly imported.

*Note*. This course follows the common practice in Python learning materials of writing functions as *func()*. The parentheses remind you that this is an object that takes arguments.

## The main packages

This course does not look at Python as a programming language, but from a very specific perspective. Our approach is mainly based on the **package Pandas**.

In the data science context, the main Python packages are:

* **NumPy** adds support for large vectors and matrices, called there **arrays**.

* Based on NumPy, the library **Matplotlib** is Python's plotting workhorse.

* Pandas is a popular library for data management, used in all the examples of this course. Pandas is built on top of NumPy and Matplotlib.

* scikit-learn is a library of **machine learning** methods.

## Numeric types

As in other languages, data can have different **data types** in Python. The data type can be learned with the function `type()`. Let me start with the numeric types. For the variable `a` defined above:

```
In [9]: type(a)
Out[9]: int
```

So, `a` has type `int` (meaning integer). Another numeric type is that of **floating-point** numbers (`float`), which have decimals:

```
In [10]: b = math.sqrt(2)
    ...: type(b)
Out[10]: float
```

There are subdivisions of these two basic types (such as `int64`), but we skip them in this brief tutorial. Note that, in Python, integers are not, as in the mathematics textbook, a subset of the real numbers, but a different type:

```
In [11]: type(2)
Out[11]: int
```

```
In [12]: type(2.0)
Out[12]: float
```

In the above square root calculation, `b` got type `float` because this is what the `math` function `sqrt()` returns. The functions `int()` and `float()` can be used to convert numbers from one type to another type (sometimes at a loss):

```
In [13]: float(2)
Out[13]: 2.0
```

```
In [14]: int(2.3)
Out[14]: 2
```

## Boolean data

We also have **Boolean** (`bool`) variables, whose value is either `True` or `False`:

```
In [15]: d = 5 < a
    ...: d
Out[15]: False
```

```
In [16]: type(d)
Out[16]: bool
```

Even if they don't appear explicitly, Booleans may come under the hood. When you enter an expression involving a comparison such as `5 < a`, the Python interpreter evaluates it, returning either `True` or `False`.  Here, we have defined a variable by means of such an expression, so we got a Boolean variable. Warning: as a comparison operator, equality is denoted by two equal signs. This may surprise you.

```
In [17]: a == 4
Out[17]: False
```

Boolean variables can be converted to `int` and `float` type by the functions mentioned above, but also by a mathematical operator:

```
In [18]: math.sqrt(d)
Out[18]: 0.0
```

```
In [19]: 1 - d
Out[19]: 1
```

## Strings

Besides numbers, we can also manage **strings** with type `str`:

```
In [20]: c = 'Messi'
    ...: type(c)
Out[20]: str
```

The quote marks indicate type `str`. You can use single or double quotes, but take care of using the same on both sides of the string. Strings come in Python with many methods attached. These methods will be discussed later in this course.

## Lists

Python has several types for objects that work as **data containers**. The most versatile is the **list**, which is represented as a sequence of comma-separated values inside square brackets. Lists can contain items of different type. A simple example of a list, of length 4, follows.

```
In [21]: mylist = ['Messi', 'Cristiano', 'Neymar', 'Coutinho']
```

```
In [22]: len(mylist)
Out[22]: 4
```

Lists can be concatenated in a very simple way in Python:

```
In [23]: newlist = mylist + [2, 3]
    ...: newlist
Out[23]: ['Messi', 'Cristiano', 'Neymar', 'Coutinho', 2, 3]
```

Now, the length of `newlist` is 6:

```
In [24]: len(newlist)
Out[24]: 6
```

The first item of `mylist` can be extracted as `mylist[0]`, the second item as `mylist[1]`, etc. The last item can be extracted either as `mylist[3]` or as `mylist[-1]`. Sublists can be extracted by using a colon inside the brackets, as in:

```
In [25]: mylist[0:2]
Out[25]: ['Messi', 'Cristiano']
```

Note that `0:2` includes `0` but not `2`. This is a general rule for indexing in Python. Other examples:

```
In [26]: mylist[2:]
Out[26]: ['Neymar', 'Coutinho']
```

```
In [27]: mylist[:3]
Out[27]: ['Messi', 'Cristiano', 'Neymar']
```

The items of a list are ordered, and can be repeated. This is not so in other data containers.

## Ranges

A **range** is a sequence of integers which in many aspects works as a list, but the terms of the sequence are not saved as in a list. Instead, only the procedure to create the sequence is saved. The syntax is `range(start, end, step)`. Example:

```
In [28]: myrange = range(0, 10, 2)
    ...: list(myrange)
Out[28]: [0, 2, 4, 6, 8]
```

Note that the items from a range cannot printed directly. So, we have converted the range to a list with the function `list`. If  `step` is omitted, it is assumed to be 1:

```
In [29]: list(range(5, 12))
Out[29]: [5, 6, 7, 8, 9, 10, 11]
```

If `start` is also omitted, it is assumed to be 0:

```
In [30]: list(range(10))
Out[30]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Dictionaries

A **dictionary** is a set of **pairs key/value**. For instance, the following dictionary contains three features of an individual:

```
In [31]: my_dict = {'name': 'Joan', 'gender': 'F', 'age': 32}
```

The keys can be listed:

```
In [32]: my_dict.keys()
Out[32]: dict_keys(['name', 'gender', 'age'])
```

In the dictionary, a value is not extracted using an index which indicates its order in a sequence, as in the list, but using the corresponding key:

```
In [33]: my_dict['name']
Out[33]: 'Joan'
```

## Other data container types

The packages used in data science come with new data container types: NumPy arrays, Pandas series and Pandas data frames. Dealing with so many types of objects is a bit challenging for the beginner. The elements of the Python data containers (*e.g*. lists) can have different data types, but NumPy and Pandas data containers have consistency constraints. So, an array has a unique data type, while a data frame has a unique data type for every column.

##  Functions

A **function** takes a collection of **arguments** and performs an action. Let me present a couple of examples of value-returning functions. They are easily distinguished from other functions, because the definition's last line is a `return` clause.

A first example follows. Note the **indentation** after the colon, which is created automatically by the console.

```
In [34]: def f(x):
    ...:     y = 1/(1 - x**2)
    ...:     return y
```

When we define a function, Python just takes note of the definition, accepting it when it is syntactically correct (parentheses, commas, etc). The function can be applied later to different arguments.

```
In [35]: f(2)
Out[35]: -0.3333333333333333
```

If we apply the function to an argument for which it does not make sense, Python will return an error message which depends on the values supplied for the argument.

```
In [36]: f(1)
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-34-281ab0a37d7d> in <module>
----> 1 f(1)

<ipython-input-32-4f34043eb656> in f(x)
      1 def f(x):
----> 2     y = 1/(1 - x**2)
      3     return(y)

ZeroDivisionError: division by zero
```

```
In [37]: f('Mary')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-35-8547eae46f78> in <module>
----> 1 f('Mary')

<ipython-input-32-4f34043eb656> in f(x)
      1 def f(x):
----> 2     y = 1/(1 - x**2)
      3     return(y)

TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
```

Functions can have more than one argument, as in:

```
In [38]: def g(x, y): return x*y/(x**2 + y**2)
    ...: g(1, 1)
Out[38]: 0.5
```

Note that, in the definition of `g()`, I have used a shorter way. Most programmers would make it longer, as I did previously for `f()`.

## Homework

1. Use Python to evaluate the expressions `1/3 + 1/3 == 2/3` and `4/3 + 1/3 + 1/3 == 4/3 + 2/3`. Do you get what you expected? Why?

2. Write a Python function which, given three integers, returns `True` if any of them is zero, and `False` otherwise.

3. Write a Python function which, given three integers, returns `True` if they are in order from smallest to largest, and `False` otherwise.
