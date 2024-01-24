#Data structures are a way of organizing data, ex: a bool, int, float, string, but also 
#tuple, set, list, dictionary, file, and array.

#Strings are a set of characters made by using quotation marks. ex: "Bean" or 'Bean'.
#Also they are unmutable so they can't be changed. Strings are ordered.
"bean" 'bean'

#mutable means that you can change it.

#ordered means that it has a position you can use.
#ex: "bean"[0] would be 'b' and "bean"[1] would be 'e'."
print("bean"[0]);
print("bean"[1]);

#multiline strings are made by using 3 quotation marks. ex: """Bean""". These strings go
#on muitiple lines
'''beeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaans'''

"Lists:"
#Lists look like this

listofBEANS = ("black bean", "brown bean", "green bean", "lean bean", "lentil bean")
print(listofBEANS[2])

# 0 is the first item of a list
print(listofBEANS[0])

#you can also put varied things in lists, like strings, bools, and integers, at the same time
color = ("red,","greem", "blu", "5")
print(color[3])
print(color[0])

fruit = ("grape","berry", "beef")
#you can make lists of lists
listLIST = ([listofBEANS],[fruit],[color])
print(listLIST[0])