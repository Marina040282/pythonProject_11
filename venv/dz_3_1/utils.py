import json

def load_candidates():
    """Функция загружаетданные из файла candidates.json"""
    with open('candidates.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all():
    """ Функция показывает всех кандидатов из файла candidates.json"""
    return load_candidates()


def get_by_pk(pk):
    """ Функция взвращает кандидата по pk"""
    for candidate in load_candidates():
        if candidate['pk'] == pk:
            return candidate
    return


def get_by_skill(skill):
    """ Функция взвращает кандидатаов по навыку"""
    candidates_skills =[]
    for candidate in load_candidates():
        if skill in candidate['skills']:
            candidates_skills.append(candidate)
    return candidates_skills

