

class Entreprise():
    def __init__(self, name):
        self.__name = name
        self.__VAT= "BE0800123456"
        self.__locations = [Ville("60411-2749","Chicago",[Batiment("A", "Main Steet n°1"), Batiment("B","Second Street n°2")]), Ville("10280-1435","New York",[Batiment("C", "Third Street")])]
        self.__employees = [Employe("Tony","Stark"), Employe("Steve","Rogers"), Employe("Black","Widow")]

    @property
    def getName(self):
        return self.__name
    
    @property
    def getVAT(self):
        return self.__VAT
    
    @property
    def getLocations(self):
        return self.__locations

    @property
    def getEmployees(self):
        return self.__employees

    
    def test(self):
        del self.__locations[0]


class Ville():
    def __init__(self, cp, city, building):
        self.__cp = cp
        self.__city = city
        self.__building = building

    @property
    def getPostalCode(self):
        return self.__cp
    
    @property
    def getCity(self):
        return self.__city

    @property
    def getBuilding(self):
        return self.__building

class Batiment():
    def __init__(self, name, addr):
        self.__name = name
        self.__addr = addr

    @property
    def getName(self):
        return self.__name

    @property
    def getAddr(self):
        return self.__addr

class Employe():
    def __init__(self, name, firstName):
        self.__name = name
        self.__firstName = firstName

    @property
    def getName(self):
        return self.__name

    @property
    def getFirstName(self):
        return self.__firstName


def companyInformationDisplay():
    #Impression du nom de la compagnie et du numéro de TVA
    print("\n" * 1 ,"My company name : ",myCompany.getName, " VAT n° :", myCompany.getVAT)
    #Voici mes différentes localisation dans le pays et leur batiments
    print("Locations and their buildings :")
    for myCities in myCompany.getLocations:
        print(" " *2 , myCities.getCity, " ", myCities.getPostalCode, ":")
        for myBuilding in myCities.getBuilding:
            print(" " *6 ,myBuilding.getName, " ", myBuilding.getAddr)

    #Recapitulatif des employés
    print("Employees list : ")
    for myEmployee in myCompany.getEmployees:
        print(" " *3 , myEmployee.getName, " ", myEmployee.getFirstName)


if __name__ == "__main__":
    #Je créer ma compagnie "The shield"
    myCompany = Entreprise("The Shield")

    #On check la compagnie
    companyInformationDisplay()

    #Le scenarion catastrophe, Chicago est détruite !!!! NAAAAAAAA ... enfaite si ..
    myCompany.test()

    #Je réimprime la liste de ce qu'il reste du SHIELD
    companyInformationDisplay()
