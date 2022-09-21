from shows import jojos_bizzare_madlibventure, mad_hero_libademia, Onelib_Madpiece
import random

if __name__ == "__main__":
    m = random.choice([jojos_bizzare_madlibventure, mad_hero_libademia, Onelib_Madpiece])
    m.madlib()