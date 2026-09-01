import pandas as pd 
import matplotlib.pyplot as plt 

#CHART 1 Viewing WAYMO VS Humans 

waymo = pd.read_csv("data/waymo_benchmarks.csv")
severity = "Any Injury Reported"
df = waymo[(waymo["severity"]== severity) & (waymo["city"] != "All locations ")]

x = range(len(df))
width = 0.35

fig, ax = plt.subplots(figsize=(9,5))
ax.bar([i - width/2 for i in x], df["waymo_rate"],width, label ="Waymo")
ax.bar([i+width/2 for i in x], df["human_rate"], width, label="Human drivers")

ax.set_xticks(list(x))
ax.set_xticklabels(df["city"], rotation = 20, ha ="right")
ax.set_ylabel("Crashes per million miles")
ax.set_title(f"{severity} crash rate: Waymo vs. human benchmark")

ax.legend()
plt.tight_layout
plt.savefig("charts/01_waymo_vs_human.png", dpi= 150)

print("saved chart 1")

#CHART 2 How Severe re AV (Autonomous Vehicle) Crashes 
sgo = pd.read_csv("data/SGO-2021-01_Incident_Reports_ADS.CSV", low_memory =False)
#sorting by report version so the newest verison of each report is last then only keep the last one 
sgo = sgo.sort_values("Report Version")

#Rows with the same ID cant be matched to anything and need to be split off 
has_id =sgo["Same Incident ID"].notna()
sgo= pd.concat([
    sgo[has_id].drop_duplicates(subset="Same Incident ID", keep = "last"),
    sgo[~has_id]
])

print(f"after dedupe: {len(sgo)} Incidents")

#count numb crashes fall into each severity categories 

sev= sgo["Highest Injury Severity Alleged"].value_counts()

fig, ax = plt.subplots(figsize=(9,5))
ax.barh(sev.index, sev.values)

ax.set_xlabel("Number of reported Crashes")
ax.set_title("Severity of reported driverless vehicle crashes\n(NHTSA SGO, June 2025 - July 2026) ")

ax.invert_yaxis()

plt.tight_layout()
plt.savefig("charts/02_severity.png",dpi = 150)
print("saved chart 2")

#CHART 3 Reported Assults in rideshares 

uber = pd.read_csv("data/uber_safety.csv")

fig, ax = plt.subplots(figsize =(8,5))
bars = ax.bar(uber["period"], uber["disclosed_incidents"], color ="#993556")

for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 80,
            f"{int(bar.get_height()):,}", ha="center")

ax.set_ylabel("Reported incidents")
ax.set_title("Sexual assault reports disclosed in Uber's US Safety Reports")

plt.tight_layout()
plt.savefig("charts/03_uber_assaults.png", dpi=150)
print("saved chart 3")