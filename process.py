from bs4 import BeautifulSoup
import csv
import re

RE_BIRTHDAY = re.compile(r"^[A-Z][a-z]{2} \d{1,2}$")

with open("page.html", "r", encoding="iso-8859-1") as f:
    print("Parsing into BeautifulSoup")
    page = BeautifulSoup(f.read(), "html.parser")
print("Finding .student_container elements")
containers = page.find_all("div", {"class": "student_container"})
students = []
for container in containers:
    info = container.find_all("div", {"class": "student_info"})
    name = container.find("h5", {"class": "yalehead"}).text
    print("Parsing " + name)
    surname, forename = name.split(", ", 1)
    college = info[0].text
    try:
        email = info[1].find("a").text
    except AttributeError:
        email = ""
    trivia = info[1].find_all(text=True, recursive=False)
    try:
        room = trivia.pop(0)
        birthday = trivia.pop()
        major = trivia.pop()
        address = "\n".join(trivia)
    except IndexError:
        room = ""
        birthday = ""
        major = ""
        address = ""
    students.append({
        "forename": forename.strip(),
        "surname": surname.strip(),
        "image_id": container.find("div", {"class": "student_img"}).find("img")["src"][len("/facebook/Photo?id="):],
        "year": int(container.find("div", {"class": "student_year"}).text.replace("'", "20")),
        "pronoun": container.find("div", {"class": "student_info_pronoun"}).text,
        "room": room,
        "birthday": birthday,
        "major": major,
        "address": address,
    })

with open("students.csv", "w", encoding="utf-8") as f:
    keys = students[0].keys()
    writer = csv.DictWriter(f, keys)
    writer.writeheader()
    writer.writerows(students)
