# %%
import matplotlib.pyplot as plt

#%%
##--------------------FLOW DISTRIBUTION-------------------##
##--------------------------------------------------------##

def flow_histogram(matrix, flow_type = None, path = None, n_bins = None, save = False):
    """
    Build the histogram and plot it through a scatter plot.
    """

    if n_bins:
        n,bins,patches = plt.hist(matrix, density=True, bins = n_bins, alpha=0.6)
    else:
        n,bins,patches = plt.hist(matrix, density=True, alpha=0.6)
    plt.show()

    if flow_type == 'U':
        plt.xlabel('$u_{i->0}$')
        plt.ylabel('P($u_{i->0}$)')
        plt.xlim([10,100000])
        plt.ylim([1e-6,1])
    elif flow_type == 'V':       
        plt.xlabel('$v_{0->i}$')
        plt.ylabel('P($v_{0->i}$)') 
        plt.xlim([10,100000]) 
        plt.ylim([1e-6,1])
    elif flow_type == 'F':       
        plt.xlabel('$f_{i->j}$')
        plt.ylabel('P($f_{i->j}$)') 
        plt.xlim([10,150000])   
        plt.ylim([1e-9,1])  
    elif flow_type == 'F_in':       
        plt.xlabel('$f_{.->i}$')
        plt.ylabel('P($f_{.->i}$)') 
        plt.xlim([10,1000000])   
        plt.ylim([1e-7,1])  
    elif flow_type == 'F_out':       
        plt.xlabel('$f_{i->.}$')
        plt.ylabel('P($f_{i->.}$)') 
        plt.xlim([10,1000000])   
        plt.ylim([1e-7,1])    
    elif flow_type == 'F15':       
        plt.xlabel('$f_{i->j}$')
        plt.ylabel('P($f_{i->j}$)') 
        plt.xlim([10,10000])   
        plt.ylim([1e-6,1])  
    elif flow_type == 'U15':
        plt.xlabel('$u_{i->0}$')
        plt.ylabel('P($u_{i->0}$)')
        plt.xlim([10,10000])
        plt.ylim([1e-5,1])
    elif flow_type == 'V15':
        plt.xlabel('$v_{0->i}$')
        plt.ylabel('P($v_{0->i}$)')
        plt.xlim([10,10000])
        plt.ylim([1e-5,1])
    
    n = n/sum(n)
    plt.xscale('log')
    plt.yscale('log')
    plt.scatter(bins[:-1]+ 0.5*(bins[1:] - bins[:-1]), n, marker='.', c='red', s=40, alpha=0.3)
    plt.grid()
    if save:
        plt.savefig(path + '/flow_distribution_'+str(flow_type)+'.png', dpi=1200)
    plt.show()
