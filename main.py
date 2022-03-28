

def seq3np1(n):
    count = 0
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    while(n != 1):
        count += 1
        #print(n)
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
   # print(n)                  # the last print is 1
    return count
def graph(turtle, upper_bound2, ):
  turtle = turtle.Turtle()
  wn = turtle.Screen 
  upper_bound2 = int(input("Input upper bound: "))
  screen = turtle.setworldcoordinates(-10, -10, 10, 10)
  max_iteration = upper_bound2
  
  
def main():
  upper_bound = int(input("Please input an upper bound number, bitch. Must be positive: "))
  if(upper_bound < 0):
    return
    #or use exit()
  for start in range(1, upper_bound+1):
    seq3np1(upper_bound)
    print("Current loop value: ",start,"Number of iterations: ", seq3np1(start))
  seq3np1(3)
main()
