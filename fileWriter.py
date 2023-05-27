def store_data(date, temperature):
    with open("files/data.txt", "a") as file:
        file.write(f"{date},{temperature}\n")


if __name__ == "__main__":
    print(read_data())