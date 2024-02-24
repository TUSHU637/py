# with open("stocks.csv", "r") as f, open("output.csv", "w") as out:
#     out.write("Company Name,PE Ratio, PB Ratio\n")
#     next(f)  # This will skip first line in the file which is a header
#     for line in f:
#         tokens = line.split(",")
#         stock = tokens[0]
#         price = float(tokens[1])
#         eps = float(tokens[2])
#         book = float(tokens[3])
#         pe = round(price / eps, 2)
#         pb = round(price / book, 2)
#         out.write(f"{stock},{pe},{pb}\n")
#ANOTHER WAY
nf=open("output.csv","a")
with open("stocks.csv","r") as f:
    for data in f:
        cleandata=data.split(",")
    #   print(cleandata)
        if(cleandata[0]=="Company Name" ):
            nf.writelines(["Company Name ","PE RATIO ","PB RATIO\n"])
            continue
           
        cn=cleandata[0]
        pe=str(round((int(cleandata[1])/int(cleandata[2])),2))
        pb=str(int(cleandata[2])/int(cleandata[3]))
        nf.writelines([cn+"\t\t ",pe+"\t   ",pb])
        nf.writelines("\n")
        print(cleandata)
