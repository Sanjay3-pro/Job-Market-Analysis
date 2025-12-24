import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/jobs.csv")

df["skills"] = df["skills"].str.split(";")
skills_df = df.explode("skills")

skill_count = skills_df["skills"].value_counts()
print(skill_count)

skill_count.plot(kind="bar", title="Skill Demand from Job Postings")
plt.xlabel("Skills")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("skill_demand.png")
plt.show()
