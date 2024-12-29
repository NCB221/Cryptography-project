import os
import Caesar_Cipher
import Hill_Cipher
import DES_Method
import AES_Method

class Menu:
    def __init__(self, name="Default name", description="Default description", action=-1):
        self.name = name
        self.description = description
        self.action = action
        self.sub_menus = []

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_action(self):
        return self.action

    def set_action(self, action):
        self.action = action

    def add_sub_menu(self, menu):
        self.sub_menus.append(menu)
        menu.sub_menus.append(self)

    def get_sub_menu(self, index):
        if 0 <= index < len(self.sub_menus):
            return self.sub_menus[index]
        return None

    def display_menu(self):
        os.system('cls')
        print(f"===== {self.name} =====")
        print(self.description)
        for i, sub_menu in enumerate(self.sub_menus):
            print(f"{i +1}. {sub_menu.get_name()}")

    def pick_option(self):
        while True:
            try:
                option = int(input("Pick an option: "))
                if 1 <= option <= len(self.sub_menus):
                    return option
                else:
                    raise ValueError("Out of range")
            except ValueError as e:
                print(f"Error: {e}")

class Main:
    ENCRYPT_CAESAR_CIPHER = 0
    DECRYPT_CAESAR_CIPHER = 1
    ENCRYPT_HILL_CIPHER = 2
    DECRYPT_HILL_CIPHER = 3
    ENCRYPT_DES = 4
    DECRYPT_DES = 5
    ENCRYPT_AES = 6
    DECRYPT_AES = 7
    EXIT_PROGRAM = 8

    def __init__(self):
        self.current_menu = self.create_main_menu()

    def create_main_menu(self):
        main_menu = Menu("Main menu", "Project main menu")
        encrypt_menu = Menu("Encrypt", "Encryption method")
        decrypt_menu = Menu("Decrypt", "Decryption method")
        exit_menu = Menu("Exit", "Program end", Main.EXIT_PROGRAM)

        main_menu.add_sub_menu(encrypt_menu)
        main_menu.add_sub_menu(decrypt_menu)
        main_menu.add_sub_menu(exit_menu)

        encrypt_menu.add_sub_menu(Menu("Caesar cipher", "Go back to encryption menu", Main.ENCRYPT_CAESAR_CIPHER))
        encrypt_menu.add_sub_menu(Menu("Hill cipher", "Go back to encryption menu", Main.ENCRYPT_HILL_CIPHER))
        encrypt_menu.add_sub_menu(Menu("DES", "Go back to encryption menu", Main.ENCRYPT_DES))
        encrypt_menu.add_sub_menu(Menu("AES", "Go back to encryption menu", Main.ENCRYPT_AES))

        decrypt_menu.add_sub_menu(Menu("Caesar cipher", "Go back to decryption menu", Main.DECRYPT_CAESAR_CIPHER))
        decrypt_menu.add_sub_menu(Menu("Hill cipher", "Go back to decryption menu", Main.DECRYPT_HILL_CIPHER))
        decrypt_menu.add_sub_menu(Menu("DES", "Go back to decryption menu", Main.DECRYPT_DES))
        decrypt_menu.add_sub_menu(Menu("AES", "Go back to decryption menu", Main.DECRYPT_AES))
        return main_menu

    def run(self):
        while True:
            self.current_menu.display_menu()
            option = self.current_menu.pick_option()
            selected_menu = self.current_menu.get_sub_menu(option - 1)
            if selected_menu:
                action = selected_menu.get_action()

                if action == -1:
                    self.current_menu = selected_menu
                elif action == Main.ENCRYPT_CAESAR_CIPHER:
                    Caesar_Cipher.encrypt_caesar_cipher()
                elif action == Main.DECRYPT_CAESAR_CIPHER:
                    Caesar_Cipher.decrypt_caesar_cipher()
                elif action == Main.ENCRYPT_HILL_CIPHER:
                    Hill_Cipher.encrypt_hill_cipher()
                elif action == Main.DECRYPT_HILL_CIPHER:
                    Hill_Cipher.decrypt_hill_cipher()
                elif action == Main.ENCRYPT_DES:
                    DES_Method.encrypt_des()
                elif action == Main.DECRYPT_DES:
                    DES_Method.decrypt_des()
                elif action == Main.ENCRYPT_AES:
                    AES_Method.aes_encrypt()
                elif action == Main.DECRYPT_AES:
                    AES_Method.aes_decrypt()
                #new method can be update here
                elif action == Main.EXIT_PROGRAM:
                    print("Exiting program...")
                    exit(0)

if __name__ == "__main__":
    Main().run()
