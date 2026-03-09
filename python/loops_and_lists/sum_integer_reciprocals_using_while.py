summation = 0
starting_index = 1
index = starting_index
maximum_index = 100
      
while index <= maximum_index:
    index += 1/index
          
print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')
