import re

# variable
sentiment_analysis = "@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%"
comment = "Agh,snow! User_mentions:9, likes: 5, number of retweets: 4"
context_2 = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"

# regex format
regex = r"@\w+\W"
regex2 = r"@robot\d\W"
regex3 = r"@\w+\d\W"



# print
print(re.findall(regex, sentiment_analysis))
print(re.findall(regex2, sentiment_analysis))
print(re.findall(regex3, sentiment_analysis))
print(re.findall(r"number\sof\sretweets:\s\d", context_2))

# import re
#
# regex = r"^[aeiouAEIOU]{2,3}\w*\.txt"
#
# for text in sentiment_analysis:
#     # Find all matches of the regex
#     print(re.findall(regex, text))
#
#     # Replace all matches with an empty string
#     print(re.sub(regex, "", text))

# Write a regex to match a valid email address
regex = r"[A-Za-z0-9!#%&*\$\.]@\w+\.com"
example = "john_doe123@mail-server.com"
print(re.findall(regex, example))
