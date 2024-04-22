from enum import Enum
import math
from typing import Any, Callable, Iterable
from functools import wraps, cache
from deprecated import deprecated
from time import sleep

type Number = int | float

@cache
def add(*numbers: Number, times: int = 1) -> Number:
    addition = 0
    for nr in numbers:
        addition += nr
    
    if times == 1:
        return addition
    answer = addition
    for _ in range(times - 1):
        answer += answer

    return answer

@deprecated(reason = "Function outdated. Use newer version add() instead.", version="1.0.0")
def plus(x: Number, y: Number) -> Number:
    return x + y

def clear_caches() -> None:
    add.cache_clear()

class PositiveNegative_Numbers:
    def __init__(self, min: int):
        if not math.isfinite(min):
            raise ValueError()
        self.mainexample = min
        if min < 0:
            self.type = 'Negative'
        elif min > 0:
            self.type = 'Positive'
        else:
            self.type = 'Null'

    def isin(self, value: Any) -> bool:
        if self.type == 'Positive' and value >= 1:
            return True
        if self.type == 'Negative' and value <= -1:
            return True
        if self.type == 'Null' and value == 0:
            return True
        return False
    
    # Această metodă specială permite utilizarea operatorului 'in'
    def __contains__(self, value):
        return self.isin(value)

Positives = PositiveNegative_Numbers(1)
Negatives = PositiveNegative_Numbers(-1)
Null = PositiveNegative_Numbers(0)
zero = PositiveNegative_Numbers(0)

class NumberExamples(Enum):
    Positive = 1
    Negative = -1
    Null = 0
    zero = 0

def retry(retries: int = 3, delay: Number = 1, log_errors: bool = True) -> Callable:
    """
    Attempt to call a function, if it fails, try again with a specified delay.

    :param retries: The max amount of retries you want for the function call
    :param delay: The delay (in seconds) between each function retry
    :return:
    """

    # Don't let the user use this decorator if they are high
    if retries < 1 or delay <= 0:
        raise ValueError('Are you high, mate?')

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(1, retries + 1):  # 1 to retries + 1 since upper bound is exclusive

                try:
                    print(f'Running ({i}): {func.__name__}()')
                    return func(*args, **kwargs)
                except Exception as e:
                    # Break out of the loop if the max amount of retries is exceeded
                    if i == retries:
                        if log_errors:
                            print(f'Error: {repr(e)}.')
                        print(f'"{func.__name__}()" failed after {retries} retries.')
                        break
                    else:
                        if log_errors:
                            print(f'Error: {repr(e)} -> Retrying...')
                        sleep(delay)  # Add a delay before running the next iteration

        return wrapper

    return decorator

class Item_Getter:
    def __init__(self, *indexes: int):
        """Create an Item_Getter instance. Afterwards, call this variable as a function and insert the list you want as the argument.
        
        :params indexes: The indexes you wish to retrieve
        :return:"""
        if indexes == ():
            raise ValueError("`indexes` can not be an empty value.")
        self.indexes = indexes

    def __call__(self, List: Iterable) -> tuple[Any]:
        """Returns the parsed indexes from a list.
        
        :params List: The list you wish to get items from
        :return: tuple[Any] <-> The items with the parsed indexes from the parsed list."""
        output = ()
        for index in self.indexes:
            val = List[index]
            tval = (val,)
            output = output + tval
        
        return output
        
