# Python-Week-2
_Anatomy of a Function:_
Programs involve systems, tasks, objects, and interacting components, thus programmers need to think of designig programs rather than just following instructions.
For this reason, the basic unit of a program is a function.
Without functions, a program lacks functionality. 
Functions:
~ Composed of a name and parameters, which are symbolised by the 'def' statement.
~ 
Named Parameters:
~
*args:
~ There is a rule when using keywords in Python, and that is they must come after the positional arguments.
~ The order for the first two arguments is important and cannot be changed. But, after these mandatory arguments, they keyword arguments can be in any order.
~ To allow users to pass in any number of variables, use the asterisk (*) symbol before the argument name to create a pointer to the inputted variables(like this: *args).
~ 
**kwargs:
~ We use kwargs method to handle keyword arguments. Kwargs is short for keyword arguments.
~ Keyword arguments are now stored as a dictionay instead of a tuple. 
~ Dictionary is a more appropriate data structure for referencing keywords, since keyword arguments have keys and values and can be passed in order.


_Variables and Scope:_
This part focuses on how gloabl and local variables interact.
Function Scope:
~ In the previous section, we had discussed that *args and *kwargs, which were used to print out the arguments passed into a function.
~ This allowed us to see a tuple and dictionary of the passed arguemens
~ A method called "locals" (locals())function allows us to access all the variables within a Python function without any asterisks.
~ For example we will use the locals functions to print the output. So, let's call perform operation with the arguments one and two and specify that the operation is multiplication.
