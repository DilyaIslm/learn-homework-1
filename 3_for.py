"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school = [
{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '4b', 'scores': [3,4,5,4]},
{'school_class': '4c', 'scores': [3,4,4,4]}]

klass = {'school_class': '4a', 'scores': [3,4,4,5,2]}

def main(school):
    # d = klass["scores"]
    # print(d)
    # scores_sum = sum(d)
    # scores_amount = len(d)
    # scores_avg = scores_sum /scores_amount
    # print(f"Средний балл по классу {scores_avg}")
    
    school_avg = 0
    for klass in school:
        d = klass["scores"]
        print(d)
        scores_sum = sum(d)
        scores_amount = len(d)
        scores_avg = scores_sum /scores_amount
        print(f"Средний балл по классу {scores_avg}")
        school_avg += scores_avg
        print(school_avg)

    print(school_avg/len(school))   
    

    
    
    
if __name__ == "__main__":
    
    main(school)
