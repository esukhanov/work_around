# Python3 program for demonstrating
# coroutine execution
import time
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        print('whait send')
        name = (yield)
        print('have send')
        if prefix in name:
            print(name)

        # calling coroutine, nothing will happen


corou = print_name("Dear")

# This will start execution of coroutine and
# Prints first line "Searchig prefix..."
# and advance execution to the first yield expression
print('next')
corou.__next__()

# sending inputs
time.sleep(3)
corou.send("Atul")
time.sleep(3)
corou.send("Dear Atul")