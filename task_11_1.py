class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)
    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])
    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return f'Все в порядке'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'
    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('15 - 11 - 2021')
print(today)
print(Data.valid(35, 12, 2010))
print(Data.valid(5, 17, 2014))
print(Data.valid(18, 10, 2022))
print(today.valid(15, 11, 2021))
print(Data.extract('31 - 11 - 2011'))
print(today.extract('15 - 11 - 2021'))