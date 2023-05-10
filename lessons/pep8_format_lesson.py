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

    # fixed!

    def summary() -> None:
        # any given long name should not take up more than 80 characters in a single line
        # if it does, use [enter] key to make it multiple lines
        pass


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

    # fixed!

    def summary(self, case, constant_case, file_name) -> None:
        case = 'snake_case'
        case = 'snake_case_example'
        constant_case = NamingConvention.CONSTANT
        constant_case = 'all caps'
        file_name = 'all lower, and snake case'


class ClassNames:

    def __init__(self) -> None:
        pass

    def class_name(self) -> None:
        print('class class_names()')

    # class names should be in Pascal Case
    # ClassName

    def fixed_class_name(self) -> None:
        print('class ClassNames()')

    # fixed!

    def summary(self) -> None:
        # class names should be in Pascal Case
        # not snake case or camel case
        pass

    # fun fact: exceptions should also be in Pascal Case


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

    # fixed!

    def summary(self) -> None:
        # top-level classes and functions should be two whitespaces apart
        # methods should be one whitespace apart
        pass


class Imports:
    def __init__(self) -> None:
        pass