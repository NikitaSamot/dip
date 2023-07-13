import requests

username = 'kekes'
password = '34901441715dn'
base_url = 'http://127.0.0.1:8000/api/'
# извлечь все курсы
r = requests.get(f'{base_url}courses/')
courses = r.json()

available_courses = ', '.join([course['title'] for course in courses])
print(f'Список доступных курсов: {available_courses}')
for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(f'{base_url}course/{course_id}/enroll/',auth=(username, password))
    if r.status_code == 200:
        print(f'Успешно добавлен курс {course_title}')

# Приведенный выше исходный код выполняет следующие действия.
# 1. Задается пользовательское имя (username) и пароль студента, которого
# нужно зачислить на курсы.

# 2. Полученные из API доступные курсы прокручиваются в цикле.

# 3. В переменной course_id cохраняется атрибут ИД курса, в переменной
# course_title – атрибут title.

# 4. Применяется метод request.post(), чтобы отправить запрос POST на
# URL-адрес http://127.0.0.1:8000/api/courses/[id]/enroll/ по каждому
# курсу. Этот URL-адрес соответствует представлению API CourseEnroll-
# View, которое позволяет зачислять пользователя на курс. Используя
# переменную course_id, формируется URL-адрес каждого курса. Пред-
# ставление CourseEnrollView требует проведения аутентификации. В нем
# используется разрешение IsAuthenticated и аутентификационный класс
# BasicAuthentication. Библиотека requests поддерживает базовую HTTP-
# аутентификацию прямо «из коробки». Параметр auth используется
# для передачи кортежа с пользовательским именем и паролем, чтобы
# аутентифицировать пользователя посредством базовой HTTP-аутен-
# тификации.

# 5. Если статусный код ответа равен 200 OK, то печатается сообщение, ука-
# зывающее на то, что пользователь успешно зачислен на курс.

