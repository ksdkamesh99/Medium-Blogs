#The below line is known as function decorator

from memory_profiler import profile

# A program to store 2 large array's in python

@profile
def main():
  a = [1] * (10 ** 6)
  b = [2] * (2 * 10 ** 7)
  del b
  print("Completed")


main()
