from model import CRMSystem
from view import CRMView

class CRMController:
    def __init__(self):
        self.model = CRMSystem()
        self.view = CRMView(self)

    def add_user(self, name, email, phone):
        self.model.add_user(name, email, phone)

    def delete_user(self, name):
        self.model.delete_user(name)

    def find_user(self, name):
        return self.model.find_user(name)

    def update_user(self, name, new_email, new_phone):
        self.model.update_user(name, new_email, new_phone)

    def run(self):
        self.view.run()

if __name__ == '__main__':
    controller = CRMController()
    controller.run()
