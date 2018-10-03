import sys

class tictac(): 
  def __init__(self):
    list_board=[["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
    self.list_board=list_board

  def get_error(self):
    print("Error")
    raise SystemExit


  def get_board(self):
    a=self.list_board[0][0]
    b=self.list_board[0][1]
    c=self.list_board[0][2]
    d=self.list_board[1][0]
    e=self.list_board[1][1]
    f=self.list_board[1][2]
    g=self.list_board[2][0]
    h=self.list_board[2][1]
    i=self.list_board[2][2]

    print("   "+a+"  |   "+b+"    |   "+c+"      \n------------------------\n   "+d+"  |   "+e+"    |   "+f+"   \n------------------------\n   "+g+"  |   "+h+"    |   "+i+"   \n")


  def check_board(self):
    a=self.list_board[0][0]
    b=self.list_board[0][1]
    c=self.list_board[0][2]
    d=self.list_board[1][0]
    e=self.list_board[1][1]
    f=self.list_board[1][2]
    g=self.list_board[2][0]
    h=self.list_board[2][1]
    i=self.list_board[2][2]

    if a==e==i:
      self.win(a)
    elif a==b==c:
      self.win(a)
    elif a==d==g:
      self.win(a)
    elif b==e==h:
      self.win(b)
    elif c==f==i:
      self.win(c)
    elif g==e==c:
      self.win(c)
    elif d==e==f:
      self.win(d)
    elif g==h==i:
      self.win(g)
    else:
      return
    




  def play1(self, played):
    if played == "a":
      self.played_a1()
    elif played == "b":
      self.played_b1()
    elif played == "c":
      self.played_c1()
    elif played == "d":
      self.played_d1()
    elif played == "e":
      self.played_e1()
    elif played == "f":
      self.played_f1()
    elif played == "g":
      self.played_g1()
    elif played == "h":
      self.played_h1()
    elif played == "i":
      self.played_i1()
    else:
      get_error()



  def played_a1(self):
    self.list_board[0][0]= "X"

  def played_b1(self):
    self.list_board[0][1]= "X"

  def played_c1(self):
    self.list_board[0][2]= "X"
  
  def played_d1(self):
    self.list_board[1][0]= "X"

  def played_e1(self):
    self.list_board[1][1]= "X"

  def played_f1(self):
    self.list_board[1][2]= "X"

  def played_g1(self):
    self.list_board[2][0]= "X"

  def played_h1(self):
    self.list_board[2][1]= "X"

  def played_i1(self):
    self.list_board[2][2]= "X"

  




  def play2(self, played):
    if played == "a":
      self.played_a2()
    elif played == "b":
      self.played_b2()
    elif played == "c":
      self.played_c2()
    elif played == "d":
      self.played_d2()
    elif played == "e":
      self.played_e2()
    elif played == "f":
      self.played_f2()
    elif played == "g":
      self.played_g2()
    elif played == "h":
      self.played_h2()
    elif played == "i":
      self.played_i2()
    else:
      get_error()



  def played_a2(self):
    self.list_board[0][0]= "O"

  def played_b2(self):
    self.list_board[0][1]= "O"

  def played_c2(self):
    self.list_board[0][2]= "O"
  
  def played_d2(self):
    self.list_board[1][0]= "O"

  def played_e2(self):
    self.list_board[1][1]= "O"

  def played_f2(self):
    self.list_board[1][2]= "O"

  def played_g2(self):
    self.list_board[2][0]= "O"

  def played_h2(self):
    self.list_board[2][1]= "O"

  def played_i2(self):
    self.list_board[2][2]= "O"
  


  def win(self, letter):
    if letter=="X":
      print("Player One WINS")
      raise SystemExit

    elif letter=="O":
      print("Player Two WINS")
      raise SystemExit



g1=tictac()
g1.get_board()
counter = 0
while counter<9:
  play1played=input("Player 1 plays at: ")
  g1.play1(play1played)
  g1.get_board()
  g1.check_board()
  counter+=1
  if counter<9:
    play2played=input("Player 2 plays at: ")
    g1.play2(play2played)
    g1.get_board()
    g1.check_board()
    counter+=1


