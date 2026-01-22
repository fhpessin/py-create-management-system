from dataclasses import dataclass
from datetime import datetime
import pickle

@dataclass
class Specialty:
    name: str
    number: int

@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str

@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]

# --- Funções de Persistência ---

def write_groups_information(groups: list[Group]) -> int:
    """Escreve a lista de grupos em groups.pickle e retorna o maior número de alunos."""
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    
    if not groups:
        return 0
    return max(len(group.students) for group in groups)

def write_students_information(students: list[Student]) -> int:
    """Escreve a lista de estudantes em students.pickle e retorna a quantidade total."""
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)

def read_groups_information() -> list[str]:
    """Lê os grupos e retorna os nomes das especialidades sem repetição."""
    try:
        with open("groups.pickle", "rb") as f:
            groups = pickle.load(f)
            # Usamos set para garantir nomes únicos e convertemos de volta para lista
            specialties = {group.specialty.name for group in groups}
            return list(specialties)
    except (FileNotFoundError, EOFError):
        return []

def read_students_information() -> list[Student]:
    """Lê e retorna a lista de instâncias de estudantes do arquivo."""
    try:
        with open("students.pickle", "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return []
