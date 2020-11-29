
class Node():
    def __init__(self,pos, linea,  adjacent =[], padre = None, rgb = (0,0,0)):
        self.pos = pos
        self. adjacent = adjacent
        self. padre = padre
        self.h = 0
        self.g = 99999999
        self.f = 99999999
        self.rgb = rgb
        self.linea = linea

    def display(self):
        fill(self.rgb[0],self.rgb[1],self.rgb[2])
        stroke(self.rgb[0],self.rgb[1],self.rgb[2])
        strokeWeight(1)
        ellipse(self.pos.x, self.pos.y, 15,15)
        

        

Piraeus = Node(PVector(223, 795),1)
Faliro = Node(PVector(337, 780),1)
Moschato = Node(PVector(369, 751),1)
Kallithea = Node(PVector(396, 721),1)
Tavros = Node(PVector(427, 690),1)
Petralona = Node(PVector(455, 661),1)
Thissio = Node(PVector(468, 626),1)
Monastiraki = Node(PVector(467, 579),0)
Omonoia = Node(PVector(465, 531),0)
Victoria = Node(PVector(467, 490),1)
Attiki = Node(PVector(420, 420),0)
Aghios_Nikolaos = Node(PVector(444, 398),1)
Kato_patissia = Node(PVector(470, 370),1)
Aghios_Eleftherios = Node(PVector(497, 341),1)
Ano_Patissia = Node(PVector(525, 313),1)
Perissos = Node(PVector(546, 288),1)
Pefkakia = Node(PVector(573, 263),1)
Nea_lonia = Node(PVector(595, 237),1)
Iraklio = Node(PVector(619, 212),1)
Irini = Node(PVector(711, 200),1)
Neratziotissa = Node(PVector(750, 198),0)
Maroussi = Node(PVector(797, 148),1)
KAT = Node(PVector(838, 105),1)
Kifissia = Node(PVector(882, 59),1)

Aghios_Antonios = Node(PVector(340, 335),2)
Sepolia = Node(PVector(382, 377),2)
Larissa_Station = Node(PVector(421, 467),2)
Metaxourghio = Node(PVector(421, 505),2)
Panepistimio = Node(PVector(492, 552),2)
Syntagma = Node(PVector(521, 577),0)
Akropoli = Node(PVector(521, 630),2)
Sygrou_fix = Node(PVector(521, 670),2)
Neos_Kosmos = Node(PVector(521, 710),2)
Aghios_loanis = Node(PVector(521, 750),2)
Dafni = Node(PVector(521, 790),2)
Aghios_Dimitrios = Node(PVector(521, 830 ),2)
Egaleo = Node(PVector(262, 464),3)
Eleonas = Node(PVector(317, 523),3)
Kerameikos = Node(PVector(357, 564),3)
Evangelismos = Node(PVector(599, 578),3)
Megaro_moussikis = Node(PVector(670, 563),3)
Ambelokipi = Node(PVector(690, 537),3)
Panormou = Node(PVector(714, 515),3)
Katehaki = Node(PVector(735, 492),3)
Ethniki_Amyna = Node(PVector(758, 466),3)
Holorgos = Node(PVector(780, 442),3)
Nomismatokopio = Node(PVector(805, 420),3)
Aghia_Paraskevi = Node(PVector(827, 395),3)
Halondri = Node(PVector(847, 371),3)
Doukissis_Plankentias = Node(PVector(884, 336),3)
Pallini = Node(PVector(949, 362),3)
Palania_Kantza = Node(PVector(948, 426),3)
Koropi = Node(PVector(948, 566),3)
Airport = Node(PVector(1026, 601),3)

Piraeus.adjacent = [(Faliro,2)]
Faliro.adjacent = [(Piraeus,2),(Moschato,3)]
Moschato.adjacent = [(Faliro,3),(Kallithea,3)]
Kallithea.adjacent = [(Moschato,3),(Tavros,1)]
Tavros.adjacent = [(Kallithea,1),(Petralona,2)]
Petralona.adjacent = [(Tavros,2),(Thissio,2)]
Thissio.adjacent = [(Petralona,2),(Monastiraki,1)]
Monastiraki.adjacent = [(Thissio,1),(Omonoia,2),(Kerameikos,2),(Syntagma,1)]
Omonoia.adjacent = [(Monastiraki,2),(Panepistimio,1),(Metaxourghio,2),(Victoria,1)]
Victoria.adjacent = [(Omonoia,1),(Attiki,3)]
Attiki.adjacent = [(Victoria,3),(Aghios_Nikolaos,1),(Larissa_Station,1),(Sepolia,2)]
Aghios_Nikolaos.adjacent = [(Attiki,1),(Kato_patissia,1)]
Kato_patissia.adjacent = [(Aghios_Nikolaos,1),(Aghios_Eleftherios,2)]
Aghios_Eleftherios.adjacent =[(Kato_patissia,2),(Ano_Patissia,2)]
Ano_Patissia.adjacent =[(Aghios_Eleftherios,2),(Perissos,2)]
Perissos.adjacent = [(Ano_Patissia,2),(Pefkakia,2)]
Pefkakia.adjacent = [(Perissos,2),(Nea_lonia,2)]
Nea_lonia.adjacent = [(Pefkakia,2),(Iraklio,3)]
Iraklio.adjacent=[(Nea_lonia,3),(Irini,2)]
Irini.adjacent = [(Iraklio,2),(Neratziotissa,1)]
Neratziotissa.adjacent = [(Irini,1),(Maroussi,2)]
Maroussi.adjacent = [(Neratziotissa,2),(KAT,2)]
KAT.adjacent =[(Maroussi,2),(Kifissia,2)]
Kifissia.adjacent = [(KAT,2)]  
Aghios_Antonios.adjacent = [(Sepolia,1)]
Sepolia.adjacent = [(Aghios_Antonios,1),(Attiki,2)]
#atikki
Larissa_Station.adjacent = [(Attiki,1),(Metaxourghio,1) ]
Metaxourghio.adjacent = [(Larissa_Station,1),(Omonoia,2)]
#Omonoia
Panepistimio.adjacent = [(Omonoia,1),(Syntagma,1)]
Syntagma.adjacent = [(Panepistimio,1),(Akropoli,1),(Evangelismos,1),(Monastiraki,1)]
Akropoli.adjacent = [(Syntagma,1),(Sygrou_fix,1)]
Sygrou_fix.adjacent = [(Akropoli,1),(Neos_Kosmos,1)]
Neos_Kosmos.adjacent = [(Sygrou_fix,1),(Aghios_loanis,1)]
Aghios_loanis.adjacent = [(Neos_Kosmos,1),(Dafni,2)]
Dafni.adjacent = [(Aghios_loanis,2),(Aghios_Dimitrios,1)]
Aghios_Dimitrios.adjacent = [(Dafni,1)]


Egaleo.adjacent = [(Eleonas,3)]
Eleonas.adjacent = [(Kerameikos,4),(Egaleo,3)]
Kerameikos.adjacent = [(Monastiraki,2),(Eleonas,4)]
#Monastiraki
#Syntagma
Evangelismos.adjacent = [(Megaro_moussikis,1),(Syntagma,1)]
Megaro_moussikis.adjacent = [(Ambelokipi,2),(Evangelismos,1)]
Ambelokipi.adjacent = [(Panormou,1),(Megaro_moussikis,2)]
Panormou.adjacent = [(Katehaki,1),(Ambelokipi,1)]
Katehaki.adjacent = [(Ethniki_Amyna,1),(Panormou,1)]
Ethniki_Amyna.adjacent = [(Holorgos,1),(Katehaki,1)]
Holorgos.adjacent = [(Nomismatokopio,1),(Ethniki_Amyna,1)]
Nomismatokopio.adjacent = [(Aghia_Paraskevi,3),(Holorgos,1)]
Aghia_Paraskevi.adjacent = [(Halondri,2),(Nomismatokopio,3)]
Halondri.adjacent = [(Doukissis_Plankentias,2),(Aghia_Paraskevi,2)]
Doukissis_Plankentias.adjacent = [(Pallini,6),(Halondri,2)]
Pallini.adjacent = [(Palania_Kantza,5),(Doukissis_Plankentias,6)]
Palania_Kantza.adjacent = [(Koropi,7),(Pallini,5)]
Koropi.adjacent = [(Airport,21),(Palania_Kantza,7)]
Airport.adjacent = [(Koropi,21)]




nodes = [Piraeus, Faliro, Moschato, Kallithea, Tavros, Petralona, Thissio, Monastiraki, Omonoia, Victoria, Attiki, Aghios_Nikolaos, Kato_patissia, Aghios_Eleftherios, 
         Ano_Patissia, Perissos, Pefkakia, Nea_lonia, Iraklio, Irini, Neratziotissa, Maroussi, KAT, Kifissia, Aghios_Antonios, Sepolia, Larissa_Station, Metaxourghio, 
         Panepistimio, Syntagma, Akropoli, Sygrou_fix, Neos_Kosmos, Aghios_loanis, Dafni, Aghios_Dimitrios, Egaleo, Eleonas, Kerameikos, Evangelismos, Megaro_moussikis, 
         Ambelokipi, Panormou, Katehaki, Ethniki_Amyna, Holorgos, Nomismatokopio, Aghia_Paraskevi, Halondri, Doukissis_Plankentias, Pallini, Palania_Kantza, Koropi,Airport]

transbordos = [Monastiraki, Syntagma, Omonoia, Attiki]        
class Boton():
    
    def __init__(self, pos, s,action):
        self.pos = pos
        self.s = s
        self.clicked = False
        self.action = action
    def press(self):
        
        if mouseX > self.pos.x and mouseX <  self.pos.x+ self.s.x and mouseY >  self.pos.y and mouseY <  self.pos.y+ self.s.y:
            self.clicked = True
        else:
            self.clicked = False
            
            
    def display(self):
        strokeWeight(4)
        stroke(0)
        fill(255)
        rect(self.pos.x,self.pos.y,self.s.x,self.s.y)
        fill(0)
        textSize(20)
        text(self.action, self.pos.x +5, self.pos.y + self.s.y - self.s.y/4)
        
        


    
def ACTIVATE(action):
    global node1, node2, node1Selected, node2Selected, path, pathFound, nodes
    if action == "run":
        runF()
        
    if action == "restart":
        node1 = Node
        node2 = Node
        node1Selected = False
        node2Selected = False
        path = []
        pathFound = False
        for node in nodes:
            node.rgb = (0,0,0)
            node. padre = None
            node.h = 0
            node.g = 99999999
            node.f = 99999999
            
        
      
      
      
def selectClosestNode():
    global nodes
    closest = Node
    closestDist = 1000000000000
    for node in nodes:
        newDist = dist(node.pos.x, node.pos.y, mouseX,mouseY)
        if newDist < closestDist:
            closest = node
            closestDist = newDist
    return closest
        
    
    
    
def runF():
    global node1Selected, node2Selected, node1, node2, Path
    
    if node1Selected == False:
        print "PLEASE SELECT NODE 1"
    elif node2Selected == False:
        print "PLEASE SELECT NODE 2"
        
    else:
        path =  AEstrella(node1,node2)
    
    
    

node1 = Node
node2 = Node
node1Selected = False
node2Selected = False



def mouseReleased():
    global listaBotones, node1, node2,node1Selected, node2Selected, run, restart
    for i in listaBotones:
        if i.clicked == True:
            ACTIVATE(i.action)
        
            
    if run.clicked != True and restart.clicked != True:
            
        if node1Selected == True and node2Selected == False:
            node2 = selectClosestNode()
            node2Selected = True
        
        if node1Selected == False :
            node1 = selectClosestNode()
            node1Selected = True
    
    
    
            

            


def interface():
    global img, nodes, node1Selected, node2Selected, node1, node2, listaBotones
    
    for boton in listaBotones:
        boton.press()
        boton.display()
    
    for node in nodes:
       node.display()
    
    selected_Node = selectClosestNode()
    
    if node1Selected == False:
        textSize(20)
        fill(255,0,0)
        text("Select Start",25,135)
        fill(0,255,0)
        ellipse(selected_Node.pos.x, selected_Node.pos.y, 15,15)
    
    elif node2Selected == False:
        textSize(20)
        fill(255,0,0)
        text("Select end",25,135)
        
        fill(255,0,0)
        ellipse(selected_Node.pos.x, selected_Node.pos.y, 15,15)
        
    else:
        textSize(20)
        fill(255,0,0)
        
        text("Run",25,135)
        
   
#=============A*=================
path = []
pathFound = False
t_trans = 9999
def AEstrella(node1, node2):
    global nodes, path, pathFound, transbordos, t_trans
    for nodo in nodes:
        nodo.h = dist(nodo.pos.x, nodo.pos.y, node2.pos.x, node2.pos.y)/100
    
    abiertos = [node1]
    cerrados = []
    gAcumulada = 0
    node1.g = 0
    node1.f = node1.g + node1.h
    
    while len(abiertos) != 0:
        actual = abiertos[0]
        for nodo in abiertos:
            if nodo.f < actual.f:
                actual = nodo
        cerrados.append(actual)
        if actual is node2:
            return camino(actual)
        
        abiertos.remove(actual)
        
        for par in actual.adjacent:
            gAcumulada = gAcumulada + par[1]
            if par[0] in cerrados:
                continue
            elif(par[0] not in abiertos):
                abiertos.append(par[0])
                par[0].padre = actual
                par[0].g = gAcumulada
                par[0].f = gAcumulada + par[0].h
                if actual != node1:
                    if actual.linea == 0:
                        if actual.padre.linea != par[0].linea:
                            par[0].f += t_trans    
            else:
                if gAcumulada < par[0].g:
                    par[0].g = gAcumulada
                        
def camino(nodo):
    global path,pathFound
    result = [nodo]
    current = nodo
    while current.padre != None:
        result.append(current.padre)
        current.rgb = (0,0,255)
        current = current.padre
        
    path = result[::-1]
    pathFound = True
    return result

#Interface:
    

run = Boton( PVector(220,160) , PVector(100,30), "run")
restart = Boton( PVector(360,160) , PVector(100,30), "restart")

listaBotones = [run,restart]

def setup():

    global img, nodes
    size(1200,900)

    img = loadImage("metroAtenas.png")
    


    
    
def draw():
    global img, nodes, node1Selected, node2Selected, node1, node2, path, pathFound
    global listaBotones 
    textSize(32)
    background(255)
    image(img,200,0,900,900)
    
    interface()
    
    if node1Selected == True:
        fill(0,255,0)
        ellipse(node1.pos.x, node1.pos.y, 15,15)
    
    if node2Selected == True:
        fill(255,0,0)
        ellipse(node2.pos.x, node2.pos.y, 15,15)
        
    for node in path[::1]:
        if node.padre != None:
            strokeWeight(4)
            stroke(0,0,255)
            line(node.pos.x, node.pos.y, node.padre.pos.x, node.padre.pos.y)
        
    
    
    
        
    fill(0,0,0)
    text( mouseX,20,40)
    text( mouseY,100,40)
   

    
    
    


            
    
    
    


    
