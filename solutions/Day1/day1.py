def numDepthIncreases(): 
    '''
    Problem: https://adventofcode.com/2021/day/1/
    '''
    with open("data.txt") as f: 
        data = f.readlines() 
    
    num_depth_increases = 0 
    for i, line in enumerate(data): 
        if i > 0 and i <= len(data): 
            if int(line.strip('\n')) > int(data[i-1].strip('\n')): 
                num_depth_increases += 1 
    
    return num_depth_increases

numDepthIncreases()