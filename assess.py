import xlrd
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.metrics import f1_score, fbeta_score
from sklearn.metrics import hamming_loss
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import jaccard_score
from sklearn.metrics import hinge_loss

work_book=xlrd.open_workbook_xls('1_total.xls')
sheets=work_book.sheets()
sheets_name=work_book.sheet_names()
sheet_1=work_book.sheet_by_index(0)

predict=[]
level=[]
rows=sheet_1.get_rows()
x=0
for row in rows:
    if x<2:
        x+=1
        continue
    predict.append(str(row[9]))
    level.append(str(row[8]))
print(predict)
print(level)

y_true=level
y_pred=predict

kappa = cohen_kappa_score(y_true,y_pred)
ham_distance = hamming_loss(y_true,y_pred)
jaccrd_score = jaccard_score(y_true,y_pred,average=None)


#hinger = hinge_loss(y_true,y_pred)
#print(kappa)
#print(ham_distance)

predict_p=[]
level_p=[]
for i in predict:
    if i == "text:'P3'":
        predict_p.append(str("3"))
    elif i=="text:'P2'":
        predict_p.append(str("1"))
    elif i=="text:'P2+P3'":
        predict_p.append(str("1"))
    elif i=="text:'P1'":
        predict_p.append(str("0"))
    elif i=="text:'P4'":
        predict_p.append(str("4"))
    else:
        predict_p.append(str("0"))

for i in level:
    if i == "text:'P3'":
        level_p.append(str("3"))
    elif i=="text:'P2'":
        level_p.append(str("1"))
    elif i=="text:'P2+P3'":
        level_p.append(str("1"))
    elif i=="text:'P1'":
        level_p.append(str("0"))
    elif i=="text:'P4'":
        level_p.append(str("4"))
    else:
        level_p.append(str("0"))

y_true_p=level_p
y_pred_p=predict_p

#print(level_p)
#print(predict_p)
kappa = cohen_kappa_score(y_true_p,y_pred_p)
ham_distance = hamming_loss(y_true_p,y_pred_p)
jaccrd_score = jaccard_score(y_true,y_pred,average=None)

#hinger = hinge_loss(y_true,y_pred)
print(kappa)
print(ham_distance)

a=accuracy_score(y_true_p, y_pred_p) # Return the number of correctly classified samples
n=accuracy_score(y_true_p, y_pred_p, normalize=False) # Return the fraction of correctly classified samples
print(n,a)
print(f1_score(y_true_p, y_pred_p, average='micro'))
print(fbeta_score(y_true, y_pred, average='micro', beta=0.5))


'''
# Calculate precision score
precision_score(y_true, y_pred, average='macro')
precision_score(y_true, y_pred, average='micro')
print(precision_score(y_true, y_pred, average=None))


# Calculate recall score
print(recall_score(y_true, y_pred, average='macro'))
print(recall_score(y_true, y_pred, average='micro'))
print(recall_score(y_true, y_pred, average=None))

# Calculate f1 score
print(f1_score(y_true, y_pred, average='macro'))
print(f1_score(y_true, y_pred, average='micro'))
print(f1_score(y_true, y_pred, average=None))

# Calculate f beta score
fbeta_score(y_true, y_pred, average='macro', beta=0.5)
fbeta_score(y_true, y_pred, average='micro', beta=0.5)
print(fbeta_score(y_true, y_pred, average=None, beta=0.5))
'''
