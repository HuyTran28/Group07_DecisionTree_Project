import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

MODEL = {'T': 'TabNet', 'X':'LightGBM'}
DATASET = {'i':'attrition', 'g':'german', 'd': 'diabetes'}
DATASETNAME = {'i':'Attrition', 'g':'German', 'd':'Diabetes'}
METHODS = {'clustering':'Clustering', 'ares':'AReS', 'cet':'CET', 'prototype':'Prototype CE', 'random':'Random CE'}
MARKER = {'clustering':'v', 'ares':'s', 'cet':'o', 'prototype':'^', 'random':'d'}


def latex_compare(model='T', datasets=['i','g'], l=0.02, g=1.0, methods=None):
    if methods is None:
        methods = ['clustering', 'ares', 'cet']
    
    filenames = [ ['../results/compare/{}/{}_{}_{}_{}.csv'.format(model, method, DATASET[dataset], l, g) for method in methods] for dataset in datasets ]
    
    # Create output directory and file
    os.makedirs('../../01_Report/tables', exist_ok=True)
    method_suffix = '_'.join(methods) if len(methods) != 3 else ''
    output_file = '../../01_Report/tables/compare_{}_{}_{}_complete.tex'.format(MODEL[model], '_'.join([DATASET[d] for d in datasets]), method_suffix).replace('__', '_').rstrip('_')
    
    latex_content = []
    
    # Begin table
    latex_content.append(r'\begin{table}[htbp]')
    latex_content.append(r'\centering')
    latex_content.append(r'\caption{Performance Comparison for ' + MODEL[model] + r' Model}')
    latex_content.append(r'\label{tab:compare_' + model.lower() + '}')
    
    # Define column alignment
    num_cols = 1 + 6  # Method column + 6 metric columns
    col_align = 'l' + 'c' * 6
    latex_content.append(r'\begin{tabular}{' + col_align + '}')
    latex_content.append(r'\toprule')
    
    # Header
    header = r'Method & \multicolumn{2}{c}{Cost} & \multicolumn{2}{c}{Loss} & \multicolumn{2}{c}{Objective} \\'
    latex_content.append(header)
    latex_content.append(r'\cmidrule(lr){2-3} \cmidrule(lr){4-5} \cmidrule(lr){6-7}')
    latex_content.append(r' & Train & Test & Train & Test & Train & Test \\')
    latex_content.append(r'\midrule')
    
    for i, dataset in enumerate(datasets):
        if len(datasets) > 1:
            latex_content.append(r'\multicolumn{' + str(num_cols) + r'}{c}{\textbf{' + DATASETNAME[dataset] + r' Dataset}} \\')
            latex_content.append(r'\midrule')
        
        for j, method in enumerate(methods):
            df = pd.read_csv(filenames[i][j])
            s = METHODS[method]
            for key1 in ['train', 'test']:
                for key2 in ['cost', 'loss', 'obj']:
                    mean_val = df['{}_{}'.format(key2, key1)].mean()
                    std_val = df['{}_{}'.format(key2, key1)].std()
                    s += r' & {:.3f} $\pm$ {:.2f}'.format(mean_val, std_val)
            s += r' \\'
            latex_content.append(s)
        
        if i < len(datasets) - 1:
            latex_content.append(r'\midrule')
    
    # End table
    latex_content.append(r'\bottomrule')
    latex_content.append(r'\end{tabular}')
    latex_content.append(r'\end{table}')
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(latex_content))
    print(f"Complete LaTeX table saved to: {output_file}")

latex_compare(model='X', datasets=['i'], l=0.02, g=1.0)

def latex_compare_time(models=['X','T'], datasets=['i','g'], l=0.02, g=1.0, methods=None):
    if methods is None:
        methods = ['clustering', 'ares', 'cet']
    
    filenames = [ [ ['../results/compare/{}/{}_{}_{}_{}.csv'.format(model, method, DATASET[dataset], l, g) for method in methods] for dataset in datasets ] for model in models]
    average = [0] * len(methods)
    
    # Create output directory and file
    os.makedirs('../../01_Report/tables', exist_ok=True)
    method_suffix = '_'.join(methods) if len(methods) != 3 else ''
    output_file = '../../01_Report/tables/compare_time_{}_{}{}_complete.tex'.format('_'.join([MODEL[m] for m in models]), '_'.join([DATASET[d] for d in datasets]), '_' + method_suffix if method_suffix else '')
    
    latex_content = []
    
    # Begin table
    latex_content.append(r'\begin{table}[htbp]')
    latex_content.append(r'\centering')
    latex_content.append(r'\caption{Runtime Comparison (seconds)}')
    latex_content.append(r'\label{tab:runtime_comparison}')
    
    # Define column alignment
    num_cols = 1 + len(methods)
    col_align = 'l' + 'c' * len(methods)
    latex_content.append(r'\begin{tabular}{' + col_align + '}')
    latex_content.append(r'\toprule')
    
    # Header
    header = r'Dataset & ' + ' & '.join([METHODS[method] for method in methods]) + r' \\'
    latex_content.append(header)
    latex_content.append(r'\midrule')
    
    for k, model in enumerate(models):
        if len(models) > 1:
            latex_content.append(r'\multicolumn{' + str(num_cols) + r'}{c}{\textbf{' + MODEL[model] + r' Model}} \\')
            latex_content.append(r'\midrule')
        
        for i, dataset in enumerate(datasets):
            s = DATASETNAME[dataset]
            for j, method in enumerate(methods):
                df = pd.read_csv(filenames[k][i][j])
                mean_time = df['time'].mean()
                std_time = df['time'].std()
                s += r' & {:.4f} $\pm$ {:.4f}'.format(mean_time, std_time)
                average[j] += mean_time / (len(models) * len(datasets))
            s += r' \\'
            latex_content.append(s)
        
        if k < len(models) - 1:
            latex_content.append(r'\midrule')
    
    # Add average row
    latex_content.append(r'\midrule')
    average_line = r'Average & ' + ' & '.join(['{:.4f}'.format(avg) for avg in average]) + r' \\'
    latex_content.append(average_line)
    
    # End table
    latex_content.append(r'\bottomrule')
    latex_content.append(r'\end{tabular}')
    latex_content.append(r'\end{table}')
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(latex_content))
    print(f"Complete LaTeX runtime table saved to: {output_file}")

# Example usage
# latex_compare_complete(model='X', datasets=['i'], l=0.02, g=1.0)
# latex_compare_time_complete()


def plot_sens_comp(model='L', datasets=['i','g'], gamma=1.0, methods=None):
    if methods is None:
        methods = ['clustering', 'ares', 'cet']
    
    plt.rcParams["font.family"] = 'arial'
    plt.rcParams['text.usetex'] = False
    plt.figure(figsize=(8,4))
    for i, dataset in enumerate(datasets):
        plt.subplot(2, 2, (i+1))
        plt.title(DATASETNAME[dataset], fontsize=16)
        for method in methods:
            df = pd.read_csv('../results/complexity/{}/{}_{}_{}.csv'.format(model, method, DATASET[dataset], gamma))
            plt.plot(df['n_actions'], df['cost_test'], marker=MARKER[method], label='{}'.format(METHODS[method]))
        plt.xlabel(r'\#Actions', fontsize=14); plt.ylabel('Cost (test)', fontsize=14); plt.xticks([4,8,12,16,20], fontsize=12); plt.yticks(fontsize=12); plt.tight_layout(); 
        # if(i==0): plt.legend()
        plt.subplot(2, 2, i+3)
        for method in methods:
            df = pd.read_csv('../results/complexity/{}/{}_{}_{}.csv'.format(model, method, DATASET[dataset], gamma))
            plt.plot(df['n_actions'], df['loss_test'], marker=MARKER[method], label='{}'.format(METHODS[method]))
        plt.xlabel(r'\#Actions', fontsize=14); plt.ylabel('Loss (test)', fontsize=14); plt.xticks([4,8,12,16,20], fontsize=12); plt.yticks(fontsize=12); plt.tight_layout(); 
        if(i==1): plt.legend(fontsize=12)

    method_suffix = '_'.join(methods) if len(methods) != 3 else ''
    os.makedirs('../../01_Report/figures/complexity/{}'.format(model), exist_ok=True)
    plt.savefig('../../01_Report/figures/complexity/{}/tradeoff{}.png'.format(model, '_' + method_suffix if method_suffix else ''), bbox_inches='tight', pad_inches=0.05)
    plt.savefig('../../01_Report/figures/complexity/{}/tradeoff{}.pdf'.format(model, '_' + method_suffix if method_suffix else ''), bbox_inches='tight', pad_inches=0.05)
    plt.clf()

plot_sens_comp(model='L', datasets=['i'], gamma=1.0)  
plot_sens_comp(model='X', datasets=['i'], gamma=1.0)


def plot_sens_comp_pareto_frontier(model='L', datasets=['i', 'g'], gamma=1.0, methods=None):
    if methods is None:
        methods = ['clustering', 'ares', 'cet']
    
    plt.rcParams["font.family"] = 'arial'
    plt.rcParams['text.usetex'] = False
    plt.figure(figsize=(8,2.75))

    for i, dataset in enumerate(datasets):
        plt.subplot(1, 2, (i+1))
        plt.title(DATASETNAME[dataset], fontsize=16)
        for method in methods:
            df = pd.read_csv('../results/complexity/{}/{}_{}_{}.csv'.format(model, method, DATASET[dataset], gamma))
            plt.scatter(df['cost_test'], df['loss_test'], marker=MARKER[method], label='{}'.format(METHODS[method]), s=75, linewidth=0.5, edgecolor='black')
            for n, (x,y) in zip(df['n_actions'], zip(df['cost_test'], df['loss_test'])):
                text_fontsize=12
                offset = 0.004
                if(dataset=='i'):
                    if(method=='ares' and n==4):
                        plt.text(x-offset, y-0.002, "{}".format(n), horizontalalignment='right', verticalalignment='top', fontsize=text_fontsize)
                    elif(method=='ares' and n==8):
                        plt.text(x-offset, y+0.06, "{}".format(n), horizontalalignment='right', verticalalignment='top', fontsize=text_fontsize)
                    elif(method=='ares' and n==12):
                        plt.text(x-offset, y+0.03, "{}".format(n), horizontalalignment='right', verticalalignment='top', fontsize=text_fontsize)
                    elif(method=='ares' and n==16):
                        plt.text(x-offset, y, "{}".format(n), horizontalalignment='right', verticalalignment='top', fontsize=text_fontsize)
                    elif(method=='ares' and n==20):
                        plt.text(x-offset, y-0.03, "{}".format(n), horizontalalignment='right', verticalalignment='top', fontsize=text_fontsize)
                    elif(method=='cet' and n==4):
                        plt.text(x+offset, y-offset, "{}".format(n), horizontalalignment='left', verticalalignment='top', fontsize=text_fontsize)
                    elif(method=='cet' and n==11):
                        plt.text(x-offset, y+offset, "{}".format(n), horizontalalignment='right', verticalalignment='bottom', fontsize=text_fontsize)
                    elif(method=='cet' and n==16):
                        plt.text(x+offset, y-offset, "{}".format(n), horizontalalignment='left', verticalalignment='top', fontsize=text_fontsize)
                    else:
                        plt.text(x-offset, y-offset, "{}".format(n), horizontalalignment='right', verticalalignment='top', fontsize=text_fontsize)
                if(dataset=='g'):
                    if(method=='ares' and n==4):
                        plt.text(x-offset, y+offset, "{}".format(n), horizontalalignment='right', verticalalignment='bottom', fontsize=text_fontsize)
                    elif(method=='ares' and n==8):
                        plt.text(x+offset, y-offset, "{}".format(n), horizontalalignment='left', verticalalignment='top', fontsize=text_fontsize)
                    elif(method=='ares' and n==12):
                        plt.text(x-offset, y+0.05, "{}".format(n), horizontalalignment='right', verticalalignment='top', fontsize=text_fontsize)
                    elif(method=='cet' and n==4):
                        plt.text(x-offset, y+offset, "{}".format(n), horizontalalignment='right', verticalalignment='bottom', fontsize=text_fontsize)
                    elif(method=='cet' and n==8):
                        plt.text(x+offset, y+offset, "{}".format(n), horizontalalignment='left', verticalalignment='bottom', fontsize=text_fontsize)
                    elif(method=='cet' and n==16):
                        plt.text(x+offset, y+offset, "{}".format(n), horizontalalignment='left', verticalalignment='bottom', fontsize=text_fontsize)
                    elif(method=='cet' and n==19):
                        plt.text(x+offset, y-offset, "{}".format(n), horizontalalignment='left', verticalalignment='top', fontsize=text_fontsize)
                    else:
                        plt.text(x-offset, y-offset, "{}".format(n), horizontalalignment='right', verticalalignment='top', fontsize=text_fontsize)
        plt.xlabel('Cost (test)', fontsize=14); plt.ylabel('Loss (test)', fontsize=14); 
        if(dataset=='i'): plt.xlim(left=0.215); 
        if(dataset=='g'): plt.xlim(left=0.03); 
        plt.xticks(fontsize=12); plt.yticks(fontsize=12); plt.tight_layout(); 
        if(i==1): plt.legend(fontsize=12)

    method_suffix = '_'.join(methods) if len(methods) != 3 else ''
    os.makedirs('../../01_Report/figures/complexity/{}'.format(model), exist_ok=True)
    plt.savefig('../../01_Report/figures/complexity/{}/tradeoff_pareto{}.png'.format(model, '_' + method_suffix if method_suffix else ''), bbox_inches='tight', pad_inches=0.05)
    plt.savefig('../../01_Report/figures/complexity/{}/tradeoff_pareto{}.pdf'.format(model, '_' + method_suffix if method_suffix else ''), bbox_inches='tight', pad_inches=0.05)
    plt.clf()

plot_sens_comp_pareto_frontier(model='L', datasets=['i'], gamma=1.0)
plot_sens_comp_pareto_frontier(model='X', datasets=['i'], gamma=1.0)


def plot_sens_comp_all(model='L', dataset='i', gamma=1.0, methods=None):
    if methods is None:
        methods = ['clustering', 'ares', 'cet']
    
    plt.rcParams["font.family"] = 'arial'
    plt.rcParams['text.usetex'] = False
    plt.figure(figsize=(10,4))
    for j, key2 in enumerate(['train', 'test']):
        for i, key1 in enumerate(['cost', 'loss', 'obj']):
            plt.subplot(2, 3, i + j*3 + 1)
            for method in methods:
                df = pd.read_csv('../results/complexity/{}/{}_{}_{}.csv'.format(model, method, DATASET[dataset], gamma))
                plt.plot(df['n_actions'], df[key1+'_'+key2], marker=MARKER[method], label='{}'.format(METHODS[method]))
            plt.xlabel(r'\#Actions'); plt.ylabel('{} ({})'.format('Invalidity' if key1=='obj' else key1.capitalize(), key2)); plt.xticks([4,8,12,16,20]); plt.tight_layout(); 
            if(i==1 and j==0): plt.legend()
    
    method_suffix = '_'.join(methods) if len(methods) != 3 else ''
    os.makedirs('../../01_Report/figures/complexity/{}'.format(model), exist_ok=True)
    plt.savefig('../../01_Report/figures/complexity/{}/tradeoff_{}{}.png'.format(model, DATASET[dataset], '_' + method_suffix if method_suffix else ''), bbox_inches='tight', pad_inches=0.05)
    plt.savefig('../../01_Report/figures/complexity/{}/tradeoff_{}{}.pdf'.format(model, DATASET[dataset], '_' + method_suffix if method_suffix else ''), bbox_inches='tight', pad_inches=0.05)
    plt.clf()

plot_sens_comp_all(model='L', dataset='i', gamma=1.0)
plot_sens_comp_all(model='X', dataset='i', gamma=1.0)


def plot_sens_gamma(model='L', datasets=['i','g'], gammas=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]):
    plt.rcParams["font.family"] = 'arial'
    plt.rcParams['text.usetex'] = False
    plt.figure(figsize=(8,2.5))
    for i, dataset in enumerate(datasets):
        plt.subplot(1, 2, i+1)
        plt.title(DATASETNAME[dataset])
        df = pd.read_csv('../results/gamma/{}/sensitivity_{}.csv'.format(model, DATASET[dataset]))
        plt.plot(gammas, [df[df['gamma']==g]['cost'].mean() for g in gammas], marker='o', label=r'cost $c(a \mid x)$ (MPS)')
        plt.plot(gammas, [df[df['gamma']==g]['loss'].mean() for g in gammas], marker='s', label=r'loss $l(f(x+a), +1)$')
        plt.xlabel(r'$\gamma$')
        if(i==0): plt.legend()
        plt.tight_layout()
    
    os.makedirs('../../01_Report/figures/gamma/{}'.format(model), exist_ok=True)
    plt.savefig('../../01_Report/figures/gamma/{}/sensitivity.png'.format(model), bbox_inches='tight', pad_inches=0.05)
    plt.savefig('../../01_Report/figures/gamma/{}/sensitivity.pdf'.format(model), bbox_inches='tight', pad_inches=0.05)
    plt.clf()

plot_sens_gamma(model='L', datasets=['i','g'])

def plot_sens_conv(model='L', dataset='g', gammas=[0.75, 1.0, 1.25], lambdas=[0.01, 0.03, 0.05]):
    plt.rcParams["font.family"] = 'arial'
    plt.rcParams['text.usetex'] = False
    if(len(lambdas)==1):
        plt.figure(figsize=(6,6))
        res_name = '../../01_Report/figures/convergence/{}/convergence_{}_partial'.format(model, DATASET[dataset])
    else:
        plt.figure(figsize=(14,7))
        res_name = '../../01_Report/figures/convergence/{}/convergence_{}'.format(model, DATASET[dataset])
    for i, g in enumerate(gammas):
        for j, l in enumerate(lambdas):
            plt.subplot(len(gammas), len(lambdas), i*len(lambdas) + j + 1)
            plt.title(r'$\gamma={}$, $\lambda={}$'.format(g,l))
            df = pd.read_csv('../results/convergence/{}/cet_{}_objective_{}_{}.csv'.format(model, DATASET[dataset], l, g))
            plt.plot(df['Iteration'], df['obj'], label=r'$t$-th objective value $o_{\gamma, \lambda}(h^{(t)})$')
            plt.plot(df['Iteration'], df['obj_bound'], label=r'Best objective value $o_{\gamma, \lambda}(h^{*})$')
            plt.xlabel(r'Iteration $t$'); plt.ylabel(r'Objective value $o_{\gamma, \lambda}(h)$')
            plt.tight_layout()
            if(i==0 and j==0): plt.legend()
            plt.tight_layout()
    
    os.makedirs('../../01_Report/figures/convergence/{}'.format(model), exist_ok=True)
    plt.savefig(res_name+'.png', bbox_inches='tight', pad_inches=0.05)
    plt.savefig(res_name+'.pdf', bbox_inches='tight', pad_inches=0.05)
    plt.clf()

plot_sens_conv(model='L', dataset='g', gammas=[0.75], lambdas=[0.01, 0.03, 0.05])
# plot_sens_conv(dataset='g', gammas=[0.75], lambdas=[0.01, 0.03, 0.05])
# plot_sens_conv(dataset='i', gammas=[0.75, 1.0, 1.25], lambdas=[0.01, 0.03, 0.05])

