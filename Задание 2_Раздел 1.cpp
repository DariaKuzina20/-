#include <iostream>
using namespace std;


class Glass {

	double capacity = 0; 	//Текущий объем жидкости в стакане
	double maxCapacity; 	//Объем стакана

public:

	
	Glass()
	{
		
		while (true)
		{
			system("cls");
			double maxCap;
			cout << "Введите объем стакана в мл: ";
			cin >> maxCap;

			if (maxCap > 0)
			{
				maxCapacity = maxCap;
				cout << "\nОбъем стакана успешно задан!\n\n";
				system("pause");
				return;
			}

			else
			{
				cout << "\nОбъем стакана не может быть <= 0.\n\n";
				system("pause");
			}
		}
	}

	void addLiquid()
	{
		double liquid;
		cout << "Введите объем доливаемой жидкости в мл: ";
		cin >> liquid;

		if (capacity + liquid > maxCapacity)
		{
			cout << "\nНевозможно долить такой объем жидкости, так как стакан переполнится.\n\n";
			return;
		}

		capacity += liquid;
		cout << endl;
	}

	void pourLiquid()
	{
		double liquid;
		cout << "Введите объем наливаемой жидкости в мл: ";
		cin >> liquid;

		if (capacity - liquid < 0)
		{
			cout << "\nВ стакане нет такого объема жидкости!\n\n";
			return;
		}

		capacity -= liquid;
		cout << endl;
	}

	void showCapacity()
	{
		cout << "Текущий объем: " << capacity << "/" << maxCapacity << endl << endl;
	}
};



int main()
{
	setlocale(LC_CTYPE, "ru");

	Glass glass;

	int choice;
	while (true)
	{
		system("cls");
		cout << "Выберите действие: ";
		cout << "1.Долить жидкость в стакан\n";
		cout << "2.Налить жидкость из стакана\n";
		cout << "3.Определить текущий объем жидкости\n\n";
		cout << "0.Выход\n\n";
		cin >> choice;

		if (choice == 1)
		{
			system("cls");      	//Очищаем консоль
			glass.addLiquid();	//Выполняем метод
			system("pause");	//Ставим на паузу и ждём следующего действия
		}
		if (choice == 2)
		{
			system("cls");
			glass.pourLiquid();
			system("pause");
		}
		if (choice == 3)
		{
			system("cls");
			glass.showCapacity();
			system("pause");
		}
		if (choice == 0)
		{
			system("cls");
			exit(0);
			system("pause");
		}
	}
}
