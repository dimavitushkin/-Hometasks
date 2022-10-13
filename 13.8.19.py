price_all = 0
while True:
    try:
        ticket_number = int(input('Сколько билетов вы хотите приобрести на мероприятие? '))
        if type(ticket_number) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age = int(input(f'Введите возраст посетителя № {i}? '))
            if age <= 0 or age > 110:
                raise ValueError
            elif age < 18:
                print('Билет бесплатный')
            elif 25 > age >= 18:
                price_all += 990
                print('Стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Введите корректный возраст!')
if ticket_number > 3:
    price_all = price_all * 0.9
    print(f'Сумма к оплате {price_all} руб. с учетом 10%-ой скидки')
else:
    print(f'Сумма к оплате {price_all} руб.')
