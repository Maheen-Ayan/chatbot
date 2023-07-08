import todo
import passwordchekeradvanced as pca
import CALC_ADV as cl
import rps

class CHATBOT():
    def time(self):
        print("6:43(pm)")
        
    def riddle(self):
        print("Why did the boy bring a ladder to school?")
        print("Cause he wanted to go to HIGH-SCHOOL. :)")
        
    def TDL(self):
        obj = todo.UserTalk()
        
    def pc(self):
        pca.code()
        
    def calculator(self):
        cl.cal()
        
    def Rock_Paper_Scissors(self):
        rps.game()
        
class interact(CHATBOT):
    def __init__(self):
        super().__init__()
        print("GREETINGS FELLOW FRIEND, HOW CAN I HELP YOU TODAY?")
        a = input()
        if "time" in a.lower():
            self.time()
        elif "riddle" in a.lower():
            self.riddle()
        elif "to do list" in a.lower() or "task" in a.lower():
            self.TDL()
        elif "thanks" in a.lower() or "thank you" in a.lower() or "thanx" in a.lower():
            print("MY PLEASURE!!!")
        elif "password" in a.lower() or "check" in a.lower() or "checker" in a.lower():
            self.pc()
        elif "calculator" in a.lower() or "calc" in a.lower() or "math" in a.lower():
            self.calculator()
        elif "game" in a.lower() or "play" in a.lower() or "rps" in a.lower():
            self.Rock_Paper_Scissors()
        else:
            print("SORRY, I cant do that for you.")
            
object = interact()