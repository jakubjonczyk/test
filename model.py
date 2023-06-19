temperatura_aluminium = 500
masa_aluminium = 100
dyfuzyjnosc_termiczna=0
pole_powierzchni=0
cieplo_wlasciwe_przy_stalym_cisnieniu=0
Stala_promieniowania=0
wysokosc = 1.5
przyspieszenie_grawitaycjne=9.80665

Dlugosc=0
Liczba_Nusselta=0
Liczba_Prandtla=0
Temperatura_plynu=0
Temperatura_powierzchni_scianki=0
Gestosc_strumienia_ciepla=0
wspolczynnik_przejmowania_ciepla=0
wspolczynnik_rozszerzalnosci_objetosciowej=0
wspolczynnik_przewodzenia_ciepla=0
wspolczynnik_lepkosci_kinematycznej=0
gestosc=0

liczba_Grashofa=(przyspieszenie_grawitaycjne * (wysokos ** 3) * wspolczynnik_rozszerzalnosci_objetosciowej * (Temperatura_powierzchni_scianki - Temperatura_plynu ))/(wspolczynnik_lepkosci_kinematycznej**2)
print(liczba_Grashofa)