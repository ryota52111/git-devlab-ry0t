#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# import ui.mainWindow as win
# import database.sql as sql

from ui import mainWindow as win
from database import sql

print("myTool Global")

def main():
    print("myTool LOCAL")


win.main()
sql.main()
main()