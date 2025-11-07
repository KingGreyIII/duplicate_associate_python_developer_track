with open("./alice.txt", encoding= "utf-8") as file:
    text = file.read()
# text = "This Web site includes information about Project Gutenberg-tm,including how to make donations to the Project Gutenberg Literary.Archive Foundation, how to help produce our new eBooks, and how to subscribe to our email newsletter to hear about new eBooks."
n = 0
for word in text.split():

    if word.lower()  == "and": #in ["cat", "cats"]:
        n+= 1

print("In the file Alice.txt, cat/cats was mentioned {} times".format(n))