from typing import Dict, List


def greeter(func):
    def util_greeter(*args) -> str:
        return f'Aloha {func(*args).title()}'

    return util_greeter


def sums_of_str_elements_are_equal(func):
    def util_sums(*args) -> str:
        numbers_str = func(*args).split(' ')

        if len(numbers_str) != 2:
            return ''
        try:
            int(numbers_str[0])
            int(numbers_str[1])
        except ValueError:
            return ''

        sums = [0, 0]
        neg = [-1 if num[0] == '-' else 1 for num in numbers_str]

        for i, num in enumerate(numbers_str):
            for n in num:
                if n == '-':
                    continue
                sums[i] += int(n)
            sums[i] *= neg[i]

        equal_or_not = ' != ' if sums[0] != sums[1] else ' == '

        return str(sums[0]) + equal_or_not + str(sums[1])

    return util_sums


def format_output(*required_keys):
    def decorator(func):
        def util_formatter(*args):
            output: Dict[str, str] = dict()
            dict_to_format: Dict[str, str] = func(*args)

            for key in required_keys:
                formatted_key = key.split("__")
                output.setdefault(key, '')

                for real_key in formatted_key:
                    if real_key not in dict_to_format.keys():
                        raise ValueError
                    output[key] += dict_to_format[real_key] + ' '

                output[key] = output[key].strip()

                if output[key] == '':
                    output[key] = 'Empty value'

            return output

        return util_formatter

    return decorator


def add_method_to_instance(klass):
    def decorator(func):
        def util_add_method_to_instance(*args, **kwargs):
            # when an instance method, first argument (args[0]) is always self
            return func(*args[1:], **kwargs)

        setattr(klass, func.__name__, util_add_method_to_instance)
        return util_add_method_to_instance

    return decorator

# resort
# planik
# towarzyska
# pawiluxy
# rakieta
