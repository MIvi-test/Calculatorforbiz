from sys import exit
import flet as ft


def Error_type(func):  # декоратор для того, чтобы выводил ошибку если неправильный ввод данных
    # def valid_types(value:str):#часть декоратора для проверки
    #     if not(value.isnumeric()):
    #         return False

    # def print_Error():
    #     ft.Text(value='Это не число', color='red')
    # # if not(valid_types):
    # return print_Error
    return func


def create_list_TextField(page: ft.Page):
    data = ["Средний чек", "Количество клиентов  в месяц", "Инвестиции, которые надо окупить",
            "Расходы в месяц", "Процентное увеличение клиентов (по стандарту 10)"]
    all_TextField = [[], [], []]
    for i in data:
        new_prefix_text = ft.Text(value=i)
        if 'Процент' in i:
            new_input = ft.TextField(width=500, suffix_text='%')
        else:
            new_input = ft.TextField(width=500)
        error_text = ft.Text(value='Введите число', color='red', visible=False)
        all_TextField[0].append(new_prefix_text)
        all_TextField[1].append(new_input)
        all_TextField[2].append(error_text)
    for i in range(len(all_TextField[0])):
        page.add(all_TextField[0][i],
                 all_TextField[1][i],
                 all_TextField[2][i])
        page.update()
    return all_TextField


def main(page: ft.Page):

    def click_LETS_GO(e):
        values = []  # тут все наши циферки
        # i индекс в массиве; k это обьект класса, то-есть переменная инпута
        for i, k in enumerate(objects_textFields[1]):
            if not (k.value.isnumeric()):
                # красный текст с предупреждением
                objects_textFields[2][i].visible = True
                objects_textFields[2][i].update()
                k.value = ''
                k.border_color = 'red'
                k.focus()
                k.update()
            else:
                if k.border_color == 'red':
                    k.border_color = 'black'
                    objects_textFields[2][i].visible = False
                    objects_textFields[2][i].update()
                values.append(int(k.value))
        # код создания изображений написать проверку на длинну в 5 значений
        # надо как-то их отобразить

    objects_textFields = create_list_TextField(page=page)
    add = ft.ElevatedButton(text='LETS GO', on_click=click_LETS_GO)
    page.add(add)
    image = ft.Image(src='/pie.png',
                     width=500,
                     height=500,
                     )
    page.add(image)
    page.update()
    # надо всё связать, сделать декоратор нормальный и тд. Удачи


if __name__ == '__main__':
    ft.app(port=7654, target=main, view=ft.WEB_BROWSER)  # type: ignore

    '''
    Надо сделать: возможность ввода данных:
    средний чек
    количество клиентов
    инвестиции
    затраты в месяц
    процентое увеличение клиентов
    
    На выходе:
    месяц безубыточности
    месяц окупаемости
    график роста прибыли от месяца
    распределние затрат на последнем месяце
    массив маржи по месяцам
    '''
