import turtle

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
    #return seq3np1(n) ???
def graph(upper_bound):
  frank = turtle.Turtle()
  sid = turtle.Turtle()
  wn = turtle.Screen() 
  wn.setworldcoordinates(0, 0, 10, 10)
  max_so_far = 0
  string = ""
  sid.pu()
  sid.goto(0, 10)
  for i in range(1, upper_bound+1):
    result = seq3np1(i)
    if result > max_so_far:
      max_so_far=result
    sid.goto(0, max_so_far)
    string = "Maximum so far: ", i, result
    sid.clear()
    sid.write(string)
    #max_iteration = upper_bound
    wn.setworldcoordinates(0, 0, i+10, max_so_far+10)
    frank.pd()
    frank.goto(i, result)
  wn.exitonclick()
  

  
def main():
  upper_bound = int(input("Please input an upper bound number. Must be positive: "))
  if(upper_bound < 0):
    return
    #or use exit()
  for start in range(1, upper_bound+1):
    seq3np1(upper_bound)
    print("Current loop value: ",start,"Number of iterations: ", seq3np1(start))
  graph(upper_bound)
  seq3np1(3)
main()
