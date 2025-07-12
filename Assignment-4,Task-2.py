statement_1=input("Enter text to write to the file: ")
with open("output.txt","w") as file:
    file.write(statement_1 + "\n")
    print("Data successfully written to output.txt.\n")

statement_2=input("Enter additional text to append: ")
with open("output.txt","a") as file:
    file.write(statement_2 + "\n")
    print("Data successfully appended.\n")

print("\nFinal content of 'output.txt':")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
