#Comments are text that will not be executed in your code. Rather comments are for other programmers to read. 

# All of the exercises below are commented out. Write your Javascript code after each exercise.

#Variables and Data Types 
#Print each variable and test your code in the terminal using the Python interpreter

#example
greeting = 'Hello Prepster'
print(greeting); #this should print 'Hello Prepster'

#1 Variables with a String value
#Declare variables named first_name, last_name, birth_place, hobby, role_model, famous_quote, fav_president, fav_food, fav_color, fav_song
first_name = 'john'
last_name = 'wright'
birth_place = 'washington d.c.'
hobby = 'riding motorcycles'
role_model = 'sgt parnass'
famous_quote = 'left turn saves lives'
fav_president = 'barack obama'
fav_food = 'pizza'
fav_color = 'green'
fav_song = 'unforbbiden fruit by drake'

#Assign your own string values to each variable and print each variable.
print(first_name)
print(last_name)
print(birth_place)
print(hobby)
print(role_model)
print(famous_quote)
print(fav_president)
print(fav_food)
print(fav_color)
print(fav_song)
#2 String Concatenation
#Declare a variable named full_name and concatenate first_name and last_name. Print the full_name variable.
full_name = first_name + " " + last_name
print(full_name)
stuff = hobby + " " + role_model + " " + famous_quote + " " + fav_president
#Declare a variable named intro that creates the following sentence:
print(full_name + " " + birth_place + " " + stuff)
#'Hello, my name is x and I was born in y.' Where x is full_name and y is birth_place. Print the intro variable.
nam = 'hello my name is'
nam1 = 'and I was born in'
print (nam + " " + full_name + " " + nam1 + " " + birth_place)

#Declare a variable named about_me that creates the following sentence:
#'My hobby is x, my favorite song is y, and I like to eat z.' Where x is hobby, y is fav_song and z is fav_food. Print the about_me variable.
name2 = 'My hobby is,'
name3 = 'My favorite song is,'
name4 = 'and I like to eat'
print(name2 + " " + hobby + " " + name3 + " " + fav_song + " " + name4 + " " + fav_food)
#3 Spacing with tabs and newlines
print("\tname2 + " " + \thobby + " " + \tname3 + " " + \tfav_song + " " + \tname4 + " " + \tfav_food")
print("\tname2" "\thobby" "\tname3" "\tfav_song" "\tname4" "\tfav_food")
print("\nname2" "\nhobby" "\nname3" "\nfav_song" "\nname4" "\nfav_food")
#Declare a variable named my_hero that the following sentence using a tab:
my_hero = 'superman'
justice_league = 'I like watching my favorite movie,'
hero = 'is my hero'
print(justice_league + " " + my_hero + " " + hero)

#'My hero is x and his famous quote is y.' Where x is role_model and y is famous_quote. Print the my_hero variable.
hero1 = 'my hero is'
hero2 = 'and his famous quote is'
print(hero1 + ' ' + my_hero + ' ' + hero2 + ' ' + famous_quote)
#Declare a variable named my_favs that creates the following sentence and returns a new line after each numbered item. 
my_favs = 'my favorite thing to do, is ride my motorcycle'
my_favs1 = 'Because one day I want to be a motogp racer'
print(my_favs+ ' ' + my_favs1)
print('my favorite thing to eat is : \npizza\neggs\nchicken')

#'This is what I like: 1. hobby 2. fav_color 3. fav_song
print('This is what I like: \n1.hobby\n2.fav_color\n3.fav_song')
#Print the my_favs variable.
print(my_favs)


#4 Variables with a Number value
#Declare variables named age, weight, shoe_size, fav_number, yen_rate, bitcoin_value, todays_temperature, hawaii_popuation, countries_traveled, number_of_siblings
name = '2'
age = '27'
weight = '215'
shoe_size = '12'

#Assign your own number values to each variable and print each variable.
print(name)
print(age)
print(weight)
print(shoe_size)
#5 Number as Strings Concatenation
print(name + ' ' + age + ' ' + weight + ' ' + shoe_size)
#Declare a variable named self_intro that creates the following sentence:

#'Aloha, my name is x and I am y years old and my shoe size is z.' Where x is full_name, y is age and z is shoe_size. Print the self_intro variable.
self_intro = 'Aloha, my name is' + ' ' + full_name + ' ' + 'and I am' + ' ' + age + ' ' + 'years old and my shoe size is' + ' ' + shoe_size
print(self_intro)


#Declare a variable name
# d market_update that creates the following sentence:
bitcoin = '6,567'
exchange_rate = '1'
market_update = "Today's bitcoin value is" + ' ' + bitcoin + ' ' + 'and the yen exchange rate is' + ' ' + exchange_rate

print(market_update)
#"Today's bitcoin value is x and the yen exchange rate is y." Where x is bitcoin_value and y is yen_rate. Print the market_update variable.


#Declare a variable named about_hawaii that creates the following sentence:
#"Did you know that Hawaii's population is x and the average temperatue is y?" Where x is hawaii_population and y is todays_temperature. Print the about_hawaii variable.
population = '390,700'
temperatue = '77*'
about_hawaii = "Did you know that Hawaii's population is" + ' ' + population + ' ' + 'and the average temperature is' + ' ' + temperatue
print(about_hawaii)
#6 Variables with a List value
#Declare a variable named fab_five and assign it a list containing five of your all time favorite snacks. Print the fab_five variable.
fab_five = 'snickers' + " " "reese's" + " " + 'hersey' + " " + 'honeybun' + " " + 'hot cheetos'
print(fab_five)
#Declare a variable named plate_lunch and assign it a list containing five of your favorite lunch items. Print the plate_lunch variable.
plate_lunch = 'pizza' + ' ' + 'tuna' + ' ' + 'chicken' + ' ' + 'burger' + ' ' + 'tacos'
print(plate_lunch)
#Declare a variable named ice_cream and assign it a list containing three of your favorite ice cream flavors. Print the ice_cream variable.
ice_cream = ['vanilla' + ' ' +'strawberry' + ' ' + 'cookies N cream' + ' ' + 'chocolate' + ' ' + 'vanilla strawberry']
for item in ice_cream:
  print(item)
#Declare a variable named west_siiiiide and assign it a list containing states found on the west coast of the US. Print the west_siiiiide variable.
west_siiiiide = ['hawaii' + ' ' + 'california' + ' ' + 'nevada' + ' ' + 'arizona']
for item in west_siiiiide:
    print(item)
#Declare a variable named mega_millions and assign it a list containing the Mega Millions Lottery results for May, 4, 2018
#https://www.lotteryusa.com/mega-millions/. Print the mega_millions variable
mega_millions = ["04" + ' ' + "05" + ' ' + "10" + ' ' + "12" + ' ' + "18" + ' ' + "21"]
for item in mega_millions:
    print(item)

#Declare a variable named hamajang and assign it a list containing six different data types. Print the hamajang variable.
hamajang = ["linux" + ' ' + "python" + ' ' + "c++" + ' ' + "microsoft" + ' ' + "apple" + ' ' + "java"]
for item in hamajang:
    print(item)
#Declare a variable named dynamic_duos and assign it a list containing 3 lists, with each list containing items that pairs well with each other. Print the dynamic_duos variable.
dynamic_duos = [
['superman', 'battman', 'hulk'],
['robin', 'spiderman', 'xmen'],
['flash', 'arrow', 'antman']
]
print(dynamic_duos)
print(dynamic_duos[0][0])
print(dynamic_duos[0][1])
print(dynamic_duos[0][2])
print(dynamic_duos[1][0])
print(dynamic_duos[1][1])
print(dynamic_duos[1][2])
print(dynamic_duos[2][0])
print(dynamic_duos[2][1])
print(dynamic_duos[2][2])

#Print the following:
#Gin
food = ['gin', 'peanut', 'cheeseburger']
#peanut butter

#cheeseburger
for item in food:
    print(item)

#7 Accessing values in List
vics_list = ['Hendricks gin', 'Fever Tree tonic', 'Costco pub mix', 'cool ranch doritos', 'oreos', 'Safeway fried chicken', 'Morning Glass coffee']
for item in vics_list:
    print(item)
#Print the entire list.
print(len(vics_list))
#Print the length of the list.

#Print only the first element in the list.
print(vics_list[0][0])
print(vics_list[0][1])
print(vics_list[0][2])
print(vics_list[0][3])
print(vics_list[0][4])
print(vics_list[0][5])
print(vics_list[0][6])
print(vics_list[0][7])
#Print only the last element in the list.
print(vics_list[0][7])
print(vics_list[6])
#Print 'Safeway fried chicken'
print(vics_list[5])
#Replace 'cool ranch doritos' with 'carrot cake' and print the list.
vics_list[4] = 'carrot cake'
print(vics_list)
#Print the last element in the list using -1
vics_list[6][-1]
print(vics_list)
print(vics_list[-1])
#8 Variables with a Dictionary value

#Declare a variable named car and create the following key-value pairs:
car = {'Telsa', 'Model', '3500', 'red', 'False', "moon roof", "leather seats", "iphone docker"}
# - key: brand string value: Tesla,
# - key: model string value: Model 3,
# - key: price number value: 35000,
# - key: color string value: red,
# - key: production boolean value: False,
# - key: features list value: moon roof, leather seats, iphone docker

#Print the car variable.
print(car)

#Declare a variable named footwear and create the following key-value pairs:
# - key: brand string value: Vivo Barefoot,
# - key: url string value: https://www.vivobarefoot.com/us,
# - key: gender string value: Mens,
# - key: type string value: Ababa Canvas,
# - key: price number value: 80,
# - key: color list value: tan, black stripes, gum
# - key: ordered boolean value: True
footwear = {"Vivo barefoot", "https://www.vivobarefoot.com/us", "Mens", "Ababa Canvas", "80", "tan", "black stripes", "gum", "True"}
#Print the footwear variable.
print(footwear)

#Declare a variable named bank and create the following key-value pairs:
# - key: name  string value: First Hawaiian Bank,
# - key: employees number value: 2200,
# - key: headquarters string value: Honolulu,
# - key: revenue number value: 700000000,
# - key: nasdaq string value: FHB,
# - key: products list value: savings, loans, trust, wealth management,
# - key: executive dictionary value: name: Robert Harrison, title CEO, salary: 2000000
bank = {"First Hawaiian Bank", "2200", "Honolulu", "70000000", "FHB"}
bank = {"savings", "loans", "trust", "wealth management"}
bank = {"Robert Harrrison", "title CEO", "salary", "200000"}



#Print the bank variable.
print(bank)

#Declare a variable pandas and assign it an EMPTY dictionary.
#You will add the following key-value pairs:
# - key: name string value: Panda Express
# - key: restaurants number value: 2000
# - key: cuisine string value: Gourmet Chinese Food
# - key: menu list value: Orange Chicken, Walnut Shrimp, Sweet and Sour pork
# - key: highest_revenue string value: Ala Moana Center Food Court
pandas = {}
pandas['name'] = 'Panda Express'
pandas['restaurants'] = 2000
pandas['cuisine'] = 'Gourmet Chinese Food'
pandas['menu'] = ['Orange Chicken', 'Walnut Shrimp', 'Sweet and Sour pork']
pandas['highest_revenue'] = 'Ala Moana Center Food Court'
print(pandas)
#Print the pandas variable.
print(pandas)

#Declare a variable named bucket_list and assign it to an EMPTY dictionary.
#You will add the following key-value pairs:
# - key: travel string value of your choice
# - key: learn string value of your choice
# - key: weight number value of your choice
# - key: to_dos list value of your choice
# - key: meet_person string value of your choice  

#Print the bucket_list variable.


#9 Variable with a Tuple value
#Declare a variable named bruce_bio and assign a tuple containing the following values: Bruce Lee, male, 32, San Francisco, [Kung-Fu Master, actor, philosopher]

#Print the bruce_bio variable.


#Declare a variable named movies and assign a tuple containing the following values: [The Big Boss, 1971],[Fist of Fury, 1972], [The Way of the Dragon, 1972], [The Game of Death, 1972]

#Print the movies variable.


#Declare a variable named updated_bio and add the bruce_bio and movies tuples together. Print the updated_bio variable.


#Print the following values:
#The length of the updated_bio tuple

#Bruce Lee

#Index position 1

#['Game of Death', 1972]

#philosopher

#1971

#The Way of the Dragon

#Fist of Fury

#The last value using -1

#Game of Death using -1


#10 Variables with a Boolean value
#Declare the following variables and assign either a True or false value for each.
#female, american, likes_coding, is_hungry, has_a_dog

#Print each variable that you declare.

