
class Base_dolni:
    '''
    def __init__ (self, width, skelet)
    width --- width mm.
    skelet --- class Skeleton
    '''
    id_shkaf = 0

    def __init__(self, skelet, width):
        self.width = width
        self.depth = skelet.depth
        self.height = skelet.height
        self.kant = skelet.kant
        self.d_ploskost = skelet.d_ploskost
        self.d_rab_plot = skelet.d_rab_plot
        self.person_name = skelet.name
        self.chelo = skelet.chelo
        self.grab = 3
        self.h_krak = 80
        Base_dolni.id_shkaf += 1

    def set_description(self, msg="test"):
        self.desctp_shkaf = msg

    def calStraniza(self):
        '''
        Return dict straniza
        '''
        str_a = self.depth - self.kant - self.chelo - self.grab
        kant_a = 1
        str_b = self.height - self.h_krak - self.d_rab_plot - self.kant
        kant_b = 1
        br_el = 2
        straniza = {
                "raz_a": str_a, "raz_b": str_b, "kant_a": kant_a,
                "kant_b": kant_b, "br_el": br_el, "name": "stra"}
        return straniza

    def calDano(self):
        '''Return dict dano '''
        str_a = self.width - (2 * self.d_ploskost)
        kant_a = 1
        str_b = self.depth - self.kant - self.chelo - self.grab
        kant_b = 0
        br_el = 1
        name = "dano"
        dano = {
                "raz_a": str_a, "raz_b": str_b, "kant_a": kant_a,
                "kant_b": kant_b, "br_el": br_el, "name": name}
        return dano

    def calMost(self):
        str_a = self.width - (2 * self.d_ploskost)
        kant_a = 0
        str_b = 80
        kant_b = 0
        if self.width >= 600:
            br_el = 2
        else:
            br_el = 1
        name = "most"
        most = {
                "raz_a": str_a, "raz_b": str_b, "kant_a": kant_a,
                "kant_b": kant_b, "br_el": br_el, "name": name}
        return most

    def calGrab(self):
        str_a = self.width
        kant_a = 0
        str_b = self.height
        kant_b = 0
        br_el = 1
        name = "grab"
        grab = {
                "raz_a": str_a, "raz_b": str_b, "kant_a": kant_a,
                "kant_b": kant_b, "br_el": br_el, "name": name}
        return grab

    def printMask(self):
        print("id shkaf {} - {}/{}/{} - {}".format(
            Base_dolni.id_shkaf,
            self.width,
            self.height,
            self.depth,
            self.desctp_shkaf))
        print(
            "\t\t\trazmerA--\tkantA--\t\trazmerB--\t\tkantB-- \tbr_elment")

    def printElement(self, element):
        if isinstance(element, dict):
            print(
                "{}\t\t--{}\t\t--{}\t\t\t--{}\t\t\t--{}\t\t\t--{}".format(
                    element["name"],
                    element["raz_a"],
                    element["kant_a"],
                    element["raz_b"],
                    element["kant_b"],
                    element["br_el"],))

    def rendModul(self):
        self.printMask()
        self.printElement(self.calStraniza())
        self.printElement(self.calDano())
        self.printElement(self.calMost())
        self.printElement(self.calGrab())


class Dolen_vrata(Base_dolni):

    def __init__(self, skelet, width, vrata_br):
        super().__init__(skelet, width)
        self.vrata_br = vrata_br

    def calVrata(self):
        '''
        Return dict vrata
        '''
        name = "vrat"
        str_a = (self.width - (2 * self.kant) - 2) / self.vrata_br
        kant_a = 2
        str_b = self.height - self.h_krak - self.d_rab_plot - (2 * self.kant)
        kant_b = 2
        br_el = 2
        vrata = {
                "raz_a": str_a, "raz_b": str_b, "kant_a": kant_a,
                "kant_b": kant_b, "br_el": br_el, "name": name}
        return vrata

    def rendModul(self):
        super().rendModul()
        self.printElement(self.calVrata())
