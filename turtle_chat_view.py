#2016-2017 PERSONAL PROJECTS: TurtleChat!
#WRITE YOUR NAME HERE! malak

#####################################################################################
#                                   IMPORTS                                         #
#####################################################################################
#import the turtle module
import turtle
#import the Client class from the turtle_chat_client module
from turtle_chat_client import Client
#Finally, from the turtle_chat_widgets module, import two classes: Button and TextInput
from turtle_chat_widgets import Button , TextInput
pic=turtle.Screen()
pic.bgpic("pic.gif")

#####################################################################################
#####################################################################################

#####################################################################################
#                                   TextBox                                         #
#####################################################################################
#Make a class called TextBox, which will be a subclass of TextInput.\
class TextBox (TextInput):

#Because TextInput is an abstract class, you must implement its abstract
#methods.  There are two:
#
    def draw_box (self):
        self.writer.penup()
        self.writer.goto(-50,220)
        self.writer.pendown()
        self.writer.write("CHAT", font = ('Arial', 30))
        self.pos=(-145,-200)
        self.height=200
        self.width=150
        turtle.hideturtle()
        self.writer=turtle.clone()
        self.writer.penup()
        self.writer.goto(self.pos)
        self.writer.pendown()
        self.writer.goto(self.width,-200)
        self.writer.goto(self.width,self.height)
        self.writer.goto(-145,self.height)
        self.writer.goto(self.pos)
        self.writer.penup()
    def write_msg(self):
        self.writer.clear()
        self.writer.goto(-130,-100)
        self.writer.pendown()
        self.writer.write('Me :' + self.get_msg(), font=('Arial',16))
        
        
#draw_box
#write_msg
#
#Hints:
#1. in draw_box, you will draw (or stamp) the space on which the user's input
#will appear.
#
#2. All TextInput objects have an internal turtle called writer (i.e. self will
#   have something called writer).  You can write new text with it using code like
#
#   self.writer.write(a_string_variable)
#
#   and you can erase that text using
#
#   self.writer.clear()
#
#3. If you want to make a newline character (i.e. go to the next line), just add
#   \r to your string.  Test it out at the Python shell for practice
#####################################################################################
#####################################################################################

#####################################################################################
#                                  SendButton                                       #
#####################################################################################
#Make a class called SendButton, which will be a subclass of Button.
#Button is an abstract class with one abstract method: fun.
#fun gets called whenever the button is clicked.  It's jobs will be to
#
# 1. send a message to the other chat participant - to do this,
#    you will need to call the send method of your Client instance
# 2. update the messages that you see on the screen
#
#HINT: You may want to override the __init__ method so that it takes one additional
#      input: view.  This will be an instance of the View class you will make next
#      That class will have methods inside of it to help
#      you send messages and update message displays.

class SendButton (Button):
    def __init__(self,view,my_turtle=None,shape=None,pos=(0,-250)):
        turtle.pencolor("white")
        if my_turtle is None:
            self.turtle=turtle.clone()
        else :
            self.turtle=my_turtle
        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(pos)
        if shape is None :
            self.turtle.shape('square')
            self.turtle.shapesize(2,10)

        else :
            turtle.addshape(shape)
            self.turtle.shape(shape)

        self.turtle.showturtle()
        self.turtle.onclick(self.fun)
        turtle.listen()
        self.view=view
##        turtle.pencolor("white")
##        turtle.penup()
##        turtle.goto(-10,-255)
##        turtle.write("Send")
        turtle.pencolor("black")
        


    def fun (self,x=0,y=0):
        turtle.pencolor("white")
        turtle.penup()
        turtle.goto(-30,-265)
        turtle.write("Send",font = ('Bradley Hand ITC', 20))
        self.view.send_msg()


        
#####################################################################################
#####################################################################################


##################################################################
#                             View                               #
##################################################################
#Make a new class called View.  It does not need to have a parent
#class mentioned explicitly.
#
#Read the comments below for hints and directions.
##################################################################
##################################################################
class View:
    _MSG_LOG_LENGTH=5 #Number of messages to retain in view
    _SCREEN_WIDTH=300
    _SCREEN_HEIGHT=600
    _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

    def __init__(self,username='Me',partner_name='Partner'):
        _MSG_LOG_LENGTH=5 #Number of messages to retain in view
        _SCREEN_WIDTH=300
        _SCREEN_HEIGHT=600
        _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

        '''
        :param username: the name of this chat user
        :param partner_name: the name of the user you are chatting with
        '''
        ###
        #Store the username and partner_name into the instance.
        self.partner_name=partner_name
        self.username=username
        ###

        ###
        #Make a new client object and store it in this instance of View
        #(i.e. self).  The name of the instance should be my_client
        
        ###
        turtle.setup(width=400,height=600,startx=None,starty=None)
        ###
        #Set screen dimensions using turtle.setup
        #You can get help on this function, as with other turtle functions,
        #by typing
        #
        #   import turtle
        #   help(turtle.setup)
        #
        #at the Python shell.
        ###
        my_client = Client()
        self.my_client=my_client
        textbox= TextBox()
        self.textbox=textbox
        self.textbox.draw_box()
        self.button=SendButton(self)
        
        ###
        #This list will store all of the messages.
        #You can add strings to the front of the list using
        #   self.msg_queue.insert(0,a_msg_string)
        #or at the end of the list using
        #   self.msg_queue.append(a_msg_string)
        self.msg_queue=[]
        ###

        ###
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase
        #and write messages for each
        ###
        
        ###
        #Create a TextBox instance and a SendButton instance and
        #Store them inside of this instance
        ###

        ###
        #Call your setup_listeners() function, if you have one,
        #and any other remaining setup functions you have invented.
        ###
        self.msg_queue_turtles= list()
        for i in range (3):
            self.msg_queue.insert(i," ")
            self.msg_queue_turtles.append(turtle.clone())
        for m in range (3):
            self.msg_queue_turtles[m].hideturtle()
            self.msg_queue_turtles[m].penup()
            self.msg_queue_turtles[m].goto(-100,m*(_LINE_SPACING))
            

    def send_msg(self):
        '''
        You should implement this method.  It should call the
        send() method of the Client object stored in this View
        instance.  It should also update the list of messages,
        self.msg_queue, to include this message.  It should
        clear the textbox text display (hint: use the clear_msg method).
        It should call self.display_msg() to cause the message
        display to be updated.
        '''
        
        self.my_client.send(self.textbox.new_msg)
        self.msg_queue.insert(0,self.textbox.new_msg)
        self.display_msg()
        self.textbox.clear_msg()
        pass

    def get_msg(self):
        return self.textbox.get_msg()

    

    def setup_listeners(self):
        '''
        Set up send button - additional listener, in addition to click,
        so that return button will send a message.
        To do this, you will use the turtle.onkeypress function.
        The function that it will take is
        self.send_btn.fun
        where send_btn is the name of your button instance

        Then, it can call turtle.listen()'''
        turtle.listen()

    def msg_received(self,msg):
        '''
        This method is called when a new message is received.
        It should update the log (queue) of messages, and cause
        the view of the messages to be updated in the display.

        :param msg: a string containing the message received
                    - this should be displayed on the screen
        '''
        print(msg) #Debug - print message
        show_this_msg=self.partner_name+' says:\r'+ msg
        self.msg_queue.insert(0,show_this_msg)
        #Add the message to the queue either using insert (to put at the beginning)
        #or append (to put at the end).
        #
        #Then, call the display_msg method to update the display
        self.display_msg()
    def display_msg(self):
        '''
        This method should update the messages displayed in the screen.
        You can get the messages you want from self.msg_queue
        '''
        for i in range (3):
            self.msg_queue_turtles[i].clear()
        for n in range (3):
            self.msg_queue_turtles[n].write(self.msg_queue[n],font=('Arial',16))
            
       

    def get_client(self):
        return self.my_client
##############################################################
##############################################################


#########################################################
#Leave the code below for now - you can play around with#
#it once you have a working view, trying to run you chat#
#view in different ways.                                #
#########################################################
if __name__ == '__main__':
    my_view=View()
    _WAIT_TIME=200 #Time between check for new message, ms
    def check() :
        #msg_in=my_view.my_client.receive()
        msg_in=my_view.get_client().receive()
        if not(msg_in is None):
            if msg_in==Client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) #Check recursively
    check()
    turtle.mainloop()
