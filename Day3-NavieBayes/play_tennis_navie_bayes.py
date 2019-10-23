import pandas as pd
dt = pd.read_csv("play_tennis.csv")
dt

# Thong ke tan so suat hien cua cac gia tri

# Outlook, play="yes"
dtOy = dt.Outlook[dt.Play=="Yes"]
P1_1 = dtOy.value_counts()/dtOy.count() # số lần xuất hiện của mỗi giá trị của thuộc tính
# Outlook, play="no"
dtOn = dt.Outlook[dt.Play=="No"]
P1_2 = dtOn.value_counts()/dtOn.count() # số lần xuất hiện của mỗi giá trị của thuộc tính

# Temperature, play="yes"
dtTy = dt.Temp[dt.Play=="Yes"]
P2_1 = dtTy.value_counts()/dtTy.count()
# Temperature, play="no"
dtTn = dt.Temp[dt.Play=="No"]
P2_2 = dtTn.value_counts()/dtTn.count()

# Humidity, play="yes"
dtHy = dt.Humidity[dt.Play=="Yes"]
P3_1 = dtHy.value_counts()/dtHy.count()
# Humidity, play="no"
dtHn = dt.Humidity[dt.Play=="No"]
P3_2 = dtHn.value_counts()/dtHn.count()

# Windy, play="yes"
dtWy = dt.Windy[dt.Play=="Yes"]
P4_1 = dtWy.value_counts()/dtWy.count()
# Windy, play="no"
dtWn = dt.Windy[dt.Play=="No"]
P4_2 = dtWn.value_counts()/dtWn.count()

# Xac suat xuat hien cua play
Play = dt.Play.value_counts()/dt.Play.count()
Play

# Predict for new value
# X  = ("rainy", "cool", "high", "false")
P_yes = P1_1[1]*P2_1[1]*P3_1[1]*P4_1[0]*Play[0]
P_no = P1_2[1]*P2_2[1]*P3_2[1]*P4_2[0]*Play[1]

P_yes
P_no
PY = P_yes/(P_no+P_yes)
PN = P_no/(P_no+P_yes)
PY
PN
