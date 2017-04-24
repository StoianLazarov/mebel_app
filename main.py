from models import Person
from models import Skeleton
from models import Base_dolni
from models import Dolen_vrata

st = Person("Stoian")
Stoian = Person("Ivanov")

dolni = Skeleton(st, 900, 600, 2, 18, 28, 40)
dolni_st = Skeleton(Stoian, 900, 590, 2, 18, 28, 40)

dol_001 = Base_dolni(dolni_st, 550)
dol_001.set_description("dolen do mivkata")
dol_001.rendModul()

dol_002 = Dolen_vrata(dolni_st, 400, 2)
dol_002.set_description("долен втори с 2 врати")
dol_002.rendModul()
