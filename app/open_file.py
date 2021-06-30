class OpenFile:

    def __init__(self, file):
        self.file = file

    def create_file(self, file):
        open(f"{file}.text", "x")

    def open_file(self, file):

        try:
            open(f"{file}.text")
            prompt = input(
                "I found your file. Would you like to write in this file?")  # try block required except or will throw an error
            if prompt == "yes":
                self.write_file(file)
            elif prompt == "no":
                print("Thanks for visiting")
        except FileNotFoundError:  # creating alias
            print(f"No file named {file}. We are creating a {file}.text now...")
            self.create_file(file)
        finally:  # finally will always execute: used to clean up code
            print("Thanks for visiting")

    def write_file(self, file):
        write = input("What would you like to write? Press enter when done.")
        file = open(f"{file}.text", "w")
        file.write(f"{write}")
        file.close()




