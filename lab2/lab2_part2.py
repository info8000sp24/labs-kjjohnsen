import marimo

__generated_with = "0.1.86"
app = marimo.App()


@app.cell
def __():
    # Kyle Johnsen
    # Lab 2 Part 2

    import marimo as mo
    import matplotlib.pyplot as plt
    return mo, plt


@app.cell
def __():
    # part A
    f = open('data.txt')
    lines = f.readlines()
    data = [int(l) for l in lines]
    print(data[:5])
    print(data[-5:])
    return data, f, lines


@app.cell
def __(data):
    # Part B
    N = len(data)//2 # actually only len/2 points
    x_values = data[:N] # first half
    y_values = data[-N:] # second half
    print(x_values[11::-1]) # print in reverse
    print(y_values[11::-1])
    return N, x_values, y_values


@app.cell
def __(plt, x_values, y_values):
    # Part C
    # Draw Traingles
    for start in range(0,len(x_values),4): # each triangle is 4 points
        triangle_x = x_values[start:start+4] 
        triangle_y = y_values[start:start+4]
        plt.plot(triangle_x,triangle_y)
    plt.show() # must call this to get a plot to show and a new one to start  

    # Part D
    # Highlight Invalid Triangles
    for start in range(0,len(x_values),4): 
        triangle_x = x_values[start:start+4] 
        triangle_y = y_values[start:start+4]
        # They are invalid if the first and last don't line up
        if triangle_x[0] != triangle_x[-1] and triangle_y[0] != triangle_y[-1]:
            plt.plot(triangle_x,triangle_y)
        else: plt.plot(triangle_x,triangle_y,color="blue",alpha=.2)
    plt.show()
    return start, triangle_x, triangle_y


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
