#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct President {
    string name;
    string country;
    int year;

    President(string p_name, string p_country, int p_year)
        : name(move(p_name)), country(move(p_country)), year(p_year) {
        cout << "I am being constructed.\n";
    }
    President(const President& other)
        : name(move(other.name)),
          country(move(other.country)),
          year(other.year) {
        cout << "I am being copy constructed.\n";
    }
    President(President&& other)
        : name(move(other.name)),
          country(move(other.country)),
          year(other.year) {
        cout << "I am being moved.\n";
    }
    President& operator=(const President& other);
};

int main() {
    vector<President> es;
    cout << "emplace_back:\n";
    es.emplace_back("Nelson Mandela", "South Africa", 1994);

    cout << "\npush_back1:\n";
    es.push_back(President("Franklin Delano Roosevelt", "the USA", 1936));

    cout << "\npush_back2:\n";
    President ps = President("Abc", "the USA", 2020);
    es.push_back(ps);

    cout << "\nemplace_back2:\n";
    es.emplace_back("Xyz", "the USA", 2003);

    cout << "\nContents:\n";
    for (President const& president : es) {
        cout << president.name << " was elected president of "
             << president.country << " in " << president.year << ".\n";
    }
}
