"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school = [
{'school_class1': '4a', 'scores1': [3,4,4,5,2]},
{'school_class2': '4b', 'scores2': [3,4,5,4]},
{'school_class3': '4c', 'scores3': [3,4,4,4]},
{'school_class4': '5a', 'scores4': [3,4,5,4]},
{'school_class5': '5b', 'scores5': [3,3,5,4]},
{'school_class6': '5c', 'scores6': [3,4,4,4]}]
def main(school_class1, scores1, school_class2, scores2, school_class3, scores3,school_class4, scores4,school_class5, scores5,school_class6, scores6):
    print (f"Средний балл по школе: {sum(scores1, scores2, scores3, scores4, scores5, scores6)/len(school_class1, school_class1
    school_class2,school_class3,school_class4,school_class5,school_class6)}")
    
    scores_sum = 0
for score in school:
		scores_sum += scores
		print(scores_sum)

    scores_avg = scores_sum / len(students_scores)
    print(f"Средний балл {scores_avg}")

for school_class in school:
    scores_sum += school_class
    scores_school_avg = sum(scores)/len
    ptint(f"Средний балл по классу {scores_school_avg}")
    
    
if __name__ == "__main__":
    
    main(school_class1, scores1, school_class2, scores2, school_class3, scores3,school_class4, scores4,school_class5, scores5,school_class6, scores6)
