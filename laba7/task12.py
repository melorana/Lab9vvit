class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return f"Имя: {self.name}, идентификационный номер: {self.id}"
class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department
    def get_info(self):
        return f"Имя: {self.name}, идентификационный номер: {self.id}, отдел: {self.department}"
    def manage_project(self):
        return f"{self.name} управляет проектами в отделе {self.department}."
class Technician(Employee):
    def __init__(self, name, id, specialisation):
        Employee.__init__(self, name, id)
        self.specialisation = specialisation
    def get_info(self):
        return f"Имя: {self.name}, идентификационный номер: {self.id}, специализация: {self.specialisation}."
    def perform_maintenance(self):
        return f"{self.name} выполняет техническое обслуживание по специализации {self.specialisation}."
class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialisation):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialisation)
        self.team = []
    def get_info(self):
        return f"Имя: {self.name}, ID: {self.id}, Отдел: {self.department}, Специализация: {self.specialisation}"
    def add_employee(self, employee):
        self.team.append(employee)
        print(f"Сотрудник {employee.name} добавлен в список подчинённых")
    def get_team_info(self):
        if not self.team:
            return "Команда пуста"
        return "\n".join(emp.get_info() for emp in self.team)

emp1 = Employee("Максим Шейдов", "Z-283")
print("1. Обычный сотрудник:")
print(emp1.get_info())

mgr1 = Manager("Клара Дерн", "Z-90", "Back-end")
print("2. Менеджер:")
print(mgr1.get_info())
print(mgr1.manage_project())

tech1 = Technician("Давид Соколов", "Z-V06", "Сетевые технологии")
print("3. Техник:")
print(tech1.get_info())
print(tech1.perform_maintenance())

tm1 = TechManager("Элианора Златова", "Z-317", "ИТ-инфраструктура", "Серверные системы")
print("4. Технический менеджер: ")
print(tm1.get_info())
print(tm1.manage_project())
print(tm1.perform_maintenance())

print("5. Добавление подчинённых")
tm1.add_employee(emp1)
tm1.add_employee(mgr1)
tm1.add_employee(tech1)

print("6. Информация о команде")
print(tm1.get_team_info())