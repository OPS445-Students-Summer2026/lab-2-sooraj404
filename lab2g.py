#!/usr/bin/env python3

# Author: Sooraj Sudhirreji
# Author ID: YOUR_SENECA_ID
# Date Created: 2026/05/29

import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print('blast off!')