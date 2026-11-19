def load_dict(file_path):
    word_dict = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    eng, chn = line.split()
                    word_dict[eng] = chn
    except FileNotFoundError:
        print("Dictionary file not found, will create a new one.")
    return word_dict

def save_dict(word_dict, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        for k, v in word_dict.items():
            f.write(f"{k} {v}\n")

def main():
    dict_path = "dictionary.txt"
    word_dict = load_dict(dict_path)
    while True:
        print("\n===== Dictionary Menu =====")
        print("1. Add word")
        print("2. Query word")
        print("3. Exit")
        choice = input("Please select option: ")
        if choice == "1":
            eng = input("Input English word: ").strip()
            chn = input("Input Chinese meaning: ").strip()
            if eng in word_dict:
                print("This word already exists!")
            else:
                word_dict[eng] = chn
                save_dict(word_dict, dict_path)
                print("Add successfully!")
        elif choice == "2":
            eng = input("Input English word to query: ").strip()
            if eng in word_dict:
                print(f"{eng} : {word_dict[eng]}")
            else:
                print("Word not found in dictionary.")
        elif choice == "3":
            print("Exit program.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()