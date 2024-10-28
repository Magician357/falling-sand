class grid:
    def __init__(self,width,height):
        self.width,self.height=width,height
        self.grid=[[element("empty",(x,height-(y+1))) for x in range(width)] for y in range(height)]
        
    def __getitem__(self,pos):
        x,y=pos
        return self.grid[self.height-(y+1)][x]
    
    def __setitem__(self,pos,value):
        x,y=pos
        self.grid[self.height-(y+1)][x]=value
        
    def swap(self,pos1,pos2):
        
        # Swap both points
        temp=self.__getitem__(pos2)
        self.__setitem__(pos2,self.__getitem__(pos1))
        self.__setitem__(pos1,temp)
        
        # Update positions
        self.__getitem__(pos1).set_position(pos1)
        self.__getitem__(pos2).set_position(pos2)
    
    def update(self):
        for y, row in enumerate(self.grid[1:-1]):
            for x, cell in enumerate(row):
                self.__getitem__((x,y)).get_next_move(self)
                

class element:
    def __init__(self,name,pos):
        self.name=name
        self.x,self.y=pos
        self.type=0
        self.color=(0,0,0)
        
    def get_next_move(self,grid):
        return
    
    def set_position(self,pos):
        self.x,self.y=pos
        
    @property
    def pos(self):
        return (self.x,self.y)

class solid(element):
    
    def __init__(self,name,pos):
        super().__init__(name,pos)
        self.type=1
        self.color=(0,255,0)
        
    def get_next_move(self,grid):
        # check below self
        below_cell=grid[self.x,self.y-1]
        
        if below_cell.type in [0,2,3]: # if below cell is either empty, liquid, or gas
            # print("swapping")
            grid.swap((self.x,self.y),(self.x,self.y-1))