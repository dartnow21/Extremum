class User:
    def userAnswer(self):
        print("Каким методом для нахождения экстремумов хотите воспользоваться? 1 - Обычный способ / 2 - Метод Лагранжа")
        user_answer = int(input())
        if user_answer == 1:
            from SearchExtremes import SearchExtremes
            SearchExtremes()
        elif user_answer == 2:
            from MethodLagranja import MethodLagranja
            MethodLagranja()
        else:
            print("Извините, такой метод не найден.")


functions = User()
functions.userAnswer()
