import vk_api
LOGIN = 'Test'
PASSWORD = 'Bot'

def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.wall.get(count=5, offset=1, fields=)
    if response['items']:
        for i in response['items']:
            print(i)


if __name__ == '__main__':
    main()