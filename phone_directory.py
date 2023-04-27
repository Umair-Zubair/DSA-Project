#making trie 

def make_trie(*words):
    with open("tst.txt","r") as testing:
        root = testing.read()
        if len(root)!=0:
            root = eval(root)
    if len(words) == 0:
        return "Please enter a name"
    for word in words:
        if not word: 
            continue
        current_dict = root 
        for letter in word:
            if letter not in current_dict:
                current_dict[letter] = {} #aik letter ki aik dict banana
            current_dict = current_dict[letter] #usi letter ke ander aik dict banana
        if letter == word[-1]: #jab end ho iska mtlb letter end hogaya hai aur Flag daaldo 
            current_dict["Flag"] = True 
    with open("tst.txt","w") as out:
        out.write(str(root))
    return root
        
    
#make_trie("Aria", "Ace", "Aspen", "Atlas", "Autumn", "Blaze", "Blue", "Cash", "Clover", "Cruz", "Dahlia", "Diesel", "Eden", "Fox", "Hunter", "Jade", "Jagger", "Kai", "Kingston", "Knox", "Luna", "Levi", "Maverick", "Meadow", "Marley", "Nova", "Ocean", "Onyx", "Orion", "Phoenix", "Poppy", "Raven", "Ruby", "Scarlett", "Skye", "Saffron", "Summer", "Storm", "Violet", "Willow")
# make_trie("Umair")
make_trie('Conrad', 'Seamus', 'Clark', 'Stephen', 'Shelby', 'Winter', 'Carson', 'Jodie', 'Essence', 'Tammy', 'Kaytlin', 'Devyn', 'Davin', 'Elisa', 'Vladimir', 'Fabiola', 'Cristina', 'Brooklyn', 'Beverly', 'Naomi', 'Bradford', 'Shelbi', 'Raheem', 'Emely', 'Alejandro', 'Valencia', 'Nathanial', 'Kami', 'Marilyn', 'Lia', 'Johnnie', 'Shea', 'Riana', 'Griffin', 'Kaitlyn', 'Treyvon', 'Kiah', 'Aniyah', 'Carolyn', 'Edgardo', 'Bayley', 'Jaquelyn', 'Milo', 'Corbin', 'Ivonne', 'Kendrick', 'Arielle', 'Kala', 'Cori', 'Ronan', 'Demonte', 'Dale', 'Rashad', 'Jimmy', 'Allie', 'Giana', 'Debra', 'Sherman', 'Arlene', 'Ayanna', 'Pearl', 'Cristal', 'Cale', 'Ilana', 'Khadijah', 'Brielle', 'Bonnie', 'Malorie', 'Joann', 'Kylan', 'Aurora', 'Autum', 'Aileen', 'Betsy', 'Sky', 'Jaden', 'Zavier', 'Addison', 'Skyla', 'Rylee', 'Todd', 'Annalee', 'Jonatan', 'Salvador', 'Isai', 'Lea', 'Shaina', 'August', 'Kristy', 'Brock', 'Julia', 'Miguel', 'Violet', 'Jay', 'Hollie', 'Iris', 'Savana', 'Aidan', 'Yulissa', 'Iyanna', 'Ashly', 'Jeffery', 'Raekwon', 'Dimitri', 'Lucero', 'Stetson', 'Rivka', 'Emerald', 'Asia', 'Richard', 'Rosario', 'Eunice', 'Jasmin', 'Jack', 'Nathanael', 'Pedro', 'Joy', 'Zechariah', 'Jamya', 'Lilia', 'Anissa', 'Kory', 'Fernando', 'Gabriella', 'Deondre', 'Destany', 'Nia', 'Terrance', 'Dean', 'Kaiden', 'Destin', 'Kelvin', 'Rianna', 'Harry', 'Jaycob', 'Kolten', 'Brennen', 'Elisha', 'Serenity', 'Chantal', 'Jamaal', 'Jarett', 'Juwan', 'Mark', 'Tabatha', 'Markell', 'Samara', 'Fidel', 'Beatrice', 'Josef', 'Lloyd', 'Kellen', 'Dwight', 'Augustus', 'Oliver', 'Jayden', 'Natalya', 'Aya', 'Mason', 'Keara', 'Crystal', 'Rayne', 'Nelly', 'Arianna', 'Anjali', 'Ladarius', 'Nathaly', 'Antonia', 'Niya', 'Bruce', 'Sheridan', 'Kia', 'Isabella', 'Andie', 'Bradly', 'Kelly', 'Reginald', 'Marley', 'Brett', 'Arthur', 'Johnson', 'Christine', 'Karina', 'Dewayne', 'Raven', 'Kirstyn', 'Daquan', 'Shlomo', 'Kailey', 'Kailyn', 'Aislinn', 'Ashton', 'Kody', 'Jolene', 'Jeremy', 'Kallie', 'Chaim', 'Rudy', 'Jeniffer', 'Belinda', 'Leann', 'Uriah', 'Sherry', 'Jorge', 'Allyson', 'Kerri', 'Shanice', 'Jenny', 'Axel', 'Miles', 'Lynette', 'Melody', 'Montana', 'Ellen', 'Alesha', 'Alejandra', 'Jovanni', 'Sean', 'Jalil', 'Skye', 'Brant', 'Ezequiel', 'Jadyn', 'Mitchel', 'Skylar', 'Jodi', 'Bobby', 'Kendra', 'Alvaro', 'Desire', 'Wesley', 'Erin', 'Brianne', 'Shannon', 'Kaliyah', 'Ignacio', 'Max', 'Hudson', 'Clyde', 'Catherine', 'Jalon', 'Lyndsay', 'Stacie', 'Annie', 'Shae', 'Brynn', 'Cecelia', 'Kalista', 'Lexi', 'Maureen', 'Luz', 'Abdul', 'Keven', 'Brenton', 'Imani', 'Rene', 'Tahj', 'Alexzander', 'Danyelle', 'Arturo', 'Stefan', 'Emmanuel', 'Elisabeth', 'Enrique', 'Lucy', 'Marcus', 'Gary', 'Konnor', 'Marquise', 'Holly', 'Brooke', 'Aiden', 'Jakob', 'Kristen', 'Alyson', 'Andy', 'Cora', 'Shamar', 'Kameron', 'Scott', 'Lilliana', 'Houston', 'Kristian', 'Noa', 'Keagan', 'Tess', 'Pierce', 'Bruno', 'Kurt', 'Justin', 'Kelsea', 'Caelan', 'Karlee', 'Krystal', 'Federico', 'Brooklynn', 'Ashlin', 'Yulisa', 'Isabela', 'Matteo', 'Alaysia', 'Darby', 'Dylon', 'China', 'Carla', 'Maira', 'Osvaldo', 'Jadon', 'Brissa', 'Willow', 'Jocelyn', 'Isabell', 'Trisha', 'Bret', 'Jaila', 'Caitlin', 'Amberly', 'Vera', 'Noel', 'Tierney', 'Reagan', 'Gino', 'Kathleen', 'Randi', 'Alvin', 'Waylon', 'Kian', 'Madeline', 'Kavon', 'Georgia', 'Autumn', 'Makayla', 'Miguelangel', 'Carter', 'Nehemiah', 'Kailee', 'Tyrell', 'Kassidy', 'Jaylon', 'Barrett', 'Kaley', 'Raina', 'Jimmie', 'Lexus', 'Danica', 'Elliott', 'Deangelo', 'Jaya', 'Daylon', 'Kacie', 'Lila', 'Joshua', 'Giovanni', 'Donavan', 'Lester', 'Abel', 'Ricky', 'Lawson', 'Maddie', 'Bowen', 'Christa', 'Kyron', 'Mackenzi', 'Aubrey', 'Dontae', 'Edgar', 'Raegan', 'Rachelle', 'Maxim', 'Gideon', 'Darian', 'Donnie', 'Jonathan', 'Breeanna', 'Roman', 'Danika', 'Muhammad', 'Ginger', 'Augustine', 'Saul', 'Camila', 'Donavon', 'Reynaldo', 'Billy', 'Sylvia', 'Keelan', 'Turner', 'Denver', 'Donnell', 'Ella', 'River', 'Noor', 'Amber', 'Trinity', 'Shantel', 'Thomas', 'Vicente', 'Aliza', 'Presley', 'Rylan', 'Gina', 'Dana', 'Julie', 'Santana', 'Halee', 'Kai', 'Georgina', 'Harlee', 'Cooper', 'Manuel', 'Madyson', 'Tomas', 'Katarina', 'Jocelyne', 'Khalid', 'Lane', 'Mykayla', 'Alexia', 'Blaze', 'Tre', 'Sam', 'Mahogany', 'Bella', 'Ian', 'Celeste', 'Amaya', 'Ronald', 'Sawyer', 'Savannah', 'Amiah', 'Gloria', 'Miranda', 'Jeanette', 'Holden', 'Paul', 'Regan', 'Cinthia', 'Truman', 'Sidney', 'Christen', 'Myia', 'Daron', 'Patience', 'Hasan', 'Abram', 'Devontae', 'Bradley', 'Sheldon', 'Beatriz', 'Shelbie', 'Jake', 'Yamileth', 'Kayley', 'Marcel', 'Alani', 'Mariano', 'Vivian', 'Terrence', 'Daren', 'Nico', 'Bronson', 'Ali', 'Seth', 'Nathen', 'Raul', 'Cullen', 'Demarco', 'Kelis', 'Lela', 'Caley', 'Blake', 'Jazmin', 'London', 'Infant', 'Anna', 'Xander', 'Savion', 'Cruz', 'Davion', 'Javen', 'Juliann', 'Brayan', 'Mindy', 'Claudia', 'Talon', 'Jarret', 'Angelina', 'Ethen', 'Junior', 'Chantel', 'Nash', 'Zane', 'Elaina', 'Amelia', 'Jase', 'Marjorie', 'Cecil', 'Perry', 'Betty', 'Diego', 'Leighton', 'Samson', 'Ezekiel', 'Anabelle', 'Jacie', 'Norman', 'Asher', 'Milena', 'Brannon', 'Kyree', 'Arely', 'Andreas', 'Stone', 'Madelyne', 'Hope', 'Benito', 'Jalyn', 'Vance', 'Tyrek', 'Tristin', 'Marcellus', 'Kathryn', 'Christina', 'Layton', 'Valeria', 'Maximiliano', 'Leila', 'Dangelo', 'Ryland', 'Tucker', 'Johnathan', 'Cherish', 'Raymond', 'Kimberly', 'Keyla', 'Louis', 'Enzo', 'Lilianna', 'Ken', 'Shayla', 'Lorena', 'Giovani', 'Joanne', 'Jaelynn', 'Aria', 'Emily', 'Lauryn', 'Jericho', 'Tyrone', 'Regina', 'Killian', 'Teagan', 'Kacey', 'Dustyn', 'Callie', 'Nicklaus', 'Nick', 'Esther', 'Daphne', 'Nathalia', 'Marcelo', 'Mackenzie', 'Priscilla', 'Kalen', 'Leeann', 'Camryn', 'Tyriq', 'Julianne', 'Gilberto', 'Antonio', 'Aspen', 'Dajah', 'Eden', 'Felix', 'Adrian', 'Hakeem', 'Devante', 'Suzanne', 'John', 'Rex', 'Aiyana', 'Abdullah', 'Linda', 'Brooks', 'Ann', 'Kinsley', 'Kylie', 'Charlie', 'Trystan', 'Aron', 'Jasmyn', 'Briar', 'Nikolas', 'Brian', 'Francis', 'Lynn', 'Ester', 'Galen', 'Jayvon', 'Dora', 'Bridget', 'Lars', 'Sofia', 'Marlene', 'Austyn', 'Dashawn', 'Bryan', 'Tayler', 'Maryam', 'Peyton', 'Keandre', 'Josiah', 'Ellis', 'Gabrielle', 'Montserrat', 'Phoenix', 'Corrina', 'Emelia', 'Reece', 'Reese', 'Aman', 'Tyler', 'Guadalupe', 'Lukas', 'Verania', 'Cristofer', 'Jose', 'Makenna', 'Candace', 'Julius', 'Lizet', 'Sariah', 'Rachel', 'Jaydon', 'Naya', 'Derick', 'Laila', 'Sana', 'Julien', 'Lana', 'Janine', 'Marcella', 'Dion', 'Genaro', 'Fredy', 'Kylah', 'Gunner', 'Kelley', 'Christion', 'Deante', 'Blair', 'Jaelyn', 'Vaughn', 'Isiah', 'Mohamed', 'Alexandra', 'Kaylin', 'Joana', 'Madison', 'Litzy', 'Nayely', 'Jordi', 'Juliana', 'Courtney', 'Kalob', 'Micaela', 'Briza', 'Yehuda', 'Caroline', 'Angel', 'Marlee', 'Graham', 'Mika', 'Carley', 'Tristen', 'Timothy', 'Keshaun', 'Daria', 'Tyron', 'Russell', 'Tatiyana', 'Aditya', 'Darwin', 'Charisma', 'Zara', 'Justina', 'Chana', 'Brigid', 'Justice', 'Edmund', 'Lucas', 'Maryjane', 'Sahil', 'Sonia', 'Damian', 'Isaiah', 'Madalynn', 'Baby', 'Hernan', 'Mathew', 'Dallas', 'Dixie', 'Jonah', 'Karli', 'Jayda', 'Yisroel', 'Dejuan', 'Laurel', 'Miah', 'Melina', 'Joseline', 'Brycen', 'Katlyn', 'Loren', 'Cristian', 'Benjamin', 'Iyana', 'Paris', 'Blayne', 'Quinton', 'Katia', 'Anisa', 'Keith', 'Juliette', 'Christopher', 'Cheyanne', 'Galilea', 'Nancy', 'Susanna', 'Dwayne', 'Mario', 'Ralph', 'Elle', 'Ada', 'Candy', 'Travon', 'Elias', 'Braydon', 'Porter', 'Alea', 'Erika', 'Gerard', 'Tracy', 'Menachem', 'Misty', 'Hallie', 'Roger', 'Danae', 'Johan', 'Laney', 'Santos', 'Kaelyn', 'Emma', 'Katlynn', 'Grecia', 'Mariana', 'Braedon', 'Daryl', 'Sebastian', 'Janeth', 'Jacquelin', 'Ammon', 'Isabelle', 'Alina', 'Catalina', 'Austin', 'Jocelynn', 'Austen', 'Alison', 'Devonte', 'Louie', 'Ivette', 'Yoselin', 'Callista', 'Jarod', 'Allan', 'Belen', 'Dominique', 'Tavian', 'Parker', 'Cordell', 'Rafael', 'Francisco', 'Khalil', 'Jabari', 'Unique', 'Duncan', 'Reed', 'Stanley', 'Hans', 'Matthias', 'Annabel', 'Brandt', 'Keri', 'Adan', 'Gianni', 'Dominick', 'Treyton', 'Kieran', 'Nyla', 'Samir', 'Toby', 'Carmen', 'Priscila', 'Devlin', 'Camille', 'Paloma', 'Jaylen', 'Carolina', 'Darrian', 'Tiara', 'Adriel', 'Jade', 'Harley', 'Lindsey', 'Bree', 'Dylan', 'Fatima', 'Darion', 'Vanesa', 'Mitchell', 'Shanna', 'Joseph', 'Ileana', 'Yaritza', 'Pauline', 'Kathy', 'Zack', 'Tasha', 'Damon', 'Noah', 'Angeles', 'Jamel', 'Tanner', 'Reina', 'Dymond', 'Marco', 'Alfredo', 'Isela', 'Lance', 'Kiana', 'Breann', 'Albert', 'Kadin', 'Elijah', 'Shira', 'Kaitlin', 'Lizeth', 'Hezekiah', 'Jude', 'Sebastien', 'Dillan', 'Katelyn', 'Giancarlo', 'Dane', 'Jaret', 'Carlo', 'Javier', 'Britton', 'Natalee', 'Uriel', 'Alexcia', 'Adrianna', 'Israel', 'Gissell', 'Gaige', 'Kent', 'Makenzie', 'Charity', 'George', 'Jermaine', 'Alfred', 'Herbert', 'Clint', 'Eduardo', 'Frances', 'Yvonne', 'Makaila', 'Ramsey', 'Bryant', 'Marcos', 'Jackson', 'Codey', 'Cedrick', 'Rick', 'Aryanna', 'Leslie', 'Lisa', 'Jamal', 'Yazmine', 'Bobbi', 'Alex', 'Henry', 'Terri', 'Jameson', 'Tavion', 'Brayden', 'Shiann', 'Ellie', 'Corey', 'Amalia', 'Martha', 'Gonzalo', 'Tye', 'Koby', 'Marion', 'Dallin', 'Jaxson', 'Rosemary', 'Eliza', 'Citlali', 'Leif', 'Eva', 'Camden', 'Kaleigh', 'Ashli', 'Ananda', 'Jessi', 'Garret', 'Genevieve', 'Dejon', 'Alysa', 'Maria', 'Dario', 'Sonny', 'Giselle', 'Maximus', 'Whitley', 'Eryn', 'Ernest', 'Mona', 'Nina', 'Cannon', 'Joe', 'Rico', 'Macey', 'Gilbert', 'Bennett', 'Alli', 'Keyanna', 'Brandi', 'Miriam', 'Oswaldo', 'Wyatt', 'Cassie', 'Harmony', 'Misael', 'Amos', 'Semaj', 'Logan', 'Hailee', 'Shauna', 'Liza', 'Harrison', 'Brendan', 'Jordin', 'Kira', 'Draven', 'Amanda', 'Mohammed', 'Bishop', 'Kasandra', 'Brennan', 'Roxana', 'Joan', 'Janelle', 'Elaine', 'Cydney', 'Destinee', 'Javon', 'Dayana', 'Madisyn', 'Sahara', 'Sadie', 'Haylie', 'Damien', 'Trevion', 'Jesse', 'Domenic', 'Mackenna', 'Sharon', 'Kassandra', 'Avery', 'Braeden', 'Averi', 'Alysia', 'Alisha', 'Harvey', 'Baylie', 'Dominic', 'Zayne', 'Constance', 'Robyn', 'Annmarie', 'Mikel', 'Salena', 'Olga', 'Messiah', 'Judah', 'Elvis')
with open("tst.txt","r") as testing:
    root = eval(testing.read())
#deletion
# print(root)
def delete_from_trie(root, word):
    with open("tst.txt","r") as testing:
        root = eval(testing.read())
    node = root
    parents = [None] * (len(word) + 1)  # keep track of parent nodes
    
    # Traverse the trie to find the node that represents the word to be deleted
    for i, c in enumerate(word):
        if c not in node:
            # Word not found in trie, do nothing
            return
        parents[i] = node #har letter ko aik list mein store krana taake baad mein use kr sakein
        node = node[c] #taake we can reach the flag
    
    # If the 'Flag' key is not in the node, the word is not in the trie, so do nothing
    if 'Flag' not in node:
        return
    
    # Remove the 'Flag' key from the node to signify that the word is no longer in the trie
    del node['Flag']
    
    # Traverse the word in reverse order and remove any nodes that have no children
    for i in range(len(word)-1, -1, -1): #reverse mein chalega 
        if not node and parents[i]: #agr node ki value none hai aur parents mein kuch hai toh krega delete
            # If the current node has no children and is not the root node, remove it
            del parents[i][word[i]]
            node = parents[i]
        else: #agr node none nahi iska mtlb parents[i] wale letter ke bache hain usko na delete kero
            # If the current node has children or is the root node, we're done
            break
    with open("tst.txt","w") as out:
            out.write(str(root))
    

#delete_from_trie(root, "Umair")
with open("tst.txt","r") as testing:
    root = eval(testing.read())
# print(root)

# delete_from_trie(root,"Shaaf")


# searching in trie using dfs

# print(root)

# this intial search checks if a word is in trie or not
def search_name(root, word):
    node = root
    for c in word:
        if c not in node:
            return False
        node = node[c]
    return 'Flag' in node


#  this search returns the words the start with a semilar prefix

def search_trie(root, prefix):
    # Traverse the trie to the point where the prefix ends
    node = root
    for c in prefix:
        if c not in node:
            return []
        node = node[c]
    
    # Perform a depth-first search to find all words with the prefix
    results = []
    stack = [(node, prefix)]
    while stack:
        current_dict, current_prefix = stack.pop()
        if 'Flag' in current_dict:
            results.append(current_prefix)
        for letter, child_dict in current_dict.items():
            if letter != 'Flag':
                stack.append((child_dict, current_prefix + letter))
    
    return results



#print(search_trie(root,"S"))
# delete_from_trie(root,"Shaaf")
# print(root)

# print(search_trie(root,"M"))

# "Aria", "Ace", "Aspen", "Atlas", "Autumn", "Blaze", "Blue", "Cash", "Clover", "Cruz", "Dahlia", "Diesel", "Eden", "Fox", "Hunter", "Jade", "Jagger", "Kai", "Kingston", "Knox", "Luna", "Levi", "Maverick", "Meadow", "Marley", "Nova", "Ocean", "Onyx", "Orion", "Phoenix", "Poppy", "Raven", "Ruby", "Scarlett", "Skye", "Saffron", "Summer", "Storm", "Violet", "Willow"


# def Select_Funtion():
#     print("Please select the option from below by typing the number corresponding to it.")
#     print("1. Create a New Contact\n2. Search a Contact.\n3. Delete a Contact.")
#     option = int(input())
#     name = input("Please Enter a Name:")
#     if option == 1:
#         make_trie(name)
#     elif option == 2:
#         print(search_name(root,name))
#     elif option == 3:
#         delete_from_trie(root,name)
#     else:
#         print("Select a Valid Option.")
        
# # Select_Funtion()