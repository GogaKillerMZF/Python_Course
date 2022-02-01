def entry(f_name, s_name, b_day, city, email, phone):
    return(f'{f_name} {s_name} родился {b_day}, живет в городе {city}. Номер телефона: {phone}, email: {email}')
s = entry(s_name = 'Shapovalov',  f_name = 'Gordey', city = 'Kemerovo', email = 'bla_bla@mail.ru', b_day = '03.03.2000', phone = '8-999-999-99-99')


print(s)
    