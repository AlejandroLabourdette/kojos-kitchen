import matplotlib.pyplot as plt
from objects import Restaurant, Client, Products


def order_type(rest: Restaurant):
    order = ['Sandwich', 'Sushi']
    amount = [0, 0]

    for client in rest.client_list:
        if client.petition == Products.Sandwich:
            amount[0] += 1
        else:
            amount[1] += 1

    xAxis = [i + 0.5 for i, _ in enumerate(order)]

    plt.bar(xAxis, amount)
    plt.title('Orders type')
    plt.xlabel('Product', fontsize=14)
    plt.ylabel('People who order it', fontsize=14)
    plt.xticks([i+0.5 for i, _ in enumerate(order)], order)

    plt.show()
    # plt.savefig('img/order_type.png', bbox_inches='tight')


def sandwich_orders_minutes(rest: Restaurant):
    time = ['3', '4', '5']
    amount = [0, 0, 0]

    for client in rest.client_list:
        if client.petition == Products.Sandwich:
            amount[client.petition_time - 3] += 1

    xAxis = [i + 0.5 for i, _ in enumerate(time)]

    plt.bar(xAxis, amount)
    plt.title('Creation time of Sandwich orders')
    plt.xlabel('Minutes', fontsize=14)
    plt.ylabel('Amount', fontsize=14)
    plt.xticks([i+0.5 for i, _ in enumerate(time)], time)

    plt.show()


def sushi_orders_minutes(rest: Restaurant):
    time = ['5', '6', '7', '8']
    amount = [0, 0, 0, 0]

    for client in rest.client_list:
        if client.petition == Products.Sushi:
            amount[client.petition_time - 5] += 1

    xAxis = [i + 0.5 for i, _ in enumerate(time)]

    plt.bar(xAxis, amount)
    plt.title('Creation time of Sushi orders')
    plt.xlabel('Minutes', fontsize=14)
    plt.ylabel('Amount', fontsize=14)
    plt.xticks([i+0.5 for i, _ in enumerate(time)], time)

    plt.show()


def people_in_queue_each_minute(rest1: Restaurant, rest2: Restaurant):
    last_minute1 = max(rest1.client_list[-1].departure, rest1.client_list[-2].departure)
    last_minute2 = max(rest2.client_list[-1].departure, rest2.client_list[-2].departure)
    last_minute = max(last_minute1, last_minute2)

    minutes = [i for i in range(last_minute)]
    people_in_queue1 = [0 for _ in range(last_minute)]
    people_in_queue2 = [0 for _ in range(last_minute)]

    for client in rest1.client_list:
        for i in range(client.arrive, client.departure - client.petition_time):
            people_in_queue1[i] += 1

    for client in rest2.client_list:
        for i in range(client.arrive, client.departure - client.petition_time):
            people_in_queue2[i] += 1

    plt.title('Amount of people waiting to be attended each minute')
    plt.xlabel('Minutes', fontsize=14)
    plt.ylabel('Amount of people', fontsize=14)
    plt.plot(minutes, people_in_queue1, 'b', label='Restaurant 1')
    plt.plot(minutes, people_in_queue2, 'r', label='Restaurant 2')
    plt.legend()
    # plt.savefig('img/order_type.png', bbox_inches='tight')
    plt.show()


def chefs_used_each_minute(rest: Restaurant):
    last_minute = max(rest.client_list[-1].departure, rest.client_list[-2].departure)

    minutes = [i for i in range(last_minute + 1)]
    chefs_working = [0 for _ in range(last_minute + 1)]

    for client in rest.client_list:
        for i in range(client.departure - client.petition_time, client.departure):
            try:
                chefs_working[i] += 1
            except:
                print(last_minute)
                print(i)

    plt.title('Chefs used each minute')
    plt.xlabel('Minutes', fontsize=14)
    plt.ylabel('Amount of chefs', fontsize=14)
    plt.plot(minutes, chefs_working, 'b')
    plt.show()


def departure_time_of_clients(rest: Restaurant):
    people = [i for i in range(len(rest.client_list))]
    departure = []

    for client in rest.client_list:
        departure.append(client.departure)

    plt.plot(people, departure)
    plt.show()


def time_waiting_of_each_client_before_attended(rest: Restaurant):
    people = [i for i in range(len(rest.client_list))]
    time_waited = []

    for client in rest.client_list:
        time_waited.append(client.departure - client.petition_time - client.arrive)

    plt.title('Time waited for each client before being attended')
    plt.xlabel('Client number', fontsize=14)
    plt.ylabel('Time waited', fontsize=14)
    plt.plot(people, time_waited)
    plt.show()


def more_than_5min_waiting(rest1: Restaurant, rest2: Restaurant):
    restaurants = ['Restaurant1', 'Restaurant2']
    more_than_5min = [0, 0]

    amount = 0
    for client in rest1.client_list:
        if client.departure - client.petition_time - client.arrive:
            amount += 1
    more_than_5min[0] = (amount/len(rest1.client_list)) * 100

    amount = 0
    for client in rest2.client_list:
        if client.departure - client.petition_time - client.arrive:
            amount += 1
    more_than_5min[1] = (amount / len(rest1.client_list)) * 100

    xAxis = [i + 0.5 for i, _ in enumerate(restaurants)]

    plt.bar(xAxis, more_than_5min)
    plt.title('Percent of people who wait more than 5 minutes without being attended')
    plt.xlabel('Restaurant', fontsize=14)
    plt.ylabel('Percent', fontsize=14)
    plt.xticks([i+0.5 for i, _ in enumerate(restaurants)], restaurants)

    plt.show()

