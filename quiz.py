
class BancoQuestoes:

    _instance = None  
    def __init__(self):
        self.banco = self.banco
    
    #Singleton pra ler só uma vez o json
    def __new__(cls, *args, **kwargs):       
        if cls._instance is None:           
            cls._instance = super().__new__(cls)
        return cls._instance

    def lerJson():
       import json
       data = json.load(open('questoes.json'))    
       return data['questoes']
    
class Alternativa:
    # define o construtor:
    def __init__(self, codigo, alternativa, certa):        
        self.codigo = codigo
        self.alternativa = alternativa
        self.certa = certa

class Questao:
    # define o construtor:
    def __init__(self, codigo, questao, alternativas):
        # inicializa os atributos:
        self.codigo = codigo
        self.questao = questao
        self.alternativas = alternativas   

    def imprimirQuestao(self):
       print(f'Questão: {self.codigo} - {self.questao}')
       print('\n')
       print(f'Alternativas:')

       for alternativa in self.alternativas:
        print(f'({alternativa.codigo}) - {alternativa.alternativa}')
    
class QuestaoMatematica(Questao):
    
    def verificarResposta(self, resposta):        
       
        resposta_certa = ''

        for alt in self.alternativas:
           if alt.certa :
               resposta_certa = alt.codigo

        if resposta == resposta_certa :
             print('\nParabéns você acertou! \n')
        else : print(f'\nQue pena, você errou!! \n Respondeu {resposta}, a alternativa correta era: {resposta_certa}\n') 
        
class QuestaoGeografica(Questao):
   
    def verificarResposta(self, resposta):        
       
        resposta_certa = ''

        for alt in self.alternativas:
           if alt.certa :
               resposta_certa = alt.codigo

        if resposta == resposta_certa :
             print('\nParabéns você acertou! \n')
        else : print(f'\nQue pena, você errou!! \n A resposta certa era a: {resposta_certa}\n') 
               

from enum import Enum
class MateriaType(Enum): 
    MATEMATICA = 1
    GEOGRAFIA = 2

class MateriaFactory:

    #Factory para instanciar a questao por materia
    @staticmethod
    def create(materia_type: MateriaType, codigo, questao) -> Questao:
        if materia_type == MateriaType.MATEMATICA:
            return  QuestaoMatematica(codigo, questao, [])
        if materia_type == MateriaType.GEOGRAFIA:
            return QuestaoGeografica(codigo, questao, [])
            
        return None

#Strategy para verificar qual materia 
class Quiz:
    @staticmethod
    def quizPorMateria(materia: MateriaType, questoes):        

        if materia == MateriaType.MATEMATICA:           
           print("Voce escolheu o quiz de matematica.")
           for questao in questoes:
    
            if questao['materia'] == 1 : 
                
                quest = MateriaFactory.create(MateriaType.MATEMATICA, questao['codigo'], questao['questao'])
                
                for alt in questao['alternativas']:
                    alternativa = Alternativa(alt['codigo'], alt['alternativa'], alt['certa'])
                    quest.alternativas.append(alternativa) 

                print("\n")
                quest.imprimirQuestao()
                print("="*40)
                resposta = input("Digite sua resposta:")
                quest.verificarResposta(resposta)
                print("="*40)


        if materia == MateriaType.GEOGRAFIA:           
           
           print("Voce escolheu o quiz de geografia.")
           for questao in questoes:
    
            if questao['materia'] == 2 : 
                
                quest = MateriaFactory.create(MateriaType.GEOGRAFIA, questao['codigo'], questao['questao'])
                
                for alt in questao['alternativas']:
                    alternativa = Alternativa(alt['codigo'], alt['alternativa'], alt['certa'])
                    quest.alternativas.append(alternativa) 

                print("\n")
                quest.imprimirQuestao()
                print("="*40)
                resposta = input("Digite sua resposta:")
                quest.verificarResposta(resposta)
                print("="*40)

        else:
            return ('Não existe essa opção, quiz encerrado.')  

if __name__ == '__main__':
   
    questoes = BancoQuestoes.lerJson()
 
    print("[1] - Matematica \n[2] - Geografia")
    opcao = input("Escolha uma materia :")

    if(opcao == "1") :
        quizz = Quiz.quizPorMateria(MateriaType.MATEMATICA, questoes);
    elif (opcao == "2") :
        Quiz.quizPorMateria(MateriaType.GEOGRAFIA, questoes); 

    




