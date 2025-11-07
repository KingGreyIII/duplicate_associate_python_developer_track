from string import Template

wikipedia = Template("$tool is a $description")

# defining variable
tool1 = "Natural Language Toolkit"
tool2 = "TextBlob"
tool3 = "Gensim"

description1 = "suite of libraries and programs for symbolic and statistical natural language processing (NLP) for English written in the Python programming language. It was developed by Steven Bird and Edward Loper in the Department of Computer and Information Science at the University of Pennsylvania."
description2 = "Python library for processing textual data. It provides a simple API for diving into common natural language processing tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more."
description3 = "Python library for processing textual data. It provides a simple API for diving into common natural language processing tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more."
# Substitute variables in template
print(wikipedia.substitute(tool =tool1, description=description1))
print(wikipedia.substitute(tool =tool2, description=description2))
print(wikipedia.substitute(tool =tool2, description=description3))