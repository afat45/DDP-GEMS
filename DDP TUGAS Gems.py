import os
import time

list = {"e_money": 0,"gems":0}

def clear():                              #template clear
    os.system("cls || clear")

def delay():                              #template delay
   time.sleep(1)

def pilihan(isi):                         #template menu
        print(40 * "-")
        print(isi)
        print(40 * "-") 

def isi_saldo():                          #isi saldo
  try:
    clear()
    list["e_money"] += int(input("berapa banyak uang yang ingin anda top up: "))
    if list["e_money"] > 0:
      print(f"e-money anda sebesar {list["e_money"]:,}")
      delay()
    else:
      print("e_money tidak bisa minus")
      delay()
  except ValueError:
      print("isi saldo tidak valid")
      delay()

def tuker():                               #tuker
  try:
    clear()
    banyak = int(input(f"""berapa banyak gems yang anda inginkan 
maksimal gems yang dapat di tukar {list["e_money"]/100} 
(100 saldo = 1 gems): """))
    if banyak <= list["e_money"]/100:
      list["e_money"] -= banyak*100
      list["gems"] += banyak
    else: 
      print("saldo tidak cukup")
      delay()
  except ValueError:
      print("tukar gems tidak valid")
      delay()

def beli():                                 #tuker
  while True:
    try:
      clear()
      pilihan(f"""gems = {list["gems"]}
1.beli mie gacoan 100 gems
2.beli mixue 500 gems
3.beli mcd 1000 gems
4.exit""")
      pilihan_beli = int(input("pilihan beli: "))
      if pilihan_beli == 1:
        if list["gems"] >= 100:
          list["gems"] -= 100
          print("kamu membeli mie gacoan")
          delay()
        else:
          print("gems mu tidak cukup")
          delay()
      elif pilihan_beli == 2:
        if list["gems"] >= 500:
          list["gems"] -= 500
          print("kamu membeli mixue")
          delay()
        else:
          print("gems mu tidak cukup")
          delay()
      elif pilihan_beli == 3:
        if list["gems"] >= 1000:
          list["gems"] -= 1000
          print("kamu membeli mcd")
          delay()
        else:
          print("gems mu tidak cukup")
          delay()
      elif pilihan_beli == 4:
        break
      else:
        print("pilihan tidak valid")
        delay()
    except ValueError:
      print("pilihan tidak valid")
      delay()

def menu_utama():                             #menu utama
  while True:               
      clear()
      print("selamat datang di go bay")
      print(f"e-money = {list["e_money"]:,}")
      print(f"gems = {list["gems"]:,}")
      pilihan("""1.isi saldo 
2.tuker saldo ke gems
3.beli 
4.exit """)
      try: 
          pilihan_menu_utama = int(input("pilihan: "))
          if pilihan_menu_utama == 1:
            isi_saldo()
          elif pilihan_menu_utama == 2:
            tuker()
          elif pilihan_menu_utama == 3:
            beli()
          elif pilihan_menu_utama == 4:
              break
          else:
              print("pilihan tidak valid")
              delay()
      except ValueError:
          print("pilihan tidak valid")
          delay()

menu_utama()