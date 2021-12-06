import pandas as pd
import numpy as np
df = pd.read_csv('input2.txt',header=None,names=["instruction","val"],sep=" ")

horizontal = df[df['instruction']=="forward"]
horizontal_sum=horizontal.val.sum()
down = df[df['instruction']=='down']
down_sum = down.val.sum()
up = df[df['instruction']=='up']
up_sum = up.val.sum()

print(horizontal_sum*(down_sum-up_sum))

#part2
aim_down = df[df['instruction']=='down']
aim_up = df[df['instruction']=='up']

depth=0
aim=0
for i in df.index:
    if df['instruction'][i] == 'down':
        aim += df.val[i]
    if df['instruction'][i] == 'up':
        aim -= df.val[i]    
    if df['instruction'][i] == 'forward':
        depth += aim * df.val[i]

print(horizontal_sum * depth)