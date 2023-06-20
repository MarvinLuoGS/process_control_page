from otree.api import *


doc = """
A page controling process in experiments. Experiment can input
password to allow participants move on to next page. Before entering,
all participants will stay on the same page.
"""


class C(BaseConstants):
    NAME_IN_URL = 'control_page'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


def creating_session(subsession: Subsession):
    # order labels in Monitor
    with open('_rooms/label.txt','r') as file:
        labels = file.readlines()
    label_list = [label.strip() for label in labels]
    file.close()
    for p,label in zip(subsession.get_players(),label_list):
        p.participant.label = label
    

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    psswd = models.IntegerField(initial=1111,blank=True) # password field, set initial value to 1111
    roleid = models.StringField(initial='experimenter') # experimenter or participant, the value of this comes from label
    # e.g. 101,102 are participants, 901 is experimenter
    # the roleid can be determined in other ways


# PAGES
class MyPage1(Page):
    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        if participant.label == '901':
            player.roleid = 'experimenter'
        else:
            player.roleid = 'participant'       


class ControlPage(Page):
    form_model = 'player'
    form_fields = ['psswd']

    @staticmethod
    def error_message(player: Player, values):
        if values['psswd'] != 1234 and player.psswd != 1234: #1234 is just a sample password
            return 'Please listen carefully to the instructions!' 
        #wituout experimenter entering the correct psswd, an error message occurs and participants can't proceed
        
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.roleid == 'experimenter':
            plist = [p for p in player.get_others_in_group()]
            for p in plist:
                setattr(p,'psswd',1234)
        setattr(player,'psswd',1111)

    @staticmethod
    def get_timeout_seconds(player: Player):
        if player.roleid != 'experimenter' and player.psswd == 1234:
            return 5

    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            roleid = player.roleid
        )

class MyPage2(Page):
    pass


class Results(Page):
    pass


page_sequence = [MyPage1, ControlPage, MyPage2, Results]
