import pandas as pd
student_marks = pd.Series({'vijaya':80,'Rahul':92,'meghna':67,'Radhika':95,'shaurya':97})
student_age=pd.Series({'Vijaya':32,'Rahul':28,'meghna':30,'Radhika':25,'Shaurya':20})
student_df = pd.DataFrame({'Marks':student_marks,'Age':student_age})
print(student_df)
print(student_df.sort_values(by=['Marks']))
print(student_df.sort_values(by=['Marks'],ascending=False))