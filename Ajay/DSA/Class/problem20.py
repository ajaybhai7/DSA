class DiaryManager:
    def __init__(self):
        self.file_name = "Secret_diary.txt"

    def add_entry(self, entry_txt):
        with open(self.file_name, 'a') as f:
            f.write(f"{entry_txt}\n")

    def show_all(self):
        with open(self.file_name, 'r') as f:
            file = f.readlines()
            for txt in file:
                print(f"{txt}")
d1 = DiaryManager()
# d1.add_entry(entry_txt=input("Write Something in Diary: "))
d1.show_all()
