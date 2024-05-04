class Individual:
    def __init__(self, name):
        self.name = name
        self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = birthday

    def get_age(self):
        pass

    def __str__(self):
        return self.name

class AU_employee(Individual):
    def __init__(self, name):
        super().__init__(name)

    def get_unique_id(self):
      
        pass

class Faculty(Individual):
    def __init__(self, name):
        super().__init__(name)

class EN_Faculty(Faculty):
    def __init__(self, name, classroom_year):
        super().__init__(name)
        self.classroom_year = classroom_year

    def assign_classroom(self, classroom_year):
        self.classroom_year = classroom_year

class Design_Faculty(Faculty):
    def __init__(self, name, classroom_year):
        super().__init__(name)
        self.classroom_year = classroom_year

    def assign_classroom(self, classroom_year):
        self.classroom_year = classroom_year


faculty1 = EN_Faculty("Rushikesh Pawar", "2023")
faculty2 = EN_Faculty("Varshali Jaiswal", "2023")
faculty3 = Design_Faculty("Sanjay Sonani", "2023")
faculty4 = EN_Faculty("Rahul Thakur", "2023")


class Roaster_Au:
    def __init__(self):
        self._faculty = []
        self.c = {}

    def __len__(self):
        return len(self._faculty)

    def add_faculty(self, faculty):
        if faculty not in self._faculty:
            self._faculty.append(faculty)
            self.c[faculty] = []

    def add_course(self, course, factl):
        if factl not in self.c:
            raise ValueError("Faculty not found")
        self.c[factl].append(course)

    def get_courses(self, fact):
        if fact not in self.c:
            raise ValueError("Faculty not found")
        return self.c[fact]

    def get_sorted_faculties(self):
        return sorted(self._faculty, key=lambda x: x.name)

roster = Roaster_Au()

roster.add_faculty(faculty1)
roster.add_faculty(faculty2)
roster.add_faculty(faculty3)
roster.add_faculty(faculty4)

roster.add_course("ITC", faculty1)
roster.add_course("FOP", faculty2)
roster.add_course("ITD", faculty3)
roster.add_course("POI", faculty4)

output = {faculty.name: course[0] for faculty, course in roster.c.items()}


print(output)
