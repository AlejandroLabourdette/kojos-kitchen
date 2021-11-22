import math

import graph
from objects import Client, Restaurant
from random_variables import Ed

lda = 0.6
lda_critic = 0.8

t = 0               # minute of day
t_max = 660         # total minutes of a day: 10am to 9pm, 11h * 60m = 660m
ta = Ed(lda) + 1    # minute of next client arrive using lda
td1 = math.inf      # minimum departure time in kitchen of case 1
td2 = math.inf      # minimum departure time in kitchen of case 2
rest1 = Restaurant()
rest2 = Restaurant(True)

while True:
    flag = 0
    if ta == min(ta, td1, td2) and ta <= t_max:
        flag = 1
        t = ta
        client = Client(t)
        client_clone = client.clone()
        td1 = rest1.new_client_event(client)
        td2 = rest2.new_client_event(client_clone)
        if (90 <= t <= 210) or (420 <= t <= 540):   # elevate frequency in critical time of day
            ta = t + Ed(lda_critic) + 1
        else:                                       # normal frequency of people
            ta = t + Ed(lda) + 1
        if ta > t_max:
            ta = math.inf
    if td1 < ta and td1 <= td2:
        flag = 1
        t = td1
        td1 = rest1.petition_completed_event()
    if td2 < ta and td2 < td1:
        flag = 1
        t = td2
        td2 = rest2.petition_completed_event()

    if flag == 0:
        # print(rest1)
        # print(rest2)
        break

