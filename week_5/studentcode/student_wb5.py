# DO NOT change anything except within the function
from approvedimports import *

def cluster_and_visualise(datafile_name:str, K:int, feature_names:list):
    """Function to get the data from a file, perform K-means clustering and produce a visualisation of results.

    Parameters
        ----------
        datafile_name: str
            path to data file

        K: int
            number of clusters to use

        feature_names: list
            list of feature names

        Returns
        ---------
        fig: matplotlib.figure.Figure
            the figure object for the plot

        ax: matplotlib.axes.Axes
            the axes object for the plot
    """
    # ====> insert your code below here
    hist_col = plt.get_cmap('viridis', K).colors

    # get the data from file into a numpy array
    data = np.genfromtxt(datafile_name, delimiter=',')

    # create a K-Means cluster model with  the specified number of clusters
    cluster_model = KMeans(n_clusters=K, n_init=10)
    cluster_model.fit(data)
    cluster_ids = cluster_model.predict(data)


    # create a canvas(fig) and axes to hold your visualisation
    num_feat = len(feature_names)  
    fig, ax = plt.subplots(num_feat, num_feat, figsize=(15,15))


    # make the visualisation
    # remember to put your user name into the title as specified
    for feature1 in range(num_feat):
        for feature2 in range(num_feat):

            # Extract the data for the feature pairs
            x_data = data[:, feature1]
            y_data = data[:, feature2]

            if feature1 != feature2:
                ax[feature1, feature2].scatter(x_data, y_data, c=cluster_ids, cmap='viridis', s=50, edgecolors='k')
            else:

                inds = np.argsort(cluster_ids)
                y = cluster_ids[inds]
                x_data = x_data[inds]

                splits = np.split(x_data, np.unique(y, return_index=True)[1][1:])


                for i, split in enumerate(splits):
                    ax[feature1, feature2].hist(split, bins=20, color=hist_col[i], edgecolor='black')
    for i in range(num_feat):
        ax[-1, i].set_xlabel(feature_names[i], fontsize=12)  
        ax[i, 0].set_ylabel(feature_names[i], fontsize=12)

    fig.suptitle(f"Visualisation of {K} Clusters by Girish Shah", fontsize=16)

    # save it to file as specified
    fig.savefig("myVisualisation.jpg")


    # if you don't delete the line below there will be problem!

    return fig,ax

    # <==== insert your code above here
