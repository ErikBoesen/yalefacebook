
with open("page.html", "r", encoding="iso-8859-1") as f:
    print("Parsing into BeautifulSoup")
    page = BeautifulSoup(f.read(), "html.parser")
print("Finding .student_container elements")
containers = page.find_all("div", {"class": "student_container"})
students = []
for container in containers:
    info = container.find_all("div", {"class": "student_info"})
    name = container.find("h5", {"class": "yalehead"}).text,
    surname, forename = name.split(", ", 1)
    college = info[0].text
    email = info[1].find("a").text
    trivia = info[1].find_all(text=True, recursive=False)
    room = trivia.pop(0)
    birthday = trivia.pop()
    major = trivia.pop()
    address = "\n".join(trivia)
    students.append({
        "forename": forename,
        "surname": surname,
        "image_id": container.find("div", {"class": "student_img"}).find("img")["src"][len("/facebook/Photo?id="):],
        "year": int(container.find("div", {"class": "student_year"}).text.replace("'", "20")),
        "pronoun": container.find("div", {"class": "student_info_pronoun"}).text,
        "room": room,
        "birthday": birthday,
        "major": major,
        "address": address,
    })
    print(students)
    break

with open("students.csv", "w") as f:
    writer = csv.writer(f)
