from person import Person
from validator import valid_init


class Skeleton:
    '''
    Definite skeleton of skaf
    def __init__(self, person, height, depth, kant, d_ploskost,
        d_rab_plot, chelo):
        person  Class Person --- name klient'''

    dic_info = {}
    valid_kant = ('0', '0.8', '2')
    valid_d_plostkost = ('16', '18', '24')
    valid_d_rab_plot = ('28', '32')
    valid_chelo = ('30', '40')

    def __init__(
            self, person=Person(), height='', depth='', kant='',
            d_ploskost='', d_rab_plot='', chelo='', grab='',
            **kwargs):
        super().__init__(**kwargs)
        self.name_person = person.name
        self.phone_person = person.phone
        self.height = height
        self.depth = depth
        self.kant = kant
        self.d_ploskost = d_ploskost
        self.d_rab_plot = d_rab_plot
        self.chelo = chelo
        self.grab = grab

        self.dic_info = self.setDicInfo()

    def setDicInfo(self):
        return dict(
                name_person=self.name_person,
                phone_person=self.phone_person,
                height=self.height,
                depth=self.depth,
                kant=self.kant,
                d_ploskost=self.d_ploskost,
                d_rab_plot=self.d_rab_plot,
                chelo=self.chelo,
                )

    def info(self):
        """info(self): ->return info object Skeleton
    return -> string"""
        info_str = '''
info the Skeleton class
=======================
height = {height}
depth = {depth}
kant = {kant}
d_ploskost = {d_ploskost}
d_rab_plot = {d_rab_plot}
chelo = {chelo}
'''.format(
            height=self.height,
            depth=self.depth,
            kant=self.kant,
            d_ploskost=self.d_ploskost,
            d_rab_plot=self.d_rab_plot,
            chelo=self.chelo
            )
        return info_str

    @staticmethod
    def promp_init():
        return dict(
                height=input("enter height (int): "),
                depth=input("enter depth (int): "),
                kant=valid_init("set kant", Skeleton.valid_kant),
                d_ploskost=valid_init(
                    "set d plostkost", Skeleton.valid_d_plostkost
                    ),
                d_rab_plot=valid_init(
                    "set d_raboten plot", Skeleton.valid_d_rab_plot
                    ),
                chelo=valid_init("set razmer na cheloto", Skeleton.valid_chelo),
                grab=input("enter depth grab (int): "),
                )
# end class Skeleton
