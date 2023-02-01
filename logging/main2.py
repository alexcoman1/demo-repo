import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

fomatter = logging.Formatter(format="%(levelname)s:%(message)s")

file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logging.basicConfig(filename= "test.log", level= logging.INFO, format="%(levelname)s:%(message)s")


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info("Created employee: {} - {}".format(self.fullname, self.email))

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    

emp_1 = Employee("John", "Smith")
emp_2 = Employee("Corey", "Schafer")
emp_3 = Employee("Jane", "Doe")