text = '''My name is Ajay Kumar
What about you?
'''
file = open("Write.txt", "w")
file.write(text)
file.close()
print("==== Done ====")
print(f"File successfully written in (Write.txt): {text} ")
