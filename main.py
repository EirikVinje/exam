from tkinter import *
import requests

from flask import jsonify


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.grid()

        self.v = IntVar()
        v = self.v
        v.set(0)
        self.get_menu_list = []
        self.menu_list = []
        self.after_menu_list = []
        self.value = int(0)
        self.btn_get = Radiobutton(self, text='Get', variable=v, value=1, state=NORMAL)
        self.btn_add = Radiobutton(self, text='Add', variable=v, value=2, state=NORMAL)
        self.btn_edit = Radiobutton(self, text='Edit', variable=v, value=3, state=NORMAL)
        self.btn_delete = Radiobutton(self, text='Delete', variable=v, value=4, state=NORMAL)
        self.btn_customer = Radiobutton(self, text='Customer', variable=v, value=5, state=NORMAL)
        self.btn_car = Radiobutton(self, text='Car', variable=v, value=6, state=NORMAL)
        self.btn_tenancy = Radiobutton(self, text='Tenancy', variable=v, value=7, state=NORMAL)
        self.btn_execute_menu = Button(self, text='Execute', command=self.handle_menu)
        self.btn_back = Button(self, text='Back', command=self.back_id)
        self.btn_back_2 = Button(self, text='Back', command=self.back_after_menu)
        self.btn_get_id = Button(self, text='Execute', command=self.get_id_customer)
        self.btn_execute_to_after_menu = Button(self, text='Execute', command=self.handle_after_menu)
        self.entry_id = Entry(self)
        self.label_id = Label(self, text=f'id')
        self.label_id.pack_forget()

        self.text_entry = Text(self)
        self.text_entry.insert(INSERT, "Hello.....")
        self.text_entry.insert(END, "Bye Bye.....")
        self.btn_execute_add_customer = Button(self, text='Execute', command=self.handle_add_customer)

        self.entry_id_customer = Entry(self)
        self.entry_lastname = Entry(self)
        self.entry_firstname = Entry(self)
        self.entry_phonenumber = Entry(self)
        self.label_lastname = Label(self, text='Lastname')
        self.label_firstname = Label(self, text='Firstname')
        self.label_phonenumber = Label(self, text='Phonenumber')

        self.menu()

    def menu(self):
        self.btn_get.pack(side='left')
        self.btn_add.pack(side='left')
        self.btn_edit.pack(side='left')
        self.btn_delete.pack(side='left')
        self.btn_execute_menu.pack(side='left')
        self.menu_list.append(self.btn_get)
        self.menu_list.append(self.btn_add)
        self.menu_list.append(self.btn_edit)
        self.menu_list.append(self.btn_delete)
        self.menu_list.append(self.btn_execute_menu)

    def after_menu(self):
        self.btn_car.pack(side='left')
        self.btn_customer.pack(side='left')
        self.btn_tenancy.pack(side='left')
        self.btn_execute_to_after_menu.pack(side='left')
        self.btn_back_2.pack(side='left')
        self.after_menu_list.append(self.btn_car)
        self.after_menu_list.append(self.btn_customer)
        self.after_menu_list.append(self.btn_tenancy)
        self.after_menu_list.append(self.btn_execute_to_after_menu)
        self.after_menu_list.append(self.btn_back_2)

    def get_frame(self):
        self.label_id.pack(side='left')
        self.entry_id.pack(side='left')
        self.btn_get_id.pack(side='left')
        self.btn_back.pack(side='left')
        self.get_menu_list.append(self.label_id)
        self.get_menu_list.append(self.entry_id)
        self.get_menu_list.append(self.btn_get_id)
        self.get_menu_list.append(self.btn_back)

    def add_customer_frame(self):
        self.entry_id_customer.grid(row=1, column=4)
        self.label_id.grid(row=1, column=5)
        self.entry_lastname.grid(row=2, column=4)
        self.label_lastname.grid(row=2, column=5)
        self.entry_firstname.grid(row=3, column=4)
        self.label_firstname.grid(row=3, column=5)
        self.entry_phonenumber.grid(row=4, column=4)
        self.label_phonenumber.grid(row=4, column=5)
        self.btn_execute_add_customer.grid(row=1, column=6)

    def handle_menu(self):
        if self.v.get() == 2:
            print("add")
            for item in self.menu_list:
                item.pack_forget()
            self.after_menu()
            self.value = 2

        elif self.v.get() == 3:
            print("edit")
            for item in self.menu_list:
                item.pack_forget()
            self.after_menu()
            self.value = 3

        elif self.v.get() == 4:
            print("delete")
            for item in self.menu_list:
                item.pack_forget()
            self.after_menu()
            self.value = 4

        elif self.v.get() == 1:
            print("Get")
            for item in self.menu_list:
                item.pack_forget()
            self.after_menu()
            self.value = 1

    def handle_after_menu(self):
        if self.v.get() == 5:
            print('Customer')
            for item in self.after_menu_list:
                item.pack_forget()
            if self.value == 1:
                self.get_frame()
            elif self.value == 2:
                self.add_customer_frame()

        elif self.v.get() == 6:
            print('Car')
            for item in self.after_menu_list:
                item.pack_forget()

        elif self.v.get() == 7:
            print('Tenancy')
            for item in self.after_menu_list:
                item.pack_forget()

    def get_id_customer(self):
        customer_id = int(self.entry_id.get())
        customer_id_request = requests.get(f'http://127.0.0.1:5000/customers/{customer_id}')
        print(f'Status code {customer_id_request.status_code}')
        if not customer_id_request.status_code == 200:
            self.entry_id.delete(0, END)
            print("No customer found")
            return

        customer = customer_id_request.json()
        print(customer["last_name"])
        self.entry_id.delete(0, END)

    def back_id(self):
        for item in self.get_menu_list:
            item.pack_forget()
        self.after_menu()

    def back_after_menu(self):
        for item in self.after_menu_list:
            item.pack_forget()
        self.menu()

    def handle_add_customer(self):
        id = int(self.entry_id_customer.get())
        lastname = self.entry_lastname.get()
        firstname = self.entry_firstname.get()
        phonenumber = int(self.entry_phonenumber.get())
        comment = dict(id=id, first_name=firstname, last_name=lastname, phone_number=phonenumber)
        new_customer = requests.post(f'http://127.0.0.1:5000/customers/', json=comment)
        print(comment)


# 1. get
# 2. add
# 3. edit
# 4. remove
# 5. customer
# 6. car
# 7. tenancy


def main():

    root = Tk()
    root.geometry('400x200')
    app = Application(master=root)
    app.mainloop()


main()





