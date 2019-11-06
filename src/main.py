def hello_world(name: str) -> None:
    return "hello {}".format(name)


if __name__ == "__main__":
    sentence = hello_world("Louis")
    print(sentence)
