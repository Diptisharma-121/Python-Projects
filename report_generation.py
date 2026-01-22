import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch


data = pd.read_csv("data.csv")


total_students = len(data)
average_marks = data["Marks"].mean()
highest_marks = data["Marks"].max()
lowest_marks = data["Marks"].min()


plt.figure()
plt.bar(data["Name"], data["Marks"])
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Report")
plt.savefig("marks_chart.png")
plt.close()


pdf = SimpleDocTemplate("Automated_Report.pdf", pagesize=A4)
styles = getSampleStyleSheet()
content = []


content.append(Paragraph("<b>Automated Student Report</b>", styles["Title"]))
content.append(Spacer(1, 0.3 * inch))


summary = f"""
Total Students: {total_students}<br/>
Average Marks: {average_marks:.2f}<br/>
Highest Marks: {highest_marks}<br/>
Lowest Marks: {lowest_marks}
"""
content.append(Paragraph(summary, styles["Normal"]))
content.append(Spacer(1, 0.3 * inch))


content.append(Paragraph("<b>Student Marks Details:</b>", styles["Heading2"]))
for i, row in data.iterrows():
    content.append(Paragraph(f"{row['Name']} : {row['Marks']}", styles["Normal"]))

content.append(Spacer(1, 0.3 * inch))


content.append(Paragraph("<b>Graphical Representation:</b>", styles["Heading2"]))
content.append(Spacer(1, 0.2 * inch))
content.append(Paragraph('<img src="marks_chart.png" width="400" height="250"/>', styles["Normal"]))


pdf.build(content)

print("Automated PDF Report Generated Successfully")
