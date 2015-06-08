'''
Setting up folder and file dirs, and method name

Authors: Junhua Mao <mjhustc@ucla.edu>
'''
import os

class Conf_Cr:
    def __init__(self):
        # Settings for image features
        self.fol_image_feat = './image_features_mRNN'
        self.name_feat = 'mRNN_refine'
        self.dim_image_feat = 1024
        self.fname_dct_feat = os.path.join(self.fol_image_feat, \
            'VGG_feat_%s_dct_mscoco_2014.npy' % self.name_feat)
        
        # Settings for annotation list file
        self.fol_anno_list = './mscoco_anno_files'
        self.fname_anno_list_ref = os.path.join(self.fol_anno_list, \
            'anno_list_mscoco_trainModelVal_m_RNN.npy')
            
        # Settings for hypotheses annotation list file
        self.fol_hypo_list = './hypotheses_mRNN'
        self.name_tar_data = 'crVal'
        self.fname_hypo_list = os.path.join(self.fol_hypo_list, \
            'anno_list_mscoco_%s_m_RNN_beamsearch10.npy' % self.name_tar_data)
        # self.fname_hypo_list = os.path.join(self.fol_hypo_list, 'test_20_genS.npy') # DEBUG
        self.gen_method = 'gen_beam_search_10'
        
        # Settings for hyperparamters (validated on crVal)
        # See more details of them in the paper
        self.distance_metric = 'euclidean'
        self.k_cider = 60
        self.m_cider = 125
        self.k_bleu = 60
        self.m_bleu = 175
        self.fpr_bleu = 1.0
        self.bleu_ngram = 4
        
        # Memory settings
        self.num_NNimg = 1000 # Only keep neatest num_NNimg images
        self.del_useless = True # Delete useless memory
        self.cal_distance_all = False # Setting this to True will accelerate the process
                                      # But requires much more memory
        
        # Cache settings
        self.name_cache = 'm_RNN'
        self.fol_root_cache = './cache'
        
        # Debug settings
        self.num_show_finished = 200
        
        # Evaluation settings
        self.fol_coco_eval = './external/coco-caption'
        self.fname_eval_ref = os.path.join(self.fol_coco_eval, \
            'annotations', 'captions_val2014.json')
