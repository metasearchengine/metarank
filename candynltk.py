import nltk
import os

def main():
	#read text file

	def_read_dir = ("/home/sudeshna/input/")
	def_write_dir = ("/home/sudeshna/output/")
	def_lower_dir = ("/home/sudeshna/temp/")
	for filename in os.listdir(def_read_dir):
		filepath = os.path.join(def_read_dir, filename)
		if os.path.isfile(filepath):
			text_file = open(filepath,"r")
			#tokenize
			tokens = nltk.word_tokenize(text_file.read())
			text_file.close()
			candies = open("candies.txt","w")
			for w in tokens:
				#w = w.lower()
				candies.write(w)
				candies.write(" ")
			candies.close()
			#pos tagging
			candies = open("candies.txt","r")
			text = candies.read()
			tokenize = nltk.word_tokenize(text)
			index=0
			tagged = nltk.pos_tag(tokenize)
			#convert list of tuples to list of lists
			taggedlist = [list(element) for element in tagged]
			list_length = len(taggedlist)
			#change NN & NP
			for i in range(1,list_length):
				if taggedlist[i][1] in ["NNPS","NNP","NN","NNS"]:
					taggedlist[i][1] = "N"
				elif taggedlist[i][1] in ["JJR","JJS","JJ"]:
					taggedlist[i][1] = "A"
				elif taggedlist[i][1] == "IN":
					taggedlist[i][1] = "P"
			loop_from = 5 #set maximum length of keyphrase as 5 words
			#os.remove("candies.txt")
			#save candidates generated from each input file to a separate output file, of the same name, in a different directory
			writefilepath = os.path.join(def_write_dir, filename)
			save = open(writefilepath,"w")
			#match for P = A*N
			for i in range(loop_from, list_length):
				m=i-4
				l=i-3
				k=i-2
				j=i-1
				if taggedlist[i][1] == "N" and j>0 and k>0 and l>0 and m>0 and taggedlist[j][1] == "A" and taggedlist[k][1] == "A" and taggedlist[l][1] == "A" and taggedlist[m][1] == "A": #matches for AAAAN
					save.write(taggedlist[m][0] + " " + taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N" and j>0 and k>0 and l>0 and taggedlist[j][1] == "A" and taggedlist[k][1] == "A" and taggedlist[l][1] == "A": #matches for AAAN
					save.write(taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N" and j>0 and k>0 and taggedlist[j][1] == "A" and taggedlist[k][1] == "A": #matches for AAN
					save.write(taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N" and j>0 and taggedlist[j][1] == "A": #matches for AN
					save.write(taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N": #matches for N
					save.write(taggedlist[i][0])
					save.write("\n")
			#match for P = N*N
			for i in range(loop_from, list_length):
				m=i-4
				l=i-3
				k=i-2
				j=i-1
				if taggedlist[i][1] == "N" and j>0 and k>0 and l>0 and m>0 and taggedlist[j][1] == "N" and taggedlist[k][1] == "N" and taggedlist[l][1] == "N" and taggedlist[m][1] == "N": #matches for NNNNN
					save.write(taggedlist[m][0] + " " + taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N" and j>0 and k>0 and l>0 and taggedlist[j][1] == "N" and taggedlist[k][1] == "N" and taggedlist[l][1] == "N": #matches for NNNN
					save.write(taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N" and j>0 and k>0 and taggedlist[j][1] == "N" and taggedlist[k][1] == "N": #matches for NNN
					save.write(taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N" and j>0 and taggedlist[j][1] == "N": #matches for NN
					save.write(taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
			#match for P = A*NP A*N
			for i in range(loop_from, list_length):
				m=i-4
				l=i-3
				k=i-2
				j=i-1
				if taggedlist[i][1] == "A" and j>0 and k>0 and l>0 and m>0 and taggedlist[j][1] == "N" and taggedlist[k][1] == "P" and taggedlist[l][1] == "A" and taggedlist[m][1] == "N": #matches for ANPAN
					save.write(taggedlist[m][0] + " " + taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "A" and j>0 and k>0 and l>0 and taggedlist[j][1] == "N" and taggedlist[k][1] == "P" and taggedlist[l][1] == "N": #matches for ANPN
					save.write(taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N" and j>0 and k>0 and l>0 and taggedlist[j][1] == "P" and taggedlist[k][1] == "A" and taggedlist[l][1] == "N": #matches for NPAN
					save.write(taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N" and j>0 and k>0 and taggedlist[j][1] == "P" and taggedlist[k][1] == "N": #matches for NPN
					save.write(taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
			#match for P = N*NP A*N, P = A*NP N*N, P = N*NP N*N
			for i in range(loop_from, list_length):
				m=i-4
				l=i-3
				k=i-2
				j=i-1
				if taggedlist[i][1] == "N" and j>0 and k>0 and l>0 and m>0 and taggedlist[j][1] == "N" and taggedlist[k][1] == "P" and taggedlist[l][1] == "N" and taggedlist[m][1] == "N": #matches for NNPNN
					save.write(taggedlist[m][0] + " " + taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N" and j>0 and k>0 and l>0 and m>0 and taggedlist[j][1] == "N" and taggedlist[k][1] == "P" and taggedlist[l][1] == "A" and taggedlist[m][1] == "N": #matches for NNPAN
					save.write(taggedlist[m][0] + " " + taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "A" and j>0 and k>0 and l>0 and m>0 and taggedlist[j][1] == "N" and taggedlist[k][1] == "P" and taggedlist[l][1] == "N" and taggedlist[m][1] == "N": #matches for ANPNN
					save.write(taggedlist[m][0] + " " + taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N" and j>0 and k>0 and l>0 and taggedlist[j][1] == "N" and taggedlist[k][1] == "P" and taggedlist[l][1] == "N": #matches for NNPN
					save.write(taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
				elif taggedlist[i][1] == "N" and j>0 and k>0 and l>0 and taggedlist[j][1] == "P" and taggedlist[k][1] == "N" and taggedlist[l][1] == "N": #matches for NPNN
					save.write(taggedlist[l][0] + " " + taggedlist[k][0] + " " + taggedlist[j][0] + " " + taggedlist[i][0])
					save.write("\n")
			#convert all candidate files to lowercase
			save.close()
			lowerfilepath = os.path.join(def_lower_dir, filename)
			lowercase = open(lowerfilepath,"w")
			mixedcase = open(writefilepath,"r")
			for mixedline in mixedcase.readlines():
				lowerline=mixedline.lower()
				lowercase.write(lowerline)
			mixedcase.close()
			lowercase.close()

main()
