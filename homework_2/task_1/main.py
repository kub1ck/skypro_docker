def main():
    while True:
        expression = input("Введите пример: ").strip().lower()

        if expression == 'stop':
            print("Вы завершили программу.")
            break

        print(f'Ответ: {eval(expression)}\n')


if __name__ == '__main__':
    main()
