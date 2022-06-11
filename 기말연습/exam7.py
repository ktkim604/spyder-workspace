# infile = open("phones.txt", "r")
# lines = infile.read()             
# print(lines)

# infile = open("phones.txt", "r")
# lines = infile.readlines()      
# print(lines)

# outfile = open("phones1.txt", "w")
# outfile.write("홍길동 010-1234-5678\n")
# outfile.write("김철수 010-1234-5679\n")
# outfile.write("김영희 010-1234-5680\n")
# outfile.close() 

outfile = open("phones.txt", "a")
outfile.write("강감찬 010-1234-5681\n")
outfile.write("김유신 010-1234-5682\n")
outfile.write("정약용 010-1234-5683\n")
outfile.close() 