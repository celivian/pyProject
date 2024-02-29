from yandex_testing_lesson import is_palindrome



def test_reverse():
    # Список тестов
    # Каждый тест — это пара (входное значение, ожидаемое выходное значение)
    test_data = (
        ('aba', True),
        ('abc', False),
    )

    for input_s, correct_output_s in test_data:
            output_s = is_palindrome(input_s)
            if correct_output_s is None:
                # это исключение и ожидалось, продолжаем тестирование
                continue
            if type(input_s) == str:
                # вход корректный, но выброшено исключение TypeError — это ошибка
                print(f'Ошибка! Не удалось вычислить reverse("{input_s}"). Ошибка: {E}')
                return False
            # Выброшено неожиданное исключение — это ошибка
            print(f'Ошибка! Не удалось вычислить reverse("{input_s}"). Ошибка: {E}')
            return False
            if output_s != correct_output_s:
                # если ответ не совпал с ожидаемым, завершаем тестирование и возвращаем False
                print(f'Ошибка! reverse({input_s}) равно {output_s} вместо "{correct_output_s}"')
                return False
    # тестирование успешно пройдено
    print('Все тесты пройдены успешно')
    return True

if testing(tests):
    print('YES')
else:
    print('NO')
