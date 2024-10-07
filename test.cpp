#include <iostream>
#include <random>
using namespace std;


void Dice(int x)
{	
	int dice = 0;
	int i = 0;
	
	while (x != dice)
	{
		dice = rand() % 100 + 1; // roll 1 to 100
		i++;
	}

	cout << "Is this your number?: " << dice << endl;
	cout << "Took this many rolls: " << i << endl;
}
void Binary(int x)
{
	int Binary[32];
	int i = 0;

	while (x > 0)
	{
		Binary[i] = x % 2;
		x = x / 2;
		i++;
	}

	cout << "This is the number in binary: 0b";

	for (int j = i - 1; j >= 0; j--)
	{
		cout << Binary[j];
	}
	cout << endl;
}

void Hex(int x)
{
	int Hex[32];
	int i = 0;

	while (x > 0)
	{
		Hex[i] = x % 16; //Gets numbers 0 - 15
		x = x / 16;
		i++;
	}

	cout << "This is the number in hex: 0x";
	
	for (int j = i - 1; j >= 0; j--)
	{
		if (Hex[j] < 10)
		{
		cout << Hex[j];
		}
		else
		{
			switch (Hex[j])
			{
				case 10:
					cout << "A";
					break;
				case 11:
					cout << "B";
					break;
				case 12:
					cout << "C";
					break;
				case 13:
					cout << "D";
					break;
				case 14:
					cout << "E";
					break;
				case 15:
					cout << "F";
					break;
			}
		}

	}
	cout << endl;
}

int main()
{
	int x = 0;

	cout << "Enter a number: ";
	cin >> x;
	
	Dice(x);
	Binary(x);
	Hex(x);
	
	return 0;
}


