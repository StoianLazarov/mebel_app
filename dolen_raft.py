from dolen_base import Dolen_base
from pprint import pprint

class Dolen_raft(Dolen_base):
    def __init__(
            self, br_raftove='',
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


data_skelet = dict(
            height=850,
            depth=500,
            kant=2,
            d_ploskost=18,
            d_rab_plot=32,
            chelo=40,
            )

data_init = data_skelet

data_dolen_base = dict(
                width=550,
                is_vrata=True
                )
data_init.update(data_dolen_base)

data_dolen_raft = dict(
                br_raftove='1',
                min_h_rav='200',
                middle_stran=0,
                )

pprint(data_init)
dol_01 =  Dolen_raft(br_raftove='2', **data_init)
print(dol_01.info())
# dol_raft = Dolen_raft(br_raftove='1', height=850)
# print(dol_raft.is_vrata)
# print(dol_raft.info())
# dol_raft = Dolen_raft(br_raftove=1, **data_init)
# print(dol_raft.info())
