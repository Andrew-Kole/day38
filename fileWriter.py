def store_data(date, temperature):
    with open("files/data.txt", "a") as file:
        file.write(f"{date},{temperature}\n")


def read_data():
    with open("files/data.txt", "r") as file:
        content = file.read()
        return content


if __name__ == "__main__":
    print(read_data())