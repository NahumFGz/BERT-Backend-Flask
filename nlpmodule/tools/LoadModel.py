import torch

#def bert_classifier(path='/home/ubuntu/BERT-Backend-Flask/nlpmodule/weights/NewPreprocesing_MDLBETO_BLCnormal_TS0.2_RS2020_epch10_lr5e-05_model1.pth'):
#def bert_classifier(path='./nlpmodule/weights/Twitter_model1.pth'):
def bert_classifier(path='./nlpmodule/weights/NewPreprocesing_MDLBETO_BLCnormal_TS0.2_RS2020_epch10_lr5e-05_model1.pth'):
#def bert_classifier(path='./nlpmodule/weights/AllHaterNetAnd20_24_MDLBETO_BLCnormal_TS0.2_RS2020_epch10_lr5e-05_model1.pth'):
    return torch.load(path, map_location='cpu')