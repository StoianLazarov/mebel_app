from skeleton import Skeleton
from utility import Utility
from pprint import pprint

class Dolen_base(Skeleton):

    MOST_WIDTH = 100
    GRAB_CLEARANCE = 2

    def __init__(
            self, width='',
            h_kraka=100,
            is_vrata=False,
            **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.h_kraka = h_kraka
        self.count_element = 0
        self.is_vrata = is_vrata
        if is_vrata:
            self.delta_vrata = self.d_ploskost
        else:
            self.delta_vrata = 0

    def cal_elements(self):
        element_dict = {}
        element_dict['straniza'] = self.cal_stran()
        element_dict['dano'] = self.cal_dano()
        element_dict['most'] = self.cal_most()
        element_dict['grab'] = self.cal_grab()
        element_dict['count_elements'] = self.count_element

        return element_dict

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

    def cal_dano(self):
        delta_x = (
            self.chelo + self.kant +
            self.delta_vrata + self.grab)
        delta_y = self.d_ploskost * 2
        x = self.depth - delta_x
        y = self.width - delta_y
        kant_x = 0
        kant_y = 1
        count_el = 1
        self.count_element += count_el

        return Utility.set_dict(x, y, kant_x, kant_y, count_el)

    def cal_stran(self):
        delta_y = self.h_kraka + self.d_rab_plot + self.kant
        delta_x = (
                self.chelo + self.kant +
                self.delta_vrata + self.grab)
        x = self.height - delta_x
        kant_x = 1
        y = self.depth - delta_y
        kant_y = 1
        br_stran = 2
        self.count_element += br_stran

        return Utility.set_dict(x, y, kant_x, kant_y, br_stran)

    def cal_most(self):
        x = Dolen_base.MOST_WIDTH
        delta_y = self.d_ploskost * 2
        y = self.width - delta_y
        br_most = 2
        self.count_element += br_most

        return Utility.set_dict(x, y, count_el=br_most)

    def cal_grab(self):
        delta_x = Dolen_base.GRAB_CLEARANCE
        x = self.width - delta_x
        delta_y = (
                self.h_kraka + self.d_rab_plot +
                Dolen_base.GRAB_CLEARANCE)
        y = self.height - delta_y
        br_grab = 1
        self.count_element += br_grab

        return Utility.set_dict(x, y)

# end class Dolen_base

# user = Person("Stoian", "555-555-555")
data_skelet = dict(
            height=850,
            depth=500,
            kant=2,
            d_ploskost=18,
            d_rab_plot=32,
            chelo=40,
            grab=3,
            )

print("="*20)
dolen_01 = Dolen_base(width=550, is_vrata=True, **data_skelet)
elment_dolen_01 = dolen_01.cal_elements()
pprint(elment_dolen_01)
