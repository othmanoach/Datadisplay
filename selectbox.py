from chart import *


def chose(type_chart, data, x, y):
    """cases of selectbox"""
    match type_chart:
        case "Histogram":
            histogram(data, x, y)
        # ------------------------------------------------------------------------
        case "Pie":
            pie(data, x, y)
        # ------------------------------------------------------------------------
        case "Line plot":
            line_plot(data, x, y)
        case "Scatter plot":
            scatter_chart(data, x, y)
        # ------------------------------------------------------------------------
        case "Boxplot":
            boxplot(data, x, y)
        case "Bar plot":
            bar_plot(data, x, y)
        case "KDE plot":
            kde_plot(data, x, y)
        case "Violin plot":
            violin_plot(data, x, y)
        case "Heatmap":
            heatmap(data, x, y)


def mean(df,x):
    s=0
    x_dtype = df[x].dtype
    if x_dtype != "object":
            for i in df[x]:
                print(i)
                s = s+i
            s = s/len(df[x])
            st.write("Mean of ",x,":",s)

