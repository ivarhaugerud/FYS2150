import pandas
import io #Used as buffer

def uncertenty(value, procent, uncertenty):
    return value*procent/100 + uncertenty

def array_uncertenty(data):
    print(np.shape(data))
    print(data[:, 0])
    for i in range(len(data[:, 0])):
        for j in range(int(len(data[0, : ])/2)):
            data[2*j + 1, i] = uncertenty(data[int(2*j), i], 5, 0.1)
    return data


def convertToLaTeX(df, alignment="c"):
    numColumns = df.shape[1]
    numRows = df.shape[0]
    output = io.StringIO()
    colFormat = ("%s|%s" % (alignment, alignment * numColumns))
    #Write header
    output.write("\\begin{tabular}{%s}\n" % colFormat)
    output.write("   \\centering\n")
    output.write("   \\caption{ }\n")
    output.write("   \\label{ }\n")
    output.write("   \\hline\n")
    output.write("   ")
    columnLabels = ["%s" % label for label in df.columns]
    output.write("%s\n" % " & ".join(columnLabels))
    output.write("   \\hline\n")

    for i in range(numRows):
        output.write("   %s\\\\\n"
                     % (" & ".join([str(val) for val in df.ix[i]])))

    output.write("   \\hline\n")
    output.write("\\end{tabular}")
    return output.getvalue()

if __name__ == "__main__":
    import numpy as np
    array = np.array([[1, 0, 1, 0, 1, 0],
                      [1, 0, 1, 0, 1, 0],
                      [1, 0, 1, 0, 1, 0],
                      [1, 0, 1, 0, 1, 0],
                      [1, 0, 1, 0, 1, 0]])
    #print(array)
    #new_array = array_uncertenty(array)
    rad_navn = ["1", "2", "3", "4", "5", "6"]

    df = pandas.DataFrame(array, index=list("abcde"), columns=list(rad_navn))
    print(convertToLaTeX(df))
