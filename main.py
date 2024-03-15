from rich.console import Console
import choice,grafic,front



def main():
    console = Console()
    try:
        console.print('Средний чек покупателя : ', style='bold yellow', end=' ', new_line_start=True)
        average_cheque = int(input())
        
        console.print('Сколько клиентов вы ожидаете в первый месяц : ',end=' ', style='bold yellow', new_line_start=True )
        N_clients =int(input())
        
        console.print('Какое количество инвестиций надо окупить : ',end=' ', style='bold yellow', new_line_start=True )
        start_capital = int(input())
        
        console.print('каковы расходы в месяц : ',end=' ', style='bold yellow', new_line_start=True )
        expenses = int(input())
        
        console.print('Процент увеличения клиентов, пример 10 (что соответсвует 10%)',end=' ', style='bold yellow', new_line_start=True )
        prosent = int(input()) / 100
    except TypeError as ex:
        console.print('Вы ввели не цифры, вам отказано в услуге')
        main()

        
        #начинаем творить магию
    Calculable = choice.Calculations(average_cheque=average_cheque, 
                                         clients=N_clients, 
                                         start_capital=start_capital,
                                         expenses=expenses, 
                                         procent=prosent, 
                                         unchanging_increase=15)
        
    arifm_data = Calculable.progression(mode='A')
    geo_data = Calculable.progression(mode='G')
    grf = grafic.Grafics(data=arifm_data)
    grf.circular(expenses=expenses)
        
    
if __name__ == '__main__':
    main()