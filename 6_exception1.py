"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


dialogue = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
def ask_user_dict (phrase):
    phrase = input ("Задай вопрос:")
    while True:
        
        try:  
           if phrase == "Как дела":
            print ("Хорошо!")
            
            
        except KeyboardInterrupt:
            
            print ("Пока!")
            break
            
if __name__ == "__main__":
    ask_user_dict ("phrase")
