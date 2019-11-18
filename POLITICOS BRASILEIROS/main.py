""" Exemplo do uso de herança. """

from Presidente import Presidente
from Senador import Senador
from DeputadoFederal import DeputadoFederal
from Governador import Governador
from DeputadoEstadual import DeputadoEstadual
from Prefeito import Prefeito
from Vereador import Vereador

pres = Presidente("Frank Underwood","Partido House of Cards")
sen = Senador("Michael Kern","Partido House of Cards","US")
dep_f = DeputadoFederal("Diogo Fraga","Partido da Tropa II","RJ")
gov = Governador("Jim Matthews","Partido House of Cards","Pensilvânia")
dep_e = DeputadoEstadual("Fortunato","Partido da Tropa II","RJ")
pref = Prefeito("Odorico Paraguaçu","Partido do Povo","Sucupira","BA")
vered = Vereador("Doroteia","Partido do Povo","Sucupira","BA")

pres.apresentacao()
sen.apresentacao()
dep_f.apresentacao()
gov.apresentacao()
dep_e.apresentacao()
pref.apresentacao()
vered.apresentacao()
