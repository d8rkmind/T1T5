#!/usr/bin/python3
from prompt_toolkit import prompt
from extra.displaylist import Menu, banner
from extra.respond import init_proceed




def main():
    try:
        while True:
            todo=prompt("> T1T5 >> ")
            if 'set' in todo:   
                target=todo.strip("set ")
            elif 'help' in todo:
                print(Menu)
            else:
                todo = todo.strip(" ")
                todo = todo.split(",")
                for i in todo:
                    init_proceed(str(i),target)
            
    except:
        pass

if __name__ == "__main__":
    print(banner)
    main()

    
