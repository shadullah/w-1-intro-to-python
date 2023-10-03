#include <iostream>
#include <map>

using namespace std;

int main()
{
    int N;
    cin >> N;

    map<int, int> count;

    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;
        count[num]++;
    }

    int removals = 0;

    for (auto it = count.begin(); it != count.end(); ++it)
    {
        int num = it->first;
        int occurrences = it->second;

        if (occurrences > num)
        {
            removals += (occurrences - num); // Remove excess occurrences
        }
        else if (occurrences < num)
        {
            removals += occurrences; // Remove all occurrences of this element
        }
    }

    cout << removals << endl;

    return 0;
}
