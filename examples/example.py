#!/usr/bin/env python3

import time
from PriorityThreadPoolExecutor import PriorityThreadPoolExecutor

########################################################################################################################
#                                             Test function for threads                                                #
########################################################################################################################


def print_number(number, seconds=3):
    print('Start %s' % number)
    time.sleep(seconds)
    print('Stop %s' % number)

########################################################################################################################
#                                                    Entry point                                                       #
########################################################################################################################


if __name__ == '__main__':
    pool = PriorityThreadPoolExecutor(max_workers=1)
    with pool:
        for x in range(10):
            pool.submit(print_number, x-1, 1, priority=9-x)
