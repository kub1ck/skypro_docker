import redis


def main():
    with redis.Redis(host='redis', port=6379) as worker:
        while True:
            expression = worker.brpop('expressions')[1].decode('utf-8')

            try:
                expression = eval(expression)
            except SyntaxError:
                continue

            print(f'Ответ: {expression}')


if __name__ == '__main__':
    main()
