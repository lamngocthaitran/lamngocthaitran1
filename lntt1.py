# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:06:15 2024

@author: lamngocthaitran
"""

print("chương trình tính điểm trung bình của học sinh")
GPA = float(input("Nhập điểm trung bình"))
if GPA < 3.5:
    print("học lực kém")
elif 3.5<=GPA<5.0:
    print("học lực yếu")
elif 5.0 <= GPA < 7.0:
    print("học lực trung bình")
elif 7.0 <= GPA < 8.0 :
    print("học lực khá")
elif 8.0 <= GPA < 9.0 :
    print("học lực giỏi")
elif 9.0 <= GPA <= 10:
    print("học lực xuất sắc")
else:
    print("không xác định")