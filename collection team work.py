# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

Authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889", }   #the mistake occured in this line so we added a comma and changed the parenthesis to the right one because it had the wrong parenthesis.

for Authors, date in authors.items():
    print("%s" % authors + " died in " + "%d." % Date)   #there was no parenthesis after the date, so we added one and also an indent.

