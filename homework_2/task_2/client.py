import redis


def main():
    with redis.Redis(host='redis', port=6379) as client:
        while True:
            expression = input("Введите пример: ").strip().lower()

            if expression == 'stop':
                print("Вы завершили программу.")
                break

            client.lpush('expressions', expression)


if __name__ == '__main__':
    main()
