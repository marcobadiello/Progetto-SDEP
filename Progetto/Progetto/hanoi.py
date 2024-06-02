class Torre():
    def __init__(self):
        self.torre = [[],[],[]]
        self.numdischi = 0
    def getdischi(self):
        x = int(input("Con qunati dischi vuoi giocare: "))
        self.numdischi = x
    def inizializza(self):
        for i in range(self.numdischi,0,-1):
            self.torre[0].append(i)
    #def estrai(self,t):
        #a = self.torre[t].pop(-1)
        #return(a)
    def aggiungi(self,x,y):
        self.torre[y].append(self.torre[x].pop(-1))
    def banner_inizio(self):
        print("""
          _                   _______ ____  _____  _____  ______     _____ _____     _    _          _   _  ____ _____  
         | |        /\       |__   __/ __ \|  __ \|  __ \|  ____|   |  __ \_   _|   | |  | |   /\   | \ | |/ __ \_   _| 
         | |       /  \         | | | |  | | |__) | |__) | |__      | |  | || |     | |__| |  /  \  |  \| | |  | || |   
         | |      / /\ \        | | | |  | |  _  /|  _  /|  __|     | |  | || |     |  __  | / /\ \ | . ` | |  | || |   
         | |____ / ____ \       | | | |__| | | \ \| | \ \| |____    | |__| || |_    | |  | |/ ____ \| |\  | |__| || |_  
         |______/_/    \_\      |_|  \____/|_|  \_\_|  \_\______|   |_____/_____|   |_|  |_/_/    \_\_| \_|\____/_____| """)
 
                                                                                                          
                                                                                                          
    def getmove(self):
        x = int(input("Da che colonna vuoi togliere il disco: "))
        y = int(input("In che colona vuoi mettere il disco: "))
        if 1 <= x <= 3 and 1 <= y <= 3:
            x = x-1
            y = y-1
            return(x,y)
    def islegal(self,x,y,):
        if len(self.torre[y]) == 0:
            return(True)
        
        elif self.torre[y][-1] > self.torre[x][-1]:
            return(True)
 
        else:
            return(False)        
    def makemove(self,x,y):
        num = Torre.estrai(self,x)
        Torre.aggiungi(self,y,num)
    def iswin(self):
        l = [[],[],[]]
        for i in range(self.numdischi,0,-1):
            l[2].append(i)
        if self.torre == l:
            return(True)
        else:
            return(False)
            
    def print(self):
        for i in range(self.numdischi,0,-1):            
            if len(self.torre[0]) < i:
                print("".center(4), end='')
            elif len(self.torre[0]) >= i:
                print(str(self.torre[0][i-1]).center(4), end='')
                
            if len(self.torre[1]) < i:
                print("".center(4), end='')
            elif len(self.torre[1]) >= i:
                print(str(self.torre[1][i-1]).center(4), end='')
                
            if len(self.torre[2]) < i:
                print("".center(4))
            elif len(self.torre[2]) >= i:
                print(str(self.torre[2][i-1]).center(4))
                
        print("-"*50)
        print("1".center(4), end='')
        print("2".center(4), end='')
        print("3".center(4))
    def banner_fine(self):
        print("""
          _    _          _____      __      _______ _   _ _______ ____  
         | |  | |   /\   |_   _|     \ \    / /_   _| \ | |__   __/ __ \ 
         | |__| |  /  \    | |        \ \  / /  | | |  \| |  | | | |  | |
         |  __  | / /\ \   | |         \ \/ /   | | | . ` |  | | | |  | |
         | |  | |/ ____ \ _| |_         \  /   _| |_| |\  |  | | | |__| |
         |_|  |_/_/    \_\_____|         \/   |_____|_| \_|  |_|  \____/ 
                                                             
                                                             """)

    def play(self):
        Torre.banner_inizio(self)
        Torre.getdischi(self)
        Torre.inizializza(self)
        while Torre.iswin(self) != True:
            Torre.print(self)
            x,y = Torre.getmove(self)
            if Torre.islegal(self,x,y) == True:
                #a = Torre.estrai(self,x)
                Torre.aggiungi(self,x,y)
            else:
                print("Mossa non valida!")
            Torre.iswin(self)
        Torre.print(self)
        Torre.banner_fine(self)

            
            
                