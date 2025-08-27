import numpy as np
import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")
from sklearn.linear_model import LogisticRegression
from lightgbm import LGBMClassifier
from utils import MyTabNetClassifier, DatasetHelper
from cet import CounterfactualExplanationTree
from random_ce import RandomCE
from prototype_ce import PrototypeCE
from utils import Cost
import pandas as pd
import time

def demo_cet(dataset='t', model='X'):
    warnings.filterwarnings('ignore', message='X does not have valid feature names')
    np.random.seed(0)
    LAMBDA = 0.01
    GAMMA = 1.0

    D = DatasetHelper(dataset=dataset, feature_prefix_index=False)
    print('# CET Demonstration')
    print('* Dataset:', D.dataset_fullname)
    for d in range(D.n_features): print('\t* x_{:<2}: {} ({}{})'.format(d+1, D.feature_names[d], D.feature_types[d], ':'+D.feature_constraints[d] if D.feature_constraints[d]!='' else ''))
    # print(D.to_markdown())

    if(model=='L'):
        print('* Classifier: LogisticRegression')
        mdl = LogisticRegression(penalty='l2', C=1.0, solver='liblinear')
        print('\t* C: {}'.format(mdl.C)); print('\t* penalty: {}'.format(mdl.penalty));
    elif(model=='X'):
        print('* Classifier: LightGBM')
        mdl = LGBMClassifier(n_estimators=50, num_leaves=8)
        print('\t* n_estimators: {}'.format(mdl.n_estimators)); print('\t* num_leaves: {}'.format(mdl.num_leaves));
    elif(model=='T'):
        print('* Classifier: TabNet')
        mdl = MyTabNetClassifier(D.feature_types, verbose=0)

    X_tr, X_ts, y_tr, y_ts = D.train_test_split()
    mdl = mdl.fit(X_tr, y_tr, X_vl=X_ts, y_vl=y_ts) if model=='T' else mdl.fit(X_tr, y_tr)
    X = X_tr[mdl.predict(X_tr)==1]; X_vl = X_ts[mdl.predict(X_ts)==1];
    print('\t* train score: ', mdl.score(X_tr, y_tr)); print('\t* train denied: ', X.shape[0]); 
    print('\t* test score: ', mdl.score(X_ts, y_ts)); print('\t* test denied: ', X_vl.shape[0]); print();

    print('## Counterfactual Explanation Tree (CET)')
    cet = CounterfactualExplanationTree(mdl, X_tr, y_tr, max_iteration=50, lime_approximation=(model!='L'),
                                        feature_names=D.feature_names, feature_types=D.feature_types, feature_categories=D.feature_categories, 
                                        feature_constraints=D.feature_constraints, target_name=D.target_name, target_labels=D.target_labels)
    cet = cet.fit(X_vl, max_change_num=1, cost_type='MPS', C=LAMBDA, gamma=GAMMA, max_leaf_size=5, time_limit=60)
    print('* Parameters:'); print('\t* lambda: {}'.format(cet.lambda_)); print('\t* gamma: {}'.format(cet.gamma_)); print('\t* max_iteration: {}'.format(cet.max_iteration_));
    print('\t* leaf size bound:', cet.leaf_size_bound_); print('\t* LIME approximation:', cet.lime_approximation_); print('\t* leaf size:', cet.n_leaves_); print('\t* Time[s]:', cet.time_); print();
    print('### Learned CET')
    cet.print_tree()

def demo_random_ce(dataset='t', model='X'):
    warnings.filterwarnings('ignore', message='X does not have valid feature names')
    np.random.seed(0)

    D = DatasetHelper(dataset=dataset, feature_prefix_index=False)
    print('# RandomCE Demonstration')
    print('* Dataset:', D.dataset_fullname)
    for d in range(D.n_features):
        print('\t* x_{:<2}: {} ({}{})'.format(d+1, D.feature_names[d], D.feature_types[d], ':'+D.feature_constraints[d] if D.feature_constraints[d]!='' else ''))

    if(model=='L'):
        print('* Classifier: LogisticRegression')
        mdl = LogisticRegression(penalty='l2', C=1.0, solver='liblinear')
    elif(model=='X'):
        print('* Classifier: LightGBM')
        mdl = LGBMClassifier(n_estimators=50, num_leaves=8)
    elif(model=='T'):
        print('* Classifier: TabNet')
        mdl = MyTabNetClassifier(D.feature_types, verbose=0)

    X_tr, X_ts, y_tr, y_ts = D.train_test_split()
    mdl = mdl.fit(X_tr, y_tr, X_vl=X_ts, y_vl=y_ts) if model=='T' else mdl.fit(X_tr, y_tr)

    # Tạo feature_bounds cho RandomCE
    feature_bounds = {i: (float(np.min(X_tr[:, i])), float(np.max(X_tr[:, i]))) for i in range(X_tr.shape[1])}

    # Chọn một mẫu denied (bị từ chối) để test
    denied_idx = np.where(mdl.predict(X_ts) == 0)[0]
    if len(denied_idx) == 0:
        print("Không có mẫu bị từ chối trong tập test.")
        return
    x = X_ts[denied_idx[0]]

    ce = RandomCE(mdl, feature_bounds, max_iter=100)
    target_class = 1  
    x_cf = ce.generate(x, target_class)
    print("Original:", x)
    print("Counterfactual:", x_cf)

def demo_compare_methods(dataset='t', model='X'):
    warnings.filterwarnings('ignore', message='X does not have valid feature names')
    np.random.seed(0)
    LAMBDA = 0.01
    GAMMA = 1.0

    # Load dataset
    D = DatasetHelper(dataset=dataset, feature_prefix_index=False)
    print('# So sánh CET vs PrototypeCE vs RandomCE')
    print('* Dataset:', D.dataset_fullname)

    if(model=='L'):
        mdl = LogisticRegression(penalty='l2', C=1.0, solver='liblinear')
    elif(model=='X'):
        mdl = LGBMClassifier(n_estimators=50, num_leaves=8)
    elif(model=='T'):
        mdl = MyTabNetClassifier(D.feature_types, verbose=0)

    # Train / test
    X_tr, X_ts, y_tr, y_ts = D.train_test_split()
    mdl = mdl.fit(X_tr, y_tr, X_vl=X_ts, y_vl=y_ts) if model=='T' else mdl.fit(X_tr, y_tr)

    # Tập bị từ chối ở test
    X_vl = X_ts[mdl.predict(X_ts) == 1]
    if len(X_vl) == 0:
        print("Không có mẫu bị từ chối trong tập test.")
        return

    results = []
    cost_fn = Cost(X_tr, y_tr)

    # ================= CET =================
    start = time.time()
    cet = CounterfactualExplanationTree(
        mdl, X_tr, y_tr, max_iteration=50, lime_approximation=(model != 'L'),
        feature_names=D.feature_names, feature_types=D.feature_types, feature_categories=D.feature_categories,
        feature_constraints=D.feature_constraints, target_name=D.target_name, target_labels=D.target_labels
    )
    cet = cet.fit(X_vl, max_change_num=1, cost_type='MPS', C=LAMBDA, gamma=GAMMA, max_leaf_size=5, time_limit=60)
    end = time.time()

    A_cet = cet.predict(X_vl)
    cost = np.array([cost_fn.compute(x, a) for x, a in zip(X_vl, A_cet)]).mean()
    loss = (mdl.predict(X_vl + A_cet) != 0).mean()
    results.append({"Method": "CET", "Cost": cost, "Loss": loss, "g(a|x)": cost + GAMMA * loss, "Time[s]": end-start})

    # ================= PrototypeCE =================
    start = time.time()
    proto = PrototypeCE(mdl, X_tr, y_tr)
    A_proto = []
    for x in X_vl:
        cf = proto.generate(x, target_class=0)
        if cf is None:
            A_proto.append(np.zeros_like(x))
        else:
            A_proto.append(cf - x)
    end = time.time()

    A_proto = np.array(A_proto)
    cost = np.array([cost_fn.compute(x, a) for x, a in zip(X_vl, A_proto)]).mean()
    loss = (mdl.predict(X_vl + A_proto) != 0).mean()
    results.append({"Method": "PrototypeCE", "Cost": cost, "Loss": loss, "g(a|x)": cost + GAMMA * loss, "Time[s]": end-start})

    # ================= RandomCE =================
    start = time.time()
    feature_bounds = {j: (X_tr[:, j].min(), X_tr[:, j].max()) for j in range(X_tr.shape[1])}
    rand = RandomCE(mdl, feature_bounds)

    A_rand = []
    for x in X_vl:
        cf = rand.generate(x, target_class=0)
        if cf is None:
            A_rand.append(np.zeros_like(x))
        else:
            A_rand.append(cf - x)
    end = time.time()

    A_rand = np.array(A_rand)
    cost = np.array([cost_fn.compute(x, a) for x, a in zip(X_vl, A_rand)]).mean()
    loss = (mdl.predict(X_vl + A_rand) != 0).mean()
    results.append({"Method": "RandomCE", "Cost": cost, "Loss": loss, "g(a|x)": cost + GAMMA * loss, "Time[s]": end-start})

    # ================= Xuất kết quả =================
    df = pd.DataFrame(results)
    print(df.to_string(index=False))
    return df

if(__name__ == '__main__'):
    demo_cet(model='X')
    #demo_random_ce(model='X')
    demo_compare_methods(model='X')