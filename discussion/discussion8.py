
# 1.1 they implement the iterator interface
# 2. since the integer type does not implement the iterator
#
# 3.
# for i in data.next():
#      if i.current() == None:
#          break
#      print(i.current())
#
# 4. implementing the "next" method
#
# 
#
#
#
#
#
#

# 2.1  type dispatching:

class KM_record(object):
    """A student record formatted via Keegan’s standard"""
    def __init__(self, name, grade):
        """name is a string containing the student’s name,
        and grade is a grade object"""
        self.student_info = [name, grade]

class JO_record(object):
    """A student record formatted via Julia’s standard"""
    def __init__(self, name, grade):
        """name is a string containing the student’s name,
        and grade is a grade object"""
        self.student_info = {'name': name, 'grade': grade}
# 
# my stuff:
#
type_tag_tags = {KM_record: 'KM', JO_record: 'JO'}

def type_tag(x):
    return type_tag_tags[type(x)]

# type_tag.implementations = {}
# type_tag.implementations[ ('KM', 'name') ] = lambda record: record[0] 
# type_tag.implementations[ ('KM', 'grade') ] = lambda record: record[1] 
# type_tag.implementations[ ('JO', 'name') ] = lambda record: record['name']
# type_tag.implementations[ ('JO', 'grade') ] = lambda record: record['grade']
# 
# def get_name(record):
#     type_tag = type_tag.tags[ type(record) ]
#     return type_tag.implementations[ (type_tag, 'name') ](record)
# 
# 
# def get_grade(record):
#     type_tag = type_tag.tags[ type(record) ]
#     return type_tag.implementations[ (type_tag, 'grade') ](record)
# 

# solution:
def get_name(record):
    data_type = type_tag(record)
    return get_name.implementations[data_type](record)
def get_grade(record):
    data_type = type_tag(record)
    return get_grade.implementations[data_type](record)

get_name.implementations = {}
get_name.implementations['KM'] = lambda x: x.student_info[0]
get_name.implementations['JO'] = lambda x: x.student_info['name']
get_grade.implementations = { }
get_grade.implementations['KM'] = lambda x: x.student_info[1]
get_grade.implementations['JO'] = lambda x: x.student_info['grade']


class KM_grade(object):
    def __init__(self, total_points):
        if total_points > 90:
            letter_grade = 'A'
        else:
            letter_grade = 'F'
        self.grade_info = (total_points, letter_grade)

class JO_grade(object):
    def __init__(self, total_points):
        self.grade_info = total_points

def get_points( grade ):
    dispatch = { KM_grade : lambda x : x.grade_info[0],
                 JO_grade : lambda x : x.grade_info }

    return dispatch[type(grade)]

def compute_average_total(lst):
    """
    >>> l = [ KM_grade(91), KM_grade(80), JO_grade(50) ]
    >>> compute_average_total(l)
    221
    """

    sum = 0
    for grade in lst:
        sum += get_points(grade)(grade)
    
    return sum

class JD_grade(object):
    """A student record formatted via John’s standard"""
    def __init__(self, name_str, grade_num):
        """NOTE: name_str must be a string, grade_num must be a number"""
        self.name_str = name_str
        self.grade_num = grade_num

    def __repr__(self):
        return "Name: " + self.name_str + ", Grade: " + str(self.grade_num)

    
def convert_to_JD(records):
    """
    >>> l = [ KM_record('peter', 12), KM_record('klaus', 34), JO_record('hans', 4)]
    >>> convert_to_JD( l )
    [Name: peter, Grade: 12, Name: klaus, Grade: 34, Name: hans, Grade: 4]
    """

    result = []
    for rec in records:
        result.append( JD_grade( get_name(rec), get_grade(rec))  )

    return result
