#include <iostream>
#include <vector>
#include <string>
#include <random>

//Swaps Characters
bool isEven(int number) {
	return number % 2 == 0;
}

void join(const std::vector<char>& v, std::string& s) {
	s.clear();
	for (std::vector<char>::const_iterator p = v.begin();
		p != v.end(); ++p) {
		s += *p;
	}
}

std::vector<char> getEvenLetters(std::string message) {
	std::vector<char> evenLetters;
	for (int i = 0; i < size(message); i++) {
		if (isEven(i) == true) {
			evenLetters.push_back(message.at(i));
		}
	}
	return evenLetters;
}

std::vector<char> getOddLetters(std::string message) {
	std::vector<char> oddLetters;
	for (int i = 0; i < size(message); i++) {
		if (isEven(i) != true) {
			oddLetters.push_back(message.at(i));
		}
	}
	return oddLetters;
}

std::string swapLetters(std::string message) {
	std::vector<char> letterList;
	if (isEven(size(message)) != true) {
		message += " ";
	}
	std::vector<char> evenLetters = getEvenLetters(message);
	std::vector<char> oddLetters = getOddLetters(message);
	for (int i = 0; i < (size(message) / 2); i++) {
		letterList.push_back(oddLetters.at(i));
		letterList.push_back(evenLetters.at(i));
	}
	std::string output;
	join(letterList, output);
	return output;
}

//Character Shifter
int random(int min, int max) {
	std::random_device rd;
	std::mt19937 mt(rd());
	std::uniform_real_distribution<double> dist(min, max);
	return int(dist(mt));
}

std::string characterShifterEncrypt(std::string message, std::string characters) {
	std::string returnMessage;
	int shift = random(5, size(characters) - 5);
	for (char& character : message) {
		if (characters.find(character) != std::string::npos || character == ' ') {
			int position = characters.find(character);
			int newPosition = (position + shift) % size(characters);
			character = characters[newPosition];
		}
		returnMessage += character;
	}
	std::string shiftStr = std::to_string(shift);
	if (size(shiftStr) == 1) {
		returnMessage += "0";
	}
	returnMessage = returnMessage + shiftStr;
	return returnMessage;
}

std::string characterShifterDecrypt(std::string message, std::string characters) {
	std::string returnMessage;
	int shift = 0;
	try {
		shift = stoi(message.substr(message.length() - 2));
	}
	catch (...) {
		std::cout << "Error decrypting message. Please check you have inputted all characters from the encrypted message. " << std::endl;
		exit(EXIT_FAILURE);
	}
	shift *= -1;
	message.pop_back(); message.pop_back();
	for (char& character : message) {
		if (characters.find(character) != std::string::npos || character == ' ') {
			int position = characters.find(character);
			int newPosition = (position + shift);
			if (newPosition < 0) {
				newPosition += size(characters);
			}
			if (newPosition > size(characters) - 1) {
				signed int Size = size(characters);
				newPosition -= Size;
			}
			character = characters[newPosition];
		}
		returnMessage += character;
	}
	return returnMessage;
}

//Reversing a string
std::string reverseString(std::string strg) {
	std::string returnStr;
	returnStr.reserve(size(strg));
	for (int i = strg.length() - 1; i >= 0; i--) {
		returnStr.push_back(strg[i]);
	}
	return returnStr;
}

//Main Functions
std::string encrypt(std::string message, std::string characters) {
	std::string encrypt1 = swapLetters(message);
	std::string encrypt2 = characterShifterEncrypt(encrypt1, characters);
	std::vector<char> encrypt3List;
	for (int i = 0; i < size(encrypt2); i++) {
		encrypt3List.push_back(encrypt2[i]);
		encrypt3List.push_back(characters[random(0, size(characters) - 1)]);
	}
	std::string encrypt3(encrypt3List.begin(), encrypt3List.end());
	std::string encrypt4 = reverseString(encrypt3);
	return encrypt4;
}

std::string decrypt(std::string message, std::string characters) {
	std::string	decrypt1 = reverseString(message);
	std::vector<char> decrypt2Vector = getEvenLetters(decrypt1);
	std::string decrypt2(decrypt2Vector.begin(), decrypt2Vector.end());
	std::string decrypt3 = characterShifterDecrypt(decrypt2, characters);
	std::string decrypt4 = swapLetters(decrypt3);
	return decrypt4;
}

int main() {
	std::string characters;
	characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"£$%^&* \\()-_=+[]{};:@#~,<.>/?¬'|";
	std::string input = "";
	std::string choice = "";
	std::cout << "Do you want to encrypt(e) or decrypt(d)? " << std::flush; std::cin >> choice;
	if (choice == "e") {
		std::cout << "Enter the secret message(press ` to complete): " << std::flush; 
		std::getline(std::cin, input, '`');
		input.erase(0, 1);
		std::cout << "Entered secret message: " << input << std::endl;
		std::string output = encrypt(input, characters);
		std::cout << "Ciphertext of message is: " << output << std::endl;
	}
	else if (choice == "d") {
		std::cout << "Enter ciphertext of message(press ` to complete): " << std::flush; 
		std::getline(std::cin, input, '`');
		input.erase(0, 1);
		std::cout << "Entered ciphertext: " << input << std::endl;
		std::string output = decrypt(input, characters);
		std::cout << "Plaintext of message is: " << output << std::endl;
	}
	else {
		std::cout << "Valid option was not entered" << std::endl;
	}
	return 0;
}