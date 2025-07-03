from fpdf import FPDF
from fpdf.enums import XPos, YPos

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font('DejaVu', '', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', uni=True)
        self.add_font('DejaVu', 'B', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', uni=True)
        self.add_font('DejaVu', 'I', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf', uni=True)
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.line_height = 6  # стандартная высота строки

    def header_block(self, name, city, email, phone, telegram_url=None):
        self.set_font('DejaVu', 'B', 16)
        self.cell(0, 10, name.upper(), ln=True, align='C')

        self.set_font('DejaVu', '', 11)
        self.set_text_color(0, 0, 0)
        self.cell(0, 8, f"{city} • {email} • {phone}", ln=True, align='C')

        if telegram_url:
            self.set_text_color(0, 0, 255)  # синий
            self.cell(0, 8, "телеграмм", ln=True, align='C', link=telegram_url)
            self.set_text_color(0, 0, 0)  # обратно в чёрный

        self.ln(4)

    def section_title(self, title):
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 8, title.upper(), ln=True)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def paragraph(self, text, align='L'):
        """Улучшенный paragraph с автоматическим переносом длинных строк"""
        self.set_font('DejaVu', '', 11)
        self.multi_cell(0, self.line_height, text, align=align)
        self.ln(2)
    
    def job_entry(self, title, company, location, dates, bullets):
        self.set_font('DejaVu', 'B', 11)
        self.cell(0, self.line_height, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_font('DejaVu', 'I', 11)
        self.cell(0, self.line_height, f"{company} • {location} • {dates}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_font('DejaVu', '', 11)
        for bullet in bullets:
            self.cell(5)  # отступ
            # Улучшенный multi_cell для маркированных списков
            x = self.get_x()
            y = self.get_y()
            self.multi_cell(0, self.line_height, f"- {bullet}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def wrap_text(self, text, max_width):
        """Автоматический перенос текста с учетом максимальной ширины"""
        words = text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            if self.get_string_width(test_line) < max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines

# Инициализация
pdf = PDF()

# 🔹 Хедер
pdf.header_block(
    name="Иван Иванов",
    city="Москва",
    email="example@gmail.com",
    phone="+7 900 999 99 99",
    telegram_url="https://t.me/"
)

# 🔹 Описание профиля
pdf.section_title("Python Backend-разработчик") # текущая позиция
pdf.paragraph(
    "Python-разработчик с более чем 3 годами опыта в backend-разработке. Работал над проектами в сферах "
    "промышленной автоматизации, телекоммуникаций и технического зрения. Разрабатывал распределённые системы, "
    "голосовых ботов и API-интеграции. Опыт внедрения CI/CD, оптимизации кода и проектирования архитектуры микросервисов. "
    "Уверенно работаю с FastAPI, Celery, PostgreSQL, Docker и системой очередей."
) # О себе

# 🔹 Опыт работы
pdf.section_title("Опыт работы")

# Место работы
# если мест много, делаем еще один вызов метода pdf.job_entry(), только ниже
pdf.job_entry(
    "Python Developer", # должность
    "OSTEC Group", # название компании
    "Москва", # город
    "декабрь 2023 – настоящее время", # время работы
    # через запятую перечисляем достижения и роль в компании
    [
        "Разработал систему технического зрения для поиска производственных дефектов в реальном времени (FastAPI + WebSockets, OpenCV, PyTorch).",
        "Разработал менеджера задач (Celery + Redis + RabbitMQ)) для запуска переодических задач, с возможностью менять время запуска задачи.",
        "Спроектировал и реализовал с нуля систему управления шаблонами смен сотрудников: REST API, PostgreSQL, Pydantic, Redis, SqlAlchemy.",
    ]
)



# 🔹 Образование
pdf.section_title("Образование")
pdf.paragraph(
    "Международный институт компьютерных технологий — Воронеж\n"
    "Бакалавр, Электроэнергетика и электротехника — 2023"
)

# 🔹 Навыки
pdf.section_title("Технические навыки")
pdf.paragraph(
    "Языки: Python, SQL, Bash\n"
    "Базы данных: PostgreSQL, MongoDB, Redis, MinIO\n"
    "Фреймворки: FastAPI, Django, Flask\n"
    "Инструменты: Docker, Celery, RabbitMQ, WebSockets, GitLab CI/CD, Pydantic, pytest\n"
    "Библиотеки: Pandas, OpenCV, PyTorch (CUDA), SQLAlchemy\n"
    "Концепции: ООП, REST API, AsyncIO, DRY, микросервисы, TDD"
)

# 🔹 Языки
pdf.section_title("Языки")
pdf.paragraph(
    "Русский — родной\nАнглийский — технический, чтение документации, переписка"
)

# Сохранение
pdf.output("/data/Резюме_2025.pdf")