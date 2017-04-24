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
            d_ploskost='', d_rab_plot='', chelo='', **kwargs):
        super().__init__(**kwargs)
        self.name_person = person.name
        self.phone_person = person.phone
        self.height = height
        self.depth = depth
        self.kant = kant
        self.d_ploskost = d_ploskost
        self.d_rab_plot = d_rab_plot
        self.chelo = chelo

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
                chelo=valid_init("set razmer na cheloto", Skeleton.valid_chelo)
                )
# end class Skeleton


class Dolen_base(Skeleton):
    def __init__(
            self, width='',
            h_kraka=100,
            is_vrata=False,
            **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.h_kraka = h_kraka
        self.is_vrata = is_vrata
        if is_vrata:
            self.delta_vrata = self.d_ploskost
        else:
            self.delta_vrata = 0

    def info(self):
        info_parent = super().info()
        info_str = '''
info the Dolen_base class
==========================
width = {width}
h_kraka = {h_kraka}
is_vrata = {is_vrata}
'''.format(
            width=self.width,
            h_kraka=self.h_kraka,
            is_vrata=self.is_vrata
            )
        return info_parent + info_str

    def cal_stran(self):
        delta_y = self.h_kraka + self.d_rab_plot + self.kant
        delta_x = self.chelo + self.kant + self.delta_vrata
        x = self.height - delta_x
        kant_x = 1
        y = self.depth - delta_y
        kant_y = 1
        br_stran = 2

        if x > y:
            l_str = x
            l_kant = kant_x
            s_str = y
            s_kant = kant_y
        else:
            l_str = y
            l_kant = kant_y
            s_str = x
            s_kant = kant_x
        return dict(
                long_el=l_str,
                short_el=s_str,
                k_long=l_kant,
                k_short=s_kant,
                br_el=br_stran,
                )


class Dolen_raft(Dolen_base):
    def __init__(
            self,
            br_raftove='',
            min_h_rav='',
            middle_stran=0,
            **kwargs):
        super().__init__(**kwargs)
        self.br_raftove = br_raftove
        self.min_h_rav = min_h_rav
        self.middle_stran = middle_stran

    def info(self):
        info_parent = super().info()
        info_str = '''
info the Dolen_raft class
==========================
br_raftove = {br_raftove}
min_h_rav = {min_h_rav}
middle_stran = {middle_stran}
'''.format(
            br_raftove=self.br_raftove,
            min_h_rav=self.min_h_rav,
            middle_stran=self.middle_stran,
            )
        return info_parent + info_str
# end Dolen_raft class

data_skelet = dict(
            height=850,
            depth=500,
            kant=2,
            d_ploskost=18,
            d_rab_plot=32,
            chelo=40,
            )

data_dolen = dict(
            height=850,
            depth=500,
            kant=2,
            d_ploskost=18,
            d_rab_plot=32,
            chelo=40,
            )


data_dolen_base = dict(
                widht=550,
                is_vrata=True
                )

data_dolen_raft = dict(
                br_raftove='1',
                min_h_rav='200',
                middle_stran=0,
                )

skel_init = dict(
            height='400',
            depth='',
            kant='',
            d_ploskost='',
            d_rab_plot='',
            chelo='',
            )

sk = Skeleton(**data_skelet)
dol_01 = Dolen_base(width='45', **data_skelet)
print(dol_01.info())

dol_02 = Dolen_base(width='300', **data_dolen)
print(dol_02.info())
