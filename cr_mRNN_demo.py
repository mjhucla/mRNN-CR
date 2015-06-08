from concensus_reranking_utils.consensus_reranking import Consensus_Reranking

# Create an CR class
cr_mRNN = Consensus_Reranking()
# Load anno file list
cr_mRNN.load_anno_ref_hypo()
# Find NN image
cr_mRNN.find_NNimg()
# Consensus Rerank
cr_mRNN.consensus_rerank(method='bleu')
cr_mRNN.consensus_rerank(method='cider')
