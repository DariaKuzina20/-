#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    setlocale(LC_ALL, "Russian");
    double a, b, c, x1, x2; 
    double D; // Дискриминант

    cout << "Уравнение вида \'ax^2 + bx + c = 0\' \n";
    cout << "Введите коэффициент a: \n"; 
    cin >> a;
    cout << "Введите коэффициент b: \n";
    cin >> b;
    cout << "Введите коэффициент c: \n";
    cin >> c;

    D = b * b - 4 * a * c; 
    if (D > 0) 
    {
        x1 = ((-b) + sqrt(D)) / (2 * a);
        x2 = ((-b) - sqrt(D)) / (2 * a);
        cout << "Количество корней уравнения: 2 \n";
        cout << "Корни уравнения: \n";
        cout << "x1 = " << x1 << "\n";
        cout << "x2 = " << x2 << "\n";
    }
    else if (D == 0) 
    {
        x1 = -(b / (2 * a));
        cout << "Так как дискриминант равен  нулю, количество корней уравнения: 1 \n";
        cout << "Корень уравнения: \n";
        cout << "x1 = x2 = " << x1 << "\n";
    }
    else if (D < 0) 
        cout << "Так как дискриминант меньше нуля, корней уравнения не существует.";
}