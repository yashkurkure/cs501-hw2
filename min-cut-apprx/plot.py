import csv
import glob
import matplotlib.pyplot as plt

files = [
        '200.csv', 
        '250.csv', 
        '300.csv', 
        '350.csv', 
        '400.csv', 
        '450.csv', 
        '500.csv', 
        '550.csv', 
        '600.csv', 
        '650.csv', 
        '700.csv', 
        '750.csv', 
        '800.csv', 
        '850.csv', 
        '900.csv', 
        '950.csv',
        '1000.csv'
        ]

def main():

    runtime_graph = ([],[])
    # do for all files
    for f in files:

        data = {
            "iter" : [],
            "cut" : [],
            "mincut" : [],
            "runtime" : []
        }

        graphs = {
            "cut_vs_iter": ([], []),
            "mincut_vs_iter": ([], []),
            "runtime_vs_nodes": ([], [])
        }



        # read the data from the file
        with open(f) as csv_file:
            
            avg_runtime = 0.0
            nodes = f.split('.')[0]

            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:

                    avg_runtime = avg_runtime + float(row[3])

                    data["iter"].append(int(row[0]))
                    data["cut"].append(int(row[1]))
                    data["mincut"].append(int(row[2]))
                    data["runtime"].append(int(row[3]))

                    if line_count%((int(f.split('.')[0]))/2) == 0:
                        graphs["cut_vs_iter"][0].append(int(row[0]))
                        graphs["cut_vs_iter"][1].append(int(row[1]))

                    graphs["mincut_vs_iter"][0].append(int(row[0]))
                    graphs["mincut_vs_iter"][1].append(int(row[2]))


                    line_count += 1

        # plot the data
        plt.plot(graphs["cut_vs_iter"][0], graphs["cut_vs_iter"][1], label = "cut")
        plt.plot(graphs["mincut_vs_iter"][0], graphs["mincut_vs_iter"][1], label = "mincut")

        plt.xlabel('iterations')
        plt.ylabel('cut value')
        plt.title ('cut, mincut vs iterations')

        plt.legend()

        plt.savefig("cut_vs_iter_" + f.split(".")[0] + ".png")

        plt.clf()

        print(str(nodes) + ", " + str( ((float(avg_runtime))/len(data["iter"]))/1000 ))
        runtime_graph[0].append(nodes)
        runtime_graph[1].append(((float(avg_runtime))/len(data["iter"]))/1000)
    
    print(str(runtime_graph[0]) + ", " +  str(runtime_graph[1]))
    plt.plot(runtime_graph[0], runtime_graph[1], label = "runtime")
    plt.xlabel('nodes')
    plt.ylabel('runtime (microseconds)')
    plt.title ('runtime')
    plt.legend()
    plt.savefig("runtime.png")

    ax = plt.gca()
    # Set x logaritmic
    ax.set_xscale('log')

    plt.savefig("runtime_log.png")






if __name__ == "__main__":
    main()
