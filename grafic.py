import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import choice

class Grafics:
    
    def __init__(self, data) -> None:
        '''geo or arifm data '''
        self.mounth = data[0]
        self.money = data[1]
        self.tax = data[2]
        self.clients = data[3]
        self.df = pd.DataFrame(data = {'margin':data[1],'clients':data[3]}, index = range(1,data[0]+1))
        
    
    def circular(self, expenses):

        dt = pd.Series(data = [self.tax[-1], expenses, self.money[-1]], index=['налог','расходы','маржа'])
        dt.plot(kind='pie', title='Финансы за последний месяц',
                legend='reverse',
                colors = ['red','gray','green'],
                autopct='%1.1f%%'
                )
        dt.sample()
        plt.savefig('pie.png')
    
    def growth_charts(self) -> None:
        '''график линии зависимости прибыли от месяца'''
        dtf = self.df
        dtf.plot(kind='line', y = 'margin')
        plt.savefig('line.png')
    
    # график роста прибыли от месяцев с красной зоной минуса и зеленой прибыли
if __name__ == '__main__':
    data = {
        'cheque': 200,
        'clients' :  400,
        'invest': 150000,
        'expenses' :100000
    }
    Calculable = choice.Calculations(average_cheque=data['cheque'], 
                                         clients=data['clients'], 
                                         start_capital=data['invest'],
                                         expenses=data['expenses'], 
                                         procent=10, 
                                         unchanging_increase=15)
        
    # arifm_data = Calculable.progression(mode='A')
    geo_data = Calculable.progression(mode='G')
    grf = Grafics(data=geo_data)
    grf.circular(expenses=data['expenses'])
    grf.growth_charts()