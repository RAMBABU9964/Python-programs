'''
1.In python the abstraction  has to be achived ,means if a class has to be declared
as an abstract class then it should inherit from the inbuilt class ABC.

2.ABC stands for Abstract base class and its is present in the module 'abc'.

3.if a method has be declared as an abstract method then a decorator @abstractmethod should be used
 on method declaration as shown below:
 '''
#Example:
from abc import ABC,abstractmethod
class Player(ABC):
    @abstractmethod
    def play(self):
        pass
class cricket(Player):
    def play(self):
        print("player is playing cricket")
class Football(Player):
    def play(self):
        print("player is playing football")
#p=player()#error
c=cricket()
c.play()
f=Football()
f.play()


#Rules of abstraction
'''
Rule-01
In python we can creat an object of abstaract clas if it does not contain any method.
'''
'''

from abc import ABC,abstractmethod
class Player(ABC):
    pass
p=Player()

'''
'''
Rule-02
If an abstract class contains only concrete method then object can be created for that abstrarct
class and the method can be invoked.
'''

class Player(ABC):
    def play(self):
        print("player is playing")
p=Player()
p.play()


'''
Rule-03
if an abstarct class contains abstact method then object for that abstarct class cannot be created

'''

class Player(ABC):
    @abstractmethod
    def play(self):
        pass
    
#p=Player()#error


'''
Rule-04
if an abstarct class contains concrete method as well as abstarct method then we cannot creat
an object of abstract class because of abstarctmethod.
'''
class Player(ABC):
    @abstractmethod
    def play(self):
        pass
    def play1(self):
         print("player is playing")
   
#p=Player()#error

'''
Rule-05
if subclass(cricket) is inheriting from the parent abstarct class(player)
and not providing the body for all the abstarct method(play,play1)in the child class
then the chaild class object cannot be created
'''
class Player(ABC):
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def play1(self):
        pass
class Cricket(Player):
    def play2(self):
        print("play2 playing cricket")
    
#c=Cricket()#error

'''
Rule-06
if a subclass is inheriting from parent abstartct class and it has provided body for
all the abstarctmethod then the child class object can be created.
'''

class Player(ABC):
    @abstractmethod
    def play(self):
        pass
    @abstractmethod
    def play1(self):
        pass
class Cricket(Player):
    def play(self):
        print("play2 playing cricket")
    def play1(self):
        print("player1 is playing cricket")
c=Cricket()
c.play()
c.play1()













