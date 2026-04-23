import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

# correct file path (with space handled properly)
file_path = "/Users/amrittr/Desktop/python INT375/AI_Impact_Student_Life_2026.csv"

# check file
if not os.path.exists(file_path):
    print("File not found ")
    print("Check path:", file_path)
    exit()

print("File found 👍\n")

# load csv
df = pd.read_csv(file_path)

# clean data
df.columns = df.columns.str.strip().str.replace(" ", "_")
df.drop_duplicates(inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

print("Data ready ✔\n")

# columns
ai_tool = "Primary_AI_Tool"
daily_usage = "Task_Frequency_Daily"   
time_saved = "Time_Saved_Hours_Weekly" 
before = "GPA_Baseline"                
after = "GPA_Post_AI"                  

# -------- 1. BAR GRAPH --------
plt.figure()
sns.countplot(x=ai_tool, data=df)
plt.title("AI Tools Usage")
plt.xticks(rotation=25)
plt.show()

# -------- 2. PIE CHART --------
plt.figure()
df[ai_tool].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title("AI Tool Share")
plt.ylabel("")
plt.show()

# -------- 3. HISTOGRAM --------
plt.figure()
plt.hist(df[daily_usage], bins=10)
plt.title("Daily Usage Frequency")
plt.show()

# -------- 4. BOX PLOT --------
plt.figure()
sns.boxplot(x=df[time_saved])
plt.title("Weekly Time Saved")
plt.show()

# -------- 5. SCATTER --------
plt.figure()
plt.scatter(df[before], df[after])
plt.xlabel("Before AI")
plt.ylabel("After AI")
plt.title("GPA Improvement")
plt.show()

# -------- 6. HEATMAP --------
plt.figure()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
