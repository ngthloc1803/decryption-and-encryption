def key():
    key = 'EIJVPGNCASRTHXKOFMWQYULBZD'
    fre = {}
    #ráng chữ cái in hoa trong bằng chữ cái bằng key phía trên và đưa nó vào fre
    for ascii in range(65,91):
        fre[chr(ascii)] = key[ascii-65]
    #ráng chữ cái in hoa trong bằng chữ cái bằng key phía trên và đưa nó vào fre
    for ascii in range(97,123):
        fre[chr(ascii)] = key[ascii-97]
    
    return fre 
print(key())

def encrypt_monoalpha(message, monoalpha_cipher):
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter, letter))
    return ''.join(encrypted_message)

message = "Today, I start studying the first day at TDTU University, I am feeling so interested"
print("Message: ",message)
print("After encrypt: ",encrypt_monoalpha(message,key()))
print()
#Decryption using Frequency Analysis.
def number (frequency_analysis):
    return frequency_analysis[1]
    
def decrypt_frequencyanalysis(massage):
    #Tần suất xuất hiện các kí tự trong mật mã bị mã hoá
    frequency_analysis = { "A" : 0,  "B" : 0,  "C" : 0,  "D" : 0,  "E" : 0,"F" : 0,  "G" : 0,
    "H" : 0,  "I" : 0,  "J" : 0,  "K" : 0,  "L" : 0,  "M" : 0,  "N" : 0,  "O" :   0,
    "P" : 0,  "Q" : 0,  "R" : 0,  "S" : 0,  "T" : 0,  "U" : 0,  "V" : 0,  "W" : 0,
    "X" : 0,  "Y" : 0,  "Z" : 0 }
    for letter in massage:
            if letter.isalpha():
                frequency_analysis[letter] += 1
    #Sắp xếp lại tần suất theo thứ tự giảm dần
    unsorted = frequency_analysis.items()
    descend = list(sorted(unsorted, key = number, reverse=True))
    #Engsub tượng trưng cho tân suất xuất hiện của bảng chữ cái ở tiếng Anh
    engsub = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
    #Ráng kí tự có tần suất xuất hiện cao nhất trong mật mã theo thứ tự của engsub
    fre = {}
    for i in range(0, 26):
        fre[descend[i][0]] = engsub[i]
    #Tiến hành thay thế kí tự đã ráng phía trên vào mật mã thu được mật mã giải mã lần thứ 1
    decryptedlist = []          
    for letter in massage:
        asciitext = ord(letter.upper())
        if  asciitext <= 90 and asciitext >= 65:
            decryptedlist.append(fre[letter])
    decrypted_message = "".join(decryptedlist)
    return decrypted_message
#50 words
message1 = "Whenever travellers penetrate into remote regions where human hunters are unknown, they find the wild things half tame, little afraid of man, and inclined to stare curiously from a distance of a few paces. But very soon they learn that man is their most dangerous enemy, and fly from him as soon as he is seen. It takes a long time and much restraint to win back their confidence"
encrypted_text1 = encrypt_monoalpha(message1,key())
#100 words
message2 = "In the early days of the West, when game abounded and when fifty yards was the extreme deadly range of the hunter's weapons, wild creatures were comparatively tame. The advent of[Pg vi] the rifle and of the lawless skin hunter soon turned all big game into fugitives of excessive shyness and wariness. One glimpse of a man half a mile off, or a whiff of him on the breeze, was enough to make a Mountain Ram or a Wolf run for miles, though formerly these creatures would have gazed serenely from a point but a hundred yards removed. The establishment of the Yellowstone Park in 1872 was the beginning of a new era of protection for wild life; and, by slow degrees, a different attitude in these animals toward us. In this Reservation, and nowhere else at present in the northwest, the wild things are not only abundant, but they have resumed their traditional Garden-of-Eden attitude toward man"
encrypted_text2 = encrypt_monoalpha(message2,key())
#500 words
message3 = "If you draw a line around the region that is, or was, known as the Wild West, you will find that you have exactly outlined the kingdom of the Coyote. He is even yet found in every part of it, but, unlike his big brother the Wolf, he never frequented the region known as Eastern America. This is one of the few wild creatures that you can see from the train. Each time I have come to the Yellowstone Park I have discovered the swift gray form of the Coyote among the Prairie-dog towns along the River flat between Livingstone and Gardiner, and in the Park itself have seen him nearly every day, and heard him every night without exception.Coyote (pronounced Ky-o'-tay, and in some regions[Pg 4] Ky-ute) is a native Mexican contribution to the language, and is said to mean halfbreed, possibly suggesting that the Coyote looks like a cross between the Fox and the Wolf. Such an origin would be a very satisfactory clue to his character, for he does seem to unite in himself every possible attribute in the mental make-up of the other two that can contribute to his success in life. He is one of the few Park animals not now protected, for the excellent reasons, first that he is so well able to protect himself, second he is even already too numerous, third he is so destructive among the creatures that he can master. He is a beast of rare cunning; some of the Indians call him God's dog or Medicine dog. Some make him the embodiment of the Devil, and some going still further, in the light of their larger experience, make the Coyote the Creator himself seeking amusement in disguise among his creatures, just as did the Sultan in the Arabian Nights. The naturalist finds the Coyote interesting for other reasons. When you see that sleek gray and yellow form among the mounds of the Prairie-dog, at once creating a zone of blankness and silence by his very presence as he goes, remember that he is hunting for something to eat; also, that there is another, his mate, not far away.[Pg 5] For the Coyote is an exemplary and moral little beast who has only one wife; he loves her devotedly, and they fight the life battle together. Not only is there sure to be a mate close by, but that mate, if invisible, is likely to be playing a game, a very clever game as I have seen it played. Furthermore, remember there is a squealing brood of little Coyotes in the home den up on a hillside a mile or two away. Father and mother must hunt continually and successfully to furnish their daily food. The dog-towns are their game preserves, but how are they to catch a Prairie-dog! Every one knows that though these little yapping Ground-squirrels will sit up and bark at an express train but twenty feet away, they scuttle down out of sight the moment a man, dog or Coyote enters into the far distant precincts of their town; and downstairs they stay in the cyclone cellar until after a long interval of quiet that probably proves the storm to be past. Then they poke their prominent eyes above the level, and, if all is still, will softly hop out and in due course, resume their feeding."
encrypted_text3 = encrypt_monoalpha(message3,key())
#1000 words
message4 = "The common Prairie-dog is typical of the West, more so than the Buffalo is, and its numbers, even now, rival those of the Buffalo in its palmiest days. I never feel that I am truly back on the open range till I hear their call and see the Prairie-dogs once more upon their mounds. As you travel up the Yellowstone Valley from Livingstone to Gardiner you may note in abundance this dunce of the plains. The dog-towns are frequent along the railway, and at each of the many burrows you see from one to six of the inmates. As you come near Gardiner there is a steady rise of the country, and somewhere near the edge of the Park the elevation is such that it imposes one of those mysterious barriers to animal extension which seem to be as impassable as they are invisible. The Prairie-dog range ends near the Park gates.General George S. Anderson tells me, however, that individuals are occasionally found on the flats along the Gardiner River, but always near the gate, and never elsewhere in the Park. On this basis, then, the Prairie-dog is entered as a Park animal. It is, of course, a kind of Ground-squirrel. The absurd name dog having been given on account of its bark. This call is a high-pitched yek-yek-yek-yeeh, uttered as an alarm cry while the creature sits up on the mound by its den, and every time it yeks it jerks up its tail. Old timers will tell you that the Prairie-dog's voice is tied to its tail, and prove it by pointing out that one is never raised without the other. As we have seen, the Coyote looks on the dog-town much as a cow does on a field of turnips or alfalfa—a very proper place, to seek for wholesome, if commonplace, sustenance. But Coyotes are not the only troubles in the life of Yek-yek. Ancient books and interesting guides will regale the traveller with most acceptable stories about the Prairie-dog, Rattlesnake, and the Burrowing Owl, all living in the same den on a basis of brotherly love and Christian charity; having effected, it would seem, a limited partnership and a most satisfactory division of labour: the Prairie-dog is to dig the hole, the Owl to mount sentry and give warning of all danger, and the Rattler is to be ready to die at his post as defender of the Prairie-dog's young. This is pleasing if true.There can be no doubt that at times all three live in the same burrow, and in dens that the hard-working rodent first made. But the simple fact is that the Owl and the Snake merely use the holes abandoned (perhaps under pressure) by the Prairie-dog; and if any two of the three underground worthies happen to meet in the same hole, the fittest survives. I suspect further that the young of each kind are fair game and acceptable, dainty diet to each of the other two. Farmers consider Prairie-dogs a great nuisance; the damage they do to crops is estimated at millions per annum. The best way to get rid of them, practically the only way, is by putting poison down each and every hole in the town, which medieval Italian mode has become the accepted method in the West. Poor helpless little Yek-yek, he has no friends; his enemies and his list of burdens increase. The prey of everything that preys, he yet seems incapable of any measure of retaliation. The only visible joy in his life is his daily hasty meal of unsucculent grass, gathered between cautious looks around for any new approaching trouble, and broken by so many dodges down the narrow hole that his ears are worn off close to his head. Could any simpler, smaller pleasure than his be discovered? Yet he is fat and merry; undoubtedly he enjoys his every day on earth, and is as unwilling as any of us to end the tale. We can explain him only if we credit him with a philosophic power to discover happiness within in spite of all the cold unfriendly world about him. When the far-off squirrel ancestor of Yek-yek took to the plains for a range, another of the family selected the rocky hills. He developed bigger claws for the harder digging, redder colour for the red-orange surroundings, and a far louder and longer cry for signalling across the peaks and canyons, and so became the bigger, handsomer, more important creature we call the Mountain Whistler, Yellow Marmot or Orange Woodchuck.In all of the rugged mountain parts of the Yellowstone one may hear his peculiar, shrill whistle, especially in the warm mornings. You carefully locate the direction of the note and proceed to climb toward it. You may have an hour's hard work before you sight the orange-breasted Whistler among the tumbled mass of rocks that surround his home, for it is a far-reaching sound, heard half a mile away at times. Those who know the Groundhog of the East would recognize in the Rock Woodchuck its Western cousin, a little bigger, yellower, and brighter in its colours, living in the rocks and blessed with a whistle that would fill a small boy with envy. Now, lest the critical should object to the combination name of Rock Woodchuck, it is well to remind them that Woodchuck has nothing to do with either wood or chucking, but is our corrupted form of an Indian name Ot-choeck, which is sometimes written also We-jack. In the ridge of broken rocks just back of Yancey's is a colony of the Whistlers; and there as I sat sketching one day, with my camera at hand, one poked his head up near me and gave me the pose that is seen in the photograph. You carefully locate the direction of the note and proceed to climb toward it. You may have an hour's hard work before you sight the orange-breasted[Pg 23] Whistler among the tumbled mass of rocks that surround his home, for it is a far-reaching sound, heard half a mile away at times."
encrypted_text4 = encrypt_monoalpha(message4,key())
print("***encrypt1 - 50 words: ", encrypt_monoalpha(message1,key()))
print("___decrypt1:",decrypt_frequencyanalysis(encrypted_text1))
print() 
print("***encrypt2 - 100 words: ", encrypt_monoalpha(message2,key()))
print("___decrypt2:",decrypt_frequencyanalysis(encrypted_text2))
print()
print("***encrypt3 - 500 words: ", encrypt_monoalpha(message3,key()))
print("___decrypt3:",decrypt_frequencyanalysis(encrypted_text3))
print()
print("***encrypt4 - 1000 words: ", encrypt_monoalpha(message4,key()))
print("___decrypt4:",decrypt_frequencyanalysis(encrypted_text4))
print()
   
    