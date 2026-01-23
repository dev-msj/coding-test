import pytest


class Student:
    def __init__(self, student_str: str):
        students = student_str.split()
        self.name = students[0]
        self.result = int(students[1])

def solution(student_str_list: str) -> list[str]:
    student_list = list(map(Student, student_str_list.split('\n')))
    
    student_list.sort(key=lambda x: x.result)
    
    return ' '.join([x.name for x in student_list])

@pytest.mark.parametrize('student_str_list, expected', [
    # 성적이 오름차순 입력
    ('kim 10\nlee 20\npark 30', 'kim lee park'),
    # 성적이 모두 같음
    ('a 50\nb 50\nc 50', 'a b c'),
    # 한 명만 입력
    ('solo 1', 'solo'),
    # 성적이 내림차순 입력
    ('z 100\ny 90\nx 80', 'x y z'),
])
def test_solution(student_str_list: str, expected: str):
    assert solution(student_str_list) == expected