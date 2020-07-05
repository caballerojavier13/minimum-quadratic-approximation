'''
    Mathematical Expression Evaluator class for Python.
    You can set the expression member, set the functions, variables and then call
    evaluate() function that will return you the result of the mathematical expression
    given as a string. 

    The user is granted rights to user, distribute and/or modify the source code 
    as long as this notice is shipped with it.
    
    The Author of this software cannot and do not warrant that any 
    functions contained in the Software will meet your requirements, 
    or that its operations will be error free. 
    
    The entire risk as to the Software performance or quality, 
    or both, is solely with the user and not the Author.
     
    You assume responsibility for the selection of the software to 
    achieve your intended results, and for the installation, use, and 
    results obtained from the Software. 
    
    The Author makes no warranty, either implied or expressed, including 
    with-out limitation any warranty with respect to this Software 
    documented here, its quality, performance, or fitness for a particular 
    purpose. In no event shall the Author be liable to you for damages, 
    whether direct or indirect, incidental, special, or consequential 
    arising out the use of or any defect in the Software, even if the 
    Author has been advised of the possibility of such damages, 
    or for any claim by any other party. 
    
    All other warranties of any kind, either express or implied, 
    including but not limited to the implied warranties of 
    merchantability and fitness for a particular purpose, are expressly 
    excluded.
    
    Copyright and all rights of this software, irrespective of what
    has been deposited with the U.S. Copyright Office, belongs
    to Bestcode.com.
'''

from math import *

class PyMathParser(object):
    '''
    Mathematical Expression Evaluator class.
    You can set the expression member, set the functions, variables and then call
    evaluate() function that will return you the result of the mathematical expression
    given as a string.
    '''
    
    '''
    Mathematical expression to evaluate.
    '''
    expression = ''
    
    '''
    Dictionary of functions that can be used in the expression.
    '''
    functions = {'__builtins__':None};
    
    '''
    Dictionary of variables that can be used in the expression.
    '''
    variables = {'__builtins__':None};

    def __init__(self):
        '''
        Constructor
        '''
    
    def evaluate(self):
        '''
        Evaluate the mathematical expression given as a string in the expression member variable.
        
        '''
        return eval(self.expression, self.variables, self.functions);

    def addDefaultFunctions(self):
        '''
        Add the following Python functions to be used in a mathemtical expression:
        acos
        asin
        atan
        atan2
        ceil
        cos
        cosh
        degrees
        exp
        fabs
        floor
        fmod
        frexp
        hypot
        ldexp
        log
        log10
        modf
        pow
        radians
        sin
        sinh
        sqrt
        tan
        tanh
        '''
        self.functions['acos']=acos
        self.functions['asin']=asin
        self.functions['atan']=atan
        self.functions['atan2']=atan2
        self.functions['ceil']=ceil
        self.functions['cos']=cos
        self.functions['cosh']=cosh
        self.functions['degrees']=degrees
        self.functions['exp']=exp
        self.functions['fabs']=fabs
        self.functions['floor']=floor
        self.functions['fmod']=fmod
        self.functions['frexp']=frexp
        self.functions['hypot']=hypot
        self.functions['ldexp']=ldexp
        self.functions['ln']=log
        self.functions['log']=log10
        self.functions['modf']=modf
        self.functions['pow']=pow
        self.functions['radians']=radians
        self.functions['sin']=sin
        self.functions['sinh']=sinh
        self.functions['sqrt']=sqrt
        self.functions['tan']=tan
        self.functions['tanh']=tanh
        
    def addDefaultVariables(self):
        '''
        Add e and pi to the list of defined variables.
        '''
        self.variables['e']=e
        self.variables['pi']=pi

    def getVariableNames(self):
        '''
        Return a List of defined variables names in sorted order.
        '''
        mylist = list(self.variables.keys())
        try:
            mylist.remove('__builtins__')
        except ValueError:
            pass
        mylist.sort()
        return mylist


    def getFunctionNames(self):
        '''
        Return a List of defined function names in sorted order.
        '''
        mylist = list(self.functions.keys())
        try:
            mylist.remove('__builtins__')
        except ValueError:
            pass
        mylist.sort()
        return mylist
    
        