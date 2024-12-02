#{"dev":500,"rahul":700,"deepak":800,"ayan":100}
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
def maxx():
  max=0
  winner=""
  for i in dict:
      ok=dict[i]
      if max<int(ok):
          max=int(ok)
          winner=i
  print(f"The winner is {winner} with a bid of ${max}")


print(logo)
a=True
dict={}
while a:
    name=input(f"What is your name?:")
    bid=int(input(f"What's your bid?: $"))
    dict[name]=bid
    ask=input(f"Are there any other bidders? Type 'yes' or 'no'.\n")
    if ask=="no":
        a=False
        maxx()
        #print(dict)
    elif ask=="yes":
        print("more player to bid")
      
    
