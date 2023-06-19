import random
import datetime
import os


puan = 0
deneme = 10
tarih = datetime.datetime.now()
tarih_format = tarih.strftime('%Y-%m-%d %H:%M')


# game starts and takes name of to user
name = input("What is your name: ")
print(
    f"******Hey {name} , Welcome to Word guessing game by Nasibullah Qarizada******")


while True:

    # list of words selected from the datasets and in case increasing the score it would change the word length.
    if puan < 20:
        cwd = os.getcwd()
        file_path = os.path.join(cwd, '3_letter_words.csv')
        with open(file_path, "r") as file:
            allText = file.read()
            kelimeler = list(map(str, allText.split()))
            secilmis = random.choice(kelimeler)

    elif puan < 40:
        cwd = os.getcwd()
        file_path = os.path.join(cwd, '4_letter_words.csv')
        with open(file_path, "r") as file:
            allText = file.read()
            kelimeler = list(map(str, allText.split()))
            secilmis = random.choice(kelimeler)

    elif puan < 60:
        cwd = os.getcwd()
        file_path = os.path.join(cwd, '5_letter_words.csv')
        with open(file_path, "r") as file:
            allText = file.read()
            kelimeler = list(map(str, allText.split()))
            secilmis = random.choice(kelimeler)
    else:
        cwd = os.getcwd()
        file_path = os.path.join(cwd, '6_letter_words.csv')
        with open(file_path, "r") as file:
            allText = file.read()
            kelimeler = list(map(str, allText.split()))
            secilmis = random.choice(kelimeler)

    print(f"OK, You have 10 attempts to guess the word correctly.")
    print(f"The word has {len(secilmis)} letters. ")
    print('The first letter is:' + secilmis[0])


# create a list equal to number of letters in selected word

    tahmin_edilen_kelime = ["_" for i in range(len(secilmis))]
    print(*tahmin_edilen_kelime)

    while(deneme, puan):
        deneme = deneme-1

    # take the letter from the user
        tahmin_edilen_harf = input("\nGuessed letter: ")

        if tahmin_edilen_harf == 'quit':
            print(f'I will miss you {name}')
            file = open('score chart.txt', 'a')
            file.write(
                f"Name: {name},  puan: {str(puan)}, Date: {tarih_format}\n")
            input("Good bye honey")
            exit()


        if tahmin_edilen_harf == 'hint':
            if puan > 5:
                print('**hint**:' + secilmis)
                puan -= 5
            else:
                print(f'I am sorry, not enough score {name}')

    # check if it is an alphabet
        if not tahmin_edilen_harf.isalpha():
            print(f'Dear {name}, it must be only from letters!')

    # check if guessed letter length is one or not
        elif(len(tahmin_edilen_harf) > 1):
            print(
                f'{name} You are not going to write a paragraph :), just one letter would be enough for me...')

    # check if tahmin_edilen_harf is matches with secilmis

        if tahmin_edilen_harf in secilmis:
            tahmin_edilen_kelime = [
                tahmin_edilen_harf
                if secilmis[i] == tahmin_edilen_harf
                else tahmin_edilen_kelime[i]
                for i in range(len(secilmis))]
            print('keep it up honey')
            puan += 1
            deneme += 1

        else:
            print("meh, you are wrong :(")



        girilen = "".join(tahmin_edilen_kelime)
        if secilmis == girilen:
            print(f'YAAY!!, {name} You Get the letter...')
            print(f'score: {puan}')
            deneme = 10
            break

    # print the guessed word
        print(*([i for i in tahmin_edilen_kelime]))

    # show attempts left
        print(f"You have {deneme} attempts left")


    # if attempts reach to 0 it will print the orginal word and assign the name. the score and the date 
    # to a txt file called score chart
        if deneme == 0:
            if secilmis != tahmin_edilen_kelime:
                print(
                    f"Honey, You lost the game ,The original Word was {secilmis}, Kachoow!")
                file = open('score chart.txt', 'a')
                file.write(
                    f"Name: {name},  puan: {str(puan)}, Date: {tarih_format}\n")
                input("Good bye honey")
                exit()
                
