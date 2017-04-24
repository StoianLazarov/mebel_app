text = '''
ENTET YOUR DATA
=============================
vid na shkafovete:
    1.dolni
    2.gorni
width (.mm)=
height (.mm) =
depth (.mm) =
kant (0, 0,8, 2 .mm)=
d_rab_plot (.mm) =
d_ploskost (.mm) =
'''


with open("input_data.txt", "a+") as f:
    f.write(text)
