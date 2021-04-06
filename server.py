from flask import Flask
import random

WELCOME_MAT = "https://media4.giphy.com/media/j2wwZqlOFQG55VmrWX/giphy.gif?cid=ecf05e47aq6z84i1jl8tvx7j5cwj9xrml5b7sk2ltzk0mwuu&rid=giphy.gif"
TOO_LOW = 'https://media0.giphy.com/media/SL7BxmyLKrsatbUiU0/giphy.gif?cid=ecf05e478r7bpmj8kbs80mb50dlz3ucroom12th8h0eht2vq&rid=giphy.gif'
TOO_HIGH = 'https://media0.giphy.com/media/xT9IgJJWlg2MAygRoY/giphy.gif?cid=ecf05e47mpzciymycsh6nmgf4jk0xxuu38h5sy8uapknsgml&rid=giphy.gif'
JUST_RIGHT = 'https://media0.giphy.com/media/92ekxqtLAvaG4/giphy.gif?cid=ecf05e478r7bpmj8kbs80mb50dlz3ucroom12th8h0eht2vq&rid=giphy.gif'

LOWER_LIMIT = 0
UPPER_LIMIT = 9

answer = ''

WELCOME_MSG = '<h1>Welcome to Marthas Vineyard!</h1>' \
             f'<h2>Guess a number between {LOWER_LIMIT} and {UPPER_LIMIT} in the url above.</h2>' \
HIGH_MSG = f'Too high! Try again.'
LOW_MSG = f'Too low. (Still goes down smooth.) Try again.'
RIGHT_MSG = f'Aw yeah! Take a drink.'
COLORS = ['#FF7F50', '#000080', '#4682B4', '#008080' '#Q9932CC', '#00BFFF' '#FFD700', '#ADD8E6', '#3CB371', 'tomato']


class GameBrain:
    def __init__(self):

        self.hello = WELCOME_MSG
        self.low = LOW_MSG
        self.high = HIGH_MSG
        self.correct = RIGHT_MSG
        self.palette = COLORS
        self.choice = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        self.application = Flask(import_name=__name__)

    @application.route('/')
    def say_hi(self):
        return self.hello, self.choice

    @application.route('/<int:number>')
    # @self.colorize
    def check_answer(self, number):
        if number == self.choice:
            return self.correct
        elif number > self.choice:
            return self.high
        elif number < self.choice:
            return self.low

    def colorize(self, function):
        color = random.choice(self.palette)
        output = f'<h2 style="color:{color}">{function}</h2>'
        return output


    # @colorize
    def youre_right(self):
       return self.correct


    # @colorize
    # def lowball(self):
    #     return self.low
    #
    # @colorize
    # def highball(self):
    #     return self.high

game = GameBrain()

game.colorize(game.youre_right())

game.application.run(debug=True)