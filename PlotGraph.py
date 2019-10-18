import matplotlib.pyplot as plt

def plot_graph(graph, title='', doplot=False):
    '''plot a graph (nodes, edges), add title'''
    def _new_graph_plot(subplots=1, fig_size=(8,6), grid=True):
        '''create a plot of fig_size big. Possibly mult subplots'''
        fig, ax = plt.subplots((subplots), figsize=fig_size)
        ax = plt.subplot(111)
        ax.grid(grid)
        ax.set_title(title)
        return fig, ax

    def _plot_node(fig, ax, x, y, node_sym = 'o', color_str = 'k', node_lbl='', lbl=True):
        '''draw nodes at coords specified, using color string'''
        ax.plot([x], [y], color=color_str, marker=node_sym, markersize=10 )
        if lbl:
            ax.annotate(node_lbl,(x+.05,y+.05)) 
            
    def _plot_di_edge(fig, ax, x0, y0, x1, y1, w, lw=2.):
        """plot directed edge as an arrow"""
        ax.arrow(x0, y0, x1-x0, y1-y0, \
                  head_starts_at_zero=False, head_width=0.1, \
                  edgecolor='red', facecolor='red', \
                  linewidth=lw, \
                  shape='full', length_includes_head=True)
        ax.annotate(w, ((x0+x1)/2. - 0.1, (y0+y1)/2. + 0.08), color='red')

    def _plot_edge(fig, ax, x0, y0, x1, y1, w, lw=2.):
        """plot undirected edge"""
        X, Y = [x0, x1], [y0, y1]
        ax.plot(X, Y, 'r-', linewidth=lw)
        ax.annotate(w, ((x0+x1)/2. - 0.1, (y0+y1)/2. + 0.08), color='red')

    # do not try to plot a None graph ...
    if graph is None:
        return

    # start creating a new figure ...    
    fig, ax = _new_graph_plot(subplots=1, fig_size=(8,6))

    # ... now plot the edge list of each node ...
    for node in graph.nodes():
        node_pos = graph.vtx_dict[node]['pos']
        node_col = graph.vtx_dict[node]['color']                 
        # go around vertex (i.e., down the adj wieght dict)
        # and plot edges plus node ...
        for nbor in graph.edges(node):
            # ... find pos of connected node ...
            weight = graph.adj_dict[node][nbor]
            nbor_pos = graph.vtx_dict[nbor]['pos']
            if graph.directed:
                _plot_di_edge(fig, ax, \
                    node_pos[0], node_pos[1], nbor_pos[0], nbor_pos[1], weight )
            else:
                _plot_edge(fig, ax, \
                    node_pos[0], node_pos[1], nbor_pos[0], nbor_pos[1], weight )
               
    # for a clear image ... 'overwrite' edge tips with nodes ...
    for node in graph.nodes():
        node_pos = graph.vtx_dict[node]['pos']
        node_col = graph.vtx_dict[node]['color']
        _plot_node(fig, ax, node_pos[0], node_pos[1], 
                   node_sym ='o', color_str = node_col, 
                   node_lbl = str(node), lbl=True)
        
    if doplot:
        plt.savefig('my_graph.pdf', orientation='landscape')