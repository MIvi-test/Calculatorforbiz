import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class Grafics:
    
    def __init__(self, data) -> None:
        '''geo or arifm data '''
        self.mounth = data[0]
        self.money = data[1]
        self.tax = data[2]
        self.clients = data[3]
        self.df = pd.DataFrame(data = data[1], index = range(1,data[0]+1))
        
    
    def circular(self, expenses):

        dt = pd.Series(data = [self.tax[-1], expenses, self.money[-1]], index=['tax','expenses','margin'])
        dt.plot(kind='pie', title='Финансы за последний месяц',
                legend='reverse',
                colors = ['red','gray','green'],
                autopct='%1.1f%%'
                )
        plt.show()
        # не проверено как работает
    # график роста прибыли от месяцев с красной зоной минуса и зеленой прибыли
    