# Word-Guessing

1.	Introduction
Word guessing game is a project developed to entertain players with making them to guess the randomly selected word by the program over 4 different datasets accordingly to the score of the players. The project is created to provide a human-nearly performance while playing the game. In other words the program is outputting a text or a functionality after each input the player enters. The moment player enters the game, it will request the player’s name. furthermore, it will continue it with welcoming the player and sharing information regarding to game including attempts left, length of the chosen word, and the first letter of the word as hint. While guessing the letters the users have 10 attempts to guess. In case of  validity, it will jump to the next word by adding the scores and not decreasing from the attempts, but if the guesses are incorrect the program will be terminated. A new level would be unlocked in each 20 points added on scores. The higher the level reaches, the game would get harder. Such as, the game chooses words with more letters from the uploaded datasets. If the user is in the middle of the game and want to forfeit or close the game and want to save the score, they can basically enter “quit” or if they need for some hint they can enter the word “hint” which makes score -5 and visualize the word. The program will give a warning in case to use numbers, symbols, and several letters in a row. Name, Score and Date played of the player will be out written in a .txt file.



2.	Project Background
The process of developing this project started on the very beginning of the semester, therefore it might contains some bugs or may cause to face some errors while using the it. Thanks to dear prof. doc. Yusuf Altunel for their contributions. Alongside, it is good to mention that some parts of the program are inspired from some source on stack overflow and medium websites which has been referenced at the end of the document and mentioned in part 5 while explaining the code parts.

3.	Libraries
•	Random: This library is used to choose randomly between words presented to the program.
•	Datetime: This library is used to write the time when game is ended at .txt score file.
