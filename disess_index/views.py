from django.shortcuts import render, redirect
from django.contrib import messages
from experta import *
# from.greetings import Greetings
# Create your views here.
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}
diseases_symptoms = []
    
        #loads the knowledge from .txt files into variables to allow the code to use it
    
        
         
def preprocess():
            diseases_list = []
            #global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
            diseases = open("diseases.txt")
            diseases_t = diseases.read()
            diseases_list = diseases_t.split("\n")
            diseases.close()
            for disease in diseases_list:
                disease_s_file = open("Disease symptoms/" + disease + ".txt")
                disease_s_data = disease_s_file.read()
                s_list = disease_s_data.split("\n")
                diseases_symptoms.append(s_list)
                symptom_map[str(s_list)] = disease
                disease_s_file.close()

                disease_s_file = open("Disease descriptions/" + disease + ".txt")
                disease_s_data = disease_s_file.read()
                d_desc_map[disease] = disease_s_data
                disease_s_file.close()

                disease_s_file = open("Disease treatments/" + disease + ".txt")
                disease_s_data = disease_s_file.read()
                d_treatment_map[disease] = disease_s_data
                disease_s_file.close()


def identify_disease(*arguments):
                    symptom_list = []
                    for symptom in arguments:
                        symptom_list.append(symptom)

                    return symptom_map[str(symptom_list)]


def get_details(disease):
                    return d_desc_map[disease]


def get_treatments(disease):
                    return d_treatment_map[disease]

            
   
  

def index(request):
   


    

    class Greetings(KnowledgeEngine):

        def __init__(self, symptom_map, if_not_matched, get_treatments, get_details):
            self.symptom_map = symptom_map
            self.if_not_matched = if_not_matched
            self.get_details = get_details
            self.get_treatments = get_treatments
            KnowledgeEngine.__init__(self)

        #code giving instructions on how to use the Expert System
        @DefFacts()
        def _initial_action(self):
            yield Fact(action="find_disease")

        #taking various input from user
        @Rule(Fact(action="find_disease"), NOT(Fact(headache=W())), salience=4)
        def symptom_0(self):
            self.declare(Fact(headache=request.GET['headache']))

        @Rule(Fact(action="find_disease"), NOT(Fact(back_pain=W())), salience=1)
        def symptom_1(self):
            self.declare(Fact(back_pain=request.GET['back_pain']))

        @Rule(Fact(action="find_disease"), NOT(Fact(chest_pain=W())), salience=1)
        def symptom_2(self):
            self.declare(Fact(chest_pain=request.GET['chest_pain']))

        @Rule(Fact(action="find_disease"), NOT(Fact(cough=W())), salience=3)
        def symptom_3(self):
            self.declare(Fact(cough=request.GET['chest_pain']))

        @Rule(Fact(action="find_disease"), NOT(Fact(fainting=W())), salience=1)
        def symptom_4(self):
            self.declare(Fact(fainting=request.GET['fainting']))

        @Rule(Fact(action="find_disease"), NOT(Fact(fatigue=W())), salience=1)
        def symptom_5(self):
            self.declare(Fact(fatigue=request.GET['fatigue']))

        @Rule(Fact(action="find_disease"), NOT(Fact(sunken_eyes=W())), salience=1)
        def symptom_6(self):
            self.declare(Fact(sunken_eyes=request.GET['sunken_eyes']))

        @Rule(Fact(action="find_disease"), NOT(Fact(low_body_temp=W())), salience=1)
        def symptom_7(self):
            self.declare(Fact(low_body_temp=request.GET['low_body_temp']))

        @Rule(Fact(action="find_disease"), NOT(Fact(restlessness=W())), salience=1)
        def symptom_8(self):
            self.declare(Fact(restlessness= request.GET['restlessness']))

        @Rule(Fact(action="find_disease"), NOT(Fact(sore_throat=W())), salience=1)
        def symptom_9(self):
            self.declare(Fact(sore_throat=request.GET['sore_throat']))

        @Rule(Fact(action="find_disease"), NOT(Fact(fever=W())), salience=1)
        def symptom_10(self):
            self.declare(Fact(fever=request.GET['fever']))

        @Rule(Fact(action="find_disease"), NOT(Fact(nausea=W())), salience=1)
        def symptom_11(self):
            self.declare(Fact(nausea=request.GET['nausea']))

        @Rule(Fact(action="find_disease"), NOT(Fact(blurred_vision=W())), salience=1)
        def symptom_12(self):
            self.declare(Fact(blurred_vision= request.GET['blurred_vision']))
        
        #different rules checking for each disease match
        @Rule(
            Fact(action="find_disease"),
            Fact(headache="no"),
            Fact(back_pain="no"),
            Fact(chest_pain="no"),
            Fact(cough="no"),
            Fact(fainting="no"),
            Fact(sore_throat="no"),
            Fact(fatigue="high"),
            Fact(restlessness="no"),
            Fact(low_body_temp="no"),
            Fact(fever="low"),
            Fact(sunken_eyes="no"),
            Fact(nausea="high"),
            Fact(blurred_vision="no"),
        )
        def disease_0(self):
            self.declare(Fact(disease="Jaundice"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="no"),
            Fact(back_pain="no"),
            Fact(chest_pain="no"),
            Fact(cough="no"),
            Fact(fainting="no"),
            Fact(sore_throat="no"),
            Fact(fatigue="no"),
            Fact(restlessness="high"),
            Fact(low_body_temp="no"),
            Fact(fever="no"),
            Fact(sunken_eyes="no"),
            Fact(nausea="no"),
            Fact(blurred_vision="no"),
        )
        def disease_1(self):
            self.declare(Fact(disease="Alzheimers"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="no"),
            Fact(back_pain="high"),
            Fact(chest_pain="no"),
            Fact(cough="no"),
            Fact(fainting="no"),
            Fact(sore_throat="no"),
            Fact(fatigue="low"),
            Fact(restlessness="no"),
            Fact(low_body_temp="no"),
            Fact(fever="no"),
            Fact(sunken_eyes="no"),
            Fact(nausea="no"),
            Fact(blurred_vision="no"),
        )
        def disease_2(self):
            self.declare(Fact(disease="Arthritis"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="no"),
            Fact(back_pain="no"),
            Fact(chest_pain="high"),
            Fact(cough="low"),
            Fact(fainting="no"),
            Fact(sore_throat="no"),
            Fact(fatigue="no"),
            Fact(restlessness="no"),
            Fact(low_body_temp="no"),
            Fact(fever="high"),
            Fact(sunken_eyes="no"),
            Fact(nausea="no"),
            Fact(blurred_vision="no"),
        )
        def disease_3(self):
            self.declare(Fact(disease="Tuberculosis"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="no"),
            Fact(back_pain="no"),
            Fact(chest_pain="high"),
            Fact(cough="high"),
            Fact(fainting="no"),
            Fact(sore_throat="no"),
            Fact(fatigue="no"),
            Fact(restlessness="low"),
            Fact(low_body_temp="no"),
            Fact(fever="no"),
            Fact(sunken_eyes="no"),
            Fact(nausea="no"),
            Fact(blurred_vision="no"),
        )
        def disease_4(self):
            self.declare(Fact(disease="Asthma"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="low"),
            Fact(back_pain="no"),
            Fact(chest_pain="no"),
            Fact(cough="high"),
            Fact(fainting="no"),
            Fact(sore_throat="high"),
            Fact(fatigue="no"),
            Fact(restlessness="no"),
            Fact(low_body_temp="no"),
            Fact(fever="low"),
            Fact(sunken_eyes="no"),
            Fact(nausea="no"),
            Fact(blurred_vision="no"),
        )
        def disease_5(self):
            self.declare(Fact(disease="Sinusitis"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="no"),
            Fact(back_pain="no"),
            Fact(chest_pain="no"),
            Fact(cough="no"),
            Fact(fainting="no"),
            Fact(sore_throat="no"),
            Fact(fatigue="low"),
            Fact(restlessness="no"),
            Fact(low_body_temp="no"),
            Fact(fever="no"),
            Fact(sunken_eyes="no"),
            Fact(nausea="no"),
            Fact(blurred_vision="no"),
        )
        def disease_6(self):
            self.declare(Fact(disease="Epilepsy"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="no"),
            Fact(back_pain="no"),
            Fact(chest_pain="high"),
            Fact(cough="no"),
            Fact(fainting="no"),
            Fact(sore_throat="no"),
            Fact(fatigue="no"),
            Fact(restlessness="no"),
            Fact(low_body_temp="no"),
            Fact(fever="no"),
            Fact(sunken_eyes="no"),
            Fact(nausea="high"),
            Fact(blurred_vision="no"),
        )
        def disease_7(self):
            self.declare(Fact(disease="Heart Disease"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="no"),
            Fact(back_pain="no"),
            Fact(chest_pain="no"),
            Fact(cough="no"),
            Fact(fainting="no"),
            Fact(sore_throat="no"),
            Fact(fatigue="high"),
            Fact(restlessness="no"),
            Fact(low_body_temp="no"),
            Fact(fever="no"),
            Fact(sunken_eyes="no"),
            Fact(nausea="low"),
            Fact(blurred_vision="low"),
        )
        def disease_8(self):
            self.declare(Fact(disease="Diabetes"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="low"),
            Fact(back_pain="no"),
            Fact(chest_pain="no"),
            Fact(cough="no"),
            Fact(fainting="no"),
            Fact(sore_throat="no"),
            Fact(fatigue="no"),
            Fact(restlessness="no"),
            Fact(low_body_temp="no"),
            Fact(fever="no"),
            Fact(sunken_eyes="no"),
            Fact(nausea="high"),
            Fact(blurred_vision="low"),
        )
        def disease_9(self):
            self.declare(Fact(disease="Glaucoma"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="no"),
            Fact(back_pain="no"),
            Fact(chest_pain="no"),
            Fact(cough="no"),
            Fact(fainting="no"),
            Fact(sore_throat="no"),
            Fact(fatigue="high"),
            Fact(restlessness="no"),
            Fact(low_body_temp="no"),
            Fact(fever="no"),
            Fact(sunken_eyes="no"),
            Fact(nausea="low"),
            Fact(blurred_vision="no"),
        )
        def disease_10(self):
            self.declare(Fact(disease="Hyperthyroidism"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="high"),
            Fact(back_pain="no"),
            Fact(chest_pain="no"),
            Fact(cough="no"),
            Fact(fainting="no"),
            Fact(sore_throat="no"),
            Fact(fatigue="no"),
            Fact(restlessness="no"),
            Fact(low_body_temp="no"),
            Fact(fever="high"),
            Fact(sunken_eyes="no"),
            Fact(nausea="high"),
            Fact(blurred_vision="no"),
        )
        def disease_11(self):
            self.declare(Fact(disease="Heat Stroke"))

        @Rule(
            Fact(action="find_disease"),
            Fact(headache="no"),
            Fact(back_pain="no"),
            Fact(chest_pain="no"),
            Fact(cough="no"),
            Fact(fainting="yes"),
            Fact(sore_throat="no"),
            Fact(fatigue="no"),
            Fact(restlessness="no"),
            Fact(low_body_temp="high"),
            Fact(fever="no"),
            Fact(sunken_eyes="no"),
            Fact(nausea="no"),
            Fact(blurred_vision="no"),
        )
        def disease_12(self):
            self.declare(Fact(disease="Hypothermia"))
        
        @Rule(
            Fact(action="find_disease"),
            Fact(headache="high"),
            Fact(back_pain="no"),
            Fact(chest_pain="high"),
            Fact(cough="high"),
            Fact(fainting="no"),
            Fact(sore_throat="high"),
            Fact(fatigue="high"),
            Fact(restlessness="no"),
            Fact(low_body_temp="no"),
            Fact(fever="high"),
            Fact(sunken_eyes="no"),
            Fact(nausea="no"),
            Fact(blurred_vision="no"),
        )
        def disease_13(self):
            self.declare(Fact(disease="Coronavirus"))

        #when the user's input doesn't match any disease in the knowledge base
        @Rule(Fact(action="find_disease"), Fact(disease=MATCH.disease), salience=-998)
        def disease(self, disease):
            id_disease = disease
            disease_details = self.get_details(id_disease)
            treatments = self.get_treatments(id_disease)
            messages.error(request, "Your symptoms match %s" % (id_disease))
            messages.error(request,"A short description of the disease is given below :")
            messages.error(request,disease_details + "")
            messages.error(request,
                "The common medications and procedures suggested by other real doctors are: "
            )
            messages.error(request, treatments + "\n")

        @Rule(
            Fact(action="find_disease"),
            Fact(headache=MATCH.headache),
            Fact(back_pain=MATCH.back_pain),
            Fact(chest_pain=MATCH.chest_pain),
            Fact(cough=MATCH.cough),
            Fact(fainting=MATCH.fainting),
            Fact(sore_throat=MATCH.sore_throat),
            Fact(fatigue=MATCH.fatigue),
            Fact(low_body_temp=MATCH.low_body_temp),
            Fact(restlessness=MATCH.restlessness),
            Fact(fever=MATCH.fever),
            Fact(sunken_eyes=MATCH.sunken_eyes),
            Fact(nausea=MATCH.nausea),
            Fact(blurred_vision=MATCH.blurred_vision),
            NOT(Fact(disease=MATCH.disease)),
            salience=-999
        )
        def not_matched(
            self,
            headache,
            back_pain,
            chest_pain,
            cough,
            fainting,
            sore_throat,
            fatigue,
            restlessness,
            low_body_temp,
            fever,
            sunken_eyes,
            nausea,
            blurred_vision,
        ):
            messages.error(request, "The bot did not find any diseases that match your exact symptoms.")
            # a = print("ffffffffffffffffffffffffffffffffffffffffffffffffffff")
            lis = [
                headache,
                back_pain,
                chest_pain,
                cough,
                fainting,
                sore_throat,
                fatigue,
                restlessness,
                low_body_temp,
                fever,
                sunken_eyes,
                nausea,
                blurred_vision,
            ]
            max_count = 0
            max_disease = ""
            for key, val in self.symptom_map.items():
                count = 0
                temp_list = eval(key)
                for j in range(0, len(lis)):
                    if temp_list[j] == lis[j] and (lis[j] == "high" or lis[j] == "low" or lis[j] == "yes"):
                        count = count + 1
                if count > max_count:
                    max_count = count
                    max_disease = val
            if max_disease != "":
                self.if_not_matched(max_disease)

   
    def if_not_matched(disease):
            id_disease = disease
            disease_details = get_details(id_disease)
            treatments = get_treatments(id_disease)
            messages.error( request,'The most probable disease that you have is %s' % (id_disease))
            messages.error(request, 'A short description of the disease is given below :\n')
            messages.error(request, disease_details + "\n")
            messages.error(request, 'The common medications and procedures suggested by other real doctors are:')
        
            messages.error(request,treatments + "\n")

    if request.method == 'GET' and 'btn' in request.GET: 
        preprocess()              
        #creating class object
        engine = Greetings(symptom_map, if_not_matched, get_treatments, get_details)
                            #loop to keep running the code until user says no when asked for another diagnosis             
        engine.reset()
        engine.run()
        
               # messages.error(request,"Would you like to diagnose some other symptoms?\n Reply yes or no")
      

    return render(request, 'index.html')

