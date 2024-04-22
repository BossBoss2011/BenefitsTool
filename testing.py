if __name__ == "__main__":
    import sys
    if __debug__:
        print("This code was used for testing, and is not needed.")
        sys.exit(2)
    from main import *

    def evaluate(expression: str):
        print(f"{expression}: {eval(expression)}")

    expressions = ["1 in Positives", "-1 in Null", "-37 in Negatives", "2 in Negatives", "0 in Negatives", "-7 in Positives", "0 in Positives", "NumberExamples.Positive.value in Positives"]

    for expression in expressions:
        evaluate(expression)

    # from random import randint

    # @retry(15, 0.1, True)
    # def chance():
    #     if randint(1, 20) != 1:
    #         raise Exception("Hey")

    # chance()