#!/bin/python3

import math
import os
import random
import re
import sys
import collections

class SpendingNotifer:
    def __init__(self, d=7, mx=200):
        self.d = d
        self.mx = 200
        self.counts = [0] * (mx+1)
        self.med = None
        self.spending_history = collections.deque()

    def add_days_spending(self, days_spending):
        if len(self.spending_history) >= self.d:
            self.update_median()
            self.counts[self.spending_history.popleft()] -= 1
        else:
            self.med = None

        self.spending_history.append(days_spending)
        self.counts[days_spending] += 1

    def account_for_days_spending(self, days_spending):
        self.add_days_spending(days_spending)

        return 1 if self.med and days_spending >= (2 * self.med) else 0

    def update_median(self):
        curr_idx = num = 0
        md_pt = self.d // 2
        last_num = 0
        while num < (self.mx + 1):
            cts = self.counts[num]
            curr_idx += cts
            if curr_idx > md_pt:
                if self.d % 2 == 1:
                    self.med = num
                elif curr_idx - cts == md_pt:
                    self.med = (num + last_num) / 2
                else:
                    self.med = num
                return
            last_num = num
            num += 1

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    alerts = 0
    sn = SpendingNotifer(d)

    for days_spending in expenditure:
        alerts += sn.account_for_days_spending(days_spending)

    return alerts

if __name__ == '__main__':
    fp = open('spending_alerts.txt', 'r')
    nd = fp.readline().split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, fp.readline().rstrip().split()))

    fp.close()

    result = activityNotifications(expenditure, d)
    print(result)
