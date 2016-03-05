#include <iostream> //InputOutput
#include <vector> //Vector
#include <string> //String
#include <algorithm> // Sort
#include <fstream> // File reading

std::string sortFunc(std::string oldstring);


int main(){
	std::vector<std::string> vectorwordlist; //This vector will hold the word list
	std::vector<std::string> vectordescramblelist; //This vector will hole the descramble list
	std::vector<std::string> vectorsortedwordlist; //This vector will hold the sorted wordlist
	std::vector<std::string> vectorsorteddescramblelist; //This vector will hold the sorted descramble list

	//* Read the WordList (fstream)
	std::fstream wordlist;
	wordlist.open("wordlist.txt", std::fstream::in);

	//* Push the lines from WordList into a vector of strings
	if (wordlist.is_open()){
		while (!wordlist.eof()) { //End of file (to get all the lines)
			std::string wordline;
			std::getline(wordlist, wordline);
			vectorwordlist.push_back(wordline);
		}
		wordlist.close();
	}

	//* Read the DescrambleList
	std::fstream descramblelist;
	descramblelist.open("descramble.txt", std::fstream::in);

	//* Push the lines from DescrambledWords into a vector of strings
	if (descramblelist.is_open()){
		while (!descramblelist.eof()) {
			std::string descrambleline;
			std::getline(descramblelist, descrambleline);
			vectordescramblelist.push_back(descrambleline);
		}
		descramblelist.close();
	}

	//* Sort copies of the original words from WordList (algorithm)
	for (int wordlistpos = 0; wordlistpos < vectorwordlist.size(); wordlistpos++){
		std::string tempstring;
		tempstring = sortFunc(vectorwordlist[wordlistpos]);
		vectorsortedwordlist.push_back(tempstring);
	}

	//* Sort copies of the original words from Descramble (algorithm)
	for (int descramblepos = 0; descramblepos < vectordescramblelist.size(); descramblepos++){
		std::string tempstring;
		tempstring = sortFunc(vectordescramblelist[descramblepos]);
		vectorsorteddescramblelist.push_back(tempstring);
	}

	//* Compare sorted copies and then print the matching copies respective original
	std::cout << "Descrambled List = Word List" << std::endl;
	for (int descramblepos = 0; descramblepos < vectorsorteddescramblelist.size(); descramblepos++) {
		//For loop through the indexs of the vector WordList
		for (int WordListpos = 0; WordListpos < vectorsortedwordlist.size(); WordListpos++){
			//Compare the sizes of the lines
			if (vectorsorteddescramblelist[descramblepos] == vectorsortedwordlist[WordListpos]){
				//Output what words match what
				std::cout << vectordescramblelist[descramblepos] << " = " << vectorwordlist[WordListpos] << std::endl;
			}
		}
	}
}

//* String sort function
std::string sortFunc(std::string oldstring){
	std::sort(oldstring.begin(), oldstring.end());
	return oldstring;
}

/*Welcome to cipher day!
For this challenge, you need to write a program that will take the scrambled words from this post, 
and compare them against THIS WORD LIST to unscramble them.  http://pastebin.com/jSD873gL
For bonus points, sort the words by length when you are finished. Post your programs and/or subroutines!
Here are your words to de-scramble:

mkeart
sleewa	
edcudls
iragoge
usrlsle
nalraoci
nsdeuto
amrhat
inknsy
iferkna

/--------------------------------------------------/

Constraints
* C++
* Usage of given wordlist
* Descramble given words

Plan
* Read the WordList (fstream)
* Push the lines from WordList into a vector of strings
* Read the Descramble
* Push the lines from DescrambledWords into a vector of strings
* String/Vector sort function
* Sort copies of the original words from WordList (algorithm)
* Sort copies of the original words from Descramble (algorithm)
* Compare sorted copies and then print the matching copies respective original
* Repeat for each word being de-scrambled

FOR LOOP THROUGH THE DESCRAMBLELIST{
	FOR LOOP THROUGH THE WORDLIST{
		COMPARE THE WORDLIST TO THE DESCRAMBLE LIST IF CORRECT RETURN INDEXES AND BREAK
		}
	}
	
	
FOR LOOP THROUGH WORDLIST{
	RUN INDEX THROUGH SORTFUNC
	ADD SORTFUNC STRING TO SORTED VECTOR
}

There is probably a more efficient way to solve this problem without having to push-
-back into the vector and create two vectors holding together over 2200 entries.
Possibly doing the sorting and comparing while reading from the Word list on the fly
rather then pushing back into the vector and then sorting and comparing.
*/