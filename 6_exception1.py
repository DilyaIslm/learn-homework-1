"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


d = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
def ask_user_dict (p):
      p = input ("Задай вопрос:")
      while True:
        
       try:  
         if p == "Как дела":
           print ("Хорошо!")

        except KeyboardInterrupt:
           print ("Пока!")
           break
if __name__ == "__main__":
    ask_user("p")
