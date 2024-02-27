mhs = ['dede','dudu','didi']
uts = [100,87,77]
uas = [30,97,66]

def calculateTotalGrade(uts,uas):
  grade = 0.4*uts + 0.6*uas
  return grade

def convertGrade(grade):
  if grade >= 80:
    return "A"
  elif grade >= 70:
    return "B"
  elif grade >= 60 :
    return "C"
  elif grade >= 50:
    return "D"
  else:
    return "E"

def graduate(result):
  if(result <="C"):
    return "LULUS"
  else:
    return "Tidak LULUS"
for i in range(0,3):
  grade = calculateTotalGrade(uts[i], uas[i])
  result = convertGrade(grade)
  resultGraduate = graduate(result)
  print(f"{mhs[i]} Mendapatkan UTS {uts[i]} dan UAS {uas[i]} dan nilai akhir {grade} predikat {result} {resultGraduate}")