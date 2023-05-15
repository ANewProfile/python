class LineLen:
    def __init__(self) -> None:
        pass

    def long_function_name_with_long_args(self, argument1, argument2, argument3, argument4, argument5, argument6, argument7) -> None:
        print(f'Run: arg1: {argument1}')

    # no more than 80 characters per line

    def fixed_long_function_name_with_long_args(
            self, argument1, argument2, argument3, argument4, argument5,
              argument6, argument7
    ) -> None:
        print(f'Run: arg1: {argument1}')


class NamingConvention:

    def __init__(self) -> None:
        CONSTANT = 'use all capitals for constants \
                    (things that shouldn\'t be canged)'
        pass

    def camelCase(self, exampleArgument) -> None:
        print(f'exampleArgument is {exampleArgument} using camelCase')

    # use snake_case for python (word_word)
    # don't use camelCase (wordWord)
    # also don't use PascalCase (WordWord)

    def snake_case(self, example_argument) -> None:
        print(f'exampleArgument is {example_argument} using snake_case')

    def file_name(self) -> None:
        print('fiLE nAmE.py')
        print('nAmE.py')

    # file names should be in all lowercase
    # file names should also be in snake case

    def fixed_file_name(self) -> None:
        print('file_name.py')
        print('name.py')


class ClassNames:

    def __init__(self) -> None:
        pass

    def class_name(self) -> None:
        print('class class_names()')

    # class names should be in Pascal Case
    # ClassName

    def fixed_class_name(self) -> None:
        print('class ClassNames()')


class Spacing:
    def __init__(self) -> None:
        pass

    def class_spacing(self, c1, c2) -> None:
        class c1:
            def __init__(self) -> None:
                pass
        
        class c2:
            def __init__(self) -> None:
                pass
            def example(self, c2):
                print(c2)

    # global(leftmost indentation) classes and functions should be two new lines apart
    # methods should be one new line apart

    def fixed_class_spacing(self, c1, c2) -> None:
        class c1:
            def __init__(self) -> None:
                pass
        

        class c2:
            def __init__(self) -> None:
                pass

            def example(self, c2) -> None:
                print(c2)


class Imports:
    def __init__(self) -> None:
        pass

    def loc(self) -> None:
        print('The location of your imports \
              should always be at the top, \
              unless there is a specific reason not to.')
        print('Even though you can, you should not \
              import two distinct modules in the same line.')
        print('Two similar modules or two modules from the same library \
              can be imported in the same line \
              (e.g. from os import path, stat).')
        print('It is also okay to not import modules \
              at the top of your code if you have a module doc string \
              (the thing with triple quotations)')
        print('DISCLAIMER: NEVER use wildcard imports \
              (e.g. from os import *)!')
        

class Strings:
    def __init__(self) -> None:
        pass

    def single_or_double(self) -> None:
        print('There is actually NO specific \
              type of quotation that you should use, \
              as long as you always use the same one!')
        print('You should wrap quotations if you can.')
        print('(e.g. "QUOTE: \'hello\'")')
        print('However, you should ALWAYS use double quotations\
               when writing doc strings(triple quotations)')


class Whitespaces:
    def __init__(self) -> None:
        pass

    def function_calls_and_brackets(self) -> None:
        print('There should be NO whitespaces in between\
               brackets, function calls, and that kind of stuff')
        print(f'Correct:\nfunc(arg[1])\n\nIncorrect:\nfunc ( arg [ 1 ])')

    def variables(self) -> None:
        print('There should be one whitespace between variable definitions, \
              one whitespace beween +=, -=, +, and -, \
              and no whitespaces between * and / symbols(usually).')
        print('DISCLAIMER: There may be some exceptions.')
        print('\nCorrect:\ni = i + 1\n\
              i += 1\n\
              x = x*2 - 1\n\
              hypt2 = x*x + y*y\n\
              c = (a+b) * (a-b)\n\n\
              Incorrect:\ni=i+1\n\
              i +=1\n\
              x = x * 2-1\n\
              hypt2= x * x + y * y\n\
              c = (a + b) * (a - b)')
    
    def default_paramaters(self) -> None:
        print('There should be NO whitespaces between the default of paramaters.')
        print('\nCorrect:\ndef complex(real, imag=0.0):\n\
                 return magic(r=real, i=imag)')
        print('\nIncorrect:\ndef complex(real, imag = 0.0):\n\
                 return magic(r = real, i= imag)')


class InLineComments:
    def __init__(self) -> None:
        pass

    def rules(self):
        print('There must be at least two spaces\
               between the code and comment.')
        print('There must be at least one space\
               between the pound symbol in the comment')
        print('If it makes sense, start the comment with a capital')
    
    def example(self) -> None:
        COLOR = (0, 255, 0)  # This is correct

        COLOR = (0, 255, 0) #this is incorrect


class IsNone:
    def __init__(self) -> None:
        pass

    def rules(self) -> None:
        print('While checking if the variable "x" is equal to none, we could\
               say `if x:`, but it\'s better practice to say `if x is None:`')
        print('Use the keyword "is" instead of "=="\
               when checking for bools and NoneType')
        print('Also, use the keyword "is not" instead of "not is"!')
    
    def example(self) -> None:
        print('x = None')
        print('if x is None:')
        print('    pass')
        print('\n\n')
        print('\#Correct')
        print('if foo is not None:')
        print('    pass')
        print()
        print('\#Incorrect')
        print('if not foo is None:')
        print('    pass')
        print('\n\n')
        print('Both work, but it\'s good practice to use the first one')


class TryExcept:
    def __init__(self) -> None:
        pass

    def rules(self) -> None:
        print('When using try-except blocks,\
               always except a specific error to be more specific')
        print('If you would like to except multiple exceptions, use multiple except blocks')
    
    def example(self) -> None:
        print('\#Correct')
        print('try:')
        print('    import platform_specific_module')
        print('except ImportError:')
        print('    platform_specific module = None')
        print('\n\n')
        print('\#Incorrect')
        print('try:')
        print('    import platform_specific_module')
        print('except:')
        print('    platform_specific_module = None')


class StartsWith:
    def __init__(self) -> None:
        pass

    def rules(self) -> None:
        print('Always use the built-in "x.startswith(\'\')" or "endswith" function instead of slicing')

    def example(self) -> None:
        print('\#Correct')
        print('if foo.startswith("bar"):')
        print('    pass')
        print('\n\n')
        print('\#Incorrect')
        print('if foo[:3] == "bar":')
        print('    pass')
