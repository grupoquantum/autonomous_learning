from Neuraline.ArtificialIntelligence.MachineLearning.AutonomousLearning.markov_chain import MarkovChain
markov_chain = MarkovChain()

markov_chain.loadModel('markov_chain_modelo_musical')
result = markov_chain.markovAudioGenerator(url_path='nova_musica.wav', vary=True, progress=True)
print(result)
