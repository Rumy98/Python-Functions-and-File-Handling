name=input("Enter name: ")
file=open('name.txt','w')
file.write(name)
file.write("\nName saved successfully.")

file.close()