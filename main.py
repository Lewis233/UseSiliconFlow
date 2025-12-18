import api

if __name__ == "__main__":
    if not api.user.check_apikey_valid():
        api.user.write_apikey(input("请输入APIKey: "))
    print(api.post_chat_completions("介绍一下阿森纳"))