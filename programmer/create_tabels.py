import pandas
import io #Used as buffer

def uncertenty(value, percentage, uncertenty):
    return value*percentage/100 + uncertenty

def array_uncertenty(data):
    for i in range(len(data[:, 0])):
        for j in range(int(len(data[0, :])*0.5)):
            data[i, 2*j+1] = uncertenty(data[i, 2*j], 0, 0.03)
    return data

def convertToLaTeX(df, alignment="c"):
    numColumns = df.shape[1]
    numRows = df.shape[0]
    output = io.StringIO()
    colFormat = ("%s|%s" % (alignment, alignment * numColumns))
    output.write("\\begin{tabular}{%s}\n" % colFormat)
    output.write("   \\centering\n")
    output.write("   \\caption{ }\n")
    output.write("   \\label{ }\n")
    output.write("   \\hline\n")
    output.write("   ")
    columnLabels = ["%s" % label for label in df.columns] #not bold headers
    #columnLabels = ["\\textbf{%s}" % label for label in df.columns] #bold headers
    output.write("%s\n" % " & ".join(columnLabels))
    output.write("   \\hline\n")

    for i in range(numRows):
        output.write("   %s\\\\\n"
                     % (" & ".join([str(val) for val in df.ix[i]])))
        output.write("\\textbf{%s} & %s\\\\\n"
                     % (df.index[i], " & ".join([str(val) for val in df.ix[i]])))

    output.write("   \\hline\n")
    output.write("\\end{tabular}")
    return output.getvalue()

if __name__ == "__main__":
    import numpy as np
    array = np.array([[11.725, 0],
                      [28.365, 0],
                      [88.700, 0],
                      [80.245, 0]])

    new_array = array_uncertenty(array)
    rad_navn = ["Avstand [mm]", "Usikkerhet [mm]"]
    kolonne_navn = ["1", "2", "3", "4"]

    df = pandas.DataFrame(new_array, index=list(kolonne_navn), columns=list(rad_navn))
    print(convertToLaTeX(df))
