from sympy import *
class User:
    def userAnswer(self):
        print("Каким методом для нахождения экстремумов хотите воспользоваться? 1 - Обычный способ / 2 - Метод Лагранжа")
        user_answer = int(input())
        if user_answer == 1:
            from searchExtremes import SearchExtremes
            x, y = symbols('x y')
            print("Введите функцию f(x, y). Например:  x**2 + y ** 2 + 1")
            f = input()
            # x/y+x**2+y**3
            # exp(x+y)*(x**2-2*y**2)
            # x**2 + y ** 2 + 1
            print('Есть ли ограничения по x и y? 1-да / 0 – нет')
            ogr = int(input())
            x_from, x_to, y_from, y_to = -10, 10, -10, 10
            if ogr == 1:
                print('Введите допустимые интервалы по x:')
                print("Введите точку от. Пример: -10")
                x_from = float(input())
                print("Введите точку до. Пример: 10")
                x_to = float(input())

                print('Введите допустимые интервалы по y:')
                print("Введите точку от. Пример: -10")
                y_from = float(input())
                print("Введите точку до. Пример: 10")
                y_to = float(input())
            functions = SearchExtremes()
            functions.find(x, y, f, x_from, x_to, y_from, y_to)
        elif user_answer == 2:
            from MethodLagranja import MethodLagranja
            x, y = 'x', 'y'
            print("Введите функцию f(x, y). Например:  4*y**2 + x**2")

            f = input()
            # 5 - 3*x - 4*y
            # x + 3*y
            # 5*x*y - 4
            print("Ввод условия(ограничения).")
            print("Введите левую часть ограничения. Например: x**2 + y**2")
            left_x_y = input()
            print("Введите правую часть ограничения. Например: 25")
            # x**2 + y**2
            # (x**2)/8 + (y**2)/2
            right_x_y = input()
            x_y = left_x_y + '-' + right_x_y

            f_x_y = f + ' + L * (' + x_y + ')'
            print('Есть ли ограничения по x и y? 1-да / 0 – нет')
            ogr = int(input())
            x_from, x_to, y_from, y_to = -30, 30, -30, 30
            if ogr == 1:
                print('Введите допустимые интервалы по x:')
                print("Введите точку от. Пример: -10")
                x_from = float(input())
                print("Введите точку до. Пример: 10")
                x_to = float(input())

                print('Введите допустимые интервалы по y:')
                print("Введите точку от. Пример: -10")
                y_from = float(input())
                print("Введите точку до. Пример: 10")
                y_to = float(input())
            functions = MethodLagranja()
            functions.find(x, y, x_y, f, f_x_y, x_from, x_to, y_from, y_to, left_x_y)

        else:
            print("Извините, такой метод не найден.")

