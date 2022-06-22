import re
import requests
import csv
# from alignment import *


ENCODING = 'ISO-8859-1'

Age_set = {"<https://w3id.org/framester/data/framestercore/Age>",
           "<https://w3id.org/framester/data/framestercore/PeopleByAge>", "<https://w3id.org/framester/data/framestercore/Aging>"}
Age_set_second = {"<https://w3id.org/framester/data/framestercore/People>",
                      "<https://w3id.org/framester/data/framestercore/MeasureDuration>"}
ApartmentOwned_set = {"<https://w3id.org/framester/data/framestercore/Possession>",
                      "<https://w3id.org/framester/data/framestercore/Building_subparts>"}
ApartmentOwned_second_set = {"<https://w3id.org/framester/data/framestercore/CommerceBuy>",
                      "<https://w3id.org/framester/data/framestercore/Building_subparts>"}
ApartmentOwned_third_set = {"<https://w3id.org/framester/data/framestercore/Possession>",
                      "<http://www.w3.org/2006/03/wn/wn30/instances/synset-apartment-noun-1>"}
ApartmentOwned_fourth_set = {"<https://w3id.org/framester/data/framestercore/CommerceBuy>",
                      "<http://www.w3.org/2006/03/wn/wn30/instances/synset-apartment-noun-1>"}
CarOwned_set = {"<https://w3id.org/framester/data/framestercore/Possession>",
                "<https://w3id.org/framester/data/framestercore/Vehicle>"}
CarOwned_second_set = {"<https://w3id.org/framester/data/framestercore/CommerceBuy>",
                "<https://w3id.org/framester/data/framestercore/Vehicle>"}
Credit_set = {"<https://w3id.org/framester/data/framestercore/Money>",
              "<https://w3id.org/framester/data/framestercore/People>"}
Criminal_set = {"<https://w3id.org/framester/data/framestercore/CommittingCrime>",
                "<https://w3id.org/framester/data/framestercore/Robbery>", "<https://w3id.org/framester/data/framestercore/Killing>"}
Criminal_second_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-crime-noun-1>", "<https://w3id.org/framester/data/framestercore/Institutionalization>"}
CriminalCharge_set = {"<https://w3id.org/framester/data/framestercore/CommittingCrime>",
                      "<https://w3id.org/framester/data/framestercore/Notification_of_charges>"}
CriminalConviction_set = {"<https://w3id.org/framester/data/framestercore/CommittingCrime>",
                          "<https://w3id.org/framester/data/framestercore/Verdict>"}
CriminalPardon_set = {"<https://w3id.org/framester/data/framestercore/CommittingCrime>",
                      "<https://w3id.org/framester/data/framestercore/Pardon>"}
Country_set = {"<https://w3id.org/framester/data/framestercore/ExpectedLocationOfPerson>",
                   "<https://w3id.org/framester/data/framestercore/PeopleByResidence>", "<https://w3id.org/framester/data/framestercore/ForeignOrDomesticCountry>"}
Demographic_set = {"<https://w3id.org/framester/data/framestercore/Sharing>",
                   "<https://w3id.org/framester/data/framestercore/People>",
                   "<https://w3id.org/framester/data/framestercore/Information>"}
Language_set = {"<https://w3id.org/framester/data/framestercore/Origin>",
                "<https://w3id.org/framester/data/framestercore/People>",
                "<https://w3id.org/framester/data/framestercore/Communication>"}
Disability_set = {"<https://w3id.org/framester/data/framestercore/Capability>",
                  "<https://w3id.org/framester/data/framestercore/MedicalConditions>"}
DrugTestResult_set = {"<https://w3id.org/framester/data/framestercore/Intoxicants>",
                    "<https://w3id.org/framester/data/framestercore/Addiction>"}
Ethnicity_set = {"<https://w3id.org/framester/data/framestercore/PeopleByOrigin>",
                    "<https://w3id.org/framester/data/framestercore/Origin>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-ethnicity-noun-1>"}
FamilyHealthHistory_set = {"<https://w3id.org/framester/data/framestercore/Kinship>",
                           "<https://w3id.org/framester/data/framestercore/IndividualHistory>",
                           "<https://w3id.org/framester/data/framestercore/MedicalConditions>"}
Favorite_set = {"<https://w3id.org/framester/data/framestercore/Preference>",
                    "<http://www.w3.org/2006/03/wn/wn30/instances/synset-prefer-verb-1>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-favored-adjectivesatellite-1>"}
FavoriteColor_set = {"<https://w3id.org/framester/data/framestercore/Preference>", "<https://w3id.org/framester/data/framestercore/Color>"}
FavoriteColor_second_set = {"<https://w3id.org/framester/data/framestercore/Color>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-prefer-verb-1>"}
FavoriteColor_third_set = {"<https://w3id.org/framester/data/framestercore/Preference>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-color-noun-1>"}
FavoriteColor_fourth_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-prefer-verb-1>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-color-noun-1>"}
FavoriteFood_set = {"<https://w3id.org/framester/data/framestercore/Preference>",
                    "<https://w3id.org/framester/data/framestercore/Food>"}
FavoriteFood_second_set = {"<https://w3id.org/framester/data/framestercore/Food>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-prefer-verb-1>"}
FavoriteFood_third_set = {"<https://w3id.org/framester/data/framestercore/Preference>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-food-noun-1>"}
FavoriteFood_fourth_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-prefer-verb-1>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-food-noun-1>"}
FavoriteMusic_set = {"<https://w3id.org/framester/data/framestercore/Preference>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-music-noun-1>"}
FavoriteMusic_second_set = {"<https://w3id.org/framester/data/framestercore/Preference>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-music-noun-1>"}
Fetish_set = {"<https://w3id.org/framester/data/framestercore/Preference>",
              "<https://w3id.org/framester/data/framestercore/Sex>",
              "<https://w3id.org/framester/data/framestercore/Aesthetics>"}
Gender_set = {"<https://w3id.org/framester/data/framestercore/Biological_classification>",
              "<https://w3id.org/framester/data/framestercore/People>"}
HairColor_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-hair-noun-1>", "<https://w3id.org/framester/data/framestercore/Possession>"}
HealthRecord_set = {"<https://w3id.org/framester/data/framestercore/MedicalConditions>",
                    "<https://w3id.org/framester/data/framestercore/Recording>"}
Height_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-height-noun-1>"}
HouseOwned_set = {"<https://w3id.org/framester/data/framestercore/Buildings>",
                  "<https://w3id.org/framester/data/framestercore/Possession>"}
HouseOwned_second_set = {"<https://w3id.org/framester/data/framestercore/Buildings>",
                  "<https://w3id.org/framester/data/framestercore/CommerceBuy>"}
IncomeBracket_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-bracket-noun-4>", "<https://w3id.org/framester/data/framestercore/EarningsAndLosses>"}
IncomeBracket_second_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-income-noun-1>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-bracket-noun-4>"}
Marriage_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-marriage-noun-2>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-wedding-noun-1>"}
MentalHealth_set = {"<https://w3id.org/framester/data/framestercore/MedicalConditions>",
                  "<https://w3id.org/framester/data/framestercore/MentalProperty>"}
Offspring_set = {"<https://w3id.org/framester/data/framestercore/Birth>", "<https://w3id.org/framester/data/framestercore/Kinship>"}
Offspring_second_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-daughter-noun-1>", "<https://w3id.org/framester/data/framestercore/Kinship>"}
Offspring_third_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-son-noun-1>", "<https://w3id.org/framester/data/framestercore/Kinship>"}
PhysicalHealth_set = {"<https://w3id.org/framester/data/framestercore/MedicalConditions>",
                      "<http://www.w3.org/2006/03/wn/wn30/instances/synset-broken-adjective-1>"}
PhysicalHealth_second_set = {"<https://w3id.org/framester/data/framestercore/ObservableBodyParts>",
                      "<https://w3id.org/framester/data/framestercore/BodyParts>"}
PhysicalTraits_set = {"<https://w3id.org/framester/data/framestercore/Possession>",
                      "<https://w3id.org/framester/data/framestercore/ObservableBodyParts>"}
Possession_set = {"<https://w3id.org/framester/data/framestercore/Possession>",
                    "<https://w3id.org/framester/data/framestercore/CommerceBuy>"}
Prescription_set = {"<https://w3id.org/framester/data/framestercore/MedicalConditions>",
                    "<https://w3id.org/framester/data/framestercore/Cure>",
                    "<https://w3id.org/framester/data/framestercore/Medical_intervention>"}
Prescription_second_set = {"<https://w3id.org/framester/data/framestercore/Intoxicants>",
                    "<https://w3id.org/framester/data/framestercore/MedicalProfessionals>"}
PrivacyPreference_set = {"<https://w3id.org/framester/data/framestercore/Preference>", "<https://w3id.org/framester/data/framestercore/Secrecy_status>"}
PrivacyPreference_second_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-prefer-verb-1>", "<https://w3id.org/framester/data/framestercore/Secrecy_status>"}
PrivacyPreference_third_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-prefer-verb-1>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-privacy-noun-1>"}
PrivacyPreference_fourth_set = {"<https://w3id.org/framester/data/framestercore/Preference>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-privacy-noun-1>"}
Proclivitie_set = {"<https://w3id.org/framester/data/framestercore/Inclination>",
                   "<https://w3id.org/framester/data/framestercore/Sex>"}
ProfessionalInterview_set = {"<https://w3id.org/framester/data/framestercore/Assessing>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-article-noun-1>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-interview-noun-1>"}
Race_set = {"<https://w3id.org/framester/data/framestercore/PeopleByOrigin>",
            "<https://w3id.org/framester/data/framestercore/Type>"}
Salary_set = {"<https://w3id.org/framester/data/framestercore/Money>",
            "<https://w3id.org/framester/data/framestercore/EarningsAndLosses>"}
School_set = {"<https://w3id.org/framester/data/framestercore/EducationTeaching>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-diploma-noun-1>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-degree-noun-1>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-school-noun-1>"}
Sexual_set = {"<https://w3id.org/framester/data/framestercore/Sex>",
                     "<http://www.w3.org/2006/03/wn/wn30/instances/synset-sexual-adjective-1>"}
SexualHistory_set = {"<https://w3id.org/framester/data/framestercore/Sex>",
                     "<https://w3id.org/framester/data/framestercore/IndividualHistory>"}
SexualHistory_second_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-sexual-adjective-1>",
                     "<https://w3id.org/framester/data/framestercore/IndividualHistory>"}
Weight_set = {"<https://w3id.org/framester/data/framestercore/Measure_mass>",
              "<https://w3id.org/framester/data/framestercore/People>",
              "<https://w3id.org/framester/data/framestercore/Dimension>"}
MaritalStatus_set = {"<https://w3id.org/framester/data/framestercore/PersonalRelationship>",
                     "<https://w3id.org/framester/data/framestercore/Kinship>"}
Parent_set = {"<https://w3id.org/framester/data/framestercore/Giving_birth>",
              "<https://w3id.org/framester/data/framestercore/Kinship>", "<https://w3id.org/framester/data/framestercore/PersonalRelationship>"}
Health_set = {"<https://w3id.org/framester/data/framestercore/MedicalConditions>",
              "<https://w3id.org/framester/data/framestercore/Come_down_with>"}
Job_set = {"<https://w3id.org/framester/data/framestercore/Work>",
           "<https://w3id.org/framester/data/framestercore/PeopleByVocation>",
           "<https://w3id.org/framester/data/framestercore/BeingEmployed>"}
Location_set = {"<https://w3id.org/framester/data/framestercore/ExpectedLocationOfPerson>",
                "<https://w3id.org/framester/data/framestercore/PeopleByResidence>", "<https://w3id.org/framester/data/framestercore/Residence>", 
                "<https://w3id.org/framester/data/framestercore/Travel>"}
MedicalHealth_set = {"<https://w3id.org/framester/data/framestercore/MedicalConditions>",
                     "<https://w3id.org/framester/data/framestercore/Cure>"}
Religion_set = {"<https://w3id.org/framester/data/framestercore/PeopleByReligion>",
                "<https://w3id.org/framester/data/framestercore/ReligiousBelief>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-Christian-adjective-1>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-Muslim-noun-1>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-Jewish-adjective-1>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-Catholic-adjective-1>"}
Professional_set = {"<https://w3id.org/framester/data/framestercore/EducationTeaching>",
                    "<https://w3id.org/framester/data/framestercore/PeopleByVocation>",
                    "<https://w3id.org/framester/data/framestercore/BeingEmployed>",
                    "<https://w3id.org/framester/data/framestercore/Work>", "<http://www.w3.org/2006/03/wn/wn30/instances/synset-career-noun-1>"}
Relationship_set = {"<https://w3id.org/framester/data/framestercore/PersonalRelationship>",
                    "<https://w3id.org/framester/data/framestercore/FormingRelationships>"}
Divorce_set = {"<http://www.w3.org/2006/03/wn/wn30/instances/instances/synset-marriage-noun-2>",
               "<https://w3id.org/framester/data/framestercore/BecomingSeparated>"}
SkinTone_set = {"<https://w3id.org/framester/data/framestercore/Color>",
                "<http://www.w3.org/2006/03/wn/wn30/instances/instances/synset-skin-noun-1>"}
SkinTone_second_set = {"<https://w3id.org/framester/data/framestercore/Possession>",
                "<http://www.w3.org/2006/03/wn/wn30/instances/instances/synset-skin-noun-1>"}
Work_set = {
    "<https://w3id.org/framester/data/framestercore/PeopleByVocation>",
    "<https://w3id.org/framester/data/framestercore/Work>",
    "<https://w3id.org/framester/data/framestercore/BeingEmployed>"
}
PoliticalAffiliation_union_set = {
    "<http://www.w3.org/2006/03/wn/wn30/instances/instances/synset-affiliated-adjectivesatellite-1>",
    "<http://www.w3.org/2006/03/wn/wn30/instances/synset-affiliation-noun-2>",
    "<https://w3id.org/framester/data/framestercore/TakingSide>"
}


def get_data_from_sentence(row):
    # base_url = "http://semantics.istc.cnr.it/fred?"
    headers = {"Accept": "text/turtle"}

    # filename = '/test_set_fred.csv'
    filename = 'Privacy corpus FRED fine-grained experiment.csv'
    fred_output = {}
    c = csv.DictReader(open(filename, encoding=ENCODING), delimiter=';')

    for row in c:
        frase = row['Sentence']
        frase = frase.strip()
        print(f'Analyzing sentence -- "{frase}"')

        # base_url = 'http://semantics.istc.cnr.it/fred?' + 'text=' + frase + '&alignToFramester=true'
        r = requests.get('http://semantics.istc.cnr.it/fred?' + 'text=' + frase + '&alignToFramester=true', headers=headers)
        framester = set([res for res in re.findall("<https://w3id\.org/framester/data/framestercore/[a-zA-Z0-9]*>", r.text)])
        synset = set([res for res in re.findall("<http://www.w3.org/2006/03/wn/wn30/instances/synset-[a-zA-Z0-9\-\_]*>", r.text)])
        results = framester.union(synset)
        fred_output[frase] = ','.join(results)

    with open('Results_NODUPLICATES.csv', 'w', encoding=ENCODING) as f:
        fieldnames = ['sentence', 'fred_output']
        thewriter = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        thewriter.writeheader()
        for frase, fred_output_frase in fred_output.items():
            thewriter.writerow({'sentence': frase, 'fred_output': fred_output_frase})


def compare_indexes():
    # Confronto indici
    with open('Results_NODUPLICATES.csv', encoding='latin-1') as fin:
        with open('Results_translated_NODUPLICATES_FRED_fine-grained.csv', 'w', encoding='latin-1') as fout:
            cin = csv.DictReader(fin, delimiter=';')
            cout = csv.DictWriter(fout, delimiter=';', fieldnames=cin.fieldnames)

            for line in cin:
                # Come trasformare line['fred_output'] in un set
                x = set(line['fred_output'].split(','))
                category = set()

                 # cercare relazione AND PersonalDataCategories
                if ApartmentOwned_set.issubset(x):
                    category.add('ApartmentOwned')
                if ApartmentOwned_second_set.issubset(x):
                    category.add('ApartmentOwned')
                if ApartmentOwned_third_set.issubset(x):
                    category.add('ApartmentOwned')
                if ApartmentOwned_fourth_set.issubset(x):
                    category.add('ApartmentOwned')
                if Age_set_second.issubset(x):
                    category.add('Age')
                if CarOwned_set.issubset(x):
                    category.add('CarOwned')
                if CarOwned_second_set.issubset(x):
                    category.add('CarOwned')
                if Credit_set.issubset(x):
                    category.add('Credit')
                if CriminalCharge_set.issubset(x):
                    category.add('CriminalCharge')
                if CriminalConviction_set.issubset(x):
                    category.add('CriminalConviction')
                if CriminalPardon_set.issubset(x):
                    category.add('CriminalPardon')
                if Demographic_set.issubset(x):
                    category.add('Demographic')
                if Disability_set.issubset(x):
                    category.add('Disability')
                if Divorce_set.issubset(x):
                    category.add('Divorce')
                if DrugTestResult_set.issubset(x):
                    category.add('DrugTestResult')
                if FamilyHealthHistory_set.issubset(x):
                    category.add('FamilyHealthHistory')
                if FavoriteColor_set.issubset(x):
                    category.add('FavoriteColor')
                if FavoriteColor_second_set.issubset(x):
                    category.add('FavoriteColor')
                if FavoriteColor_third_set.issubset(x):
                    category.add('FavoriteColor')
                if FavoriteColor_fourth_set.issubset(x):
                    category.add('FavoriteColor')
                if FavoriteFood_set.issubset(x):
                    category.add('FavoriteFood')
                if FavoriteFood_second_set.issubset(x):
                    category.add('FavoriteFood')
                if FavoriteFood_third_set.issubset(x):
                    category.add('FavoriteFood')
                if FavoriteFood_fourth_set.issubset(x):
                    category.add('FavoriteFood')
                if FavoriteMusic_set.issubset(x):
                    category.add('FavoriteMusic')
                if FavoriteMusic_second_set.issubset(x):
                    category.add('FavoriteMusic')
                if Fetish_set.issubset(x):
                    category.add('Fetish')
                if Gender_set.issubset(x):
                    category.add('Gender')
                if HairColor_set.issubset(x):
                    category.add('HairColor')
                if HealthRecord_set.issubset(x):
                    category.add('HealthRecord')
                if Height_set.issubset(x):
                    category.add('Height')
                if HouseOwned_set.issubset(x):
                    category.add('HouseOwned')
                if HouseOwned_second_set.issubset(x):
                    category.add('HouseOwned')
                if IncomeBracket_set.issubset(x):
                    category.add('IncomeBracket')
                if IncomeBracket_second_set.issubset(x):
                    category.add('IncomeBracket')
                if Language_set.issubset(x):
                    category.add('Language')
                if MentalHealth_set.issubset(x):
                    category.add('MentalHealth')
                if Offspring_set.issubset(x):
                    category.add('Offspring')
                if Offspring_second_set.issubset(x):
                    category.add('Offspring')
                if Offspring_third_set.issubset(x):
                    category.add('Offspring')
                if PhysicalTraits_set.issubset(x):
                    category.add('PhysicalTraits')
                if Prescription_set.issubset(x):
                    category.add('Prescription')
                if Prescription_second_set.issubset(x):
                    category.add('Prescription')
                if PrivacyPreference_set.issubset(x):
                    category.add('PrivacyPreference')
                if PrivacyPreference_second_set.issubset(x):
                    category.add('PrivacyPreference')
                if PrivacyPreference_third_set.issubset(x):
                    category.add('PrivacyPreference')
                if PrivacyPreference_fourth_set.issubset(x):
                    category.add('PrivacyPreference')
                if Relationship_set.issubset(x):
                    category.add('Relationship')
                if SexualHistory_set.issubset(x):
                    category.add('SexualHistory')
                if SexualHistory_second_set.issubset(x):
                    category.add('SexualHistory')
                if SkinTone_set.issubset(x):
                    category.add('SkinTone')
                if SkinTone_second_set.issubset(x):
                    category.add('SkinTone')
                if Parent_set.issubset(x):
                    category.add('Parent')
                
                 # cercare relazione OR per PersonalDataCategories (frame e frame + synset)
                # un elemento o più  è contenuto nella riga
                if x.intersection(Age_set):
                    category.add('Age')
                if x.intersection(Country_set):
                    category.add('Country')
                if x.intersection(Criminal_set):
                    category.add('Criminal')
                if x.intersection(Criminal_second_set):
                    category.add('Criminal')
                if x.intersection(Ethnicity_set):
                    category.add('Ethnicity')
                if x.intersection(Favorite_set):
                    category.add('Favorite')
                    category.add('Favorite')
                if x.intersection(Health_set):
                    category.add('Health')
                if x.intersection(Job_set):
                    category.add('Job')
                if x.intersection(Location_set):
                    category.add('Location')
                if x.intersection(Marriage_set):
                    category.add('Marriage')
                if x.intersection(MedicalHealth_set):
                    category.add('MedicalHealth')
                if x.intersection(ProfessionalInterview_set):
                    category.add('ProfessionalInterview')
                if x.intersection(Religion_set):
                    category.add('Religion')
                if x.intersection(Possession_set):
                    category.add('PersonalPossession')
                if x.intersection(Professional_set):
                    category.add('Professional')
                if x.intersection(School_set):
                    category.add('School')
                if x.intersection(Sexual_set):
                    category.add('Sexual')
                if set("<https://w3id.org/framester/data/framestercore/RewardsAndPunishments>").issubset(x) and x.intersection(Work_set):
                    category.add('DisciplinaryAction')
                if set("<https://w3id.org/framester/data/framestercore/IndividualHistory>").issubset(x) and x.intersection(Work_set):
                    category.add('EmploymentHistory')
                if set("<https://w3id.org/framester/data/framestercore/IndividualHistory>").issubset(x) and x.intersection(
                     Health_set):
                    category.add('HealthHistory')
                if set("<http://www.w3.org/2006/03/wn/wn30/instances/synset-husband-noun-1>").issubset(x) and x.intersection(MaritalStatus_set):
                    category.add('MaritalStatus')
                if PhysicalHealth_set.issubset(x) and PhysicalHealth_second_set.issubset(x):
                    category.add('MaritalStatus')  
                if set("<https://w3id.org/framester/data/framestercore/Inclination>").issubset(x) and x.intersection(Sexual_set):
                    category.add('Proclivitie') 
                if set("<https://w3id.org/framester/data/framestercore/Documents>").issubset(x) and x.intersection(Work_set):
                    category.add('ProfessionalCertification')
                if set("<https://w3id.org/framester/data/framestercore/Assessing>").issubset(x) and x.intersection(Work_set):
                    category.add('ProfessionalEvaluation')
                if set("<http://www.w3.org/2006/03/wn/wn30/instances/synset-race-noun-2>").issubset(x) and x.intersection(Race_set):
                    category.add('Race')  
                if set("<https://w3id.org/framester/data/framestercore/Attempt_suasion>").issubset(x) and x.intersection(Work_set):
                    category.add('Reference')
                if set("<http://www.w3.org/2006/03/wn/wn30/instances/synset-weight-noun-1>").issubset(x) and x.intersection(Weight_set):
                    category.add('Weight')
                if x.intersection(PhysicalHealth_set) and x.intersection(PhysicalHealth_second_set):
                    category.add('PhysicalHealth')
                if x.intersection(Professional_set) and x.intersection(ProfessionalInterview_set):
                    category.add('ProfessionalInterview')
                if x.intersection(Favorite_set) and x.intersection(Sexual_set):
                    category.add('SexualPreference')
                if x.intersection(Salary_set) and x.intersection(Work_set):
                    category.add('Salary')
                if set("<http://www.w3.org/2006/03/wn/wn30/instances/instances/synset-party-noun-1>").issubset(x) and x.intersection(
                        PoliticalAffiliation_union_set):
                    category.add('PoliticalAffiliation')
                    
                # cercare allineamento 1:1 PersonalDataCategories
                if {"<https://w3id.org/framester/data/framestercore/EarningsAndLosses>"}.issubset(x):
                    category.add('Credit')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-disability-noun-1>"}.issubset(x):
                    category.add('Disability')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-wheelchair-noun-1>"}.issubset(x):
                    category.add('Disability')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-divorce-noun-1>"}.issubset(x):
                    category.add('Divorce')
                if {"<https://w3id.org/framester/data/framestercore/Kinship>"}.issubset(x):
                    category.add('Family')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-fetish-noun-3>"}.issubset(x):
                    category.add('Fetish')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-male-noun-1>"}.issubset(x):
                    category.add('Gender')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-female-noun-1>"}.issubset(x):
                    category.add('Gender')
                if {"<https://w3id.org/framester/data/framestercore/HairConfiguration>"}.issubset(x):
                    category.add('HairColor')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-income-noun-1>"}.issubset(x):
                    category.add('IncomeBracket')
                if {"<https://w3id.org/framester/data/framestercore/CommunicationManner>"}.issubset(x):
                    category.add('Language')
                if {"<https://w3id.org/framester/data/framestercore/Body_description_holistic>"}.issubset(x):
                    category.add('PhysicalCharacteristic')
                if {"<https://w3id.org/framester/data/framestercore/IndividualHistory>"}.issubset(x):
                    category.add('LifeHistory')
                if {"<https://w3id.org/framester/data/framestercore/MentalProperty>"}.issubset(x):
                    category.add('MentalHealth')
                if {"<https://w3id.org/framester/data/framestercore/BeingNamed>"}.issubset(x):
                    category.add('Name') 
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-dad-noun-1>"}.issubset(x):
                    category.add('Parent')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-mum-noun-3>"}.issubset(x):
                    category.add('Parent')
                if {"<https://w3id.org/framester/data/framestercore/Body_description_holistic> "}.issubset(x):
                    category.add('PhysicalTraits')
                if {"<https://w3id.org/framester/data/framestercore/SocialEvent>"}.issubset(x):
                    category.add('PublicLife')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-race-noun-2>"}.issubset(x):
                    category.add('Race')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/instances/synset-sibling-noun-1>"}.issubset(x):
                    category.add('Sibling')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/synset-skin-noun-1>"}.issubset(x):
                    category.add('SkinTone')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/instances/synset-tattoo-noun-2>"}.issubset(x):
                    category.add('Tattoo')
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/instances/synset-tattoo-noun-3>"}.issubset(x):
                    category.add('Tattoo')   
                if {"<http://www.w3.org/2006/03/wn/wn30/instances/instances/synset-tattoo-verb-1>"}.issubset(x):
                    category.add('Tattoo')

                cout.writerow({
                    'sentence': line['sentence'], 'fred_output': category if category != '' else 'No category'
                })


if __name__ == '__main__':
    #get_data_from_sentence('')
    compare_indexes()
