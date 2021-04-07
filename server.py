from flask import Flask
import random

WELCOME_MAT = "<img src=https://media4.giphy.com/media/j2wwZqlOFQG55VmrWX/giphy.gif?cid=ecf05e47aq6z84i1jl8tvx7j5cwj9xrml5b7sk2ltzk0mwuu&rid=giphy.gif>"
TOO_LOW = '<img src=https://media0.giphy.com/media/SL7BxmyLKrsatbUiU0/giphy.gif?cid=ecf05e478r7bpmj8kbs80mb50dlz3ucroom12th8h0eht2vq&rid=giphy.gif>'
TOO_HIGH = '<img src=https://media0.giphy.com/media/xT9IgJJWlg2MAygRoY/giphy.gif?cid=ecf05e47mpzciymycsh6nmgf4jk0xxuu38h5sy8uapknsgml&rid=giphy.gif>'
JUST_RIGHT = '<img src=https://media0.giphy.com/media/92ekxqtLAvaG4/giphy.gif?cid=ecf05e478r7bpmj8kbs80mb50dlz3ucroom12th8h0eht2vq&rid=giphy.gif>'

LOWER_LIMIT = 0
UPPER_LIMIT = 9

answer = ''

WELCOME_MSG = '<h1>Welcome to Marthas Vineyard!</h1>' \
             f'<h2>Guess a number between {LOWER_LIMIT} and {UPPER_LIMIT} in the url above.</h2>'
HIGH_MSG = f'<h2>Too high! Try again.</h2>'
LOW_MSG = f'<h2>Too low. (Still goes down smooth.) Try again.</h2>'
RIGHT_MSG = f'<h2>Aw yeah! Take a drink.</h2>'
COLORS = ['#FF7F50', '#000080', '#4682B4', '#008080' '#Q9932CC', '#00BFFF' '#FFD700', '#ADD8E6', '#3CB371', 'tomato']

class GameBrain(Flask):
    def __init__(self, import_name):
        super().__init__(import_name)
        # self.hello = WELCOME_MSG
        # self.low = LOW_MSG
        # self.high = HIGH_MSG
        # self.correct = RIGHT_MSG
        self.palette = COLORS
        self.application = Flask(import_name)
        self.choice = random.randint(LOWER_LIMIT, UPPER_LIMIT)

        def colorize(function):
            def wrap_up(*args, **kwargs):
                color = random.choice(self.palette)
                output = function()
                output = output.replace(f'<h2>', f'<h2 style="color:{color}">')
                return output
            return wrap_up

        @self.application.route('/')
        def say_hi():
            return WELCOME_MSG + WELCOME_MAT

        @colorize
        def too_low():
            return LOW_MSG + TOO_LOW

        @colorize
        def too_high():
            return HIGH_MSG + TOO_HIGH

        @colorize
        def correct():
            return RIGHT_MSG + JUST_RIGHT

        @self.application.route('/<int:number>')
        def check_answer(number):
            if number == self.choice:
                return correct()
            elif number < self.choice:
                return too_low()
            elif number > self.choice:
                return too_high()

game = GameBrain(import_name=__name__)

game.application.run(debug=True)