import rich
from typing import Literal, List


class Calculations:
    
    def __init__(self, average_cheque:int, clients:int, start_capital:int, expenses:int, procent:int|float = 0.10, unchanging_increase: int = 10):
        self.average_cheque = average_cheque
        self.clients = clients
        self.start_capital = start_capital
        self.expenses = expenses
        if procent > 1:
            procent = procent / 100
        self.procent = procent
        self.unchanging_increase = unchanging_increase
        #определяю в поля класса, чтобы пользоваться ими в других фунциях
    
    def tax_regime(self):
        revenue = self.average_cheque * self.clients # выручка
        tax = {}
        if (revenue - self.expenses) <= (revenue *0.01):# проверка, если доход отрицательный или он меньше 1% выручки, то налог 1%
            _income = revenue - self.expenses - revenue * 0.01 # выручка - доходы - налог
            tax['mode'] = '1% от дохода'
            tax['amount'] = revenue * 0.01
            tax['income'] = _income
        else:
            if (revenue - self.expenses) * 0.15 > revenue * 0.06: # выясняем какой налоговый режим нам лучше
                _income = revenue - self.expenses - revenue * 0.06
                tax['mode'] = '6% от дохода'
                tax['amount'] = revenue * 0.06
                tax['income'] = _income
            else:
                _income = (revenue - self.expenses) * 0.85
                tax['mode'] = '15% от доходы-расходы'
                tax['amount'] = (revenue - self.expenses) * 0.15
                tax['income'] = _income
        return tax    
   
    def progression(self, mode = Literal['A','G']) -> list[int,list,list,list]: # type: ignore
        '''0-mounth; 1-list of money; 2-list of tax; 3-list of clients'''
        month = 1
        money = []
        taxs = []
        clients = []
        _clints = self.clients
        _increase = self.unchanging_increase
        if mode == 'A':
            if self.unchanging_increase == None:
                rich.console.console.print('WORNING ARIFMETIC',style='bold red')
                self.unchanging_increase = 10
        
        while month < 100:
            if mode == 'A' and month > 1:
                self.clients = self.clients + self.unchanging_increase
            elif mode == 'G' and month > 1:
                self.clients = self.clients + round(self.clients * self.procent)
            clients.append(self.clients)
            money.append(self.tax_regime()['income'])
            taxs.append(self.tax_regime()['amount'])
            
            if sum(money) > self.start_capital:
                break    
            month += 1
        #возращаем первоначальные значения переменных
        self.unchanging_increase = _increase
        self.clients = _clints
        return [month, money, taxs, clients] # type: ignore
    
    def __start__(self):
        #запуск всех методов \ не сделано
        pass
    