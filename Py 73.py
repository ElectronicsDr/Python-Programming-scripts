file=open("filename.docx","w")
file.write("Programming just got better")
file.close()
file=open("filename.docx","r")
print(file.read())
file.close()
